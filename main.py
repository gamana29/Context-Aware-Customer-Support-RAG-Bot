import os
import sqlite3

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise Exception("GROQ_API_KEY not found")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.1-8b-instant"
)

app = FastAPI(
    title="Riva Context-Aware Customer Support RAG Bot"
)

class ChatRequest(BaseModel):
    user_id: int
    user_query: str


@app.get("/")
def home():
    return {
        "message": "Welcome to Riva AI Customer Support Bot"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, membership_tier FROM users WHERE user_id=?",
        (request.user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        conn.close()
        return {
            "response": "User not found. Please enter a valid user_id."
        }

    name, membership = user

    docs = vectorstore.similarity_search(
        request.user_query,
        k=3
    )

    if not docs:
        conn.close()
        return {
            "response": "I do not have enough information in the provided knowledge base to answer this."
        }

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
You are Riva AI Customer Support Assistant.

Customer Name: {name}

Membership Tier: {membership}

Always greet the customer by name.

Answer ONLY using the context below.

Context:
{context}

Question:
{request.user_query}

Answer:
"""

    try:
        response = llm.invoke(prompt)

        conn.close()

        return {
            "name": name,
            "membership": membership,
            "answer": response.content
        }

    except Exception as e:
        conn.close()
        return {
            "error": str(e)
        }