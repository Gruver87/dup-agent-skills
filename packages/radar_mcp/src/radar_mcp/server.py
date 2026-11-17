"""MCP stdio server — read-only radar-ops tools."""

from __future__ import annotations

import json
from collections.abc import Callable
from typing import Any

from mcp.server.fastmcp import FastMCP

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

mcp = FastMCP("radar-ops")


def _run(fn: Callable[[], dict[str, Any]]) -> str:
    try:
        data = fn()
        return json.dumps(data, ensure_ascii=False, default=str)
    except RadarClientError as exc:
        return json.dumps(exc.as_dict(), ensure_ascii=False, default=str)


@mcp.tool()
def radar_health() -> str:
    """GET /api/health — honest ops health (not always green)."""

    def _inner() -> dict[str, Any]:
        return summarize_health(RadarClient().health())

    return _run(_inner)


@mcp.tool()
def radar_ready() -> str:
    """GET /api/ready — readiness probe body (503 → structured error)."""

    def _inner() -> dict[str, Any]:
        return summarize_ready(RadarClient().ready())

    return _run(_inner)


@mcp.tool()
def radar_snapshot_summary() -> str:
    """GET /api/snapshot — compact summary; never invents prices if down."""

    def _inner() -> dict[str, Any]:
        return summarize_snapshot(RadarClient().snapshot())

    return _run(_inner)


@mcp.tool()
def radar_metrics_up() -> str:
    """GET /api/metrics — confirms metrics endpoint responds."""

    def _inner() -> dict[str, Any]:
        return summarize_metrics(RadarClient().metrics())

    return _run(_inner)


@mcp.tool()
def radar_trade_paper_status() -> str:
    """GET /api/trade/paper — paper ledger summary (API key if required)."""

    def _inner() -> dict[str, Any]:
        return summarize_paper(RadarClient().trade_paper())

    return _run(_inner)


@mcp.tool()
def radar_trade_status() -> str:
    """GET /api/trade/status — auto/manual surface (read-only; never toggles)."""

    def _inner() -> dict[str, Any]:
        return summarize_trade_status(RadarClient().trade_status())

    return _run(_inner)


@mcp.tool()
def radar_telegram_status() -> str:
    """GET /api/telegram/status — bot/watches surface (no tokens)."""

    def _inner() -> dict[str, Any]:
        return summarize_telegram(RadarClient().telegram_status())

    return _run(_inner)


@mcp.tool()
def radar_recovery_status() -> str:
    """GET /api/ops/recovery — self-recovery supervisor (not a soak claim)."""

    def _inner() -> dict[str, Any]:
        return summarize_recovery(RadarClient().recovery_status())

    return _run(_inner)


def run() -> None:
    mcp.run(transport="stdio")
