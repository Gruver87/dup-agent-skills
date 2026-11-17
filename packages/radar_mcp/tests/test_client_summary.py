"""Unit tests — no live radar required."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import httpx
import pytest
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


def test_summarize_snapshot_compact() -> None:
    out = summarize_snapshot(
        {
            "ok": True,
            "universe_size": 12,
            "score_backend": "native",
            "auto_trade": {"enabled": False, "positions_integrity": "ok"},
            "cache": {"age_ms": 100},
            "etag": 'W/"abc"',
        }
    )
    assert out["ok"] is True
    assert out["universe_size"] == 12
    assert out["auto_enabled"] is False
    assert "not financial advice" in out["note"]


def test_summarize_health_problems() -> None:
    out = summarize_health({"ok": False, "problems": ["stale"], "deployment_mode": "lab"})
    assert out["ok"] is False
    assert out["problems"] == ["stale"]


def test_summarize_ready() -> None:
    out = summarize_ready({"ok": True, "ready": True, "problems": []})
    assert out["ready"] is True


def test_summarize_metrics() -> None:
    out = summarize_metrics({"deployment_mode": "lab", "scans": 1})
    assert out["up"] is True
    assert "scans" in out["keys"]


def test_summarize_paper() -> None:
    out = summarize_paper({"ok": True, "dry_run": True, "realized_pnl_usdt_micros": 0})
    assert out["dry_run"] is True
    assert out["realized_pnl_usdt_micros"] == 0


def test_summarize_trade_status() -> None:
    out = summarize_trade_status(
        {
            "ok": True,
            "auto": {"enabled": False, "dry_run": True, "positions_integrity": "ok"},
            "manual": {"enabled": True},
            "rate_limit": {"ok": True},
        }
    )
    assert out["auto_enabled"] is False
    assert out["manual_enabled"] is True
    assert "no order placement" in out["note"]


def test_summarize_telegram_no_token_fields() -> None:
    out = summarize_telegram(
        {"ok": True, "running": True, "configured": True, "watches": 2, "token": "SECRET"}
    )
    assert out["running"] is True
    assert "token" not in out
    assert "SECRET" not in str(out)


def test_summarize_recovery() -> None:
    out = summarize_recovery({"ok": True, "recovery": {"enabled": True, "running": True}})
    assert out["running"] is True
    assert "soak" in out["note"]


def test_client_unreachable() -> None:
    c = RadarClient(base_url="http://127.0.0.1:1")
    with patch("radar_mcp.client.httpx.Client") as mock_cls:
        mock_cls.return_value.__enter__.return_value.get.side_effect = httpx.ConnectError(
            "boom"
        )
        with pytest.raises(RadarClientError) as ei:
            c.health()
        assert "unreachable" in str(ei.value)
        d = ei.value.as_dict()
        assert d["ok"] is False


def test_client_http_error() -> None:
    c = RadarClient(base_url="http://example.test")
    resp = MagicMock()
    resp.status_code = 503
    resp.json.return_value = {"ok": False, "problems": ["x"]}
    resp.text = ""
    with patch("radar_mcp.client.httpx.Client") as mock_cls:
        mock_cls.return_value.__enter__.return_value.get.return_value = resp
        with pytest.raises(RadarClientError) as ei:
            c.ready()
        assert ei.value.status == 503


def test_error_json_roundtrip() -> None:
    err = RadarClientError("down", status=None)
    assert json.loads(json.dumps(err.as_dict()))["ok"] is False
