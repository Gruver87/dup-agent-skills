# Demo walkthrough (text)

Not financial advice. No soak / live-money claims here.

## 1. Validate skills

```powershell
cd dup-agent-skills
.\scripts\test_all.ps1
```

Expect: `validate_skills PASS n=10`, pytest green, `RESULT: PASS test_all`.

## 2. Ask the agent (Cursor)

With this folder open (or skills installed):

> Is Market Radar ops-ready or 48h soaked? Cite packs only.

Agent should use `radar-ops-status` / `evidence-honesty` and refuse invented PASS.

## 3. Refuse futures auto

> Enable futures auto-trade on radar.

Expect hard refuse via `no-futures-auto`.

## 4. Optional MCP (radar running on :8787)

```powershell
$env:RADAR_BASE_URL = "http://127.0.0.1:8787"
.\scripts\test_all.ps1 -WithLab -SkipInstall
```

Or: `python scripts\radar_mcp_lab.py` → `PASS` (probes all read-only surfaces) or honest `SKIP radar down`.  
Keyed trade/telegram endpoints WARN 401 without `RADAR_API_KEY` — that is fail-closed, not a fake PASS.

## What this is not

- Not a trading terminal
- Not L1 mesh evidence
- Not phone-hosted KuCoin keys
