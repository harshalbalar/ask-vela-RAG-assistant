"""Phase 1 ingest pipeline: load -> chunk -> embed -> persist to Chroma.

Run from the project root:
    python -m src.ingest
"""
import shutil

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import VECTOR_DB_DIR, EMBED_MODEL, COLLECTION_NAME, require_api_key
from src.loader import load_documents, split_documents


def build_index() -> None:
    require_api_key()

    docs = load_documents()
    chunks = split_documents(docs)
    print(f"Loaded {len(docs)} documents -> {len(chunks)} chunks")

    # Rebuild from scratch each run for a clean, reproducible index
    if VECTOR_DB_DIR.exists():
        shutil.rmtree(VECTOR_DB_DIR)

    embeddings = GoogleGenerativeAIEmbeddings(model=EMBED_MODEL)
    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTOR_DB_DIR),
        collection_name=COLLECTION_NAME,
    )
    print(f"Indexed {len(chunks)} chunks -> {VECTOR_DB_DIR}")


if __name__ == "__main__":
    build_index()
