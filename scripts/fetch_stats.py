#!/usr/bin/env python3
"""Fetch GitHub metadata (stars, license, last push) for every source repo
in the registry and write docs/stats.json for the web UI.

Run by the weekly refresh-stats workflow (and manually). Stdlib-only.
Failed fetches keep the previous value, so a rate limit never erases data.
Set GITHUB_TOKEN for authenticated (higher-limit) requests.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "index.json"
STATS = ROOT / "docs" / "stats.json"


def fetch_repo(repo: str) -> dict | None:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "skilldex-registry-stats",
            **(
                {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
                if os.environ.get("GITHUB_TOKEN")
                else {}
            ),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.load(response)
    except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as exc:
        print(f"WARN: {repo}: {exc}", file=sys.stderr)
        return None
    return {
        "stars": data.get("stargazers_count", 0),
        "license": (data.get("license") or {}).get("spdx_id"),
        "pushed_at": (data.get("pushed_at") or "")[:10],
    }


def main() -> int:
    entries = json.loads(INDEX.read_text(encoding="utf-8"))["entries"]
    repos = sorted({e["source"]["repo"] for e in entries if e.get("source", {}).get("repo")})
    previous = {}
    if STATS.exists():
        previous = json.loads(STATS.read_text(encoding="utf-8")).get("repos", {})

    stats = {}
    for repo in repos:
        fetched = fetch_repo(repo)
        stats[repo] = fetched if fetched is not None else previous.get(repo, {})
        star_count = stats[repo].get("stars", "?")
        print(f"{repo}: {star_count} stars")

    STATS.write_text(
        json.dumps({"repos": stats}, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"Wrote {STATS.relative_to(ROOT)} ({len(stats)} repos)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
