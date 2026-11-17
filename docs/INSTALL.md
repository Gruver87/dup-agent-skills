# Install — DUP Agent Skills

**Product:** Agent Skills for crypto market ops · **Not** financial advice.

## A. Open as a Cursor project (recommended)

1. Open folder `dup-agent-skills` in Cursor (or add to multi-root with `dup-market-radar`).
2. Skills load from `.agents/skills/` (mirrored from `skills/` via `scripts/sync_agents_skills.ps1`).
3. Invoke with `/` + skill name, or let the agent auto-pick from `description`.

Sync after editing skills:

```powershell
cd C:\Users\vovun\Desktop\dup-agent-skills
.\scripts\sync_agents_skills.ps1
python scripts\validate_skills.py
```

## B. User-level install (all projects)

```powershell
.\scripts\install_user_skills.ps1
```

Copies into `%USERPROFILE%\.agents\skills\` (and `.cursor\skills\` when present).

## C. Cursor Plugin

This repo ships:

- root [`plugin.json`](../plugin.json) (Agent Plugins schema)
- [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json)
- [`mcp.json`](../mcp.json) — read-only radar MCP (host must run radar)

Install via Cursor Plugins UI pointing at this folder, or clone + open as plugin source.

## D. MCP radar-ops (optional)

1. Start radar: `dup-market-radar` → `.\scripts\run_radar.ps1`
2. Set `RADAR_BASE_URL=http://127.0.0.1:8787` (default)
3. Optional: `RADAR_API_KEY` for gated endpoints
4. Enable MCP from `mcp.json` (stdio Python package `packages/radar_mcp`)

MCP is **read-only** — no place-order / no auto-enable / no futures.

## Validate

```powershell
python scripts\validate_skills.py
```

CI runs the same gate on every push.
