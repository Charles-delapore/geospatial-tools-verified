#!/usr/bin/env python
"""Check relative links in every report and index."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
ROOT_README = ROOT / "README.md"
LINK = re.compile(r"\]\(([^)]+)\)")


def main() -> int:
    missing = []
    total = 0
    for path in [ROOT_README, *sorted(DOCS.rglob("*.md"))]:
        text = path.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#",
                                  "sandbox://")):
                continue
            total += 1
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    if missing:
        print("broken links:")
        for item in missing:
            print("  -", item)
        return 1
    print(f"doc links ok ({total} relative links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

