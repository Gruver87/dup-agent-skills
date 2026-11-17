# Install — DUP Agent Skills

**Product:** Agent Skills for crypto market ops · **Not** financial advice.

## A. Open as a Cursor project (recommended)

1. Open [`dup-labs.code-workspace`](../dup-labs.code-workspace) (radar + skills + trading-bot) or this folder alone.
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
Folder names stay equal to skill `name` (no `dup-` prefix — that broke agentskills.io matching).

## C. Cursor Plugin

This repo ships:

- root [`plugin.json`](../plugin.json) (Agent Plugins schema)
- [`.cursor-plugin/plugin.json`](../.cursor-plugin/plugin.json)
- [`mcp.json`](../mcp.json) — read-only radar MCP (host must run radar)

Install via Cursor Plugins UI pointing at this folder, or clone + open as plugin source.

## D. MCP radar-ops (optional)

1. Start radar: `dup-market-radar` → `.\scripts\run_radar.ps1`
2. Install package: `.\scripts\install_mcp.ps1`
3. Prefer `mcp.json` → `scripts/run_radar_mcp.ps1` (loads `RADAR_API_KEY` from sibling radar `.env`, never prints)
4. Or lab shell: `.\scripts\load_radar_env.ps1` then `python scripts\radar_mcp_lab.py`

Full detail: [`MCP.md`](MCP.md). **Read-only** — no place-order / no auto-enable / no futures.

## E. From dup-market-radar checkout

```powershell
cd ..\dup-market-radar
.\scripts\link_agent_skills.ps1
```

See radar [`docs/AGENT_SKILLS.md`](https://github.com/Gruver87/dup-market-radar/blob/main/docs/AGENT_SKILLS.md).

## F. From absolute-trading-bot-final checkout

```powershell
cd ..\absolute-trading-bot-final
.\scripts\link_agent_skills.ps1
.\scripts\test_all.ps1
```

Policy: [`PROTOCOL_STATUS`](https://github.com/Gruver87/absolute-trading-bot-final/blob/main/docs/PROTOCOL_STATUS.md) — v1 stopped, `SPOT_ENTRIES` off.  
Bot docs: [`AGENT_SKILLS.md`](https://github.com/Gruver87/absolute-trading-bot-final/blob/main/docs/AGENT_SKILLS.md).

## G. Link both companions at once

```powershell
cd C:\Users\vovun\Desktop\dup-agent-skills
.\scripts\link_companions.ps1
```

Calls each sibling `link_agent_skills.ps1` (radar + trading bot). No soak / no live unlock.

## Validate / test gate

```powershell
.\scripts\test_all.ps1              # sync + validate + ruff + pytest
.\scripts\test_all.ps1 -WithLab     # + radar_mcp_lab (SKIP if radar down)
python scripts\validate_skills.py   # skills-only
```

CI runs validate + ruff + pytest on every push.
