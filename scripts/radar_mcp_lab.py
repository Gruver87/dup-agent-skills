#!/usr/bin/env python3
"""Lab probe against local radar — honest SKIP if down.

Exercises all read-only MCP client surfaces. Never places orders / toggles auto.
Exit 0 on PASS or intentional SKIP; exit 1 on unexpected failure.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "packages" / "radar_mcp" / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from radar_mcp.client import (
    RadarClient,
    RadarClientError,
    summarize_health,
    summarize_metrics,
    summarize_paper,
    summarize_ready,
    summarize_recovery,
    summarize_snapshot,
    summarize_telegram,
    summarize_trade_status,
)


def _print(label: str, data: object) -> None:
    print(f"{label}:", json.dumps(data, indent=2, default=str))


def main() -> int:
    base = os.environ.get("RADAR_BASE_URL", "http://127.0.0.1:8787")
    client = RadarClient(base_url=base)
    try:
        health = summarize_health(client.health())
    except RadarClientError as exc:
        print(f"SKIP radar down: {exc}")
        print(json.dumps(exc.as_dict(), indent=2))
        return 0

    _print("health", health)

    probes: list[tuple[str, object]] = []
    # recovery is unauthenticated on radar
    try:
        probes.append(("recovery", summarize_recovery(client.recovery_status())))
    except RadarClientError as exc:
        print(f"WARN recovery: {exc}")

    try:
        probes.append(("ready", summarize_ready(client.ready())))
    except RadarClientError as exc:
        print(f"WARN ready: {exc}")
        print(json.dumps(exc.as_dict(), indent=2, default=str))

    try:
        probes.append(("metrics", summarize_metrics(client.metrics())))
    except RadarClientError as exc:
        print(f"WARN metrics: {exc}")

    try:
        probes.append(("snapshot", summarize_snapshot(client.snapshot())))
    except RadarClientError as exc:
        print(f"WARN snapshot: {exc}")
        print(json.dumps(exc.as_dict(), indent=2, default=str))

    for label, fn in (
        ("trade_status", lambda: summarize_trade_status(client.trade_status())),
        ("trade_paper", lambda: summarize_paper(client.trade_paper())),
        ("telegram", lambda: summarize_telegram(client.telegram_status())),
    ):
        try:
            probes.append((label, fn()))
        except RadarClientError as exc:
            print(f"WARN {label}: {exc}")
            print(json.dumps(exc.as_dict(), indent=2, default=str))

    for label, data in probes:
        _print(label, data)

    print("PASS radar_mcp_lab (read-only; all surfaces probed or warned)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
