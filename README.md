# AI-Powered Customer Support Automation System

An AI-powered customer support application built with Python, LangGraph, LangChain, and the Groq API. The system classifies customer queries, routes them to specialized support workflows, retrieves relevant information from company documents, maintains conversation history, and supports human approval for high-risk requests.

## Features

- **Intent Classification:** Categorizes customer queries into Sales, Technical Support, Billing, or Account.
- **Conditional Routing:** Routes queries to the appropriate support workflow using LangGraph.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant information from company documents to support response generation.
- **Vector Search:** Uses FAISS and Hugging Face embeddings for document retrieval.
- **LLM Integration:** Uses the Groq API through LangChain for language-model-powered support tasks.
- **Conversation Memory:** Uses SQLite to store conversation history.
- **Human-in-the-Loop Approval:** Supports human review for designated high-risk requests.
- **AI Supervisor Review:** Includes a response-review step in the support workflow.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| LangChain | LLM integration and tools |
| LangGraph | Workflow orchestration and conditional routing |
| Groq API | Hosted language-model inference |
| Hugging Face Embeddings | Document and query embeddings |
| FAISS | Vector similarity search |
| SQLite | Conversation persistence |

## Architecture

```text
Customer Query
      |
      v
Intent Classification
      |
      v
LangGraph Routing
      |
      v
Specialized Support Workflow
      |
      v
Retrieve Relevant Documents
      |
      v
FAISS Vector Search
      |
      v
LLM Response Generation
      |
      v
AI Supervisor Review
      |
      v
Human Approval, When Required
      |
      v
Store Conversation in SQLite
      |
      v
Final Response
```

The exact execution path depends on the query and the workflow conditions.

## API Integration and Security

The application integrates a hosted language model through the Groq API using LangChain.

- **Authentication:** Configure the Groq API key through the `GROQ_API_KEY` environment variable if this matches the current application configuration.
- **Credential Security:** Never commit a real API key or `.env` file to GitHub.
- **Configuration Example:** A `.env.example` file can document required environment variables using placeholder values.
- **Error Handling:** API timeouts, rate limits, failed requests, and malformed model responses should be documented according to the behavior actually implemented and tested.

The application uses the LLM for language-related tasks, while FAISS handles document retrieval and SQLite handles conversation storage.

## Project Structure

```text
CustomerSupportBot/
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
├── documents/
│   ├── company_policy.txt
│   ├── pricing_guide.txt
│   ├── technical_manual.txt
│   └── faq.txt
├── database/
└── README.md
```

This structure should match the files present in the repository.

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/rvdeepikareddy1/AI-Powered-Customer-Support-Automation-System.git
cd AI-Powered-Customer-Support-Automation-System
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root if the application uses `python-dotenv`:

```text
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholder with your own API key. Never publish the real key.

### 5. Run the application

If the repository's entry point is `app.py`:

```bash
python app.py
```

Follow the application's prompts to submit customer queries.

## Example Queries

- What pricing plans are available?
- I forgot my account password.
- My application crashes when I upload a file.
- I need a refund for my annual subscription.
- What was my previous support issue?

## How It Works

1. The system receives a customer query.
2. The intent classifier identifies the appropriate support category.
3. LangGraph routes the query to the corresponding workflow.
4. RAG retrieves potentially relevant information from the company knowledge base using embeddings and FAISS.
5. The LLM generates a response using the query and retrieved context.
6. The supervisor and human-approval steps execute according to the configured workflow.
7. Conversation information is persisted using SQLite.

If the knowledge base does not contain sufficient information, the application should avoid inventing company policies. The exact fallback behavior depends on the implemented retrieval and response-validation logic.

## Future Improvements

- Add and test explicit handling for API timeouts and rate limits.
- Implement bounded retries for transient API failures where appropriate.
- Validate model outputs before using them in downstream operations.
- Add automated tests for routing, retrieval, API failures, and approval workflows.
- Add a demo showing the end-to-end workflow.

## Author

**R. Venkata Deepika Reddy**  
B.Tech, Computer Science and Engineering  
VIT-AP University

GitHub: https://github.com/rvdeepikareddy1
