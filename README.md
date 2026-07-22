# skilldex-registry

[![Validate](https://github.com/skilldex-hub/skilldex-hub.github.io/actions/workflows/validate.yml/badge.svg)](https://github.com/skilldex-hub/skilldex-hub.github.io/actions/workflows/validate.yml)

**A community registry of Claude Code skills, subagents, and MCP servers.**

**Browse it: [skilldex-hub.github.io](https://skilldex-hub.github.io/)**

Every entry is a small JSON file, validated by CI, and served as a single
machine-readable [`index.json`](index.json) consumed by the
[`skilldex`](https://github.com/skilldex-hub/skilldex) CLI:

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
| `api-and-interface-design` | Design clean, evolvable APIs and interfaces: contracts, naming, versioning, and ergonomics. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `beautiful-article` | Turn content into beautifully formatted, publication-ready articles. | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) |
| `brainstorming` | Superpowers brainstorming skill: structured idea generation before committing to a plan. | [obra/superpowers](https://github.com/obra/superpowers) |
| `brand-guidelines` | Apply consistent brand identity — colors, typography, tone — across generated content. | [anthropics/skills](https://github.com/anthropics/skills) |
| `browser-testing-with-devtools` | Test and debug web apps using browser DevTools: console, network, and performance panels. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `canvas-design` | Design visual layouts, posters, and graphics on an HTML canvas. | [anthropics/skills](https://github.com/anthropics/skills) |
| `ci-cd-and-automation` | Design reliable CI/CD pipelines: build, test, deploy stages and automation best practices. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `claude-api` | Reference for building with the Claude API: models, pricing, streaming, tool use, and caching. | [anthropics/skills](https://github.com/anthropics/skills) |
| `code-review-and-quality` | Production-grade code review skill: correctness, readability, maintainability, and review etiquette. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `code-simplification` | Simplify and reduce code: remove needless complexity while preserving behavior. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `context-engineering` | Techniques for feeding AI agents the right context: structuring repos, docs, and prompts for better results. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `crafting-effective-readmes` | Write READMEs that convert visitors into users: structure, examples, and badges. | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) |
| `database-schema-designer` | Design normalized, scalable database schemas with sensible indexing. | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) |
| `debugging-and-error-recovery` | Systematic debugging methodology: hypothesis-driven diagnosis, minimal repros, and safe recovery. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `dispatching-parallel-agents` | Coordinate parallel subagent work: decomposition and result merging. | [obra/superpowers](https://github.com/obra/superpowers) |
| `doc-coauthoring` | Structured collaborative document writing: outlines, drafts, and revision workflows. | [anthropics/skills](https://github.com/anthropics/skills) |
| `documentation-and-adrs` | Write docs that last: architecture decision records, READMEs, and API docs. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `docx` | Create and edit Microsoft Word .docx files: formatting, styles, tracked changes, and templates. | [anthropics/skills](https://github.com/anthropics/skills) |
| `executing-plans` | Superpowers skill for working through implementation plans step by step with verification. | [obra/superpowers](https://github.com/obra/superpowers) |
| `frontend-design` | Guides Claude toward distinctive, production-quality frontend interfaces instead of generic AI-styled pages. | [anthropics/skills](https://github.com/anthropics/skills) |
| `frontend-ui-engineering` | Build robust frontend interfaces: component architecture, state, styling, and performance. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `git-workflow-and-versioning` | Effective git usage: branching strategy, commit hygiene, and semantic versioning. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `golang-concurrency` | Write correct concurrent Go: goroutines, channels, sync primitives, and race avoidance. | [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) |
| `golang-design-patterns` | Go-idiomatic design patterns: interfaces, composition, and functional options. | [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) |
| `golang-error-handling` | Idiomatic Go error handling: wrapping, sentinel errors, and errors.Is/As patterns. | [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) |
| `internal-comms` | Write clear internal communications: announcements, updates, and team messages. | [anthropics/skills](https://github.com/anthropics/skills) |
| `kb-retriever` | Retrieve and synthesize answers from local knowledge bases and document collections. | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) |
| `mcp-builder` | Helps build MCP servers: protocol concepts, SDK usage, tool design, and testing guidance. | [anthropics/skills](https://github.com/anthropics/skills) |
| `mermaid-diagrams` | Create clear Mermaid diagrams: flowcharts, sequence diagrams, and architecture visuals. | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) |
| `pdf` | Extract text and tables from PDFs, create new PDFs, fill forms, and merge or split documents. | [anthropics/skills](https://github.com/anthropics/skills) |
| `performance-optimization` | Find and fix performance bottlenecks: measurement first, then targeted optimization. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `planning-and-task-breakdown` | Break large goals into ordered, estimable tasks with clear acceptance criteria. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `pptx` | Create and edit PowerPoint .pptx presentations: slides, layouts, themes, and speaker notes. | [anthropics/skills](https://github.com/anthropics/skills) |
| `qa-test-planner` | Plan test coverage: test cases, edge cases, and regression suites. | [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) |
| `requesting-code-review` | Prepare changes for review: context, scope, and reviewable diffs. | [obra/superpowers](https://github.com/obra/superpowers) |
| `security-and-hardening` | Secure coding and hardening practices: input validation, secrets, dependencies, and attack surface. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `skill-creator` | Guides Claude through authoring new skills: structure, frontmatter, progressive disclosure, and packaging. | [anthropics/skills](https://github.com/anthropics/skills) |
| `slack-gif-creator` | Create animated GIFs sized and optimized for Slack. | [anthropics/skills](https://github.com/anthropics/skills) |
| `spec-driven-development` | Write the spec first, then implement against it: tighter scope, fewer surprises. | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) |
| `systematic-debugging` | Superpowers debugging methodology: root-cause tracing, condition-based waiting, and defense in depth. | [obra/superpowers](https://github.com/obra/superpowers) |
| `taste-skill` | Gives your AI good design taste — stops generic, boring generated UIs in favor of distinctive work. | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `test-driven-development` | Superpowers TDD skill: strict red-green-refactor discipline for AI-assisted coding. | [obra/superpowers](https://github.com/obra/superpowers) |
| `theme-factory` | Generate cohesive visual themes: palettes, typography pairings, and style tokens. | [anthropics/skills](https://github.com/anthropics/skills) |
| `using-git-worktrees` | Work on multiple branches in parallel with git worktrees. | [obra/superpowers](https://github.com/obra/superpowers) |
| `verification-before-completion` | Never claim done without proof: verify behavior before reporting completion. | [obra/superpowers](https://github.com/obra/superpowers) |
| `web-artifacts-builder` | Build polished single-page web artifacts with solid layout, styling, and interactivity. | [anthropics/skills](https://github.com/anthropics/skills) |
| `web-design-engineer` | Design-engineering skill for building beautiful, well-structured web pages. | [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) |
| `webapp-testing` | Test local web applications with Playwright: navigate, interact, screenshot, and verify behavior. | [anthropics/skills](https://github.com/anthropics/skills) |
| `writing-plans` | Superpowers planning skill: turn goals into executable, verifiable implementation plans. | [obra/superpowers](https://github.com/obra/superpowers) |
| `writing-skills` | Meta-skill for authoring effective Claude Code skills. | [obra/superpowers](https://github.com/obra/superpowers) |
| `xlsx` | Create and edit Excel .xlsx spreadsheets: formulas, charts, pivot tables, and data analysis. | [anthropics/skills](https://github.com/anthropics/skills) |

### Subagents

| ID | Description | Source |
|---|---|---|
| `accessibility-compliance` | Subagents for WCAG auditing and building accessible interfaces. | [wshobson/agents](https://github.com/wshobson/agents) |
| `agent-orchestration` | Subagents for coordinating multi-agent workflows: task decomposition, delegation, and synthesis. | [wshobson/agents](https://github.com/wshobson/agents) |
| `api-scaffolding` | Subagents for designing and scaffolding REST and GraphQL APIs. | [wshobson/agents](https://github.com/wshobson/agents) |
| `application-performance` | Subagents for profiling, load testing, and performance optimization. | [wshobson/agents](https://github.com/wshobson/agents) |
| `backend-development` | Subagents for backend work: architecture, GraphQL, event sourcing, and performance engineering. | [wshobson/agents](https://github.com/wshobson/agents) |
| `core-development` | VoltAgent's core dev subagents: frontend, backend, fullstack, API designer, GraphQL and microservices architects. | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) |
| `debugging-toolkit` | Subagents for systematic debugging: error diagnosis, root-cause analysis, and fix verification. | [wshobson/agents](https://github.com/wshobson/agents) |
| `full-stack-team` | lst97's coordinated subagent team for full-stack development work. | [lst97/claude-code-sub-agents](https://github.com/lst97/claude-code-sub-agents) |
| `indie-toolkit` | Ian Nuttall's practical subagents: PRD writer, task planner, code refactorer, security auditor, content writer, vibe-coding coach. | [iannuttall/claude-agents](https://github.com/iannuttall/claude-agents) |
| `kubernetes-operations` | Subagents for K8s work: manifests, helm, cluster operations, and troubleshooting. | [wshobson/agents](https://github.com/wshobson/agents) |
| `language-specialists` | VoltAgent's language specialists: expert subagents for Python, TypeScript, Go, Rust, Java, and more. | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) |
| `llm-application-dev` | Subagents for building LLM-powered applications: prompts, RAG, evals, and agent design. | [wshobson/agents](https://github.com/wshobson/agents) |
| `python-development` | Subagents for expert Python work: idiomatic code, typing, packaging, and performance. | [wshobson/agents](https://github.com/wshobson/agents) |
| `security-scanning` | Subagents for security audits: vulnerability scanning, dependency checks, and hardening. | [wshobson/agents](https://github.com/wshobson/agents) |
| `studio-design` | Contains Studio's design subagents: UI, UX research, brand, and visual storytelling. | [contains-studio/agents](https://github.com/contains-studio/agents) |
| `studio-engineering` | Contains Studio's engineering subagents: rapid prototyping, backend, frontend, mobile, and AI engineers. | [contains-studio/agents](https://github.com/contains-studio/agents) |
| `studio-marketing` | Contains Studio's marketing subagents: growth, content, TikTok/Instagram strategy, and app store optimization. | [contains-studio/agents](https://github.com/contains-studio/agents) |
| `studio-product` | Contains Studio's product subagents: feedback synthesis, prioritization, and sprint planning. | [contains-studio/agents](https://github.com/contains-studio/agents) |
| `tdd-workflows` | Subagents for test-driven development: red-green-refactor cycles and test design. | [wshobson/agents](https://github.com/wshobson/agents) |
| `tech-experts` | 0xfurai's expert subagents for 138 technologies: React, Rust, Postgres, Kubernetes, Android, and far more. | [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) |

### MCP Servers

| ID | Description | Source |
|---|---|---|
| `antv-chart` | AntV's official MCP server: generate 25+ chart types as images from data. | [antvis/mcp-server-chart](https://github.com/antvis/mcp-server-chart) |
| `apify` | Apify's official MCP server: run 3000+ pre-built web scraping and automation actors. | [apify/actors-mcp-server](https://github.com/apify/actors-mcp-server) |
| `aws-docs` | AWS Labs' official documentation MCP server: search and read AWS docs. | [awslabs/mcp](https://github.com/awslabs/mcp) |
| `azure` | Microsoft's official Azure MCP server: manage and query Azure resources. | [microsoft/mcp](https://github.com/microsoft/mcp) |
| `azure-devops` | Microsoft's official Azure DevOps MCP server: work items, repos, builds, and boards. | [microsoft/azure-devops-mcp](https://github.com/microsoft/azure-devops-mcp) |
| `brave-search` | Brave's official MCP server: web, image, news, and video search with AI summaries. | [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server) |
| `brightdata` | Bright Data's official MCP server: web scraping that gets past blocks, plus search and structured data feeds. | [brightdata/brightdata-mcp](https://github.com/brightdata/brightdata-mcp) |
| `browserbase` | Browserbase's official MCP server: cloud headless browsers for automation at scale. | [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) |
| `browserstack` | BrowserStack's official MCP server: run tests on real devices and browsers. | [browserstack/mcp-server](https://github.com/browserstack/mcp-server) |
| `chroma` | Chroma's official MCP server: vector database for embeddings, collections, and semantic search. | [chroma-core/chroma-mcp](https://github.com/chroma-core/chroma-mcp) |
| `chrome-devtools` | Google's official MCP server for Chrome DevTools: inspect pages, debug, profile performance, and automate the browser. | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| `circleci` | CircleCI's official MCP server: find failed builds, fix flaky tests, monitor pipelines. | [CircleCI-Public/mcp-server-circleci](https://github.com/CircleCI-Public/mcp-server-circleci) |
| `clickhouse` | ClickHouse's official MCP server: run analytical SQL queries against your cluster. | [ClickHouse/mcp-clickhouse](https://github.com/ClickHouse/mcp-clickhouse) |
| `cloudflare-docs` | Cloudflare's official remote MCP server for searching Cloudflare documentation. | [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) |
| `context7` | Up-to-date, version-specific documentation and code examples for any library, injected straight into context. | [upstash/context7](https://github.com/upstash/context7) |
| `dbt` | dbt Labs' official MCP server: explore models, run transformations, and query metadata. | [dbt-labs/dbt-mcp](https://github.com/dbt-labs/dbt-mcp) |
| `e2b` | E2B's official MCP server: run code safely in cloud sandboxes. | [e2b-dev/mcp-server](https://github.com/e2b-dev/mcp-server) |
| `elasticsearch` | Elastic's official MCP server: query indices and search your Elasticsearch data. | [elastic/mcp-server-elasticsearch](https://github.com/elastic/mcp-server-elasticsearch) |
| `elevenlabs` | ElevenLabs' official MCP server: text-to-speech and voice generation. | [elevenlabs/elevenlabs-mcp](https://github.com/elevenlabs/elevenlabs-mcp) |
| `exa` | Exa's official MCP server: AI-native web search, company research, and content crawling. | [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) |
| `fetch` | Reference MCP server that fetches web pages and converts them to markdown for LLM consumption. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `figma` | Framelink's Figma MCP server: give Claude your Figma designs for accurate design-to-code. | [GLips/Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) |
| `filesystem` | Reference MCP server for secure, configurable file operations within allowed directories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `firecrawl` | Web scraping and crawling MCP server: extract clean content from any site, with search and batch crawls. | [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) |
| `git` | Reference MCP server for reading, searching, and manipulating local Git repositories. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `github` | GitHub's official remote MCP server: repos, issues, pull requests, and code search. | [github/github-mcp-server](https://github.com/github/github-mcp-server) |
| `huggingface` | Hugging Face's official remote MCP server: search models, datasets, Spaces, and papers. |  |
| `kubernetes` | MCP server for Kubernetes: manage pods, deployments, services, and cluster resources via kubectl. | [Flux159/mcp-server-kubernetes](https://github.com/Flux159/mcp-server-kubernetes) |
| `linear` | Linear's official remote MCP server: issues, projects, and team workflows. |  |
| `magic-ui` | 21st.dev's Magic MCP server: generate polished UI components from natural language. | [21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp) |
| `memory` | Reference MCP server providing a knowledge-graph-based persistent memory across sessions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `mongodb` | MongoDB's official MCP server: query collections, inspect schemas, and manage Atlas. | [mongodb-js/mongodb-mcp-server](https://github.com/mongodb-js/mongodb-mcp-server) |
| `neon` | Neon's official MCP server: manage serverless Postgres databases, branches, and queries. | [neondatabase/mcp-server-neon](https://github.com/neondatabase/mcp-server-neon) |
| `netlify` | Netlify's official MCP server: deploy sites, manage projects and environment variables. | [netlify/netlify-mcp](https://github.com/netlify/netlify-mcp) |
| `notion` | Notion's official MCP server: search, read, and write pages and databases. | [makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server) |
| `obsidian` | Work with your Obsidian vault: read, search, and edit notes via the Local REST API plugin. | [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian) |
| `playwright` | Microsoft's official MCP server for browser automation: navigate, click, fill forms, and capture accessibility snapshots. | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) |
| `postgres` | Postgres MCP Pro: safe SQL access, index tuning, explain plans, and database health checks. | [crystaldba/postgres-mcp](https://github.com/crystaldba/postgres-mcp) |
| `sentry` | Sentry's official remote MCP server: query issues, errors, and performance data. | [getsentry/sentry-mcp](https://github.com/getsentry/sentry-mcp) |
| `sequential-thinking` | Reference MCP server for structured, revisable step-by-step reasoning chains. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `serena` | Coding-agent toolkit MCP server: semantic code retrieval and editing via language servers. | [oraios/serena](https://github.com/oraios/serena) |
| `stripe` | Stripe's official agent toolkit MCP server: customers, products, invoices, and payment data. | [stripe/ai](https://github.com/stripe/ai) |
| `supabase` | Supabase's official MCP server: query databases, manage tables, and call the Management API. | [supabase/mcp](https://github.com/supabase/mcp) |
| `tavily` | Tavily's official MCP server: real-time web search and content extraction built for AI agents. | [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) |
| `time` | Reference MCP server for time and timezone conversions. | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| `twilio` | Twilio's official (alpha) MCP server: SMS, voice, and the full Twilio API surface. | [twilio-labs/mcp](https://github.com/twilio-labs/mcp) |
| `vercel` | Vercel's official remote MCP server: manage deployments, projects, and logs. |  |

<!-- REGISTRY:END -->

## License

MIT. Entry metadata describes third-party projects; each project keeps its own license.
Not affiliated with Anthropic.
