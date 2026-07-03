# AI-Powered Customer Support Automation System using LangGraph

## Project Overview

This project is an AI-powered Customer Support Automation System developed using LangGraph and LangChain. It automates customer support by identifying customer intent, routing queries to the appropriate department, retrieving information from company documents using Retrieval-Augmented Generation (RAG), maintaining conversation history with SQLite memory, and supporting Human-in-the-Loop approval for high-risk requests.

---

## Features

* Intent Classification
* Conditional Routing
* Sales Support Agent
* Technical Support Agent
* Billing Support Agent
* Account Support Agent
* Retrieval-Augmented Generation (RAG)
* FAISS Vector Database
* HuggingFace Embeddings
* SQLite Conversation Memory
* Human-in-the-Loop Approval
* AI Supervisor Response Review

---

## Technologies Used

* Python
* LangGraph
* LangChain
* Groq LLM (Llama 3.3 70B Versatile)
* HuggingFace Embeddings
* FAISS
* SQLite
* VS Code

---

## Project Structure

```
CustomerSupportBot
│
├── app.py
├── graph.py
├── router.py
├── agents.py
├── rag.py
├── memory.py
├── approval.py
├── supervisor.py
├── state.py
├── requirements.txt
│
├── documents
│   ├── company_policy.txt
│   ├── pricing_guide.txt
│   ├── technical_manual.txt
│   └── faq.txt
│
├── database
│   └── memory.db
│
└── README.md
```

---

## Installation

Create a virtual environment:

```
python -m venv venv
```

Activate it:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run

```
python app.py
```

---

## Sample Queries

* What are the pricing plans available for your software?
* I forgot my account password.
* My application crashes whenever I upload a file.
* I need a refund for my annual subscription.
* What was my previous support issue?

---

## Project Workflow

Customer Query

↓

Intent Classification

↓

Department Routing

↓

RAG Retrieval

↓

Generate Response

↓

Human Approval (if required)

↓

Supervisor Review

↓

Store Conversation in SQLite

↓

Final Response

---

## Author

R. Venkata Deepika Reddy

VIT-AP University

B.Tech CSE
