# skilldex-registry

[![Validate](https://github.com/drewn-ed/skilldex-registry/actions/workflows/validate.yml/badge.svg)](https://github.com/drewn-ed/skilldex-registry/actions/workflows/validate.yml)

**A community registry of Claude Code skills, subagents, and MCP servers.**

**Browse it: [drewn-ed.github.io/skilldex-registry](https://drewn-ed.github.io/skilldex-registry/)**

Every entry is a small JSON file, validated by CI, and served as a single
machine-readable [`index.json`](index.json) consumed by the
[`skilldex`](https://github.com/drewn-ed/skilldex) CLI:

```bash
uvx skilldex search pdf
uvx skilldex install pdf
```

## Add your project (one small PR)

1. Copy an existing file from [`registry/`](registry/) as a template:
   - skills → `registry/skills/<id>.json`
   - subagents → `registry/agents/<id>.json`
   - MCP servers → `registry/mcp/<id>.json`
2. Run `python scripts/build_index.py` to regenerate `index.json` and the tables below.
3. Open a PR. CI validates your entry automatically.

Full field reference in [CONTRIBUTING.md](CONTRIBUTING.md). Never put API keys
in an entry — use `${VAR}` placeholders (CI rejects anything that looks like a secret).

## Registry

<!-- REGISTRY:START -->

### Skills

| ID | Description | Source |
|---|---|---|
| `docx` | Create and edit Microsoft Word .docx files: formatting, styles, tracked changes, and templates. | [anthropics/skills](https://github.com/anthropics/skills) |
| `frontend-design` | Guides Claude toward distinctive, production-quality frontend interfaces instead of generic AI-styled pages. | [anthropics/skills](https://github.com/anthropics/skills) |
| `mcp-builder` | Helps build MCP servers: protocol concepts, SDK usage, tool design, and testing guidance. | [anthropics/skills](https://github.com/anthropics/skills) |
| `pdf` | Extract text and tables from PDFs, create new PDFs, fill forms, and merge or split documents. | [anthropics/skills](https://github.com/anthropics/skills) |
| `pptx` | Create and edit PowerPoint .pptx presentations: slides, layouts, themes, and speaker notes. | [anthropics/skills](https://github.com/anthropics/skills) |
| `skill-creator` | Guides Claude through authoring new skills: structure, frontmatter, progressive disclosure, and packaging. | [anthropics/skills](https://github.com/anthropics/skills) |
| `webapp-testing` | Test local web applications with Playwright: navigate, interact, screenshot, and verify behavior. | [anthropics/skills](https://github.com/anthropics/skills) |
| `xlsx` | Create and edit Excel .xlsx spreadsheets: formulas, charts, pivot tables, and data analysis. | [anthropics/skills](https://github.com/anthropics/skills) |

### Subagents

| ID | Description | Source |
|---|---|---|
| `agent-orchestration` | Subagents for coordinating multi-agent workflows: task decomposition, delegation, and synthesis. | [wshobson/agents](https://github.com/wshobson/agents) |
| `backend-development` | Subagents for backend work: architecture, GraphQL, event sourcing, and performance engineering. | [wshobson/agents](https://github.com/wshobson/agents) |

### MCP Servers

| ID | Description | Source |
|---|---|---|
| `context7` | Up-to-date, version-specific documentation and code examples for any library, injected straight into context. | [upstash/context7](https://github.com/upstash/context7) |
| `fetch` | Reference MCP server that fetches web pages and converts them to markdown for LLM consumption. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `filesystem` | Reference MCP server for secure, configurable file operations within allowed directories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `git` | Reference MCP server for reading, searching, and manipulating local Git repositories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `github` | GitHub's official remote MCP server: repos, issues, pull requests, and code search. | [github/github-mcp-server](https://github.com/github/github-mcp-server) |
| `memory` | Reference MCP server providing a knowledge-graph-based persistent memory across sessions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `playwright` | Microsoft's official MCP server for browser automation: navigate, click, fill forms, and capture accessibility snapshots. | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| `sequential-thinking` | Reference MCP server for structured, revisable step-by-step reasoning chains. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `time` | Reference MCP server for time and timezone conversions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |

<!-- REGISTRY:END -->

## License

MIT. Entry metadata describes third-party projects; each project keeps its own license.
Not affiliated with Anthropic.
