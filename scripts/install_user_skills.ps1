# Install skills into user Agent Skills directories (~/.agents/skills and ~/.cursor/skills).
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Src = Join-Path $Root "skills"
if (-not (Test-Path $Src)) { throw "missing skills/" }

$targets = @(
  (Join-Path $env:USERPROFILE ".agents\skills"),
  (Join-Path $env:USERPROFILE ".cursor\skills")
)

foreach ($dstRoot in $targets) {
  New-Item -ItemType Directory -Path $dstRoot -Force | Out-Null
  Get-ChildItem $Src -Directory | ForEach-Object {
    $name = "dup-$($_.Name)"
    $target = Join-Path $dstRoot $name
    if (Test-Path $target) { Remove-Item $target -Recurse -Force }
    Copy-Item $_.FullName $target -Recurse -Force
    Write-Host "installed $name -> $target"
  }
}
Write-Host "OK user skills install"
