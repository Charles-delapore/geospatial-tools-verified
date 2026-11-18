#!/usr/bin/env python
"""Check relative links in the report index."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "docs" / "00-总索引.md"
LINK = re.compile(r"\]\(([^)]+)\)")


def main() -> int:
    text = INDEX.read_text(encoding="utf-8")
    missing = []
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = (INDEX.parent / target.split("#", 1)[0]).resolve()
        if not path.exists():
            missing.append(target)
    if missing:
        print("broken links:")
        for target in missing:
            print("  -", target)
        return 1
    print(f"index links ok ({len(LINK.findall(text))} links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
