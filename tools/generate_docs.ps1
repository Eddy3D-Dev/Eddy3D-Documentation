# Regenerate the component docs (markdown + icons + canvas screenshots) with no human at the
# canvas - the Windows counterpart of generate_docs.sh. Same driver (run_export_unattended.py,
# OS-agnostic RhinoCommon/Grasshopper calls), only the launch syntax differs: Windows Rhino.exe
# takes /nosplash and /runscript="..." (forward slash), vs the Mac bundle's -nosplash/-runscript=.
#
#   powershell -File tools\generate_docs.ps1            # regenerate, leave changes in the working tree
#   powershell -File tools\generate_docs.ps1 -Check     # regenerate and fail if anything changed
#
# ASCII-only on purpose (no em-dashes/curly quotes): this file is UTF-8, and Windows PowerShell
# 5.1 misreads a BOM-less UTF-8 file as CP1252 when it contains one, turning the em-dash's last
# byte into a stray curly quote that desyncs the whole parser - a documented trap for exactly
# this kind of release-adjacent script (see .claude/skills/release-eddy3d in the Eddy3D repo).
# Written WITH a UTF-8 BOM as a second, independent guard against the same failure.
#
# This drives the real Rhino + Grasshopper: the export captures each component off the GH canvas
# (GH_Canvas.GenerateHiResImage), so a canvas - and therefore a logged-in GUI session - must
# exist. It is UNATTENDED, not headless: Rhino will open, work, and quit on its own.
#
# Requires: Rhino 8 (licensed, with the Eddy3D plugins installed), and this repo checked out
# alongside the Eddy3D repo (..\Eddy3D\GenerateDocumentation.ghx). Override with $env:EDDY3D_GHX.
param([switch]$Check)
$ErrorActionPreference = 'Stop'

$ToolsDir = $PSScriptRoot
$DocsRepo = Split-Path $ToolsDir -Parent
$RhinoExe = if ($env:RHINO_EXE) { $env:RHINO_EXE } else { "C:\Program Files\Rhino 8\System\Rhino.exe" }
$Driver = Join-Path $ToolsDir "run_export_unattended.py"

if (-not (Test-Path $RhinoExe)) {
    Write-Error "Rhino not found at '$RhinoExe'. Set `$env:RHINO_EXE to your install."
    exit 2
}
if (-not (Test-Path $Driver)) {
    Write-Error "Driver script missing: $Driver"
    exit 2
}

if (Get-Process -Name Rhino -ErrorAction SilentlyContinue) {
    Write-Error "A Rhino instance is already running. Close it first - this drives its own instance."
    exit 2
}

$Sentinel = [System.IO.Path]::GetTempFileName()
Remove-Item $Sentinel -Force  # the driver creates it; a pre-existing empty file would look like a false success
$env:EDDY3D_DOCS_SENTINEL = $Sentinel

try {
    Write-Host "==> Driving Rhino to regenerate docs (a Rhino window will open and close on its own)"
    # Launch the binary directly (not Start-Process -Wait through cmd) so the child inherits this
    # process's environment (EDDY3D_DOCS_SENTINEL) exactly, matching the "exec, don't launchd"
    # note in the Mac wrapper. The script path is wrapped in parens per Rhino's own /runscript
    # convention for paths that might contain spaces, rather than nested double-quote escaping.
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $RhinoExe
    $psi.Arguments = "/nosplash /runscript=`"-_RunPythonScript ($Driver)`""
    $psi.UseShellExecute = $false
    $proc = [System.Diagnostics.Process]::Start($psi)
    $proc.WaitForExit()

    if (-not (Test-Path $Sentinel)) {
        Write-Error "FAILED: Rhino exited without reporting a result - the export did not run to completion. (Set `$env:EDDY3D_DOCS_KEEP_OPEN=1 and watch the Rhino command line.)"
        exit 1
    }
    $status = (Get-Content $Sentinel -Raw).Trim()
    if ($status -ne "0") {
        Write-Error "FAILED: the export reported errors inside Grasshopper (see the Rhino command line / EDDY3D_DOCS_LOG)."
        exit 1
    }

    Write-Host "==> Export finished"
    Push-Location $DocsRepo
    try {
        $changed = (git status --porcelain -- docs mkdocs.yml | Measure-Object -Line).Lines
        Write-Host "==> $changed changed file(s) under docs/ and mkdocs.yml"

        if ($Check) {
            if ($changed -ne 0) {
                Write-Host "Docs are out of date - regenerate and commit:" -ForegroundColor Red
                git status --short -- docs mkdocs.yml
                exit 1
            }
            Write-Host "==> Docs are up to date"
        }
    } finally {
        Pop-Location
    }
} finally {
    Remove-Item $Sentinel -Force -ErrorAction SilentlyContinue
    Remove-Item Env:\EDDY3D_DOCS_SENTINEL -ErrorAction SilentlyContinue
}
