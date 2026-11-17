# Changelog

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
