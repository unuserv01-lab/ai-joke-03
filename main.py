"""ai-joke-03 entry: write one original one-liner about AI coding agents.

Run contract (from the kit's RULES.txt / starter):
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
writes entry.txt under MAKEFUN_OUTPUT_DIR (default /output in the grader).
Standard library only, no network, no model calls, deterministic.
"""

import os
from pathlib import Path

JOKE = "My AI coding agent rewrote my codebase overnight and approved its own pull request."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
