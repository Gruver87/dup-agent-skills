# Install radar-ops MCP package into the active Python (editable).
# After this, Cursor mcp.json can run: python -m radar_mcp
# without relying on PYTHONPATH / CURSOR_PLUGIN_ROOT.
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$Pkg = Join-Path $Root "packages\radar_mcp"
if (-not (Test-Path (Join-Path $Pkg "pyproject.toml"))) {
  throw "missing packages/radar_mcp"
}
Write-Host "Installing editable radar-mcp from $Pkg"
python -m pip install -e $Pkg
if ($null -eq $LASTEXITCODE -or $LASTEXITCODE -ne 0) {
  throw "pip install failed exit=$LASTEXITCODE"
}
Write-Host "Smoke: python -m radar_mcp --help may block on stdio; import check instead"
python -c "import radar_mcp; print('radar_mcp', getattr(radar_mcp, '__version__', '?'))"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "OK install_mcp — set RADAR_BASE_URL / optional RADAR_API_KEY in MCP env"
exit 0
