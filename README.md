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
## Case 1: Valid User
```bash 

Input:

User ID: 101  
Query: What is the refund policy?

Output:

Hi Riya Sharma 👋  
As a Gold member, you are eligible for a 7-day refund window.  
You can initiate a refund from your account settings under Billing → Refunds.
```
<img width="1250" height="172" alt="image" src="https://github.com/user-attachments/assets/80b7c788-496a-485f-8186-6082f9ee9e95" />

<img width="1293" height="401" alt="image" src="https://github.com/user-attachments/assets/74467a62-1af1-4e45-a145-c2427c43294a" />


## Case 2: Invalid User
```bash 

Input:

User ID: 999  
Query: What are my benefits?

Output:

User not found. Please enter a valid user_id.
```
<img width="1517" height="167" alt="image" src="https://github.com/user-attachments/assets/3bf94569-8b60-4a07-94e0-fc7db9412375" />

<img width="1547" height="371" alt="image" src="https://github.com/user-attachments/assets/70602889-e14e-4c1f-a6d3-5ec25ec6aa38" />


## Case 3: FAQ Retrieval

```bash

Input:

User ID: 102  
Query: Can I cancel my account?

Output:

Yes, you can cancel your account anytime from settings.  
Silver members retain access until the end of the billing cycle.
```
<img width="1523" height="188" alt="image" src="https://github.com/user-attachments/assets/aca9e1f1-02a3-4525-bb23-548bf6265192" />

<img width="1511" height="437" alt="image" src="https://github.com/user-attachments/assets/e7af1ce4-0598-4b89-965a-30a47f15aa42" />


---
<img width="1917" height="990" alt="image" src="https://github.com/user-attachments/assets/5b7f28e8-e964-4568-a09f-bfde2a5df0c5" />

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
