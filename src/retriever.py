"""Phase 2 retrieval strategies — implemented directly (no langchain.retrievers).

LangChain 1.x removed `langchain.retrievers`, so instead of depending on its
moved wrapper classes we implement the two core techniques ourselves:

  - Reciprocal Rank Fusion (RRF) to combine BM25 (keyword) + dense (semantic)
  - a cross-encoder re-ranker to re-score the fused candidates

Modes:
  dense   : semantic only (Phase 1 baseline)
  hybrid  : BM25 + dense, fused with RRF
  rerank  : hybrid candidates re-scored by a local cross-encoder (full Phase 2)

Dense reuses the Chroma index you already built. BM25 and the cross-encoder run
locally and free.
"""
import re

from langchain_chroma import Chroma
from rank_bm25 import BM25Okapi

from src.config import (
    VECTOR_DB_DIR, COLLECTION_NAME, TOP_K,
    CANDIDATE_K, HYBRID_DENSE_WEIGHT, RERANKER_MODEL,
)
from src.embeddings import get_embeddings
from src.loader import load_documents, split_documents

_TOKEN = re.compile(r"[a-z0-9]+")


def _tok(text: str):
    """Tokenize on alphanumerics so 'OKTA-403' -> ['okta','403'] and loose
    queries like '403' or 'STR 418' still match."""
    return _TOKEN.findall(text.lower())


def _doc_key(doc):
    return f"{doc.metadata.get('source', '')}::{hash(doc.page_content)}"


# ---- lazy singletons (built once per process) ----
_vectordb = None
_chunks = None
_bm25 = None
_reranker = None


def _get_vectordb():
    global _vectordb
    if _vectordb is None:
        _vectordb = Chroma(
            persist_directory=str(VECTOR_DB_DIR),
            embedding_function=get_embeddings(),
            collection_name=COLLECTION_NAME,
        )
    return _vectordb


def _get_bm25():
    global _chunks, _bm25
    if _bm25 is None:
        _chunks = split_documents(load_documents())
        _bm25 = BM25Okapi([_tok(c.page_content) for c in _chunks])
    return _chunks, _bm25


def _get_reranker():
    global _reranker
    if _reranker is None:
        from sentence_transformers import CrossEncoder  # lazy: heavy import
        _reranker = CrossEncoder(RERANKER_MODEL)
    return _reranker


# ---- ranked candidate lists ----
def _dense_docs(query: str, k: int):
    return _get_vectordb().similarity_search(query, k=k)


def _bm25_docs(query: str, k: int):
    chunks, bm25 = _get_bm25()
    scores = bm25.get_scores(_tok(query))
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
    return [chunks[i] for i in top]


def _rrf(ranked_lists, weights, k: int = 60):
    """Weighted Reciprocal Rank Fusion of several ranked document lists."""
    scores, docs = {}, {}
    for ranking, weight in zip(ranked_lists, weights):
        for rank, doc in enumerate(ranking):
            key = _doc_key(doc)
            docs[key] = doc
            scores[key] = scores.get(key, 0.0) + weight * (1.0 / (k + rank + 1))
    ordered = sorted(scores, key=lambda key: scores[key], reverse=True)
    return [docs[key] for key in ordered]


def _rerank(query: str, candidates, top_n: int):
    ce = _get_reranker()
    pairs = [(query, d.page_content) for d in candidates]
    scores = ce.predict(pairs)
    order = sorted(range(len(candidates)), key=lambda i: scores[i], reverse=True)
    return [candidates[i] for i in order[:top_n]]


class HybridRetriever:
    """Minimal retriever exposing .invoke(query) -> list[Document]."""

    def __init__(self, mode: str = "rerank"):
        if mode not in {"dense", "hybrid", "rerank"}:
            raise ValueError(f"Unknown mode {mode!r} (use dense | hybrid | rerank)")
        self.mode = mode

    def invoke(self, query: str):
        if self.mode == "dense":
            return _dense_docs(query, TOP_K)

        fused = _rrf(
            [_dense_docs(query, CANDIDATE_K), _bm25_docs(query, CANDIDATE_K)],
            weights=[HYBRID_DENSE_WEIGHT, 1 - HYBRID_DENSE_WEIGHT],
        )
        if self.mode == "hybrid":
            return fused[:TOP_K]
        return _rerank(query, fused, TOP_K)   # rerank the full fused candidate pool


def build_retriever(mode: str = "rerank") -> HybridRetriever:
    return HybridRetriever(mode)
