# radar-mcp

Read-only MCP (stdio) for [DUP Market Radar](https://github.com/Gruver87/dup-market-radar).

**Tools:** `radar_health`, `radar_ready`, `radar_snapshot_summary`, `radar_metrics_up`, `radar_trade_paper_status`.

**Never:** place order, enable auto, futures.

```powershell
$env:RADAR_BASE_URL = "http://127.0.0.1:8787"
$env:RADAR_API_KEY = "<optional>"
python -m radar_mcp
```

Lab: `python scripts/radar_mcp_lab.py`
