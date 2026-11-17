---
name: evidence-honesty
description: >-
  Fail-closed claims for DUP Labs products — packs on disk, no invented PASS,
  no soak without approx_48h_claim_ok. Use for readiness, audit, or marketing copy.
---

# Evidence honesty

## Matrix (radar)

| Claim | Needs |
|-------|--------|
| Unit green | pytest / CI |
| Ops-ready | `READY_OPS.json` `ops_ready=true` |
| Short soak | `hard_fails=0` in soak pack (not 48h) |
| 48h soak | `approx_48h_claim_ok=true` AND `hard_fails=0` |
| Live money ready | `go_live_money.ps1` PASS + operator keys |

## L1 (dup-protocol*)

Do not mix radar packs with L1 mesh soak / tip-v2 industrial claims. Cite the correct repo and ADR/evidence docs.

## Writing rules

- Missing pack ⇒ **⏳ / not claimed** — never invent PASS.
- Prefer paths: `docs/evidence/runs/...`, `data/evidence/...`.
- After code change: do not claim 48h soak unless it was actually run.

## Refuse

- “We’re mainnet ready” without sealed diligence packs.
- Equating CI green with soak PASS.
