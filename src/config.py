"""Central config: env loading, model names, paths, and shared constants."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Project root = one level above this file's folder (src/)
ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = Path(os.getenv("DATA_DIR", ROOT / "data" / "docs"))
VECTOR_DB_DIR = Path(os.getenv("VECTOR_DB_DIR", ROOT / ".chroma"))

CHAT_MODEL = os.getenv("CHAT_MODEL", "gemini-2.5-flash")
EMBED_MODEL = os.getenv("EMBED_MODEL", "gemini-embedding-001")

# Embedding provider: "gemini" (API, SOTA) or "local" (offline, free, no rate limit)
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "gemini")
LOCAL_EMBED_MODEL = os.getenv("LOCAL_EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2")
ACTIVE_EMBED_MODEL = EMBED_MODEL if EMBEDDING_PROVIDER == "gemini" else LOCAL_EMBED_MODEL

# Chunking + retrieval knobs (you'll tune these in Phase 2)
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 4              # final number of chunks passed to the LLM

# --- Phase 2: hybrid search + re-ranking ---
RETRIEVAL_MODE = os.getenv("RETRIEVAL_MODE", "rerank")   # dense | hybrid | rerank
CANDIDATE_K = 10            # candidates fetched (per arm) before re-ranking
HYBRID_DENSE_WEIGHT = 0.5   # ensemble weight on dense; BM25 gets the remainder
RERANKER_MODEL = os.getenv("RERANKER_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2")

COLLECTION_NAME = "vela_docs"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")


def require_api_key() -> None:
    """Fail fast with a clear message if no Gemini key is configured."""
    if not GOOGLE_API_KEY:
        raise SystemExit(
            "Missing GOOGLE_API_KEY. Copy .env.example to .env and add your "
            "Gemini key from https://aistudio.google.com/app/apikey"
        )
    # langchain-google-genai reads GOOGLE_API_KEY from the environment
    os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
