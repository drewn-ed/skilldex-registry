# skilldex-registry

**A community registry of Claude Code skills, subagents, and MCP servers.**

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
| `mcp-builder` | Helps build MCP servers: protocol concepts, SDK usage, tool design, and testing guidance. | [anthropics/skills](https://github.com/anthropics/skills) |
| `pdf` | Extract text and tables from PDFs, create new PDFs, fill forms, and merge or split documents. | [anthropics/skills](https://github.com/anthropics/skills) |
| `skill-creator` | Guides Claude through authoring new skills: structure, frontmatter, progressive disclosure, and packaging. | [anthropics/skills](https://github.com/anthropics/skills) |

### Subagents

| ID | Description | Source |
|---|---|---|
| `agent-orchestration` | Subagents for coordinating multi-agent workflows: task decomposition, delegation, and synthesis. | [wshobson/agents](https://github.com/wshobson/agents) |

### MCP Servers

| ID | Description | Source |
|---|---|---|
| `fetch` | Reference MCP server that fetches web pages and converts them to markdown for LLM consumption. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `filesystem` | Reference MCP server for secure, configurable file operations within allowed directories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `github` | GitHub's official remote MCP server: repos, issues, pull requests, and code search. | [github/github-mcp-server](https://github.com/github/github-mcp-server) |

<!-- REGISTRY:END -->

## License

MIT. Entry metadata describes third-party projects; each project keeps its own license.
Not affiliated with Anthropic.
