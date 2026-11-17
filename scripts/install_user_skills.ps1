# Install skills into user Agent Skills directories (~/.agents/skills and ~/.cursor/skills).
# Folder name MUST match SKILL.md `name` (agentskills.io) — do not prefix with dup-.
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
    $name = $_.Name
    $target = Join-Path $dstRoot $name
    # Remove legacy dup-<name> copies that break name==folder
    $legacy = Join-Path $dstRoot ("dup-" + $name)
    if (Test-Path $legacy) {
      Remove-Item $legacy -Recurse -Force
      Write-Host "removed legacy $legacy"
    }
    if (Test-Path $target) { Remove-Item $target -Recurse -Force }
    Copy-Item $_.FullName $target -Recurse -Force
    Write-Host "installed $name -> $target"
  }
}
Write-Host "OK user skills install (names match SKILL.md)"
