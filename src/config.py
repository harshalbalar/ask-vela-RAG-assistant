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

# Chunking + retrieval knobs (you'll tune these in Phase 2)
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
TOP_K = 4

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
