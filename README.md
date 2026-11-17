# DUP Agent Skills — Market Ops

**Org:** [DUP Labs](https://github.com/Gruver87) · **Author:** Uladzimir Dabranski  
**Product:** Installable [Agent Skills](https://github.com/anthropics/skills) for crypto **market ops** — not a trading bot, not an L1.

Companion to:

| Repo | Role |
|------|------|
| [`dup-market-radar`](https://github.com/Gruver87/dup-market-radar) | Watchlist / KuCoin spot ops (PWA + Telegram) |
| [`absolute-trading-bot-final`](https://github.com/Gruver87/absolute-trading-bot-final) | Research / holdout trading bot |
| [`dup-protocol`](https://github.com/Gruver87/dup-protocol) | Industrial L1 pin |
| [`dup-protocol-experimental`](https://github.com/Gruver87/dup-protocol-experimental) | R&D sandbox |

## What this is

Markdown skills your coding agent (Cursor / Claude Code / compatible) can load to:

- Talk to **Market Radar** honestly (ops-ready ≠ 48h soak ≠ live money)
- Refuse **futures auto-trade** framing
- Run fail-closed checklists before `dry_run: false`
- Draft digests / status without inventing PASS claims

**Not financial advice.** No guarantees. Keys stay on the host — skills do not embed secrets.

## Install (Cursor)

1. Clone next to your other DUP folders:

```powershell
cd $env:USERPROFILE\Desktop
git clone https://github.com/Gruver87/dup-agent-skills.git
```

2. Point the agent at `skills/` (project rule, skill path, or `@dup-agent-skills/skills/...`).
3. Prefer running radar on the host: `dup-market-radar` → `.\scripts\run_radar.ps1`.

## Skills (v0)

| Skill | Path | Purpose |
|-------|------|---------|
| `radar-ops-status` | [`skills/radar-ops-status/SKILL.md`](skills/radar-ops-status/SKILL.md) | Honest radar / go_ready / soak language |
| `radar-live-money-gate` | [`skills/radar-live-money-gate/SKILL.md`](skills/radar-live-money-gate/SKILL.md) | Preflight before live spot capital |
| `no-futures-auto` | [`skills/no-futures-auto/SKILL.md`](skills/no-futures-auto/SKILL.md) | Hard refuse futures in auto-trade advice |
| `market-digest` | [`skills/market-digest/SKILL.md`](skills/market-digest/SKILL.md) | 1h / funding / TG-style digest from radar |
| `evidence-honesty` | [`skills/evidence-honesty/SKILL.md`](skills/evidence-honesty/SKILL.md) | Claims need packs; no invented PASS |

## Honesty

- Ops-ready ≠ 48h soak PASS  
- Lab smoke ≠ mainnet  
- Skills never claim exchange fills happened without operator evidence  

See [`docs/DISCLAIMER.md`](docs/DISCLAIMER.md).

## License

MIT — see [`LICENSE`](LICENSE).
