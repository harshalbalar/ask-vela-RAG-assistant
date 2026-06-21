"""Phase 1 query side: retrieve relevant chunks, answer with citations."""
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

from src.config import (
    VECTOR_DB_DIR, CHAT_MODEL, EMBED_MODEL, TOP_K, COLLECTION_NAME, RETRIEVAL_MODE, require_api_key,
)

SYSTEM_PROMPT = """You are the Vela Cloud internal knowledge assistant.
Answer the employee's question using ONLY the numbered context below, which comes
from Vela Cloud's internal documents.

Rules:
- If the answer is not contained in the context, reply exactly:
  "I don't know based on Vela Cloud's available documents."
- Do not use outside knowledge and do not guess.
- Cite the sources you used with bracketed numbers like [1] or [2] that match the context.
- Be concise and specific. Include exact figures (days, amounts, percentages) when present.

Context:
{context}
"""

PROMPT = ChatPromptTemplate.from_messages(
    [("system", SYSTEM_PROMPT), ("human", "{question}")]
)


def get_retriever():
    # Phase 2: dense / hybrid / hybrid+rerank, chosen by RETRIEVAL_MODE in .env
    from src.retriever import build_retriever
    return build_retriever(RETRIEVAL_MODE)


def _format_context(docs) -> str:
    """Number each retrieved chunk so the model can cite [1], [2], ..."""
    blocks = []
    for i, d in enumerate(docs, start=1):
        title = d.metadata.get("title", "Untitled")
        source = d.metadata.get("source", "unknown")
        blocks.append(f"[{i}] {title} ({source})\n{d.page_content}")
    return "\n\n".join(blocks)


def answer_question(question: str) -> dict:
    require_api_key()

    retriever = get_retriever()
    docs = retriever.invoke(question)
    context = _format_context(docs)

    llm = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0)
    chain = PROMPT | llm | StrOutputParser()
    answer = chain.invoke({"context": context, "question": question})

    sources = [
        {"n": i, "title": d.metadata.get("title"), "source": d.metadata.get("source")}
        for i, d in enumerate(docs, start=1)
    ]
    return {"answer": answer, "sources": sources, "context": context}
