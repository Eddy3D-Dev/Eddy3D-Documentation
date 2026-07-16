# -*- coding: utf-8 -*-
"""
Drives GenerateDocumentation.ghx without a human at the canvas.

Run by Rhino itself (see generate_docs.sh), NOT by system python:

    "/Applications/Rhino 8.app/Contents/MacOS/Rhinoceros" -nosplash \
        -runscript='-_RunPythonScript "<this file>"'

ENGINE GOTCHA (why this file is plain ASCII with a coding header): -_RunPythonScript may host
this with IronPython 2, whose parser rejects any non-ASCII byte unless a PEP-263 coding line is
present -- an em-dash in a COMMENT once produced "SyntaxError: Non-ASCII character '\\xe2'" and the
export silently never started. Keep this file ASCII-only; keep the coding line as a belt.

AS HEADLESS AS RHINO GETS: there is no headless launch mode in Rhino 8 for Mac (no -headless
argument in the binary, no LSBackgroundOnly, and `rhinocode script` only talks to an already
running instance). The Rhino window does open. But the Grasshopper EDITOR is never shown: the
canvas object is created by LoadEditor() and GH_Canvas.GenerateHiResImage paints into an offscreen
bitmap, so the screenshots do not need the editor on screen. What this removes is the HUMAN and
the GH window; a logged-in GUI session must still exist for the canvas control to be creatable.

IMPORT GOTCHA: the plain-Rhino python host references RhinoCommon but NOT Grasshopper, so a bare
`import Grasshopper` fails ("No module named Grasshopper"). Loading the plug-in object first puts
the assembly in the domain; clr.AddReference then makes the import resolve. (Inside a GH Python
component neither step is needed, which is why the .ghx's own scripts do not do this.)

API GOTCHA: do NOT use DocumentServer.AddDocument(doc, True) -- its second parameter is by-ref and
the python binding rejects it ("expected StrongBox[bool], got bool"). Assigning canvas.Document is
sufficient and registers the document.

Outcome is written to the file named by EDDY3D_DOCS_SENTINEL ("0" ok, "1" failed); the wrapper
reads it so a failed export can never look like a success. Progress is appended to
EDDY3D_DOCS_LOG (default ~/eddy3d_docs_export.log) because Rhino's command line is invisible to
the shell that launched it.
"""

import os
import sys
import traceback

import clr
import Rhino

_GH = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
if _GH is None:
    raise RuntimeError("Grasshopper plug-in object not available - is Grasshopper installed?")
clr.AddReference("Grasshopper")
import Grasshopper  # noqa: E402  (must follow AddReference)

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_GITHUB_ROOT = os.path.abspath(os.path.join(_THIS_DIR, "..", ".."))
GHX_PATH = os.environ.get(
    "EDDY3D_GHX", os.path.join(_GITHUB_ROOT, "Eddy3D", "GenerateDocumentation.ghx"))
LOG_PATH = os.environ.get(
    "EDDY3D_DOCS_LOG", os.path.expanduser("~/eddy3d_docs_export.log"))


def log(message):
    line = "[docs-export] " + str(message)
    print(line)  # Rhino command line
    try:
        with open(LOG_PATH, "a") as fh:
            fh.write(line + "\n")
    except Exception:
        pass


def load_editor():
    _GH.DisableBanner()
    if not _GH.IsEditorLoaded():
        log("loading Grasshopper editor (canvas object needed; the window is never shown)")
        _GH.LoadEditor()
    canvas = Grasshopper.Instances.ActiveCanvas
    if canvas is None:
        raise RuntimeError(
            "Grasshopper editor loaded but ActiveCanvas is still null - screenshots cannot be "
            "captured. Is this a logged-in GUI session (not ssh)?")
    return canvas


def open_on_canvas(path, canvas):
    if not os.path.exists(path):
        raise IOError("Definition not found: " + path)

    io = Grasshopper.Kernel.GH_DocumentIO()
    if not io.Open(path):
        raise IOError("Grasshopper refused to open: " + path)
    doc = io.Document
    if doc is None:
        raise IOError("Opened but produced no GH_Document: " + path)

    # The export script reads Grasshopper.Instances.ActiveCanvas.Document directly
    # (export_components.py:320) and captures off that canvas, so the definition must be the
    # ACTIVE canvas document. See the AddDocument gotcha in the module docstring.
    canvas.Document = doc
    doc.Enabled = True
    log("opened " + os.path.basename(path) + " (FilePath set: " + str(bool(doc.FilePath)) + ")")
    return doc


def set_export_toggles(doc, value):
    toggled = 0
    for obj in doc.Objects:
        if isinstance(obj, Grasshopper.Kernel.Special.GH_BooleanToggle):
            obj.Value = value
            obj.ExpireSolution(False)
            toggled += 1
    if toggled == 0:
        raise RuntimeError(
            "No Boolean Toggle found - cannot trigger the export. Did the definition change?")
    log("set " + str(toggled) + " toggle(s) to " + str(value))


def collect_errors(doc):
    errors = []
    level = Grasshopper.Kernel.GH_RuntimeMessageLevel.Error
    for obj in doc.Objects:
        if isinstance(obj, Grasshopper.Kernel.IGH_ActiveObject):
            for msg in obj.RuntimeMessages(level):
                errors.append(obj.NickName + ": " + msg)
    return errors


def main():
    log("definition: " + GHX_PATH)
    canvas = load_editor()
    doc = open_on_canvas(GHX_PATH, canvas)
    try:
        set_export_toggles(doc, True)
        log("solving (writes markdown, icons and canvas captures - a few minutes)")
        doc.NewSolution(True)  # synchronous: returns when the export has finished
        log("solution finished")

        errors = collect_errors(doc)
        if errors:
            raise RuntimeError("Definition reported errors:\n  " + "\n  ".join(errors))
    finally:
        # Leave the toggle off so an automated run does not dirty the checked-in definition.
        try:
            set_export_toggles(doc, False)
        except Exception:
            pass
    log("export completed")


if __name__ == "__main__":
    exit_code = 0
    try:
        open(LOG_PATH, "w").close()
        main()
    except Exception as ex:
        log("FAILED: " + str(ex))
        log(traceback.format_exc())
        exit_code = 1

    sentinel = os.environ.get("EDDY3D_DOCS_SENTINEL")
    if sentinel:
        try:
            with open(sentinel, "w") as fh:
                fh.write(str(exit_code))
        except Exception:
            pass

    # Do not let a save prompt block the unattended quit. RhinoApp.Exit() was observed NOT to
    # terminate the process under -runscript; the _Exit command does.
    try:
        active = Rhino.RhinoDoc.ActiveDoc
        if active is not None:
            active.Modified = False
    except Exception:
        pass
    if os.environ.get("EDDY3D_DOCS_KEEP_OPEN") != "1":
        Rhino.RhinoApp.RunScript("_-Exit", False)
