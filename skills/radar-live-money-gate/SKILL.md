---
name: radar-live-money-gate
description: >-
  Preflight before DUP Market Radar live spot capital. Fail-closed checklist;
  never enable futures auto. Use when user asks to go live or dry_run false.
---

# Live money gate (spot only)

## Hard rules

1. Default lab config stays `auto_trade.dry_run: true` until overlay/profile.
2. Activate with `RADAR_PROFILE=live-money` + filled `.env` — see `dup-market-radar/docs/LIVE_MONEY.md`.
3. **Futures auto is forbidden** (`FUTURES_BLOCK`). Do not suggest enabling futures sectors for auto.
4. Do not commit `.env`. Do not print secret values.

## Checklist (in order)

1. `.\scripts\go_ready.ps1` → `ops_ready=true`
2. Native prefer+fail_closed available (`radar_native`)
3. `.env`: `KUCOIN_API_KEY` / `SECRET` / `PASSPHRASE` (Spot Trade + IP whitelist)
4. `.env`: `RADAR_API_KEY` + `RADAR_REQUIRE_API_KEY=1`
5. `.\scripts\go_live_money.ps1` → PASS
6. Run: `$env:RADAR_PROFILE='live-money'; .\scripts\run_radar.ps1`
7. Dashboard: confirm `ok=true`, `mtf_ensure_ok=true`, then Auto ON only if operator asks
8. Keep size caps small (overlay default 5 USDT)

## Rollback

Unset `RADAR_PROFILE` or Auto OFF immediately. Stops still run on degrade when bags are open.

## Refuse

- Flipping `dry_run: false` in `config/default.yaml` as the primary path (use profile overlay).
- “Just enable auto” without keys / go_live PASS.
