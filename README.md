# Aman Kag Portfolio Chatbot

A production-deployed **Retrieval-Augmented Generation (RAG) chatbot** that allows visitors to explore my professional experience, technical skills, and projects through natural-language conversations.

A single FastAPI backend powers two portfolio assistants:

- **IT Support Assistant** — focused on Service Desk, Desktop Support, infrastructure, troubleshooting, and IT experience.
- **Data Science Assistant** — focused on Data Science, Machine Learning, analytics, cloud, and technical projects.

Both assistants share the same backend architecture while maintaining **isolated knowledge bases and system prompts**, selected dynamically using the `site` parameter.

---

## Architecture

```text
Portfolio Website
       │
       ▼
JavaScript Chat Widget
       │
       ▼
FastAPI /chat API
       │
       ▼
Semantic Retrieval
       │
       ▼
ChromaDB Vector Store
       │
       ▼
Relevant Portfolio Context
       │
       ▼
Groq — GPT-OSS 120B
       │
       ▼
Grounded Response
```

The chatbot uses RAG rather than sending the entire portfolio to the language model with every request. This allows the system to retrieve only the information most relevant to a visitor's question before generating a response.

---

## How It Works

### 1. Knowledge Base

Professional experience, skills, certifications, and projects are stored as topic-focused chunks in `app/knowledge_base.py`.

Separate knowledge bases are maintained for the IT and Data Science portfolios.

### 2. Local Embeddings

At application startup, knowledge-base chunks are converted into vector embeddings using `all-MiniLM-L6-v2` and stored in isolated **ChromaDB** collections.

This keeps the retrieval layer independent of the LLM API and avoids requiring a paid embedding service.

### 3. Semantic Retrieval

When a visitor submits a question, the backend:

1. Identifies the requested portfolio (`it` or `ds`).
2. Embeds the visitor's question.
3. Searches the corresponding ChromaDB collection.
4. Retrieves the three most relevant knowledge chunks.
5. Adds those chunks as context for the language model.

### 4. Response Generation

The retrieved context and visitor question are sent to **GPT-OSS 120B through Groq**.

The model generates a concise response grounded in the retrieved portfolio information. If retrieval confidence is weak, the assistant is instructed to acknowledge uncertainty rather than invent information.

---

## Key Features

- Retrieval-Augmented Generation (RAG)
- Semantic search using vector embeddings
- Separate IT and Data Science knowledge bases
- ChromaDB vector storage
- Local MiniLM embeddings
- GPT-OSS 120B inference through Groq
- FastAPI REST backend
- Reusable JavaScript chat widget
- CORS protection
- IP-based rate limiting
- Retrieval-confidence fallback handling
- Environment-based configuration
- Cloud deployment on Render

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| LLM | GPT-OSS 120B |
| Inference | Groq |
| Vector Database | ChromaDB |
| Embeddings | all-MiniLM-L6-v2 |
| Frontend Integration | JavaScript |
| API Server | Uvicorn |
| Deployment | Render |
| Source Control | Git / GitHub |

---

## API

### Endpoint

```text
POST /chat
```

### Example Request

```json
{
  "message": "What experience does Aman have with AWS and data engineering?",
  "site": "ds"
}
```

The `site` field determines which knowledge base the RAG system searches. Supported values are `it` and `ds`.

### Example Response

```json
{
  "reply": "Response generated from the relevant portfolio context."
}
```

---

## Local Development

Clone the repository and create a virtual environment:

```bash
git clone https://github.com/amankag/kag-portfolio-chatbot.git
cd kag-portfolio-chatbot

python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the environment file:

```bash
cp .env.example .env
```

Add a Groq API key to `.env`:

```text
GROQ_API_KEY=your_api_key
GROQ_MODEL=openai/gpt-oss-120b
```

Start the API:

```bash
uvicorn app.main:app --reload --port 8000
```

---

## Testing the API

### IT Portfolio

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"What IT tools does Aman use?","site":"it"}'
```

### Data Science Portfolio

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Tell me about Aman’s machine learning projects","site":"ds"}'
```

---

## Rate Limiting

The API includes IP-based rate limiting to prevent unnecessary API usage.

Current configuration:

- 15 requests per visitor
- 10-minute rolling window

The limits are configurable through `RATE_LIMIT_MAX_REQUESTS` and `RATE_LIMIT_WINDOW_SECONDS` in `app/main.py`.

---

## Updating Portfolio Knowledge

The chatbot does not require model retraining when portfolio information changes.

Content can be updated directly in `app/knowledge_base.py`. When the application restarts, embeddings and ChromaDB collections are rebuilt automatically from the updated knowledge base.

---

## Model Migration

The chatbot was originally built using **Llama 3.3 70B Versatile through Groq**.

Following the model's decommissioning in 2026, the generation layer was migrated to `openai/gpt-oss-120b`.

Because the LLM is configured independently from the retrieval and embedding layers, the model could be replaced without redesigning the RAG architecture. This separation makes the system easier to maintain as inference models and APIs evolve.

---

## Project Structure

```text
kag-portfolio-chatbot/
├── app/
│   ├── __init__.py
│   ├── knowledge_base.py
│   ├── rag_engine.py
│   └── main.py
│
├── widget/
│   └── chat-widget.html
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Core Components

**`knowledge_base.py`** — Contains structured portfolio information for semantic retrieval.

**`rag_engine.py`** — Handles embeddings, ChromaDB collections, semantic retrieval, context construction, and Groq generation.

**`main.py`** — Provides the FastAPI application, `/chat` endpoint, CORS configuration, validation, and rate limiting.

**`chat-widget.html`** — Reusable frontend chatbot interface that connects the portfolio websites to the API.

---

## Design Decisions

### One Backend, Multiple Portfolios

Instead of deploying separate AI backends, both portfolio assistants use one API while maintaining isolated knowledge collections. This reduces duplicated infrastructure while preventing information from one portfolio from being unintentionally retrieved for the other.

### Local Embeddings

Embeddings are generated locally rather than through an external embedding API. This reduces external dependencies and keeps semantic retrieval inexpensive.

### Retrieval Before Generation

Only relevant portfolio information is supplied to the language model. This reduces unnecessary context and helps keep responses grounded in known information.

### Model-Independent Architecture

Retrieval, embeddings, and generation are separated so the underlying LLM can be replaced without rebuilding the entire application.

---

## Deployment

The FastAPI backend is deployed as a **Render Web Service**.

Production configuration, including API credentials, is stored using environment variables rather than committed to the repository. The frontend portfolio sites communicate with the backend through the `/chat` API.

---

## Author

**Aman Kag**

This project was built as part of my portfolio to demonstrate practical experience with **Python APIs, RAG systems, semantic search, vector databases, LLM integration, deployment, and frontend/backend integration**.
