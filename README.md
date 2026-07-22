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
| `algorithmic-art` | Create generative and algorithmic art: patterns, fractals, and procedural visuals. | [anthropics/skills](https://github.com/anthropics/skills) |
| `brand-guidelines` | Apply consistent brand identity — colors, typography, tone — across generated content. | [anthropics/skills](https://github.com/anthropics/skills) |
| `canvas-design` | Design visual layouts, posters, and graphics on an HTML canvas. | [anthropics/skills](https://github.com/anthropics/skills) |
| `claude-api` | Reference for building with the Claude API: models, pricing, streaming, tool use, and caching. | [anthropics/skills](https://github.com/anthropics/skills) |
| `doc-coauthoring` | Structured collaborative document writing: outlines, drafts, and revision workflows. | [anthropics/skills](https://github.com/anthropics/skills) |
| `docx` | Create and edit Microsoft Word .docx files: formatting, styles, tracked changes, and templates. | [anthropics/skills](https://github.com/anthropics/skills) |
| `frontend-design` | Guides Claude toward distinctive, production-quality frontend interfaces instead of generic AI-styled pages. | [anthropics/skills](https://github.com/anthropics/skills) |
| `internal-comms` | Write clear internal communications: announcements, updates, and team messages. | [anthropics/skills](https://github.com/anthropics/skills) |
| `mcp-builder` | Helps build MCP servers: protocol concepts, SDK usage, tool design, and testing guidance. | [anthropics/skills](https://github.com/anthropics/skills) |
| `pdf` | Extract text and tables from PDFs, create new PDFs, fill forms, and merge or split documents. | [anthropics/skills](https://github.com/anthropics/skills) |
| `pptx` | Create and edit PowerPoint .pptx presentations: slides, layouts, themes, and speaker notes. | [anthropics/skills](https://github.com/anthropics/skills) |
| `skill-creator` | Guides Claude through authoring new skills: structure, frontmatter, progressive disclosure, and packaging. | [anthropics/skills](https://github.com/anthropics/skills) |
| `slack-gif-creator` | Create animated GIFs sized and optimized for Slack. | [anthropics/skills](https://github.com/anthropics/skills) |
| `theme-factory` | Generate cohesive visual themes: palettes, typography pairings, and style tokens. | [anthropics/skills](https://github.com/anthropics/skills) |
| `web-artifacts-builder` | Build polished single-page web artifacts with solid layout, styling, and interactivity. | [anthropics/skills](https://github.com/anthropics/skills) |
| `webapp-testing` | Test local web applications with Playwright: navigate, interact, screenshot, and verify behavior. | [anthropics/skills](https://github.com/anthropics/skills) |
| `xlsx` | Create and edit Excel .xlsx spreadsheets: formulas, charts, pivot tables, and data analysis. | [anthropics/skills](https://github.com/anthropics/skills) |

### Subagents

| ID | Description | Source |
|---|---|---|
| `accessibility-compliance` | Subagents for WCAG auditing and building accessible interfaces. | [wshobson/agents](https://github.com/wshobson/agents) |
| `agent-orchestration` | Subagents for coordinating multi-agent workflows: task decomposition, delegation, and synthesis. | [wshobson/agents](https://github.com/wshobson/agents) |
| `api-scaffolding` | Subagents for designing and scaffolding REST and GraphQL APIs. | [wshobson/agents](https://github.com/wshobson/agents) |
| `application-performance` | Subagents for profiling, load testing, and performance optimization. | [wshobson/agents](https://github.com/wshobson/agents) |
| `backend-development` | Subagents for backend work: architecture, GraphQL, event sourcing, and performance engineering. | [wshobson/agents](https://github.com/wshobson/agents) |

### MCP Servers

| ID | Description | Source |
|---|---|---|
| `chrome-devtools` | Google's official MCP server for Chrome DevTools: inspect pages, debug, profile performance, and automate the browser. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| `context7` | Up-to-date, version-specific documentation and code examples for any library, injected straight into context. | [upstash/context7](https://github.com/upstash/context7) |
| `fetch` | Reference MCP server that fetches web pages and converts them to markdown for LLM consumption. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `filesystem` | Reference MCP server for secure, configurable file operations within allowed directories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `firecrawl` | Web scraping and crawling MCP server: extract clean content from any site, with search and batch crawls. | [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) |
| `git` | Reference MCP server for reading, searching, and manipulating local Git repositories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `github` | GitHub's official remote MCP server: repos, issues, pull requests, and code search. | [github/github-mcp-server](https://github.com/github/github-mcp-server) |
| `memory` | Reference MCP server providing a knowledge-graph-based persistent memory across sessions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `notion` | Notion's official MCP server: search, read, and write pages and databases. | [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) |
| `playwright` | Microsoft's official MCP server for browser automation: navigate, click, fill forms, and capture accessibility snapshots. | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| `sentry` | Sentry's official remote MCP server: query issues, errors, and performance data. | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) |
| `sequential-thinking` | Reference MCP server for structured, revisable step-by-step reasoning chains. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `serena` | Coding-agent toolkit MCP server: semantic code retrieval and editing via language servers. | [oraios/serena](https://github.com/oraios/serena) |
| `stripe` | Stripe's official agent toolkit MCP server: customers, products, invoices, and payment data. | [stripe/ai](https://github.com/stripe/ai) |
| `supabase` | Supabase's official MCP server: query databases, manage tables, and call the Management API. | [supabase/mcp](https://github.com/supabase/mcp) |
| `time` | Reference MCP server for time and timezone conversions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |

<!-- REGISTRY:END -->

## License

MIT. Entry metadata describes third-party projects; each project keeps its own license.
Not affiliated with Anthropic.
