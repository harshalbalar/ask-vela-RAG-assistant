"""Ask the Vela Cloud knowledge assistant a question.

Usage:
    python -m src.ask "How many vacation days do I get?"   # one-shot
    python -m src.ask                                       # interactive
"""
import sys

from src.rag import answer_question


def _print_result(result: dict) -> None:
    print("\nAnswer:\n" + result["answer"])
    print("\nSources:")
    for s in result["sources"]:
        print(f"  [{s['n']}] {s['title']}  ({s['source']})")
    print()


def main() -> None:
    if len(sys.argv) > 1:
        _print_result(answer_question(" ".join(sys.argv[1:])))
        return

    print("Vela Cloud knowledge assistant (Phase 1). Type 'exit' to quit.")
    while True:
        try:
            question = input("\nAsk> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not question or question.lower() in {"exit", "quit"}:
            break
        _print_result(answer_question(question))


if __name__ == "__main__":
    main()
