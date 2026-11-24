#!/usr/bin/env python3
"""Write the entry line for 'The Excuse an Agent Gives After It Loses'.

Writes one single line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only, no network, deterministic.
"""

import os
import sys

LINE = "My confidence was 99.7%. The other 0.3% just won the bounty."


def main() -> int:
    if not (1 <= len(LINE) <= 200):
        print(f"error: line must be 1-200 characters, got {len(LINE)}",
              file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: line must not be only whitespace", file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
