#!/usr/bin/env python3
"""Lab probe against local radar — honest SKIP if down.

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
    summarize_snapshot,
)


def main() -> int:
    base = os.environ.get("RADAR_BASE_URL", "http://127.0.0.1:8787")
    client = RadarClient(base_url=base)
    try:
        health = summarize_health(client.health())
    except RadarClientError as exc:
        print(f"SKIP radar down: {exc}")
        print(json.dumps(exc.as_dict(), indent=2))
        return 0
    print("health:", json.dumps(health, indent=2, default=str))
    try:
        snap = summarize_snapshot(client.snapshot())
        print("snapshot:", json.dumps(snap, indent=2, default=str))
    except RadarClientError as exc:
        print(f"WARN snapshot: {exc}")
        print(json.dumps(exc.as_dict(), indent=2, default=str))
    print("PASS radar_mcp_lab (read-only)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
