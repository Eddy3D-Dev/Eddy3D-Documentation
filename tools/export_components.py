import Grasshopper
import System.Drawing
import shutil
import os
import glob
import re
import json
import time

# --- CROSS-COMPATIBLE URL DECODING (IronPython 2.7 & Python 3) ---
try:
    from urllib.parse import unquote, quote
except ImportError:
    from urllib import unquote, quote

# --- CONFIGURATION -----------------------------------------------------------
CLEAN_OUTPUT_DIR = True
USE_CROPPED_IMAGES = False

# --- SAFETY SETTINGS ---
DISABLE_SOLVER = True 
COMPONENT_WAIT_TIME = 0.1 

# --- FILE TRACKER ---
WRITTEN_FILES = []
# -----------------------------------------------------------------------------

def track_file(path):
    norm_path = os.path.normpath(path)
    if norm_path not in WRITTEN_FILES:
        WRITTEN_FILES.append(norm_path)

def _read_text_safely(path):
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            with open(path, "r", encoding=enc) as f: return f.read()
        except UnicodeDecodeError: continue
    with open(path, "r", encoding="utf-8", errors="replace") as f: return f.read()

def _ensure_parent_dir(path):
    parent = os.path.dirname(path)
    if parent and not os.path.exists(parent): os.makedirs(parent, exist_ok=True)

def ensure_utf8_file(path):
    if not os.path.exists(path): return
    try:
        with open(path, "r", encoding="utf-8") as _f: _ = _f.read()
    except UnicodeDecodeError:
        txt = _read_text_safely(path)
        _ensure_parent_dir(path)
        with open(path, "w", encoding="utf-8", newline="\n") as f: f.write(txt)

def write_utf8(path, text, mode="w"):
    _ensure_parent_dir(path)
    with open(path, mode, encoding="utf-8", newline="\n") as f: f.write(text)
    track_file(path)

# --- ROBUST STRING SANITIZATION ---
def clean_string(text):
    if not text: return ""
    
    # 1. Decode URL percent-encoding (%28 -> '(', %29 -> ')', %C2%B7 -> '·')
    try:
        text = unquote(str(text))
    except:
        pass 
    
    # 2. UPDATED: Replace middle dots, slashes, ampersands, pipes, colons, AND parentheses with an underscore
    text = re.sub(r"[_\s]*[·/\\&|:()][_\s]*", "_", text)
    
    # 3. Strip out invalid filesystem characters (<, >, "?", "*", etc.)
    text = re.sub(r"[<>?*\"']", "", text)
    
    # 4. Remove control characters (invisible ghosts)
    text = "".join([c for c in text if ord(c) >= 32])
    
    # 5. Collapse any remaining consecutive spaces or underscores into a single underscore
    text = re.sub(r"[\s_]+", "_", text)
    
    # 6. Strip leading/trailing underscores (prevents 'UTCI_Simulation_' from closing parens)
    return text.strip("_")

def write_grouped_components(file_path, exposure_dict, base_folder, link_prefix="components/"):
    main_components = []
    hidden_components = []
    
    for expo_name in sorted(exposure_dict.keys()):
        comps = sorted(exposure_dict[expo_name])
        
        # Validate existence
        valid_comps = []
        for c in comps:
            md_path = os.path.join(base_folder, "components", f"{c}.md")
            if os.path.exists(md_path):
                valid_comps.append(c)
            else:
                print(f"Warning: Skipping broken link for {c} (File missing: {md_path})")

        if "obscure" in expo_name.lower(): hidden_components.extend(valid_comps)
        else: main_components.extend(valid_comps)

    if main_components:
        write_utf8(file_path, "#### Main Components\n", mode="a")
        for comp in main_components:
            write_utf8(file_path, f"* [{comp.replace('_', ' ')}]({link_prefix}{comp}.md)\n", mode="a")
    if hidden_components:
        write_utf8(file_path, "\n#### Hidden Components\n", mode="a")
        for comp in hidden_components:
            write_utf8(file_path, f"* [{comp.replace('_', ' ')}]({link_prefix}{comp}.md)\n", mode="a")

def reset_output_directories(base_dir):
    if not CLEAN_OUTPUT_DIR: return
    print(f"Cleaning output directories in {base_dir}...")
    for d in [os.path.join(base_dir, "categories"), os.path.join(base_dir, "text", "categories")]:
        if os.path.exists(d): 
            try: shutil.rmtree(d)
            except: pass
    comp_dir = os.path.join(base_dir, "components")
    if os.path.exists(comp_dir):
        for f in glob.glob(os.path.join(comp_dir, "*.md")):
            try: os.remove(f)
            except: pass

def captureGrasshopperScreen(fileName, workingDirectory):
    target_dir = os.path.join(workingDirectory, "images", "components")
    if not os.path.exists(target_dir): os.makedirs(target_dir, exist_ok=True)
    
    imageSettings = Grasshopper.GUI.Canvas.GH_Canvas.GH_ImageSettings()
    imageSettings.Zoom = 2.15
    canvas = Grasshopper.GH_InstanceServer.ActiveCanvas
    canvas.Refresh()
    
    rect = System.Drawing.Rectangle(0, 0, 2, 2)
    imgsOfCanvas = canvas.GenerateHiResImage(rect, imageSettings)
    screenCapture = imgsOfCanvas[0][0]
    
    filePath = os.path.join(target_dir, fileName)
    if os.path.exists(filePath): os.remove(filePath)
    
    shutil.copyfile(screenCapture, filePath)
    track_file(filePath)
    
    path = os.path.split(screenCapture)[0]
    try: shutil.rmtree(path)
    except: pass

def exportIcon(component, pluginName, workingDirectory):
    target_dir = os.path.join(workingDirectory, "images", "icons")
    if not os.path.exists(target_dir): os.makedirs(target_dir, exist_ok=True)
    
    fileName = getComponentName(component) + ".png"
    filePath = os.path.join(target_dir, fileName)
    component.Icon_24x24.Save(filePath)
    track_file(filePath)

def getComponentByName(document, name):
    for component in document.Objects:
        if component.Name == name: return component

def getComponentName(component_obj_or_desc):
    raw_name = component_obj_or_desc.Name
    name_no_prefix = raw_name.replace(pluginName + "_", "")
    return clean_string(name_no_prefix)



def get_source_path(class_name, repo_dir):
    import os
    import re
    if not class_name: return None
    pattern = re.compile(r'class\s+' + re.escape(class_name) + r'\b')
    try:
        for root, dirs, files in os.walk(repo_dir):
            if any(x in root for x in ["obj", "bin", "Tests", "Properties", ".git"]):
                continue
            for f in files:
                if f.endswith(".cs"):
                    path = os.path.join(root, f)
                    try:
                        with open(path, "r", encoding="utf-8", errors="ignore") as f_obj:
                            file_content = f_obj.read()
                            if pattern.search(file_content):
                                return os.path.relpath(path, repo_dir).replace("\\", "/")
                    except: pass
    except Exception: pass
    return None

def exportDescription(component, pluginName, githubFolder, githubRepo=None):
    originalName = component.Name
    bName = originalName.replace(pluginName + "_", "")
    name = getComponentName(component)
    
    components_dir = os.path.join(githubFolder, "components")
    os.makedirs(components_dir, exist_ok=True)

    lines = []
    lines.append(f"## ![](../images/icons/{name}.png)")
    if githubRepo:
        repo_dir = os.path.abspath(os.path.join(githubFolder, "..", "Eddy3D"))
        try: class_name = type(component).__name__
        except: class_name = None
        mapped_path = get_source_path(class_name, repo_dir) if repo_dir and os.path.exists(repo_dir) else None
        
        if mapped_path:
            lines[-1] += f" [[source code]]({githubRepo}/blob/dev/{mapped_path})\n"
        else:
            search_query = quote(f'"{originalName}"')
            lines[-1] += f" [[source code]]({githubRepo}/search?q={search_query})\n"
    else: lines[-1] += "\n"

    image_filename = f"{name}-crop.png" if USE_CROPPED_IMAGES else f"{name}.png"
    lines.append(f"![](../images/components/{image_filename})")
    
    desc_cleaned = component.Description.split("Provided by ")[0].replace("\n", " ")
    desc_cleaned = re.sub(r"(?i)\s*Version\s+\d+\.\d+\.\d+\.\d+", "", desc_cleaned)
    lines.append("\n" + desc_cleaned)

    try:
        def format_param(param):
            try:
                name = str(param.Name).strip()
                nick = str(param.NickName).strip()
                if len(nick) > 0 and len(nick) <= 2 and nick != name and nick.upper() == nick:
                    return f"{name} ({nick})"
            except:
                pass
            return param.NickName

        lines.append("\n#### Input")
        for i in range(component.Params.Input.Count):
            in_desc = component.Params.Input[i].Description.replace('\n', ' ')
            display_name = format_param(component.Params.Input[i])
            lines.append(f"* ##### {display_name} \n{in_desc}")
            
        lines.append("\n#### Output")
        for i in range(component.Params.Output.Count):
            out_desc = component.Params.Output[i].Description.replace('\n', ' ')
            display_name = format_param(component.Params.Output[i])
            lines.append(f"* ##### {display_name}\n{out_desc}")
    except: pass

    fileName = f"{name}.md"
    write_utf8(os.path.join(components_dir, fileName), "\n".join(lines))

def getPluginComponents(pluginName):
    components = {}
    for proxy in Grasshopper.Instances.ComponentServer.ObjectProxies:
        if proxy.Obsolete: continue
        if proxy.Desc.Category.strip() == pluginName:
            try:
                if str(proxy.Kind) == "CompiledObject": components[proxy.Desc.Name] = proxy.CreateInstance()
                elif str(proxy.Kind) == "UserObject": components[proxy.Desc.Name] = Grasshopper.Kernel.GH_UserObject(proxy.Location).InstantiateObject()
                else: components[proxy.Desc.Name] = proxy.CreateInstance()
            except: print(f"Skipping {proxy.Desc.Name} - Could not instantiate")
    return components

def createFolderStructure(githubFolder):
    os.makedirs(githubFolder, exist_ok=True)
    for sub in ["images/components", "images/icons", "categories", "components"]:
        os.makedirs(os.path.join(githubFolder, sub), exist_ok=True)

# --- MAIN EXECUTION ---
componentsHeights = {}
pluginComponents = {} 

_workingDir = globals().get('workingDir', None)
_pluginName = globals().get('pluginName', 'Eddy3D')
_doc_repo = _pluginName + "-Documentation"
if not _workingDir:
    _found = False
    try:
        ghdoc = Grasshopper.Instances.ActiveCanvas.Document
        if ghdoc and ghdoc.FilePath:
            _cur = os.path.dirname(ghdoc.FilePath)
            for _ in range(5):
                _candidate = os.path.join(_cur, _doc_repo, "docs")
                if os.path.isdir(_candidate):
                    githubFolder = _candidate
                    _found = True
                    break
                _cur = os.path.dirname(_cur)
    except Exception:
        pass
    if not _found:
        githubFolder = os.path.expanduser("~/Documents/GitHub/%s/docs" % _doc_repo)
else:
    githubFolder = _workingDir

doc = Grasshopper.Instances.ActiveCanvas.Document
original_solver_state = doc.Enabled
if DISABLE_SOLVER:
    print("Disabling Solver...")
    doc.Enabled = False

if export:
    reset_output_directories(githubFolder)
    createFolderStructure(githubFolder)
    components = getPluginComponents(pluginName)

    for GHObjectName, GHObject in components.items():
        if GHObject.Attributes:
            GHObject.Attributes.Pivot = System.Drawing.PointF(200, 215)
            
            print(f"Processing: {GHObjectName}")
            
            try:
                doc.AddObject(GHObject, False, 0)
                GHObject.Attributes.ExpireLayout()
                GHObject.Attributes.PerformLayout()
                
                if COMPONENT_WAIT_TIME > 0:
                    System.Windows.Forms.Application.DoEvents()
                    time.sleep(COMPONENT_WAIT_TIME)

                component = getComponentByName(doc, GHObjectName)
                name = getComponentName(component)
                
                try:
                    captureGrasshopperScreen(name + ".png", githubFolder)
                    exportIcon(component, pluginName, githubFolder)
                    exportDescription(component, pluginName, githubFolder, pluginGHRepo)
                    componentsHeights[name] = str(component.Attributes.Bounds.Height)

                    # Apply cleaning to category names
                    cleanSubCat = clean_string(component.SubCategory)
                    if cleanSubCat not in pluginComponents: pluginComponents[cleanSubCat] = {}
                    expo = str(component.Exposure).split(",")[-1].strip()
                    if expo not in pluginComponents[cleanSubCat]: pluginComponents[cleanSubCat][expo] = []
                    pluginComponents[cleanSubCat][expo].append(name)
                except Exception as e:
                    print(f" - Error exporting contents: {str(e)}")

            except Exception as e:
                print(f" - CRITICAL ERROR processing component: {str(e)}")
            
            finally:
                try: doc.RemoveObject(GHObject, False)
                except: print(" - Warning: Could not remove object cleanly.")

    json_path = os.path.join(githubFolder, "images", "componentsHeight.json")
    with open(json_path, "w", encoding="utf-8") as compHeight:
        json.dump(componentsHeights, compHeight, ensure_ascii=False, indent=4)
    track_file(json_path)

if DISABLE_SOLVER:
    doc.Enabled = original_solver_state
    print("Solver state restored.")

finalOutputFolder = githubFolder 
for cleanSubCat in pluginComponents:
    # Ensure category filenames are safely sanitized
    safeFileName = clean_string(cleanSubCat)
    categoryFilePath = os.path.join(finalOutputFolder, "categories", f"{safeFileName}.md")
    ensure_utf8_file(categoryFilePath)
    
    # Use clean readable names for the Markdown headers
    readableHeader = cleanSubCat.replace("_", " ")
    write_utf8(categoryFilePath, f"# {readableHeader}\n")
    write_grouped_components(categoryFilePath, pluginComponents[cleanSubCat], finalOutputFolder, link_prefix="../components/")

summaryPath = os.path.join(finalOutputFolder, "README.md")
ensure_utf8_file(summaryPath)
write_utf8(summaryPath, "# Eddy3D Component list\n")
for cleanSubCat in sorted(pluginComponents.keys()):
    readableHeader = cleanSubCat.replace("_", " ")
    write_utf8(summaryPath, f"## {readableHeader}\n", mode="a")
    write_grouped_components(summaryPath, pluginComponents[cleanSubCat], finalOutputFolder, link_prefix="components/")

# --- GENERATE MKDOCS NAV BLOCK ---
navPath = os.path.join(finalOutputFolder, "components_nav.yml")
ensure_utf8_file(navPath)
nav_lines = ["  - Components:"]
for cleanSubCat in sorted(pluginComponents.keys()):
    readableHeader = cleanSubCat.replace("_", " ")
    nav_lines.append(f"      - \"{readableHeader}\":")
    
    main_components = []
    hidden_components = []
    for expo_name in sorted(pluginComponents[cleanSubCat].keys()):
        comps = sorted(pluginComponents[cleanSubCat][expo_name])
        if "obscure" in expo_name.lower(): hidden_components.extend(comps)
        else: main_components.extend(comps)
        
    for comp in main_components:
        nav_lines.append(f"          - \"{comp.replace('_', ' ')}\": components/{comp}.md")
    for comp in hidden_components:
        nav_lines.append(f"          - \"{comp.replace('_', ' ')}\": components/{comp}.md")
write_utf8(navPath, "\n".join(nav_lines))

# --- PRINT SUMMARY OF WRITTEN FILES ---
print("\n" + "="*60)
print(f"EXPORT COMPLETE: {len(WRITTEN_FILES)} Files Written")
print("="*60)

images = [f for f in WRITTEN_FILES if f.endswith(('.png', '.jpg', '.jpeg'))]
docs = [f for f in WRITTEN_FILES if f.endswith('.md')]
data_files = [f for f in WRITTEN_FILES if f.endswith('.json')]

if docs:
    print(f"\n--- Markdown Documents ({len(docs)}) ---")
    for f in sorted(docs): print(f"  [MD]   {f}")

if images:
    print(f"\n--- Images & Icons ({len(images)}) ---")
    for f in sorted(images): print(f"  [IMG]  {f}")

if data_files:
    print(f"\n--- Data Files ({len(data_files)}) ---")
    for f in sorted(data_files): print(f"  [DATA] {f}")

print("\nDone!")
