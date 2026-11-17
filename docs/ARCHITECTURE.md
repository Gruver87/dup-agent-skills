# Architecture — DUP Agent Skills

## Layers

```text
Agent (Cursor / Claude Code)
  → Agent Skills (SKILL.md + references/)
  → optional MCP radar-ops (stdio)
      → HTTP GET only → dup-market-radar :8787
```

## Skills

Canonical packs live in `skills/<name>/SKILL.md` (Agent Skills / agentskills.io).

- Frontmatter: `name` (= folder), `description` (WHAT+WHEN), `license`, optional `compatibility` / `metadata`
- Progressive disclosure: long matrices in `references/`
- Discovery mirror: `.agents/skills/` via `scripts/sync_agents_skills.ps1`

## Plugin

| File | Role |
|------|------|
| `plugin.json` | Agent Plugins schema |
| `.cursor-plugin/plugin.json` | Cursor plugin manifest |
| `mcp.json` | MCP server wiring |

Version pin: **0.1.2** (plugin / package semver).

## MCP `radar-ops`

Package: `packages/radar_mcp` (Python, stdio, FastMCP).

| Tool | Endpoint |
|------|----------|
| `radar_health` | GET `/api/health` |
| `radar_ready` | GET `/api/ready` |
| `radar_snapshot_summary` | GET `/api/snapshot` |
| `radar_metrics_up` | GET `/api/metrics` |
| `radar_trade_paper_status` | GET `/api/trade/paper` |

Auth: `RADAR_API_KEY` from process env only. Fail-closed on unreachable radar.  
Install: `scripts/install_mcp.ps1` (editable pip). Detail: [`MCP.md`](MCP.md).

**Out of scope:** POST trade/order, enable auto, futures.

## Validation

`scripts/validate_skills.py` — name match, description length, license, body size, `.agents` mirror.
