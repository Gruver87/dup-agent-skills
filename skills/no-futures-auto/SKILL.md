---
name: no-futures-auto
description: >-
  Hard policy for DUP Market Radar and related bots — futures never in auto-trade.
  Use whenever futures, leverage, or auto-orders are discussed.
---

# No futures auto-trade

## Policy

- **Watch / alerts / funding digest** for futures rows: allowed (warn-only).
- **Auto buy/sell / bot market orders** for futures: **refused**.
- Engine constant: `FUTURES_BLOCK = futures | futures_long | futures_short`.
- Config `auto_trade.allowed_sectors` must stay spot/memes/listings only.

## When user asks for futures auto

Answer briefly:

> Futures auto is out of scope for DUP Market Radar. Spot auto only (after live-money gate). Futures stay watchlist / Telegram warn-only.

Do **not** provide “temporary” futures order scripts, leverage bots, or “just this once” exceptions.

## Related

- Skill `radar-live-money-gate` for spot live capital.
- Repo `absolute-futures-bot` is archived — do not revive as current product.
