"""Phase 3: answer-quality evaluation (LLM-as-judge), batched for tiny free quotas.

Phase 2 measured whether we RETRIEVE the right documents. This measures the
ANSWER the system writes: faithfulness (no hallucination), relevancy (answers
the question), and abstention (says "I don't know" when the docs lack the answer).

Free-tier friendly: generates each answer, then grades them ALL in ONE judge call.
Total Gemini calls = N answers + N_abstain answers + 1 batched judge.
With N=8 that's ~12 calls — under the 20/day free cap.

Usage:
    python -m src.judge
"""
import json
import re
import time
from datetime import datetime, timezone

from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import CHAT_MODEL, require_api_key
from src.rag import answer_question
from eval.eval_set_hard import ANSWERABLE, ABSTAIN

N_ANSWERABLE = 8           # answers graded (keep small for the 20/day free cap)
SLEEP_SECONDS = 12         # spacing between answer-generation calls (safe for low RPM)
ABSTAIN_PHRASE = "i don't know"

BATCH_JUDGE_PROMPT = """You are a strict grader for a question-answering system.
Below are <<N>> ITEMS. Each has a QUESTION, the CONTEXT documents the system
retrieved, and the system's ANSWER. For EACH item, score the ANSWER 0.0-1.0 on:

- faithfulness: are ALL factual claims in the ANSWER supported by the CONTEXT?
  1.0 = fully supported. Lower it for any claim not in the context (hallucination).
- relevancy: does the ANSWER directly address the QUESTION?
  1.0 = directly answers it. Lower it if off-topic, vague, or a non-answer.

Reply with ONLY a JSON array, one object per item, nothing else:
[{"item": 1, "faithfulness": 0.9, "relevancy": 1.0, "note": "short reason"}, ...]

<<ITEMS>>
"""


def _judge_batch(llm, items):
    blocks = []
    for idx, q, ctx, ans in items:
        blocks.append(f"### ITEM {idx}\nQUESTION: {q}\n\nCONTEXT:\n{ctx}\n\nANSWER: {ans}\n")
    prompt = (BATCH_JUDGE_PROMPT
              .replace("<<N>>", str(len(items)))
              .replace("<<ITEMS>>", "\n".join(blocks)))
    raw = llm.invoke(prompt).content.strip()
    raw = re.sub(r"^```(?:json)?|```$", "", raw, flags=re.MULTILINE).strip()
    data = json.loads(raw)
    out = {}
    for d in data:
        out[int(d["item"])] = (float(d["faithfulness"]), float(d["relevancy"]), str(d.get("note", "")))
    return out


def run():
    require_api_key()
    llm = ChatGoogleGenerativeAI(model=CHAT_MODEL, temperature=0)

    # --- 1) generate answers for the answerable questions ---
    answerable = ANSWERABLE[:N_ANSWERABLE]
    items, abst_rows, abst_ok = [], [], 0
    for i, (q, _gold) in enumerate(answerable, 1):
        print(f"[answer {i}/{len(answerable)}] {q}")
        res = answer_question(q)
        items.append((i, q, res["context"], res["answer"]))
        time.sleep(SLEEP_SECONDS)

    # --- 2) generate answers for the abstention questions (should refuse) ---
    for i, q in enumerate(ABSTAIN, 1):
        print(f"[abstain {i}/{len(ABSTAIN)}] {q}")
        res = answer_question(q)
        said_idk = ABSTAIN_PHRASE in res["answer"].lower()
        abst_ok += int(said_idk)
        abst_rows.append((q, said_idk))
        time.sleep(SLEEP_SECONDS)

    # --- 3) grade ALL answers in a single batched call ---
    print("judging all answers in one call...")
    scores = _judge_batch(llm, items)

    rows, f_scores, r_scores = [], [], []
    for idx, q, _ctx, _ans in items:
        f, r, note = scores.get(idx, (None, None, "(no score returned)"))
        if f is not None:
            f_scores.append(f)
            r_scores.append(r)
        rows.append((q, f, r, note))

    faith = sum(f_scores) / len(f_scores) if f_scores else 0.0
    rel = sum(r_scores) / len(r_scores) if r_scores else 0.0
    abst_acc = abst_ok / len(ABSTAIN) if ABSTAIN else 0.0

    print("\nAnswer quality")
    print("-" * 52)
    print(f"  Faithfulness    : {faith:.3f}  (no hallucination)")
    print(f"  Relevancy       : {rel:.3f}  (answers the question)")
    print(f"  Abstention acc. : {abst_acc:.3f}  ({abst_ok}/{len(ABSTAIN)} correctly refused)")

    out = ["# Answer-Quality Eval (Phase 3)", "",
           f"- Generated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",
           f"- Judge: `{CHAT_MODEL}` (batched LLM-as-judge)",
           f"- Answerable graded: {len(items)} · Abstention: {len(ABSTAIN)}",
           "",
           "| Metric | Value |", "|---|---|",
           f"| Faithfulness (no hallucination) | {faith:.3f} |",
           f"| Relevancy (answers the question) | {rel:.3f} |",
           f"| Abstention accuracy | {abst_acc:.3f} |",
           "", "## Answerable — per question", "",
           "| Question | Faithful | Relevant | Note |", "|---|---|---|---|"]
    for q, f, r, note in rows:
        fs = f"{f:.2f}" if f is not None else "—"
        rs = f"{r:.2f}" if r is not None else "—"
        out.append(f"| {q} | {fs} | {rs} | {note} |")
    out += ["", '## Abstention — should say "I don\'t know"', "",
            "| Question | Correctly refused? |", "|---|---|"]
    for q, ok in abst_rows:
        out.append(f"| {q} | {'yes' if ok else 'NO'} |")

    with open("eval/results-answers.md", "w", encoding="utf-8") as fout:
        fout.write("\n".join(out) + "\n")
    print("\nwrote eval/results-answers.md")


if __name__ == "__main__":
    run()