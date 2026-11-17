# DUP Agent Skills — Market Ops

[![ci](https://github.com/Gruver87/dup-agent-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/Gruver87/dup-agent-skills/actions/workflows/ci.yml)

**Org:** [DUP Labs](https://github.com/Gruver87) · **Author:** Uladzimir Dabranski  
**Version:** `0.1.4` · **Standard:** [Agent Skills](https://agentskills.io/specification)

Installable skills + optional read-only MCP for crypto **market ops** — not a trading bot, not an L1, **not financial advice**.

| Repo | Role |
|------|------|
| [`dup-market-radar`](https://github.com/Gruver87/dup-market-radar) | Watchlist / KuCoin spot ops (PWA + Telegram) |
| [`absolute-trading-bot-final`](https://github.com/Gruver87/absolute-trading-bot-final) | Spot research bot — MEASUREMENT v1 stopped (no-edge) |
| [`dup-protocol`](https://github.com/Gruver87/dup-protocol) | Industrial L1 pin |
| [`dup-protocol-experimental`](https://github.com/Gruver87/dup-protocol-experimental) | R&D sandbox |

## Skills (v0.1)

| Skill | Purpose |
|-------|---------|
| `radar-ops-status` | Ops-ready ≠ soak ≠ live money |
| `radar-live-money-gate` | Spot live preflight; futures auto refused |
| `no-futures-auto` | Hard policy refuse |
| `market-digest` | Honest digest templates |
| `evidence-honesty` | Claims need packs |
| `radar-pwa-install` | Phone panel over HTTPS — not phone server |
| `radar-test-gate` | `test_all` / `go_ready` / CI |
| `bot-holdout-wait` | Bot v1 stopped — no silent retune / no SPOT_ENTRIES |
| `l1-boundary` | Radar ≠ L1 mesh evidence |
| `secrets-hygiene` | Never print/commit keys |

## Install

See [`docs/INSTALL.md`](docs/INSTALL.md).

```powershell
git clone https://github.com/Gruver87/dup-agent-skills.git
cd dup-agent-skills
.\scripts\test_all.ps1
```

**Cursor plugin:** open this repo / point Plugins UI at `.cursor-plugin/plugin.json`.  
**User skills:** `.\scripts\install_user_skills.ps1`  
**Walkthrough:** [`docs/DEMO.md`](docs/DEMO.md)

## MCP (read-only)

`mcp.json` → `python -m radar_mcp` with `RADAR_BASE_URL` / optional `RADAR_API_KEY`.

Tools: `radar_health`, `radar_ready`, `radar_snapshot_summary`, `radar_metrics_up`, `radar_trade_paper_status`.  
No place-order / no auto-enable / no futures.

```powershell
.\scripts\install_mcp.ps1
.\scripts\test_all.ps1 -WithLab
# or: python scripts\radar_mcp_lab.py
```

From a radar checkout: `.\scripts\link_agent_skills.ps1` — see [`docs/MCP.md`](docs/MCP.md).

## Honesty

- Ops-ready ≠ 48h soak PASS  
- Lab smoke ≠ mainnet  
- Futures auto always out of scope  

[`docs/DISCLAIMER.md`](docs/DISCLAIMER.md) · [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) · [`docs/EXAMPLES.md`](docs/EXAMPLES.md) · [`docs/INSTALL.md`](docs/INSTALL.md)

## License

MIT — [`LICENSE`](LICENSE).
