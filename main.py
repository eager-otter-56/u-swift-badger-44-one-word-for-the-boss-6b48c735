#!/usr/bin/env python3
"""One Word for the Boss.

Writes exactly one word describing the boss to /output/entry.txt:
"ghost" — the boss who haunts the office but is never actually seen,
only felt through 2 a.m. emails. Funny on its own, true of the absent
boss everywhere, fresh, and it travels to any workplace.
"""

import os

ENTRY = "ghost"  # 5 chars, within the 1-30 gate; exactly one word


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
