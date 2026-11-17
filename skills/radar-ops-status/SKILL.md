---
name: radar-ops-status
description: >-
  Honest status language for DUP Market Radar — ops-ready vs short soak vs 48h
  claim vs live money. Use when the user asks if radar is ready, green, or soaked.
---

# Radar ops status (fail-closed)

## Invariants

1. **Ops-ready** = `go_ready.ps1` PASS + `READY_OPS.json` with `ops_ready=true`.  
   This is **not** a 48h soak claim.
2. **48h soak PASS** only if pack has `approx_48h_claim_ok=true` **and** `hard_fails=0`.  
   Never invent PASS from pytest alone.
3. **Live money** needs `.env` KuCoin Spot keys + `go_live_money.ps1` — separate from ops-ready.
4. Futures may appear in **watchlist / data**; they are **never** auto-traded.

## What to run (Windows, repo `dup-market-radar`)

```powershell
cd <path>\dup-market-radar
.\scripts\test_all.ps1 -SkipBuild          # gate + pytest + smokes (no 48h)
.\scripts\go_ready.ps1 -SkipBuild          # ops-ready pack
# Soak48h ONLY after explicit operator approval
```

## How to answer the user

| They say | You say |
|----------|---------|
| «всё зелёное / ready» | Cite which gate: pytest / go_ready / soak pack fields — or refuse |
| «soak passed» | Only if pack on disk says so; else **not claimed** |
| «можно на деньги» | Point to `docs/LIVE_MONEY.md` + `go_live_money.ps1`; do not flip `dry_run` silently |

## Refuse

- Painting green without command output or pack paths.
- Mixing L1 mesh soak evidence with radar packs.
