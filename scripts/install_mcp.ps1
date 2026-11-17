# Install radar-ops MCP package into a real Python (editable).
# After this, Cursor mcp.json can run: python -m radar_mcp
# Prefer this over PYTHONPATH / CURSOR_PLUGIN_ROOT hacks.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Pkg = Join-Path $Root "packages\radar_mcp"
if (-not (Test-Path (Join-Path $Pkg "pyproject.toml"))) {
  throw "missing packages/radar_mcp"
}

$PyExe = "python"
$PyPrefix = @()
$cmd = Get-Command python -ErrorAction SilentlyContinue
if ($null -eq $cmd) { throw "python not found on PATH" }
if ([string]$cmd.Source -match "WindowsApps\\python\.exe$") {
  $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
  if ($null -eq $pyLauncher) {
    throw "PATH python is WindowsApps stub and 'py' launcher missing — install Python 3.11+"
  }
  Write-Host "Note: PATH python is WindowsApps stub; using py -3"
  $PyExe = "py"
  $PyPrefix = @("-3")
}

Write-Host "Using: $PyExe $($PyPrefix -join ' ')"
Write-Host "Installing editable radar-mcp from $Pkg"
& $PyExe @($PyPrefix + @("-m", "pip", "install", "-e", $Pkg))
if ($null -eq $LASTEXITCODE -or $LASTEXITCODE -ne 0) {
  throw "pip install failed exit=$LASTEXITCODE"
}
Write-Host "Import smoke (stdio server not started)"
& $PyExe @($PyPrefix + @("-c", "import radar_mcp; print('radar_mcp', getattr(radar_mcp, '__version__', '?'))"))
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "OK install_mcp — set RADAR_BASE_URL / optional RADAR_API_KEY in MCP env"
Write-Host "mcp.json expects 'python -m radar_mcp' on the same interpreter"
exit 0
