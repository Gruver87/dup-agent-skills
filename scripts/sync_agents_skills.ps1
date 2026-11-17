# Copy skills/ -> .agents/skills/ for Cursor project discovery.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Src = Join-Path $Root "skills"
$Dst = Join-Path $Root ".agents\skills"
if (-not (Test-Path $Src)) { throw "missing skills/" }
New-Item -ItemType Directory -Path $Dst -Force | Out-Null
Get-ChildItem $Dst -Directory -ErrorAction SilentlyContinue | ForEach-Object {
  Remove-Item $_.FullName -Recurse -Force
}
Get-ChildItem $Src -Directory | ForEach-Object {
  $target = Join-Path $Dst $_.Name
  Copy-Item $_.FullName $target -Recurse -Force
  Write-Host "synced $($_.Name)"
}
Write-Host "OK -> .agents/skills"
