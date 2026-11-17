# Dot-source or call to inject RADAR_* from sibling radar .env into *this* PowerShell session.
# Never prints secret values. Does not start soak / live-money.
param(
  [string]$RadarRoot = "",
  [switch]$Quiet
)
$ErrorActionPreference = "Stop"
$SkillsRoot = Split-Path -Parent $PSScriptRoot
if (-not $RadarRoot) {
  $cand = Join-Path (Split-Path $SkillsRoot) "dup-market-radar"
  if (Test-Path $cand) { $RadarRoot = $cand }
  else { $RadarRoot = Join-Path $env:USERPROFILE "Desktop\dup-market-radar" }
}
$envPath = Join-Path $RadarRoot ".env"
$loaded = @()
if (Test-Path $envPath) {
  Get-Content $envPath | ForEach-Object {
    if ($_ -match '^\s*#' -or $_ -notmatch '=') { return }
    $p = $_ -split '=', 2
    $n = $p[0].Trim()
    $v = if ($p.Count -gt 1) { $p[1].Trim().Trim('"').Trim("'") } else { "" }
    if ($n -notin @("RADAR_API_KEY", "RADAR_BASE_URL", "RADAR_REQUIRE_API_KEY")) { return }
    if ([string]::IsNullOrWhiteSpace($v)) { return }
    Set-Item -Path "Env:$n" -Value $v
    $loaded += $n
  }
}
if (-not $env:RADAR_BASE_URL) { $env:RADAR_BASE_URL = "http://127.0.0.1:8787" }
if (-not $Quiet) {
  Write-Host ("OK load_radar_env keys=[{0}] base={1} (values hidden)" -f ($loaded -join ','), $env:RADAR_BASE_URL)
}
