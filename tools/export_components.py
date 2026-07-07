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
USE_CROPPED_IMAGES = True

# --- SAFETY SETTINGS ---
DISABLE_SOLVER = True 
COMPONENT_WAIT_TIME = 0.05 

# --- FILE TRACKER ---
WRITTEN_FILES = []
FILES_TO_CROP = []
COMPONENT_DESCRIPTIONS = {}
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
    
    # Sort exposures by their logical GH_Exposure enum order, not alphabetically
    exposure_order = ["primary", "secondary", "tertiary", "quarternary", "quinary", "senary", "septenary", "hidden", "obscure"]
    def get_expo_weight(expo):
        try: return exposure_order.index(expo.lower())
        except ValueError: return 99

    sorted_exposures = sorted(exposure_dict.keys(), key=get_expo_weight)
    
    for expo_name in sorted_exposures:
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

    def write_cards(comps, title):
        if not comps: return
        # Raw HTML heading: keeps it out of the integrated nav TOC (toc.integrate)
        slug = title.lower().replace(" ", "-")
        write_utf8(file_path, f"<h4 id=\"{slug}\">{title}</h4>\n<div class=\"index-quicklink-container\">\n", mode="a")
        for comp in comps:
            desc = COMPONENT_DESCRIPTIONS.get(comp, "")
            card_html = f'    <a href="/components/{comp}/" style="text-decoration: none;">\n'
            card_html += f'        <div class="index-quicklink">\n'
            card_html += f'            <div class="index-quicklink-title">\n'
            card_html += f'                <img src="/images/icons/{comp}.png" class="nav-gh-icon"> {comp.replace("_", " ")}\n'
            card_html += f'            </div>\n'
            card_html += f'            <div class="index-quicklink-text">{desc}</div>\n'
            card_html += f'        </div>\n'
            card_html += f'    </a>\n'
            write_utf8(file_path, card_html, mode="a")
        write_utf8(file_path, "</div>\n\n", mode="a")

    write_cards(main_components, "Main Components")
    write_cards(hidden_components, "Hidden Components")

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

def captureGrasshopperScreen(fileName, workingDirectory, component=None):
    target_dir = os.path.join(workingDirectory, "images", "components")
    if not os.path.exists(target_dir): os.makedirs(target_dir, exist_ok=True)
    
    imageSettings = Grasshopper.GUI.Canvas.GH_Canvas.GH_ImageSettings()
    imageSettings.Zoom = 2.15
    canvas = Grasshopper.GH_InstanceServer.ActiveCanvas
    canvas.Refresh()
    
    if component and component.Attributes:
        b = component.Attributes.Bounds
        margin = 150 # Generous margin to capture all shadows, wires, and balloons without clipping
        rect = System.Drawing.Rectangle(int(b.X) - margin, int(b.Y) - margin, int(b.Width) + 2*margin, int(b.Height) + 2*margin)
    else:
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
    lines.append(f"# ![](/images/icons/{name}.png) {bName}")
    if githubRepo:
        repo_dir = os.path.abspath(os.path.join(githubFolder, "..", "Eddy3D"))
        try: class_name = type(component).__name__
        except: class_name = None
        mapped_path = get_source_path(class_name, repo_dir) if repo_dir and os.path.exists(repo_dir) else None
        
        if mapped_path:
            lines[-1] += f" - [[source code]]({githubRepo}/blob/dev/{mapped_path})\n"
        else:
            search_query = quote(f'"{originalName}"')
            lines[-1] += f" - [[source code]]({githubRepo}/search?q={search_query})\n"
    else: lines[-1] += "\n"

    image_filename = f"{name}-crop.png" if USE_CROPPED_IMAGES else f"{name}.png"
    lines.append(f"![](/images/components/{image_filename})")
    
    desc_cleaned = component.Description.split("Provided by ")[0].replace("\n", " ")
    desc_cleaned = re.sub(r"(?i)\s*Version\s+\d+\.\d+\.\d+\.\d+", "", desc_cleaned)
    lines.append("\n" + desc_cleaned)

    try:
        def param_row(param):
            def cell(v):
                return str(v).strip().replace('\n', ' ').replace('|', '\\|')
            name = cell(param.Name)
            nick = cell(param.NickName)
            if nick == name:
                nick = ""
            desc = cell(param.Description)
            try: type_name = cell(param.TypeName)
            except: type_name = ""
            type_cell = f"`{type_name}`" if type_name else ""
            return f"| {name} | {nick} | {desc} | {type_cell} |"

        def param_table(params):
            rows = [param_row(params[i]) for i in range(params.Count)]
            if not rows:
                return ["*None*"]
            return ["| Name | Nickname | Description | Type |",
                    "| ---- | -------- | ----------- | ---- |"] + rows

        lines.append("\n#### Input\n")
        lines.extend(param_table(component.Params.Input))
        lines.append("\n#### Output\n")
        lines.extend(param_table(component.Params.Output))
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

                # Hidden/obscure components are excluded from the documentation entirely
                expo_check = str(component.Exposure).lower()
                if "hidden" in expo_check or "obscure" in expo_check:
                    print(" - Skipping hidden component.")
                    continue

                try:
                    captureGrasshopperScreen(name + ".png", githubFolder, component)
                    exportIcon(component, pluginName, githubFolder)
                    exportDescription(component, pluginName, githubFolder, pluginGHRepo)
                    componentsHeights[name] = str(component.Attributes.Bounds.Height)

                    try:
                        desc = component.Description.split("Provided by ")[0].replace("\n", " ")
                        desc = re.sub(r"(?i)\s*Version\s+\d+\.\d+\.\d+\.\d+", "", desc)
                        COMPONENT_DESCRIPTIONS[name] = desc
                    except:
                        COMPONENT_DESCRIPTIONS[name] = ""

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
    # Scoped style dims every toolbar group except the current category's
    dim_style = (
        "<style>\n"
        f'.Main-GhToolbar-Container .SubGroup-Container:not([data-category="{safeFileName}"]) {{\n'
        "  filter: grayscale(1);\n"
        "  opacity: 0.35;\n"
        "}\n"
        "</style>\n"
    )
    write_utf8(categoryFilePath, f"{{!toolbar.md!}}\n\n{dim_style}\n# {readableHeader}\n")
    write_grouped_components(categoryFilePath, pluginComponents[cleanSubCat], finalOutputFolder, link_prefix="../components/")

summaryPath = os.path.join(finalOutputFolder, "Components.md")
ensure_utf8_file(summaryPath)
write_utf8(summaryPath, "# Eddy3D Component list\n")

# --- GENERATE GRASSHOPPER RIBBON TOOLBAR (pure HTML, no markdown) ---
def build_toolbar_html(pluginComponents):
    import re
    exposure_order = ["primary", "secondary", "tertiary", "quarternary", "quinary", "senary", "septenary", "hidden", "obscure"]
    def get_expo_weight(expo):
        try: return exposure_order.index(expo.lower())
        except ValueError: return 99

    html = '<div class="Main-GhToolbar-Container">\n'
    for cleanSubCat in sorted(pluginComponents.keys()):
        readableHeader = cleanSubCat.replace("_", " ")
        shortTitle = re.sub(r'^\d+[\s_]+', '', readableHeader)
        
        html += f'<div class="SubGroup-Container" data-category="{clean_string(cleanSubCat)}">\n'
        html += '<div class="SubGroup-Icons">\n'
        html += '<div class="sub-group">\n'
        
        sorted_exposures = sorted(pluginComponents[cleanSubCat].keys(), key=get_expo_weight)
        index = 0
        for expo_name in sorted_exposures:
            comps = sorted(pluginComponents[cleanSubCat][expo_name])
            for comp in comps:
                dataAttr = "above-dataComment" if (index % 2 == 0) else "below-dataComment"
                comp_display = comp.replace("_", " ")
                html += f'<a href="/components/{comp}/" class="GhComponentItem" {dataAttr}="{comp_display}"><img src="/images/icons/{comp}.png" class="gh-component-selected" alt="{comp_display}" /></a>\n'
                index += 1

        html += '</div>\n'
        html += '</div>\n'
        html += f'<div class="SubGroup-Title">{shortTitle}</div>\n'
        html += '</div>\n'
    html += '</div>\n\n'
    return html

toolbar_html = build_toolbar_html(pluginComponents)

# Write to a standalone toolbar file that can be included anywhere!
toolbarPath = os.path.join(finalOutputFolder, "toolbar.md")
ensure_utf8_file(toolbarPath)
write_utf8(toolbarPath, toolbar_html)

write_utf8(summaryPath, toolbar_html, mode="a")

# --- GENERATE COMPONENT CARDS ---
for cleanSubCat in sorted(pluginComponents.keys()):
    readableHeader = cleanSubCat.replace("_", " ")
    # Raw HTML heading: keeps it out of the integrated nav TOC (toc.integrate)
    header_slug = readableHeader.lower().replace(" ", "-").replace("+", "")
    write_utf8(summaryPath, f"<h2 id=\"{header_slug}\">{readableHeader}</h2>\n", mode="a")
    write_grouped_components(summaryPath, pluginComponents[cleanSubCat], finalOutputFolder, link_prefix="components/")

# --- GENERATE MKDOCS NAV BLOCK ---
navPath = os.path.join(finalOutputFolder, "components_nav.yml")
ensure_utf8_file(navPath)
nav_lines = ["  - Components:"]
nav_lines.append("      - \"Overview\": Components.md")
for cleanSubCat in sorted(pluginComponents.keys()):
    readableHeader = cleanSubCat.replace("_", " ")
    nav_lines.append(f"      - \"{readableHeader}\":")
    nav_lines.append(f"          - \"Overview\": categories/{cleanSubCat}.md")
    
    main_components = []
    hidden_components = []
    exposure_order = ["primary", "secondary", "tertiary", "quarternary", "quinary", "senary", "septenary", "hidden", "obscure"]
    def get_expo_weight(expo):
        try: return exposure_order.index(expo.lower())
        except ValueError: return 99

    for expo_name in sorted(pluginComponents[cleanSubCat].keys(), key=get_expo_weight):
        comps = sorted(pluginComponents[cleanSubCat][expo_name])
        if "obscure" in expo_name.lower(): hidden_components.extend(comps)
        else: main_components.extend(comps)
        
    for comp in main_components:
        nav_lines.append(f"          - \"<img src='/images/icons/{comp}.png' class='nav-gh-icon' /> {comp.replace('_', ' ')}\": components/{comp}.md")
    for comp in hidden_components:
        nav_lines.append(f"          - \"<img src='/images/icons/{comp}.png' class='nav-gh-icon' /> {comp.replace('_', ' ')}\": components/{comp}.md")
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
