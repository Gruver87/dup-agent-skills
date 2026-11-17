---
name: market-digest
description: >-
  Build honest 1h movers / funding / status digests using DUP Market Radar
  Telegram commands or API — no invented prices.
---

# Market digest

## Prefer live radar

If `dup-market-radar` is running (`http://127.0.0.1:8787/`):

- Telegram (allow-listed): `/digest`, `/funding`, `/status`, `/price`, `/bubbles`
- HTTP: `/api/snapshot`, `/api/health`, `/api/metrics` (respect API key if set)

## Rules

1. Integer money / bps language — no float “approx profits”.
2. If snapshot `ok=false` or stale → **refuse** digest claims; say degraded.
3. Label sources (sector, radar pin version if known).
4. Always: **not financial advice**.

## Output shape (chat)

```text
1h digest · n=<with_1h>
Gainers: …
Losers: …
Funding extremes (if asked): …
scan_ok=… age_ms=… · not advice
```

## Refuse

- Fabricating symbols/prices when radar is down.
- Turning digest into auto-order instructions.
