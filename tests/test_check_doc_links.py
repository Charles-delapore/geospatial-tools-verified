"""Tests for the report link checker."""

from __future__ import annotations

import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _load():
    path = ROOT / "tools" / "check_doc_links.py"
    spec = importlib.util.spec_from_file_location("check_doc_links", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


checker = _load()


def test_missing_link_is_reported(tmp_path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "README.md").write_text("[x](docs/missing.md)\n", encoding="utf-8")
    assert checker.check(tmp_path)


def test_existing_link_passes(tmp_path):
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "a.md").write_text("# a\n", encoding="utf-8")
    (tmp_path / "README.md").write_text("[a](docs/a.md)\n", encoding="utf-8")
    assert checker.check(tmp_path) == []


def test_external_links_are_skipped(tmp_path):
    (tmp_path / "README.md").write_text("[x](https://example.org)\n", encoding="utf-8")
    assert checker.check(tmp_path) == []
