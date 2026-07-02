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
    print("Error: GROQ_API_KEY not found.")
    exit()

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

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

user_id = int(input("Enter User ID: "))
user_query = input("Ask your question: ")


cursor.execute(
    "SELECT name, membership_tier FROM users WHERE user_id=?",
    (user_id,)
)

user = cursor.fetchone()

if user is None:
    print("User not found. Please enter a valid user_id.")
    conn.close()
    exit()

name, membership = user


docs = vectorstore.similarity_search(
    user_query,
    k=3
)

if not docs:
    print("I do not have enough information in the provided knowledge base to answer this.")
    conn.close()
    exit()

context = "\n\n".join([doc.page_content for doc in docs])


prompt = f"""
You are Riva AI Customer Support Assistant.

You are currently assisting the following customer:

Customer Name: {name}
Membership Tier: {membership}

Always greet the customer by name.

If the membership tier is relevant to the question, mention the membership benefits naturally.

Answer ONLY using the context provided below.

Do not make up information.

If the answer is not available in the context, respond exactly with:

"I do not have enough information in the provided knowledge base to answer this."

Context:
{context}

Customer Question:
{user_query}

Answer:
"""


try:
    response = llm.invoke(prompt)

    print("\n" + "=" * 60)
    print("Riva AI Support")
    print("=" * 60)
    print(response.content)
    print("=" * 60)

except Exception as e:
    print(f"Error: {e}")


conn.close()