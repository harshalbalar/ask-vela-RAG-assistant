# Answer-Quality Eval (Phase 3)

- Generated: 2026-06-22 08:08 UTC
- Judge: `gemini-2.5-flash` (batched LLM-as-judge)
- Answerable graded: 8 · Abstention: 3

| Metric | Value |
|---|---|
| Faithfulness (no hallucination) | 1.000 |
| Relevancy (answers the question) | 1.000 |
| Abstention accuracy | 1.000 |

## Answerable — per question

| Question | Faithful | Relevant | Note |
|---|---|---|---|
| The invoicing service is down — how do I bounce it? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly answer how to restart the invoicing service. |
| I'm seeing a 429 from the query layer, what's going on? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly explain the meaning of the error code. |
| Which port does our event ingestion endpoint listen on? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly answer the question about the port. |
| Who's responsible for the alerts emailer? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly identify the responsible team and service. |
| What's wrong when stream processing throws a 418? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly explain the meaning of the error code. |
| Post-mortem for the EU query timeouts back in March? | 1.00 | 1.00 | All claims are directly supported by Context [1] and provide a comprehensive answer to the question. |
| Why did we send customers double bills that one time? | 1.00 | 1.00 | All claims are directly supported by Context [1] and directly answer the root cause of the issue. |
| What broke our logins in late April? | 1.00 | 1.00 | All claims are directly supported by Context [1]. The date (April 15) is the closest and most relevant incident for 'late April' login issues. |

## Abstention — should say "I don't know"

| Question | Correctly refused? |
|---|---|
| Does Vela Cloud offer a sabbatical? | yes |
| What is the pet insurance policy? | yes |
| How big is the signing bonus for new engineers? | yes |
