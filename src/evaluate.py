"""Retrieval evaluation harness (Phase 2 — multi-mode, multi-set).

Scores a retrieval strategy on a labeled set, independent of the LLM. Run several
mode/set combinations and diff the generated eval/results-*.md reports.

Metrics (averaged, truncated to top_k so modes are comparable):
  Hit@k : a gold doc appears in the top-k
  MRR   : reciprocal rank of the first gold doc (ranking quality)
  P@k   : gold docs retrieved / docs retrieved
  R@k   : gold docs retrieved / gold docs that exist

Examples (after `python -m src.ingest`):
    python -m src.evaluate baseline                            # dense, standard set
    python -m src.evaluate dense-hard   --mode dense   --set hard
    python -m src.evaluate hybrid-hard  --mode hybrid  --set hard
    python -m src.evaluate rerank-hard  --mode rerank  --set hard
"""
import argparse
from datetime import datetime, timezone

from src.config import TOP_K, ACTIVE_EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP, RETRIEVAL_MODE
from src.retriever import build_retriever


def _load_set(name: str):
    if name == "hard":
        from eval.eval_set_hard import ANSWERABLE
        return ANSWERABLE
    from eval.eval_set import ANSWERABLE
    return ANSWERABLE


def _unique_sources(docs):
    """Ordered unique source paths; normalise Windows backslashes."""
    seen, ordered = set(), []
    for d in docs:
        src = (d.metadata.get("source") or "").replace("\\", "/")
        if src and src not in seen:
            seen.add(src)
            ordered.append(src)
    return ordered


def _first_gold_rank(retrieved, gold):
    for i, src in enumerate(retrieved, start=1):
        if src in gold:
            return i
    return None


def evaluate(tag: str, mode: str, set_name: str) -> None:
    answerable = _load_set(set_name)
    retriever = build_retriever(mode)

    rows = []
    hit = mrr = prec = rec = 0.0
    n = len(answerable)

    for question, gold in answerable:
        docs = retriever.invoke(question)
        retrieved = _unique_sources(docs)[:TOP_K]   # cap so modes compare fairly
        gold_set = set(gold)

        rank = _first_gold_rank(retrieved, gold_set)
        found = len(gold_set & set(retrieved))

        hit += 1.0 if rank else 0.0
        mrr += (1.0 / rank) if rank else 0.0
        prec += found / len(retrieved) if retrieved else 0.0
        rec += found / len(gold_set) if gold_set else 0.0
        rows.append((question, rank, retrieved))

    hit, mrr, prec, rec = hit / n, mrr / n, prec / n, rec / n

    print(f"\n[{tag}]  mode={mode}  set={set_name}  ({n} questions, top_k={TOP_K})")
    print(f"  Hit@{TOP_K}={hit:.3f}   MRR={mrr:.3f}   P@{TOP_K}={prec:.3f}   R@{TOP_K}={rec:.3f}")
    misses = [q for q, r, _ in rows if not r]
    if misses:
        print(f"  Misses ({len(misses)}):")
        for q in misses:
            print(f"    - {q}")

    out = [f"# Retrieval Eval — {tag}", "",
           f"- Generated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",
           f"- Mode: **{mode}** · Set: **{set_name}** · top_k={TOP_K}",
           f"- Embeddings: `{ACTIVE_EMBED_MODEL}` · chunk_size={CHUNK_SIZE}, overlap={CHUNK_OVERLAP}",
           "", "| Metric | Value |", "|---|---|",
           f"| Hit@{TOP_K} | {hit:.3f} |", f"| MRR | {mrr:.3f} |",
           f"| P@{TOP_K} | {prec:.3f} |", f"| R@{TOP_K} | {rec:.3f} |",
           "", "## Per-question", "",
           "| Question | First gold rank | Top retrieved |", "|---|---|---|"]
    for q, rank, top in rows:
        out.append(f"| {q} | {rank if rank else '**MISS**'} | {', '.join(top)} |")

    path = f"eval/results-{tag}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"  wrote {path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tag", nargs="?", default="baseline")
    ap.add_argument("--mode", default=RETRIEVAL_MODE, choices=["dense", "hybrid", "rerank"])
    ap.add_argument("--set", dest="set_name", default="standard", choices=["standard", "hard"])
    args = ap.parse_args()
    evaluate(args.tag, args.mode, args.set_name)
