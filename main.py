"""Write one AI coding-agent joke to /output/entry.txt.

One line, no trailing newline, deterministic: the same bytes on every run.
"""

import os

JOKE = "My AI agent keeps saying 'You're absolutely right!' right before doing the exact same thing again, like a golden retriever with commit access."


def main():
    # Gate rules: 1-280 Unicode chars, exactly one line, no trailing newline.
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
