#!/usr/bin/env bash
# Regenerate the component docs (markdown + icons + canvas screenshots) with no human at the canvas.
#
#   tools/generate_docs.sh            # regenerate, leave changes in the working tree
#   tools/generate_docs.sh --check    # regenerate and fail if anything changed (drift detector)
#
# This drives the real Rhino + Grasshopper: the export captures each component off the GH canvas
# (GH_Canvas.GenerateHiResImage), so a canvas — and therefore a logged-in GUI session — must exist.
# It is UNATTENDED, not headless: Rhino will open, work, and quit on its own. Do not expect it to
# run over ssh or from a cron job with no desktop; a launchd *user agent* is fine.
#
# Requires: Rhino 8 (licensed, with the Eddy3D plugins installed), and this repo checked out
# alongside the Eddy3D repo (../Eddy3D/GenerateDocumentation.ghx). Override with EDDY3D_GHX.
set -euo pipefail

TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCS_REPO="$(cd "$TOOLS_DIR/.." && pwd)"
RHINO_APP="${RHINO_APP:-/Applications/Rhino 8.app}"
DRIVER="$TOOLS_DIR/run_export_unattended.py"

CHECK_MODE=0
[[ "${1:-}" == "--check" ]] && CHECK_MODE=1

if [[ ! -d "$RHINO_APP" ]]; then
  echo "Rhino not found at '$RHINO_APP'. Set RHINO_APP to your install." >&2
  exit 2
fi
if [[ ! -f "$DRIVER" ]]; then
  echo "Driver script missing: $DRIVER" >&2
  exit 2
fi

RHINO_BIN="$RHINO_APP/Contents/MacOS/Rhinoceros"
if [[ ! -x "$RHINO_BIN" ]]; then
  echo "Rhino binary not found/executable: $RHINO_BIN" >&2
  exit 2
fi

SENTINEL="$(mktemp -t eddy3d-docs)"
trap 'rm -f "$SENTINEL"' EXIT
export EDDY3D_DOCS_SENTINEL="$SENTINEL"

if pgrep -x Rhinoceros >/dev/null; then
  echo "A Rhino instance is already running. Quit it first — this drives its own instance." >&2
  exit 2
fi

echo "==> Driving Rhino to regenerate docs (a Rhino window will open and close on its own)"
# Launch the binary DIRECTLY, not via `open`: `open` starts GUI apps through launchd, which does
# NOT inherit this shell's exported env (so EDDY3D_DOCS_SENTINEL would be lost), and its -W/-runscript
# handling proved unreliable here. A direct exec inherits the env and lets us wait on the real PID.
"$RHINO_BIN" -nosplash -runscript="-_RunPythonScript \"$DRIVER\"" >/dev/null 2>&1 &
RHINO_PID=$!
wait "$RHINO_PID" || true

STATUS="$(cat "$SENTINEL" 2>/dev/null || echo "")"
if [[ -z "$STATUS" ]]; then
  echo "FAILED: Rhino exited without reporting a result — the export did not run to completion." >&2
  echo "        (Run the driver with EDDY3D_DOCS_KEEP_OPEN=1 and watch the Rhino command line.)" >&2
  exit 1
fi
if [[ "$STATUS" != "0" ]]; then
  echo "FAILED: the export reported errors inside Grasshopper (see the Rhino command line)." >&2
  exit 1
fi

echo "==> Export finished"
cd "$DOCS_REPO"
CHANGED="$(git status --porcelain -- docs | wc -l | tr -d ' ')"
echo "==> $CHANGED changed file(s) under docs/"

if [[ "$CHECK_MODE" == "1" ]]; then
  if [[ "$CHANGED" != "0" ]]; then
    echo "Docs are out of date — regenerate and commit:" >&2
    git status --short -- docs >&2
    exit 1
  fi
  echo "==> Docs are up to date"
fi
