#!/usr/bin/env python3
"""Publish markdown files to Telegraph via API."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import markdown
import requests
import yaml

TELEGRAPH_API = "https://api.telegra.ph"
SCRIPT_DIR = Path(__file__).parent
TOKEN_FILE = SCRIPT_DIR / ".telegraph_token"
PAGES_FILE = SCRIPT_DIR / ".telegraph_pages.json"

ACCOUNT_SHORT_NAME = "Notes"
ACCOUNT_AUTHOR_NAME = "mazamaka"
ACCOUNT_AUTHOR_URL = "https://github.com/mazamaka"

# Telegraph поддерживает только эти теги
ALLOWED_TAGS = frozenset({
    "a", "aside", "b", "blockquote", "br", "code", "em", "figcaption",
    "figure", "h3", "h4", "hr", "i", "iframe", "img", "li", "ol",
    "p", "pre", "s", "strong", "u", "ul", "video",
})

# Маппинг неподдерживаемых heading-тегов
HEADING_MAP: dict[str, str] = {
    "h1": "h3",
    "h2": "h3",
    "h5": "h4",
    "h6": "h4",
}


class TelegraphAPIError(Exception):
    """Telegraph API returned an error."""


def telegraph_request(method: str, **params: Any) -> dict[str, Any]:
    """Make a request to Telegraph API and return result."""
    resp = requests.post(f"{TELEGRAPH_API}/{method}", json=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    if not data.get("ok"):
        raise TelegraphAPIError(data.get("error", "Unknown Telegraph API error"))
    return data["result"]


def get_or_create_token() -> str:
    """Load token from file or create a new Telegraph account."""
    if TOKEN_FILE.exists():
        token = TOKEN_FILE.read_text().strip()
        if token:
            return token

    result = telegraph_request(
        "createAccount",
        short_name=ACCOUNT_SHORT_NAME,
        author_name=ACCOUNT_AUTHOR_NAME,
        author_url=ACCOUNT_AUTHOR_URL,
    )
    token: str = result["access_token"]
    TOKEN_FILE.write_text(token)
    return token


def load_pages_map() -> dict[str, str]:
    """Load mapping {md_file_path: telegraph_page_path}."""
    if PAGES_FILE.exists():
        return json.loads(PAGES_FILE.read_text())
    return {}


def save_pages_map(pages: dict[str, str]) -> None:
    """Save pages mapping to disk."""
    PAGES_FILE.write_text(json.dumps(pages, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Markdown -> Telegraph Nodes
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """Extract YAML front matter and return (metadata, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    body = text[match.end():]
    return meta, body


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML string."""
    extensions = ["tables", "fenced_code", "codehilite", "nl2br"]
    extension_configs = {
        "codehilite": {"use_pygments": False},
    }
    return markdown.markdown(
        md_text,
        extensions=extensions,
        extension_configs=extension_configs,
    )


def table_to_text(html: str) -> str:
    """Convert HTML tables to plain-text paragraphs before node parsing.

    Telegraph does not support <table>. We extract cell text row by row
    and replace each table with a series of <p> tags.
    """
    table_pattern = re.compile(r"<table.*?>(.+?)</table>", re.DOTALL)

    def _replace_table(m: re.Match[str]) -> str:
        table_html = m.group(1)
        rows: list[str] = []
        for row_match in re.finditer(r"<tr.*?>(.*?)</tr>", table_html, re.DOTALL):
            cells = re.findall(r"<t[hd].*?>(.*?)</t[hd]>", row_match.group(1), re.DOTALL)
            cells_clean = [re.sub(r"<[^>]+>", "", c).strip() for c in cells]
            if cells_clean:
                rows.append(" | ".join(cells_clean))
        return "".join(f"<p>{row}</p>" for row in rows)

    return table_pattern.sub(_replace_table, html)


class HtmlToNodesParser(HTMLParser):
    """Parse HTML string into Telegraph Node list (JSON-compatible)."""

    def __init__(self) -> None:
        super().__init__()
        self._stack: list[dict[str, Any]] = []
        self._result: list[Any] = []
        self._current_target: list[Any] = self._result

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        # Remap headings
        tag = HEADING_MAP.get(tag, tag)

        # Skip unsupported tags — push content to parent
        if tag not in ALLOWED_TAGS:
            return

        node: dict[str, Any] = {"tag": tag}
        if attrs:
            filtered = {k: v for k, v in attrs if v is not None and k in ("href", "src")}
            if filtered:
                node["attrs"] = filtered

        node["children"] = []
        self._current_target.append(node)
        self._stack.append(node)
        self._current_target = node["children"]

    def handle_endtag(self, tag: str) -> None:
        tag = HEADING_MAP.get(tag, tag)
        if tag not in ALLOWED_TAGS:
            return
        if not self._stack:
            return

        finished = self._stack.pop()
        # Remove empty children list
        if not finished["children"]:
            del finished["children"]

        if self._stack:
            self._current_target = self._stack[-1]["children"]
        else:
            self._current_target = self._result

    def handle_data(self, data: str) -> None:
        if data:
            self._current_target.append(data)

    def get_nodes(self) -> list[Any]:
        return self._result


def html_to_nodes(html: str) -> list[Any]:
    """Convert HTML string to Telegraph Node list."""
    parser = HtmlToNodesParser()
    parser.feed(html)
    return parser.get_nodes()


def md_file_to_telegraph(file_path: Path) -> tuple[str, list[Any]]:
    """Read MD file and return (title, telegraph_nodes)."""
    raw = file_path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(raw)

    title = meta.get("title", "")
    if not title:
        # Попробуем взять первый h1
        h1_match = re.match(r"^#\s+(.+)", body, re.MULTILINE)
        title = h1_match.group(1).strip() if h1_match else file_path.stem

    html = md_to_html(body)
    html = table_to_text(html)
    nodes = html_to_nodes(html)

    # Если nodes пустые или первый элемент — не блочный, обернуть в <p>
    if not nodes:
        nodes = [{"tag": "p", "children": ["(empty)"]}]

    return title, nodes


# ---------------------------------------------------------------------------
# Publish / Update
# ---------------------------------------------------------------------------

def publish(file_path: Path) -> str:
    """Publish or update a markdown file on Telegraph. Returns URL."""
    token = get_or_create_token()
    title, content = md_file_to_telegraph(file_path)
    pages = load_pages_map()

    file_key = str(file_path.resolve())

    if file_key in pages:
        # Update existing page
        page_path = pages[file_key]
        result = telegraph_request(
            "editPage",
            access_token=token,
            path=page_path,
            title=title,
            content=content,
            author_name=ACCOUNT_AUTHOR_NAME,
            author_url=ACCOUNT_AUTHOR_URL,
        )
        url: str = result["url"]
        print(f"Updated: {url}")
    else:
        # Create new page
        result = telegraph_request(
            "createPage",
            access_token=token,
            title=title,
            content=content,
            author_name=ACCOUNT_AUTHOR_NAME,
            author_url=ACCOUNT_AUTHOR_URL,
            return_content=False,
        )
        url = result["url"]
        pages[file_key] = result["path"]
        save_pages_map(pages)
        print(f"Published: {url}")

    return url


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python publish_telegraph.py <path_to_md_file>", file=sys.stderr)
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}", file=sys.stderr)
        sys.exit(1)
    if not file_path.suffix.lower() == ".md":
        print(f"Expected .md file, got: {file_path.suffix}", file=sys.stderr)
        sys.exit(1)

    publish(file_path)


if __name__ == "__main__":
    main()
