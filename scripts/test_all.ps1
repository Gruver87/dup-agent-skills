# One-shot gate for dup-agent-skills (Windows).
# Exit 0 only when sync + validate + ruff + pytest all PASS.
# Lab against radar is optional (-WithLab); SKIP-if-down still exits 0.
param(
  [switch]$WithLab,
  [switch]$SkipInstall
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

function Assert-NativeExit {
  param([string]$Step)
  if ($null -eq $LASTEXITCODE) {
    Write-Host "FAIL $Step : LASTEXITCODE unset"
    exit 1
  }
  if ($LASTEXITCODE -ne 0) {
    Write-Host "FAIL $Step : exit=$LASTEXITCODE"
    exit $LASTEXITCODE
  }
}

Write-Host "== sync .agents/skills =="
& "$PSScriptRoot\sync_agents_skills.ps1"
if (-not $?) {
  Write-Host "FAIL sync"
  exit 1
}

Write-Host "== validate_skills =="
python "$PSScriptRoot\validate_skills.py"
Assert-NativeExit "validate_skills"

if (-not $SkipInstall) {
  Write-Host "== pip install radar_mcp[dev] =="
  python -m pip install -e "$Root\packages\radar_mcp[dev]" -q
  Assert-NativeExit "pip install"
  python -m pip install ruff -q
  Assert-NativeExit "pip ruff"
}

Write-Host "== ruff =="
python -m ruff check packages/radar_mcp scripts
Assert-NativeExit "ruff"

Write-Host "== pytest =="
python -m pytest packages/radar_mcp/tests -q
Assert-NativeExit "pytest"

if ($WithLab) {
  Write-Host "== radar_mcp_lab (SKIP ok if radar down) =="
  python "$PSScriptRoot\radar_mcp_lab.py"
  Assert-NativeExit "radar_mcp_lab"
}

Write-Host "RESULT: PASS test_all"
exit 0
