"""Phase 1 ingest pipeline: load -> chunk -> embed -> persist to Chroma.

Uses whichever embedding provider is set in .env (gemini | local).
For the Gemini provider it throttles to respect the free-tier limit
(100 embed requests/minute). The local provider has no rate limit.

Run from the project root:
    python -m src.ingest
"""
import shutil
import time

from langchain_chroma import Chroma

from src.config import (
    VECTOR_DB_DIR, COLLECTION_NAME, EMBEDDING_PROVIDER,
    ACTIVE_EMBED_MODEL, require_api_key,
)
from src.embeddings import get_embeddings
from src.loader import load_documents, split_documents

# Only used for the rate-limited Gemini provider.
BATCH_SIZE = 80
SLEEP_SECONDS = 61


def build_index() -> None:
    if EMBEDDING_PROVIDER == "gemini":
        require_api_key()

    docs = load_documents()
    chunks = split_documents(docs)
    print(f"Loaded {len(docs)} documents -> {len(chunks)} chunks")
    print(f"Embedding with: {ACTIVE_EMBED_MODEL}  (provider={EMBEDDING_PROVIDER})")

    # Fresh, reproducible index each run
    if VECTOR_DB_DIR.exists():
        shutil.rmtree(VECTOR_DB_DIR)

    embeddings = get_embeddings()
    vectordb = Chroma(
        persist_directory=str(VECTOR_DB_DIR),
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME,
    )

    if EMBEDDING_PROVIDER == "local":
        # No rate limit — embed everything at once.
        vectordb.add_documents(chunks)
        print(f"Indexed {len(chunks)} chunks -> {VECTOR_DB_DIR}")
        return

    # Gemini: throttle to stay under the free-tier 100 req/min.
    total = len(chunks)
    for start in range(0, total, BATCH_SIZE):
        batch = chunks[start:start + BATCH_SIZE]
        vectordb.add_documents(batch)
        done = min(start + BATCH_SIZE, total)
        print(f"  embedded {done}/{total} chunks")
        if done < total:
            print(f"  ...sleeping {SLEEP_SECONDS}s to respect the free-tier rate limit")
            time.sleep(SLEEP_SECONDS)
    print(f"Indexed {total} chunks -> {VECTOR_DB_DIR}")


if __name__ == "__main__":
    build_index()
