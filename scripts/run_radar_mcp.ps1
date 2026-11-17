# Stdio MCP launcher — loads RADAR_* from sibling dup-market-radar .env (never prints secrets).
# Cursor mcp.json should invoke this instead of bare `python -m radar_mcp` when API key is required.
param(
  [string]$RadarRoot = ""
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot

if (-not $RadarRoot) {
  $cand = Join-Path (Split-Path $Root) "dup-market-radar"
  if (Test-Path (Join-Path $cand ".env")) { $RadarRoot = $cand }
  else { $RadarRoot = Join-Path $env:USERPROFILE "Desktop\dup-market-radar" }
}

$envPath = Join-Path $RadarRoot ".env"
if (Test-Path $envPath) {
  Get-Content $envPath | ForEach-Object {
    if ($_ -match '^\s*#' -or $_ -notmatch '=') { return }
    $p = $_ -split '=', 2
    $n = $p[0].Trim()
    $v = if ($p.Count -gt 1) { $p[1].Trim().Trim('"').Trim("'") } else { "" }
    if ($n -notin @("RADAR_API_KEY", "RADAR_BASE_URL", "RADAR_REQUIRE_API_KEY")) { return }
    if ([string]::IsNullOrWhiteSpace($v)) { return }
    Set-Item -Path "Env:$n" -Value $v
  }
  Write-Host "radar_mcp env loaded from .env (values not shown) root=$RadarRoot" 1>&2
} else {
  Write-Host "WARN no .env at $RadarRoot — using process env only" 1>&2
}

if (-not $env:RADAR_BASE_URL) {
  $env:RADAR_BASE_URL = "http://127.0.0.1:8787"
}

# Prefer editable install; fall back to PYTHONPATH for plugin checkout
$src = Join-Path $Root "packages\radar_mcp\src"
if (Test-Path $src) {
  if ($env:PYTHONPATH) { $env:PYTHONPATH = "$src;$env:PYTHONPATH" }
  else { $env:PYTHONPATH = $src }
}

$keySet = -not [string]::IsNullOrWhiteSpace($env:RADAR_API_KEY)
Write-Host "radar_mcp start base=$($env:RADAR_BASE_URL) api_key_set=$keySet" 1>&2
python -m radar_mcp
exit $LASTEXITCODE
