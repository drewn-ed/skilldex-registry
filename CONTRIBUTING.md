# Contributing to skilldex-registry

Adding an entry is a one-file PR. Thank you!

## Entry format

One JSON file per entry, in the folder matching its type
(`registry/skills/`, `registry/agents/`, `registry/mcp/`), named `<id>.json`.

### Common fields (all types)

| Field | Required | Notes |
|---|---|---|
| `id` | yes | kebab-case, must match the filename |
| `type` | yes | `skill`, `agent`, or `mcp` |
| `name` | yes | Human-readable name |
| `description` | yes | One or two sentences, ≤1024 chars — this is what search matches |
| `author` | no | Person or org |
| `tags` | no | List of lowercase strings |

### Skills and subagents

```json
{
  "id": "my-skill",
  "type": "skill",
  "name": "My Skill",
  "description": "What it does and when Claude should use it.",
  "source": { "repo": "you/your-repo", "path": "skills/my-skill", "ref": "main" },
  "tags": ["example"]
}
```

`source.repo` + `source.path` point at the directory containing `SKILL.md`
(or the `.md` agent files). `ref` is optional and defaults to the repo's default branch.

### MCP servers

```json
{
  "id": "my-server",
  "type": "mcp",
  "name": "My Server",
  "description": "What tools it exposes.",
  "source": { "repo": "you/your-repo", "path": "." },
  "mcp": {
    "type": "stdio",
    "command": "uvx",
    "args": ["my-mcp-server"],
    "env": { "MY_API_KEY": "${MY_API_KEY}" }
  }
}
```

`mcp.type` is `stdio` (needs `command`), or `http`/`sse` (needs `url`).
**Never hardcode secrets** — use `${VAR}` placeholders. CI rejects anything that
looks like a real credential.

## Before opening the PR

```bash
python scripts/build_index.py   # regenerates index.json + README tables
```

Commit the regenerated files together with your entry. CI runs
`python scripts/build_index.py --check` and fails if anything is invalid or stale.

## Ground rules

- The linked project must be public and actually work with Claude Code.
- Descriptions are neutral: what it does, not marketing copy.
- One entry per PR keeps reviews fast.
