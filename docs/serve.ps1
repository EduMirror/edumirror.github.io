param(
    [int]$Port = 8765
)

$ErrorActionPreference = 'Stop'

Write-Host "Starting live documentation preview on http://127.0.0.1:$Port"
Write-Host 'Save a Markdown file or an image under docs/_static; the page will rebuild and refresh automatically.'

# Use the project's EduMirror environment even when this script is launched
# from Explorer or an unactivated PowerShell window.
conda run --no-capture-output -n EduMirror python -m sphinx_autobuild `
    -E `
    -b html `
    --port $Port `
    --open-browser `
    --watch (Join-Path $PSScriptRoot '_static') `
    $PSScriptRoot (Join-Path $PSScriptRoot '_build/live_html')
