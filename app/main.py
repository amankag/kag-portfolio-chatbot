"""
FastAPI backend serving both portfolio chatbots.

Single /chat endpoint; "site": "it" or "ds" in the request body selects
knowledge base and system prompt.

Run locally:
    uvicorn app.main:app --reload --port 8000

Required env vars:
    GROQ_API_KEY     - Groq API key
    ALLOWED_ORIGINS  - comma-separated allowed frontend origins
"""

import os
import time
import logging
from collections import defaultdict, deque

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from app.rag_engine import get_engine

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

app = FastAPI(title="Aman Kag Portfolio Chatbot API")

allowed_origins = os.environ.get("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# In-memory rate limiting, per IP. Sufficient for a single-instance deploy;
# swap for Redis if scaling to multiple instances.
RATE_LIMIT_MAX_REQUESTS = 15
RATE_LIMIT_WINDOW_SECONDS = 60 * 10  # 10 minutes
_request_log: dict[str, deque] = defaultdict(deque)


def check_rate_limit(client_ip: str):
    now = time.time()
    log = _request_log[client_ip]
    while log and now - log[0] > RATE_LIMIT_WINDOW_SECONDS:
        log.popleft()
    if len(log) >= RATE_LIMIT_MAX_REQUESTS:
        raise HTTPException(
            status_code=429,
            detail="You've sent a lot of messages! Please wait a few minutes "
                   "before trying again, or reach out to Aman directly.",
        )
    log.append(now)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=500)
    site: str = Field(..., pattern="^(it|ds)$")


class ChatResponse(BaseModel):
    reply: str


@app.on_event("startup")
def startup_event():
    # Load model + build vector stores at startup, not on first request.
    logger.info("Starting up - initialising RAG engine...")
    get_engine()
    logger.info("RAG engine ready.")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest, request: Request):
    client_ip = request.client.host if request.client else "unknown"
    check_rate_limit(client_ip)

    try:
        engine = get_engine()
        reply = engine.generate(query=req.message, site=req.site)
        return ChatResponse(reply=reply)
    except Exception as exc:
        logger.exception("Error generating chat response")
        raise HTTPException(status_code=500, detail="Something went wrong generating a response.") from exc
