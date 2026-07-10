#!/usr/bin/env python3
"""Build index.json and the README tables from registry/**/*.json.

Usage:
    python scripts/build_index.py           # regenerate index.json and README.md
    python scripts/build_index.py --check   # CI mode: fail if invalid or out of date

Stdlib-only on purpose, so registry CI needs no dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry"
INDEX = ROOT / "index.json"
DOCS_INDEX = ROOT / "docs" / "index.json"  # served by GitHub Pages for the web UI
README = ROOT / "README.md"

START_MARKER = "<!-- REGISTRY:START -->"
END_MARKER = "<!-- REGISTRY:END -->"

TYPE_DIRS = {"skill": "skills", "agent": "agents", "mcp": "mcp"}
ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REPO_RE = re.compile(r"^[\w.-]+/[\w.-]+$")
SECRET_RE = re.compile(
    r"(sk-[A-Za-z0-9_-]{8,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[A-Z0-9]{12,}"
    r"|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{5,})"
)


def validate(entry: dict, path: Path) -> list[str]:
    errors = []
    for field in ("id", "type", "name", "description"):
        if not entry.get(field):
            errors.append(f"missing required field: {field}")
    etype = entry.get("type")
    if etype not in TYPE_DIRS:
        errors.append(f"type must be one of {sorted(TYPE_DIRS)}, got {etype!r}")
    elif path.parent.name != TYPE_DIRS[etype]:
        errors.append(f"type {etype!r} entries belong in registry/{TYPE_DIRS[etype]}/")
    eid = entry.get("id")
    if eid:
        if not ID_RE.match(str(eid)):
            errors.append(f"id {eid!r} must be kebab-case")
        if path.stem != eid:
            errors.append(f"id {eid!r} must match filename {path.name!r}")
    if len(entry.get("description") or "") > 1024:
        errors.append("description longer than 1024 characters")
    if etype in ("skill", "agent"):
        source = entry.get("source") or {}
        if not source.get("repo") or not REPO_RE.match(source.get("repo", "")):
            errors.append("source.repo must look like 'owner/repo'")
        if not source.get("path"):
            errors.append("source.path is required")
    if etype == "mcp":
        mcp = entry.get("mcp") or {}
        transport = mcp.get("type", "stdio")
        if transport == "stdio" and not mcp.get("command"):
            errors.append("mcp stdio entries need mcp.command")
        if transport in ("http", "sse") and not mcp.get("url"):
            errors.append(f"mcp {transport} entries need mcp.url")
        if transport not in ("stdio", "http", "sse"):
            errors.append(f"mcp.type {transport!r} must be stdio, http, or sse")
    if SECRET_RE.search(json.dumps(entry)):
        errors.append("entry contains what looks like a hardcoded secret")
    return errors


def load_entries() -> tuple[list[dict], list[str]]:
    entries, problems = [], []
    for path in sorted(REGISTRY.glob("*/*.json")):
        try:
            entry = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        for error in validate(entry, path):
            problems.append(f"{path.relative_to(ROOT)}: {error}")
        entries.append(entry)
    ids = [e.get("id") for e in entries]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        problems.append(f"duplicate id: {dup}")
    return entries, problems


def render_index(entries: list[dict]) -> str:
    entries = sorted(entries, key=lambda e: (e.get("type", ""), e.get("id", "")))
    return json.dumps({"version": 1, "count": len(entries), "entries": entries}, indent=2) + "\n"


def render_tables(entries: list[dict]) -> str:
    sections = []
    for etype, title in (("skill", "Skills"), ("agent", "Subagents"), ("mcp", "MCP Servers")):
        rows = sorted((e for e in entries if e.get("type") == etype), key=lambda e: e["id"])
        if not rows:
            continue
        lines = [f"### {title}", "", "| ID | Description | Source |", "|---|---|---|"]
        for e in rows:
            repo = (e.get("source") or {}).get("repo", "")
            link = f"[{repo}](https://github.com/{repo})" if repo else ""
            lines.append(f"| `{e['id']}` | {e.get('description', '')} | {link} |")
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def render_readme(entries: list[dict]) -> str:
    current = README.read_text(encoding="utf-8")
    if START_MARKER not in current or END_MARKER not in current:
        raise SystemExit(f"README.md is missing {START_MARKER} / {END_MARKER} markers")
    head, rest = current.split(START_MARKER, 1)
    _, tail = rest.split(END_MARKER, 1)
    return f"{head}{START_MARKER}\n\n{render_tables(entries)}\n\n{END_MARKER}{tail}"


def main() -> int:
    check = "--check" in sys.argv
    entries, problems = load_entries()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        return 1

    new_index = render_index(entries)
    new_readme = render_readme(entries)

    if check:
        stale = []
        for target in (INDEX, DOCS_INDEX):
            if not target.exists() or target.read_text(encoding="utf-8") != new_index:
                stale.append(str(target.relative_to(ROOT)))
        if README.read_text(encoding="utf-8") != new_readme:
            stale.append("README.md")
        if stale:
            print(
                f"ERROR: {', '.join(stale)} out of date — run: python scripts/build_index.py",
                file=sys.stderr,
            )
            return 1
        print(f"OK: {len(entries)} entries valid, index up to date")
        return 0

    INDEX.write_text(new_index, encoding="utf-8")
    DOCS_INDEX.parent.mkdir(exist_ok=True)
    DOCS_INDEX.write_text(new_index, encoding="utf-8")
    README.write_text(new_readme, encoding="utf-8")
    print(f"Wrote index.json, docs/index.json, and README.md ({len(entries)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
