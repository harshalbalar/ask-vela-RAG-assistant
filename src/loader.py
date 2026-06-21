"""Load markdown docs and split them into chunks.

This module deliberately has NO dependency on the LLM/embeddings, so the
loading + chunking logic can be tested without any API key or network.
"""
from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP


def _title_from_markdown(text: str, fallback: str) -> str:
    """Use the first H1 (`# ...`) line as a human-friendly title for citations."""
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def load_documents(data_dir: Path = DATA_DIR) -> list[Document]:
    """Read every .md file into a Document with useful metadata."""
    data_dir = Path(data_dir)
    docs: list[Document] = []
    for path in sorted(data_dir.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(data_dir)
        # Top folder (hr/engineering/...) becomes the category
        category = rel.parts[0] if len(rel.parts) > 1 else "general"
        docs.append(
            Document(
                page_content=text,
                metadata={
                    "source": str(rel),
                    "category": category,
                    "title": _title_from_markdown(text, path.stem),
                },
            )
        )
    return docs


def split_documents(docs: list[Document]) -> list[Document]:
    """Split docs on markdown structure first, then fall back to plain text."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        # Prefer splitting on headings/paragraphs so chunks stay coherent
        separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(docs)
