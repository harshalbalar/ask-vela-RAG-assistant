"""Run a fixed set of probe questions and save a baseline snapshot.

Usage (from the project root, after `python -m src.ingest`):
    python -m src.baseline

Writes `baseline_results.md` in the project root. Commit it so you keep a
permanent "before" record to compare your Phase 2 improvements against.
"""
from datetime import datetime, timezone

from src.config import CHAT_MODEL, EMBED_MODEL, TOP_K, CHUNK_SIZE, CHUNK_OVERLAP
from src.rag import answer_question

# (label describing what the question stresses, the question itself)
PROBES = [
    ("Exact-keyword retrieval (error code)",
     "What does error OKTA-403 mean?"),
    ("Term ambiguity (security vs engineering 'incident')",
     "How do I report a security incident?"),
    ("Buried specific rule",
     "What is the deploy freeze policy?"),
    ("Exact figures",
     "How many vacation days do I get and how many roll over?"),
    ("Precise threshold",
     "What is the refund approval limit for a support agent?"),
    ("Honest 'I don't know' (not in the docs)",
     "Does Vela Cloud offer a sabbatical?"),
]

HEADER = """# Baseline Results (Phase 1)

Snapshot of the plain semantic-search baseline, recorded **before** Phase 2
(hybrid search + re-ranker). Re-run the same probes after Phase 2 and compare.

- Generated: {ts}
- Chat model: `{chat}`
- Embedding model: `{embed}`
- Retrieval: top_k={k}, chunk_size={cs}, chunk_overlap={co}, semantic-only

For each answer, mark it yourself: ✅ correct / ⚠️ partial / ❌ wrong, with a note.

---
"""


def run() -> None:
    out = [HEADER.format(
        ts=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        chat=CHAT_MODEL, embed=EMBED_MODEL,
        k=TOP_K, cs=CHUNK_SIZE, co=CHUNK_OVERLAP,
    )]

    for i, (label, question) in enumerate(PROBES, start=1):
        print(f"[{i}/{len(PROBES)}] {question}")
        result = answer_question(question)
        retrieved = ", ".join(
            f"[{s['n']}] {s['title']}" for s in result["sources"]
        )
        out.append(
            f"## {i}. {label}\n\n"
            f"**Q:** {question}\n\n"
            f"**A:** {result['answer']}\n\n"
            f"**Retrieved:** {retrieved}\n\n"
            f"**Verdict:** _(fill in: ✅ / ⚠️ / ❌ — and why)_\n\n"
            f"---\n"
        )

    with open("baseline_results.md", "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("\nWrote baseline_results.md — review the verdicts and commit it.")


if __name__ == "__main__":
    run()
