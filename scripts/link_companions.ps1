# Link this pack's skills into sibling companion checkouts (radar + trading bot).
# Does not start soak, live money, or SPOT_ENTRIES.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Desktop = Split-Path $Root
$companions = @(
  (Join-Path $Desktop "dup-market-radar"),
  (Join-Path $Desktop "absolute-trading-bot-final")
)

$ok = 0
foreach ($c in $companions) {
  $link = Join-Path $c "scripts\link_agent_skills.ps1"
  if (-not (Test-Path $link)) {
    Write-Host "SKIP missing $link"
    continue
  }
  Write-Host "== link -> $c =="
  & $link -SkillsRoot $Root
  if (-not $?) {
    Write-Host "FAIL link $c"
    exit 1
  }
  $ok++
}
if ($ok -eq 0) {
  throw "no companion link scripts found under $Desktop"
}
Write-Host "OK link_companions n=$ok"
exit 0
