# Changelog

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
