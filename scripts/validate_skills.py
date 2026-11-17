#!/usr/bin/env python3
"""Validate Agent Skills layout against agentskills.io naming rules.

Exit 0 only when every skills/*/SKILL.md passes. No network.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("missing YAML frontmatter")
    block = m.group(1)
    out: dict[str, str] = {}
    key: str | None = None
    acc: list[str] = []
    for line in block.splitlines():
        if re.match(r"^[a-zA-Z0-9_-]+:\s*", line) and not line.startswith(" "):
            if key is not None:
                out[key] = "\n".join(acc).strip().strip("\"'")
            k, _, rest = line.partition(":")
            key = k.strip()
            rest = rest.strip()
            if rest == ">|" or rest == ">":
                acc = []
            elif rest.startswith((">-", ">")):
                # folded scalar continues on next indented lines
                acc = [rest.lstrip(">").lstrip("-").strip()]
            else:
                acc = [rest.strip("\"'")] if rest else []
        else:
            if key is not None:
                acc.append(line.strip())
    if key is not None:
        out[key] = "\n".join(acc).strip().strip("\"'")
    return out


def validate_skill(dir_path: Path) -> list[str]:
    errs: list[str] = []
    skill_md = dir_path / "SKILL.md"
    folder = dir_path.name
    if not skill_md.is_file():
        return [f"{folder}: missing SKILL.md"]
    if not NAME_RE.match(folder) or "--" in folder or folder.startswith("-") or folder.endswith("-"):
        errs.append(f"{folder}: invalid directory name")
    if len(folder) > 64:
        errs.append(f"{folder}: name longer than 64")
    text = skill_md.read_text(encoding="utf-8")
    try:
        meta = _parse_frontmatter(text)
    except ValueError as exc:
        return [f"{folder}: {exc}"]
    name = (meta.get("name") or "").strip()
    desc = (meta.get("description") or "").strip()
    if not name:
        errs.append(f"{folder}: missing name")
    elif name != folder:
        errs.append(f"{folder}: name={name!r} must match folder")
    elif not NAME_RE.match(name):
        errs.append(f"{folder}: name fails charset rules")
    if not desc:
        errs.append(f"{folder}: missing description")
    elif len(desc) > 1024:
        errs.append(f"{folder}: description > 1024 chars ({len(desc)})")
    license_f = (meta.get("license") or "").strip()
    if not license_f:
        errs.append(f"{folder}: missing license field")
    # Nested metadata.version (indented under metadata:)
    vm = re.search(r"(?m)^  version:\s*[\"']?([^\"'\s]+)[\"']?\s*$", text)
    if not vm:
        errs.append(f"{folder}: missing metadata.version")
    else:
        # stash for pack-level pin check via attribute on list return — also return in errs channel
        ver = vm.group(1).strip()
        if not re.match(r"^\d+\.\d+\.\d+$", ver):
            errs.append(f"{folder}: metadata.version not semver ({ver!r})")
        else:
            # attach for caller via sentinel-free side channel on the Path is awkward;
            # re-read in main — store on module dict
            _SKILL_VERSIONS[folder] = ver
    body = FRONTMATTER_RE.sub("", text, count=1)
    if len(body.splitlines()) > 500:
        errs.append(f"{folder}: SKILL.md body > 500 lines (progressive disclosure)")
    return errs


_SKILL_VERSIONS: dict[str, str] = {}


def _plugin_version() -> str | None:
    import json

    path = ROOT / "plugin.json"
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    ver = data.get("version")
    return str(ver).strip() if ver is not None else None


def main() -> int:
    _SKILL_VERSIONS.clear()
    if not SKILLS.is_dir():
        print("FAIL: skills/ missing", file=sys.stderr)
        return 1
    dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not dirs:
        print("FAIL: no skills", file=sys.stderr)
        return 1
    all_errs: list[str] = []
    for d in dirs:
        all_errs.extend(validate_skill(d))
    # Mirror check: if .agents/skills exists, every skill must be present
    agents = ROOT / ".agents" / "skills"
    if agents.is_dir():
        for d in dirs:
            mirror = agents / d.name / "SKILL.md"
            if not mirror.is_file():
                all_errs.append(f"mirror missing: .agents/skills/{d.name}/SKILL.md")
    pin = _plugin_version()
    if not pin:
        all_errs.append("plugin.json: missing version")
    else:
        for folder, ver in sorted(_SKILL_VERSIONS.items()):
            if ver != pin:
                all_errs.append(f"{folder}: metadata.version={ver!r} != plugin.json {pin!r}")
    if all_errs:
        print("validate_skills FAIL")
        for e in all_errs:
            print(f" - {e}")
        return 1
    print(f"validate_skills PASS n={len(dirs)} pin={pin}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
