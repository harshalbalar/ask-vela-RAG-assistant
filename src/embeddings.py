"""Single place that decides which embedding model to use.

Set EMBEDDING_PROVIDER in .env:
  gemini : Google's gemini-embedding-001 (API, state-of-the-art, rate-limited)
  local  : a small sentence-transformers model (offline, free, no rate limit)

Switching providers changes the vector dimensions, so re-run `python -m src.ingest`
after changing it.
"""
from src.config import EMBEDDING_PROVIDER, EMBED_MODEL, LOCAL_EMBED_MODEL


def get_embeddings():
    if EMBEDDING_PROVIDER == "local":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=LOCAL_EMBED_MODEL)

    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    return GoogleGenerativeAIEmbeddings(model=EMBED_MODEL)
