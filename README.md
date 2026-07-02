# 🤖 Riva Context-Aware Customer Support RAG Bot

## Overview

Riva is a Retrieval-Augmented Generation (RAG) chatbot developed using Python, LangChain, Groq API, SQLite, and FAISS.

The chatbot answers customer support queries using a company FAQ document and personalizes responses based on user information stored in an SQLite database.

---
## Architecture Overview
```bash
User Query
↓
SQLite (User Profile Retrieval)
↓
Query Embedding (HuggingFace)
↓
FAISS Vector Search (FAQ Retrieval)
↓
Context + User Data Prompt Construction
↓
Groq LLM Inference
↓
Personalized Response
```
---

##  Why This Architecture?

This system is designed in modular layers:

### 1. Data Layer
- SQLite stores structured user profiles
- Enables personalization (membership-based responses)

### 2. Retrieval Layer
- FAQ document is chunked and embedded
- FAISS performs fast semantic similarity search

### 3. Generation Layer
- Groq LLM generates final response
- Prompt includes retrieved context + user information

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

##  System Architecture

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
### Sample Output

```bash 
Case 1: Valid User
Input:

User ID: 101  
Query: What is the refund policy?

Output:

Hi Riya Sharma 👋  
As a Gold member, you are eligible for a 7-day refund window.  
You can initiate a refund from your account settings under Billing → Refunds.
```
<img width="1571" height="802" alt="image" src="https://github.com/user-attachments/assets/294b77f1-18a4-452e-a2f1-1879177192a5" />
<img width="1538" height="683" alt="image" src="https://github.com/user-attachments/assets/21f53ae7-8fb9-44fd-953a-0d9c257e5de9" />

Case 2: Invalid User
```bash 
<img width="1571" height="802" alt="image" src="https://github.com/user-attachments/assets/294b77f1-18a4-452e-a2f1-1879177192a5" />
<img width="1538" height="683" alt="image" src="https://github.com/user-attachments/assets/21f53ae7-8fb9-44fd-953a-0d9c257e5de9" />
```bash
Input:

User ID: 999  
Query: What are my benefits?

Output:

User not found. Please enter a valid user_id.
```
Case 3: FAQ Retrieval

```bash

Input:

User ID: 102  
Query: Can I cancel my account?

Output:

Yes, you can cancel your account anytime from settings.  
Silver members retain access until the end of the billing cycle.
```
---

<img width="1606" height="766" alt="image" src="https://github.com/user-attachments/assets/eb1aa9c6-272c-4984-aed1-ba62c32e749d" />





## Error Handling

- Invalid User ID
- Missing API Key
- Missing Context
- API Errors

---

## Model

The original assignment specified `llama3-8b-8192`. Since this model has been deprecated by Groq, the implementation uses a currently supported Groq model.

---

##  Notes

- Run `ingest.py` before starting chatbot  
- Do not commit `.env`, `venv/`, or cache files  
- FAISS index must exist before querying  

---

##  Author

Built as part of an AI internship assessment focused on Retrieval-Augmented Generation systems, vector databases, and LLM integration.

---

## 📜 License

For educational and evaluation purposes only.
