"""HTTP client for DUP Market Radar read-only endpoints."""

from __future__ import annotations

import os
from typing import Any

import httpx

DEFAULT_BASE = "http://127.0.0.1:8787"
TIMEOUT_S = 10.0


class RadarClientError(Exception):
    """Structured fail-closed error (never invent market data)."""

    def __init__(self, message: str, *, status: int | None = None, body: Any = None) -> None:
        super().__init__(message)
        self.status = status
        self.body = body

    def as_dict(self) -> dict[str, Any]:
        out: dict[str, Any] = {"ok": False, "error": str(self)}
        if self.status is not None:
            out["status"] = self.status
        if self.body is not None:
            out["detail"] = self.body
        return out


class RadarClient:
    def __init__(
        self,
        base_url: str | None = None,
        api_key: str | None = None,
        timeout: float = TIMEOUT_S,
    ) -> None:
        self.base_url = (base_url or os.environ.get("RADAR_BASE_URL") or DEFAULT_BASE).rstrip(
            "/"
        )
        self.api_key = api_key if api_key is not None else os.environ.get("RADAR_API_KEY")
        self.timeout = timeout

    def _headers(self) -> dict[str, str]:
        h: dict[str, str] = {"Accept": "application/json"}
        if self.api_key:
            h["X-Radar-Api-Key"] = self.api_key
        return h

    def get_json(self, path: str, *, auth: bool = False) -> dict[str, Any]:
        url = f"{self.base_url}{path}"
        headers = self._headers() if auth or self.api_key else {"Accept": "application/json"}
        if auth and not self.api_key:
            # Still attempt; radar may not require key in lab
            headers = self._headers()
        try:
            with httpx.Client(timeout=self.timeout) as client:
                resp = client.get(url, headers=headers)
        except httpx.HTTPError as exc:
            raise RadarClientError(f"radar unreachable: {exc}") from exc
        try:
            data = resp.json()
        except ValueError:
            data = {"raw": (resp.text or "")[:500]}
        if resp.status_code >= 400:
            raise RadarClientError(
                f"radar HTTP {resp.status_code} for {path}",
                status=resp.status_code,
                body=data,
            )
        if not isinstance(data, dict):
            raise RadarClientError(f"unexpected payload type for {path}", status=resp.status_code)
        return data

    def health(self) -> dict[str, Any]:
        return self.get_json("/api/health")

    def ready(self) -> dict[str, Any]:
        return self.get_json("/api/ready")

    def metrics(self) -> dict[str, Any]:
        return self.get_json("/api/metrics")

    def snapshot(self) -> dict[str, Any]:
        return self.get_json("/api/snapshot", auth=True)

    def trade_paper(self) -> dict[str, Any]:
        return self.get_json("/api/trade/paper", auth=True)


def summarize_snapshot(snap: dict[str, Any]) -> dict[str, Any]:
    """Compact summary — no invented prices if fields missing."""
    auto = snap.get("auto_trade") if isinstance(snap.get("auto_trade"), dict) else {}
    cache = snap.get("cache") if isinstance(snap.get("cache"), dict) else {}
    return {
        "ok": bool(snap.get("ok")),
        "product": snap.get("product") or "DUP Market Radar",
        "schema_version": snap.get("schema_version"),
        "generated_at_ms": snap.get("generated_at_ms") or snap.get("generated_at"),
        "universe_size": snap.get("universe_size"),
        "score_backend": snap.get("score_backend"),
        "mtf_ensure_ok": snap.get("mtf_ensure_ok"),
        "auto_enabled": auto.get("enabled"),
        "positions_integrity": auto.get("positions_integrity"),
        "cache_age_ms": cache.get("age_ms") or cache.get("age_ms_est"),
        "etag": snap.get("etag"),
        "note": "summary only — not financial advice; no order placement",
    }


def summarize_health(body: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": bool(body.get("ok")),
        "problems": body.get("problems") or [],
        "deployment_mode": body.get("deployment_mode"),
        "last_scan_ok": body.get("last_scan_ok"),
        "api_key_required": body.get("api_key_required"),
        "auto_trade": body.get("auto_trade"),
        "manual_trade": body.get("manual_trade"),
        "native": body.get("native"),
    }


def summarize_ready(body: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": bool(body.get("ok")),
        "ready": bool(body.get("ready")),
        "problems": body.get("problems") or [],
        "positions_integrity": body.get("positions_integrity"),
    }


def summarize_metrics(body: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": True,
        "keys": sorted(str(k) for k in body)[:40],
        "deployment_mode": body.get("deployment_mode"),
        "up": True,
    }


def summarize_paper(body: dict[str, Any]) -> dict[str, Any]:
    return {
        "ok": bool(body.get("ok", True)),
        "dry_run": body.get("dry_run"),
        "open_positions": body.get("open_positions") or body.get("n_open"),
        "realized_pnl_usdt_micros": body.get("realized_pnl_usdt_micros"),
        "unrealized_pnl_usdt_micros": body.get("unrealized_pnl_usdt_micros"),
        "note": "integer micros when present — not advice",
    }
