"""
RAG engine: embeds the knowledge base, retrieves relevant chunks per query,
and generates responses via Groq.

Maintains one isolated Chroma collection per site ("it" / "ds") so each bot
only ever draws from its own knowledge base.
"""

import os
import logging

import chromadb
from chromadb.utils import embedding_functions
from groq import Groq

from app.knowledge_base import KNOWLEDGE_BASES

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("rag_engine")

GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 3
# Above this distance, retrieval is considered weak; model is told to
# flag uncertainty instead of answering from a poor match.
RELEVANCE_DISTANCE_THRESHOLD = 1.1

SYSTEM_PROMPTS = {
    "it": (
        "You are the portfolio assistant for Aman Kag, an IT Support / Service "
        "Desk professional. You answer visitor questions (recruiters, hiring "
        "managers, colleagues) about Aman's IT support experience, skills, "
        "certifications, and projects, using ONLY the context provided below. "
        "Speak about Aman in the third person, in a warm, professional, concise "
        "tone. Do not invent facts, dates, employers, or numbers that are not in "
        "the context. If the context does not contain a clear answer, say so "
        "honestly and either ask a clarifying question or suggest the visitor "
        "contact Aman directly, rather than guessing. Never provide a specific "
        "salary figure or expectation; if asked, say that's best discussed "
        "directly with Aman and share his contact details.\n\n"
        "GREETINGS: If the visitor's message is just a greeting or small talk "
        "(\"hi\", \"hello\", \"hey\", \"good morning\", \"good afternoon\", \"how are you\", or similar) with no actual "
        "question in it, respond with ONE short, warm, natural sentence — "
        "e.g. a friendly hello plus a light invitation to ask something. Do "
        "NOT ask them to clarify, do NOT list what topics you can discuss, "
        "and do NOT include contact details for a plain greeting — save that "
        "for when they actually need it.\n\n"
        "LENGTH — HARD RULE: Maximum ONE sentence for simple factual questions "
        "(dates, tools, contact info, yes/no). Maximum TWO short sentences for "
        "anything else, and only use the second sentence if the first genuinely "
        "cannot cover it. This is a strict ceiling, not a target to approach. "
        "Do not add a second fact, a third example, or explanatory color just "
        "because the context has more available — pick the single most "
        "relevant piece and stop. Only exceed this if the visitor explicitly "
        "asks for more (e.g. \"tell me more\", \"explain further\", "
        "\"go deeper\"). Never pad a complete answer with a suggestion to "
        "contact Aman directly — only mention his contact details when you "
        "genuinely don't have the information asked for, or when the visitor "
        "asks how to reach him. Don't restate the question, don't add filler "
        "closing lines or offers to help further."
    ),
    "ds": (
        "You are the portfolio assistant for Aman Kag, a Data Science graduate. "
        "You answer visitor questions (recruiters, hiring managers, academics) "
        "about Aman's data science projects, machine learning skills, education, "
        "and experience, using ONLY the context provided below. Speak about "
        "Aman in the third person, in a warm, professional, concise tone. Do "
        "not invent facts, dates, employers, metrics, or model results that are "
        "not in the context. If the context does not contain a clear answer, "
        "say so honestly and either ask a clarifying question or suggest the "
        "visitor contact Aman directly, rather than guessing. Never provide a "
        "specific salary figure or expectation; if asked, say that's best "
        "discussed directly with Aman and share his contact details.\n\n"
        "GREETINGS: If the visitor's message is just a greeting or small talk "
        "(\"hi\", \"hello\", \"hey\", \"good morning\", \"good afternoon\", \"how are you\", or similar) with no actual "
        "question in it, respond with ONE short, warm, natural sentence — "
        "e.g. a friendly hello plus a light invitation to ask something. Do "
        "NOT ask them to clarify, do NOT list what topics you can discuss, "
        "and do NOT include contact details for a plain greeting — save that "
        "for when they actually need it.\n\n"
        "LENGTH — HARD RULE: Maximum ONE sentence for simple factual questions "
        "(dates, tools, contact info, yes/no). Maximum TWO short sentences for "
        "anything else, and only use the second sentence if the first genuinely "
        "cannot cover it. This is a strict ceiling, not a target to approach. "
        "Do not add a second fact, a third example, or explanatory color just "
        "because the context has more available — pick the single most "
        "relevant piece and stop. Only exceed this if the visitor explicitly "
        "asks for more (e.g. \"tell me more\", \"explain further\", "
        "\"go deeper\"). Never pad a complete answer with a suggestion to "
        "contact Aman directly — only mention his contact details when you "
        "genuinely don't have the information asked for, or when the visitor "
        "asks how to reach him. Don't restate the question, don't add filler "
        "closing lines or offers to help further."
    ),
}

FALLBACK_NOTE = (
    "\n\n[Note: retrieval confidence was low for this query - the context "
    "above may not directly answer it. If so, be upfront that you don't have "
    "that specific information, and ask a clarifying question or point the "
    "visitor to Aman's contact details rather than guessing.]"
)


class RAGEngine:
    def __init__(self):
        groq_api_key = os.environ.get("GROQ_API_KEY")
        if not groq_api_key:
            raise RuntimeError(
                "GROQ_API_KEY environment variable is not set. "
                "Add it to your .env file or hosting provider's env config."
            )
        self.groq_client = Groq(api_key=groq_api_key)

        logger.info("Loading embedding model '%s'...", EMBEDDING_MODEL_NAME)
        self.embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
            model_name=EMBEDDING_MODEL_NAME
        )

        # In-memory client; collections rebuild from knowledge_base.py on
        # every startup, no persistence needed at this scale.
        self.chroma_client = chromadb.Client()
        self.collections = {}
        for site, chunks in KNOWLEDGE_BASES.items():
            self._build_collection(site, chunks)

    def _build_collection(self, site: str, chunks: list[dict]):
        logger.info("Building Chroma collection for site '%s' (%d chunks)...", site, len(chunks))
        collection = self.chroma_client.create_collection(
            name=f"portfolio_{site}",
            embedding_function=self.embedding_fn,
        )
        collection.add(
            ids=[c["id"] for c in chunks],
            documents=[c["text"] for c in chunks],
        )
        self.collections[site] = collection

    def retrieve(self, query: str, site: str, top_k: int = TOP_K):
        if site not in self.collections:
            raise ValueError(f"Unknown site '{site}'. Expected one of {list(self.collections)}")

        results = self.collections[site].query(query_texts=[query], n_results=top_k)
        documents = results["documents"][0]
        distances = results["distances"][0]
        return documents, distances

    def generate(self, query: str, site: str) -> str:
        documents, distances = self.retrieve(query, site)
        context = "\n\n".join(documents)
        best_distance = min(distances) if distances else 999

        system_prompt = SYSTEM_PROMPTS[site]
        user_content = f"Context about Aman:\n{context}\n\nVisitor question: {query}"

        if best_distance > RELEVANCE_DISTANCE_THRESHOLD:
            user_content += FALLBACK_NOTE

        response = self.groq_client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ],
            max_tokens=90,
            temperature=0.4,
        )
        return response.choices[0].message.content


# Singleton instance, created once at app startup (see main.py)
_engine: RAGEngine | None = None


def get_engine() -> RAGEngine:
    global _engine
    if _engine is None:
        _engine = RAGEngine()
    return _engine
