#!/usr/bin/env python3
"""Обновление документации из официальных llms.txt / llms-full.txt источников.

Usage:
    python update_docs.py          # обновить все доки
    python update_docs.py --list   # показать источники
"""
from __future__ import annotations

import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

DOCS_DIR = Path(__file__).parent / "docs"

# Формат: (имя файла, URL источника, описание)
SOURCES: list[tuple[str, str, str]] = [
    ("browser-use.md", "https://docs.browser-use.com/llms-full.txt", "Browser Use — LLM browser automation"),
    ("ruff.md", "https://docs.astral.sh/ruff/llms.txt", "Ruff — Python linter/formatter"),
    ("uv.md", "https://docs.astral.sh/uv/llms.txt", "uv — Python package manager"),
    # Добавляй новые источники здесь:
    # ("name.md", "https://example.com/llms-full.txt", "Description"),
]


def fetch(url: str) -> bytes:
    req = Request(url, headers={"User-Agent": "docs-updater/1.0"})
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def update_all() -> None:
    DOCS_DIR.mkdir(exist_ok=True)
    for filename, url, desc in SOURCES:
        path = DOCS_DIR / filename
        try:
            data = fetch(url)
            path.write_bytes(data)
            size_kb = len(data) // 1024
            print(f"  {filename:<25} {size_kb:>5} KB  <- {url}")
        except (URLError, TimeoutError) as e:
            print(f"  {filename:<25} FAILED   {e}")


def list_sources() -> None:
    for filename, url, desc in SOURCES:
        path = DOCS_DIR / filename
        status = f"{path.stat().st_size // 1024} KB" if path.exists() else "missing"
        print(f"  {filename:<25} {status:<10} {url}")
    print(f"\nВсего: {len(SOURCES)} источников")
    print("Добавить новый: отредактируй SOURCES в update_docs.py")


if __name__ == "__main__":
    if "--list" in sys.argv:
        list_sources()
    else:
        print("Обновление документации...\n")
        update_all()
        print("\nГотово.")
