# MCP radar-ops (read-only)

**Not financial advice.** Tools never place orders, enable auto, or trade futures.

## Install (Windows)

```powershell
cd C:\Users\vovun\Desktop\dup-agent-skills
.\scripts\install_mcp.ps1
```

This does `pip install -e packages/radar_mcp` so `python -m radar_mcp` works without `PYTHONPATH`.

## Cursor wiring

Repo root [`mcp.json`](../mcp.json):

```json
{
  "mcpServers": {
    "radar-ops": {
      "command": "python",
      "args": ["-m", "radar_mcp"],
      "env": {
        "RADAR_BASE_URL": "http://127.0.0.1:8787"
      }
    }
  }
}
```

Optional: set `RADAR_API_KEY` in the MCP server env (process only — never commit).

Root `mcp.json` runs `python -m radar_mcp` only — **requires** `.\scripts\install_mcp.ps1` first (no `CURSOR_PLUGIN_ROOT` PYTHONPATH dependency).

## Tools

| Tool | Radar API |
|------|-----------|
| `radar_health` | GET `/api/health` |
| `radar_ready` | GET `/api/ready` |
| `radar_snapshot_summary` | GET `/api/snapshot` |
| `radar_metrics_up` | GET `/api/metrics` |
| `radar_trade_paper_status` | GET `/api/trade/paper` |

Radar must be running (`dup-market-radar` → `.\scripts\run_radar.ps1`). If down → structured error / lab `SKIP` — no invented prices.

## Lab

```powershell
python scripts\radar_mcp_lab.py
# or
.\scripts\test_all.ps1 -WithLab
```
