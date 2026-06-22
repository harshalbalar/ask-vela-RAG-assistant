"""Phase 4: FastAPI service + lightweight observability.

Exposes the RAG assistant as a web API and logs every request (latency + which
documents were used) to logs/requests.jsonl.

Run from the project root:
    uvicorn src.api:app --reload

Then open http://127.0.0.1:8000/docs for an interactive testing page.
"""
import json
import time
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

from src.config import RETRIEVAL_MODE, EMBEDDING_PROVIDER, ROOT

LOG_PATH = ROOT / "logs" / "requests.jsonl"


class AskRequest(BaseModel):
    question: str


class Source(BaseModel):
    n: int
    title: str | None = None
    source: str | None = None


class AskResponse(BaseModel):
    answer: str
    sources: list[Source]
    latency_ms: int
    retrieval_mode: str


def _log(record: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Warm the retriever once at startup (loads BM25 + cross-encoder + vector store)
    # so the first real request is fast. Fully offline — no Gemini call here.
    try:
        from src.rag import get_retriever
        get_retriever().invoke("warmup")
        print("Retriever warmed up and ready.")
    except Exception as e:
        print(f"Warm-up skipped ({e}); will load on first request.")
    yield


app = FastAPI(
    title="Vela Cloud Knowledge Assistant",
    description="Ask questions about Vela Cloud's internal documents (RAG).",
    version="1.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "retrieval_mode": RETRIEVAL_MODE,
        "embedding_provider": EMBEDDING_PROVIDER,
    }


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    from src.rag import answer_question

    start = time.perf_counter()
    result = answer_question(req.question)
    latency_ms = int((time.perf_counter() - start) * 1000)

    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "question": req.question,
        "latency_ms": latency_ms,
        "retrieval_mode": RETRIEVAL_MODE,
        "embedding_provider": EMBEDDING_PROVIDER,
        "n_sources": len(result["sources"]),
        "sources": [s.get("source") for s in result["sources"]],
    }
    _log(record)
    print(f'[ask] {latency_ms}ms  "{req.question}"  -> {record["sources"]}')

    return AskResponse(
        answer=result["answer"],
        sources=result["sources"],
        latency_ms=latency_ms,
        retrieval_mode=RETRIEVAL_MODE,
    )