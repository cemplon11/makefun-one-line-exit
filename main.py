#!/usr/bin/env python3
"""The One-Line Exit — make.fun bounty entry.

Writes one funny one-line resignation letter (1-140 chars, UTF-8,
no trailing newline) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).

Pure Python standard library. Deterministic: the same line every run.
"""

import os

LINE = (
    "Dear boss: I'm resigning effective immediately, because my "
    "houseplants get more sunlight, water, and respect than I do here."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise SystemExit(f"entry line is {len(LINE)} chars, must be 1-140")
    encoded = LINE.encode("utf-8")
    if not 1 <= len(encoded) <= 140:
        raise SystemExit(f"entry line is {len(encoded)} UTF-8 bytes, must be 1-140")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
