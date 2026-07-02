# 🤖 Riva Context-Aware Customer Support RAG Bot

## Overview

Riva is a Retrieval-Augmented Generation (RAG) chatbot developed using Python, LangChain, Groq API, SQLite, and FAISS.

The chatbot answers customer support queries using a company FAQ document and personalizes responses based on user information stored in an SQLite database.

---

## Features

- Retrieval-Augmented Generation (RAG) over FAQ documents  
- Semantic search using FAISS vector store  
- Personalized responses using SQLite user profiles  
- Fast inference using Groq API  
- Terminal-based chatbot interface  
- FastAPI-based API support  
- Structured error handling and fallback responses  

---

## Technologies

- Python 3.x
- LangChain
- Groq API
- FAISS (Vector Database)  
- SQLite (User Data Storage)  
- HuggingFace Sentence Transformers  
- FastAPI (optional API layer)  
- Uvicorn (ASGI server)  

---

## 🧠 System Architecture

User Query  
→ SQLite (User Profile)  
→ Embedding Model (HuggingFace)  
→ FAISS Vector Search (FAQ Retrieval)  
→ Prompt Builder (Context + User Info)  
→ Groq LLM (Response Generation)  
→ Final Answer  

---

## Project Structure

```
customer-support-rag/
│
├── app.py # Terminal chatbot application
├── main.py # FastAPI backend (optional API mode)
├── ingest.py # Embedding + vector store creation
├── create_db.py # SQLite database setup
├── company_faq.txt # Knowledge base (FAQ document)
├── users.db # SQLite database
├── faiss_index/ # Stored embeddings (vector DB)
├── requirements.txt # Dependencies
├── README.md
├── .env.example
├── .gitignore
```
---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/gamana29/Context-Aware-Customer-Support-RAG-Bot.git
cd customer-support-rag
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

## 🗄️ Setup Instructions
### Step 1: Create SQLite Database

```bash
python create_db.py
```

### Step 2: Generate Vector Store

```bash
python ingest.py
```



## Run chatbot

### 🖥️ Terminal Version
Run the chatbot directly in the terminal:
```bash
python app.py
```

### ⚡ FastAPI Version
Run the backend API server:

```bash
uvicorn main:app --reload
```

Open in browser:
```bash
http://127.0.0.1:8000/docs
```
---

## Sample Users

| User ID | Name | Membership |
|---------|------|------------|
|101|Riya Sharma|Gold|
|102|Aman Verma|Silver|
|103|Neha Iyer|Platinum|

---

## Sample Questions

- What is the refund policy?
- Can I cancel my account?
- What are my membership benefits?
- Do I get premium customer support?

---

## Error Handling

- Invalid User ID
- Missing API Key
- Missing Context
- API Errors

---

## Model

The original assignment specified `llama3-8b-8192`. Since this model has been deprecated by Groq, the implementation uses a currently supported Groq model.

---

## 📌 Notes

- Run `ingest.py` before starting chatbot  
- Do not commit `.env`, `venv/`, or cache files  
- FAISS index must exist before querying  

---

## 👨‍💻 Author

Built as part of an AI internship assessment focused on Retrieval-Augmented Generation systems, vector databases, and LLM integration.

---

## 📜 License

For educational and evaluation purposes only.
