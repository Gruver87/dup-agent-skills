# Changelog

## 0.1.9 — 2026-11-17

- `dup-labs.code-workspace` multi-root (skills + radar + trading-bot).
- INSTALL points at the workspace file.

## 0.1.8 — 2026-11-17

- MCP: `run_radar_mcp.ps1` + `load_radar_env.ps1` load `RADAR_API_KEY` from sibling radar `.env` (never print/commit).
- `mcp.json` invokes the PowerShell launcher (keyed tools no longer stuck at 401 when `.env` has the key).
- `radar-live-money-gate`: `-Status` path; refuse inventing KuCoin keys / soak-as-live.

## 0.1.7 — 2026-11-17

- `radar_mcp_lab.py` probes all read-only surfaces (health/ready/metrics/snapshot/trade/telegram/recovery).
- `radar-test-gate` skill: `verify Quick/Full` explicitly **NO soak**; refuse casual Soak48h.
- Radar companion docs list MCP tool table (≥0.1.6).

## 0.1.6 — 2026-11-17

- MCP: `radar_telegram_status` + `radar_recovery_status` (read-only; no tokens; not a soak claim).
- `scripts/link_companions.ps1` — mirror skills into radar + trading-bot siblings.
- Docs: INSTALL §G; package README tool list.

## 0.1.5 — 2026-11-17

- MCP: read-only `radar_trade_status` (GET `/api/trade/status` — never toggles auto).
- `validate_skills` also pins `.cursor-plugin/plugin.json` + `radar_mcp` pyproject to the same semver.
- INSTALL §F for absolute-trading-bot `test_all` / `bot_gate`.

## 0.1.4 — 2026-11-17

- `validate_skills.py` enforces `metadata.version` == `plugin.json` version.
- Evidence claim-matrix covers absolute-trading-bot PROTOCOL_STATUS / no silent MEASUREMENT rewrite.
- README bot companion wording: v1 stopped (not “holdout” theater).

## 0.1.3 — 2026-11-17

- `bot-holdout-wait` aligned to `PROTOCOL_STATUS` — MEASUREMENT v1 stopped, no silent retune, `SPOT_ENTRIES` off (not obsolete Oct-25 holdout theater).
- Skill metadata versions bumped to 0.1.3; companion docs in absolute-trading-bot-final.

## 0.1.2 — 2026-11-17

- `scripts/install_mcp.ps1` — editable pip install; avoid WindowsApps stub via `py -3`.
- `mcp.json` — `python -m radar_mcp` only (no `CURSOR_PLUGIN_ROOT` PYTHONPATH).
- `install_user_skills.ps1` — keep folder names = skill `name` (remove legacy `dup-*` prefixes).
- `docs/MCP.md` / ARCHITECTURE pin honesty **0.1.2**.
- Radar companion: `link_agent_skills.ps1` / AGENT_SKILLS cross-link.

## 0.1.1 — 2026-11-17

- Fix CI ruff `EXE001` (Windows shebang / non-executable) via `ruff.toml`.
- Add `scripts/test_all.ps1` one-shot local gate.
- Add `docs/DEMO.md` + CI badge in README.

## 0.1.0 — 2026-11-17

- Spec-aligned Agent Skills (license, rich descriptions, references, refuse sections).
- 10 skills: radar-ops-status, radar-live-money-gate, no-futures-auto, market-digest, evidence-honesty, radar-pwa-install, radar-test-gate, bot-holdout-wait, l1-boundary, secrets-hygiene.
- `scripts/validate_skills.py` + `.agents/skills` sync + CI.
- Cursor / Agent plugin manifests at version 0.1.0.
- Read-only MCP `radar-ops` (`packages/radar_mcp`) + lab script + unit tests.
- Docs: INSTALL, ARCHITECTURE, EXAMPLES, DISCLAIMER.
