# MCP radar-ops (read-only)

**Not financial advice.** Tools never place orders, enable auto, or trade futures.

## Install (Windows)

```powershell
cd C:\Users\vovun\Desktop\dup-agent-skills
.\scripts\install_mcp.ps1
```

This does `pip install -e packages/radar_mcp` so `python -m radar_mcp` works without `PYTHONPATH`.

## Cursor wiring

Repo root [`mcp.json`](../mcp.json) launches `scripts/run_radar_mcp.ps1`, which loads `RADAR_API_KEY` / `RADAR_BASE_URL` from sibling `dup-market-radar/.env` (**never** commits secrets, never prints values).

```powershell
# Lab in current shell (values hidden):
.\scripts\load_radar_env.ps1
python scripts\radar_mcp_lab.py
```

Requires `.\scripts\install_mcp.ps1` first. If Cursor does not expand `${CURSOR_PLUGIN_ROOT}`, point the MCP File path at this repo’s `scripts/run_radar_mcp.ps1` absolutely or open the plugin from this folder.

## Tools

| Tool | Radar API |
|------|-----------|
| `radar_health` | GET `/api/health` |
| `radar_ready` | GET `/api/ready` |
| `radar_snapshot_summary` | GET `/api/snapshot` |
| `radar_metrics_up` | GET `/api/metrics` |
| `radar_trade_paper_status` | GET `/api/trade/paper` |
| `radar_trade_status` | GET `/api/trade/status` (read-only; never toggles auto) |
| `radar_telegram_status` | GET `/api/telegram/status` (no tokens) |
| `radar_recovery_status` | GET `/api/ops/recovery` (not a soak claim) |

Radar must be running (`dup-market-radar` → `.\scripts\run_radar.ps1`). If down → structured error / lab `SKIP` — no invented prices.

## Lab

```powershell
python scripts\radar_mcp_lab.py
# or
.\scripts\test_all.ps1 -WithLab
```
