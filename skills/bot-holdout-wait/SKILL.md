---
name: bot-holdout-wait
description: >-
  absolute-trading-bot holdout discipline — do not retune until the holdout
  date. Use when the user asks to retune, optimize, or change strategy before
  the frozen evaluation window ends.
license: MIT
compatibility: absolute-trading-bot-final checkout; consult HOLD_OUT / freeze docs in that repo.
metadata:
  author: dup-labs
  version: "0.1.0"
  product: absolute-trading-bot
---

# Bot holdout wait

## When to Use

- Retune / optimize / “улучши стратегию” on absolute-trading-bot before holdout ends

## Policy

1. Find the holdout / freeze date and freeze commit in that repo’s docs.
2. Until that date: **observe only** — no parameter hunt that invalidates the holdout.
3. After holdout: retune only with a new labeled experiment + evidence.

## Answer template

> Holdout is active until &lt;date&gt;. No retune. Log observations only; next experiment starts after the window with a new evidence folder.

## Refuse

- Silent hyperparameter search during holdout.
- Claiming improved expectancy without a post-holdout pack.
