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
SOURCE_LINKS = {
    "Calculated Value": "OutdoorPlus/CMP/Obsolete/Values/CalculatedVecCMP.cs",
    "Calculated Vector Value": "OutdoorPlus/CMP/Obsolete/Values/CalculatedVecCMP.cs",
    "Constant Value": "OutdoorPlus/CMP/Obsolete/Values/ConstantCMP.cs",
    "Create Address": "OutdoorPlus/CMP/Meta/CreateAddressCMP.cs",
    "Create Entry Key": "OutdoorPlus/CMP/Meta/CreateEntryKeyCMP.cs",
    "Create Setting": "OutdoorPlus/CMP/Meta/CreateSettingCMP.cs",
    "Debugger": "OutdoorPlus/CMP/Meta/DebuggerCMP.cs",
    "Deconstruct Entry": "OutdoorPlus/CMP/Simulation/DeconstructCaseCMP.cs",
    "Deconstruct FileContainer": "OutdoorPlus/CMP/Meta/DeFileContainerCMP.cs",
    "Deconstruct Setting": "OutdoorPlus/CMP/Simulation/DeconstructCaseCMP.cs",
    "Entry from a Key and Value": "OutdoorPlus/CMP/Meta/CreateEntryKeyValueCMP.cs",
    "Install Engines": "Radiance/CMP/InstallEnginesCMP.cs",
    "Uniform Value": "OutdoorPlus/CMP/Obsolete/Values/UniformVecCMP.cs",
    "Uniform Vector Value": "OutdoorPlus/CMP/Obsolete/Values/UniformVecCMP.cs",
    "Zero Gradient Value": "OutdoorPlus/CMP/Obsolete/Values/ZeroGradientCMP.cs",
    "Select Template": "OutdoorPlus/CMP/Meta/SelectTemplateCMP.cs",
    "STL Exporter": "Outdoor/CMP/StlExporterCMP.cs",
    "Safety Toggle": "Outdoor/CMP/SafetyToggleCMP.cs",
    "Atmospheric Boundary Layer": "OutdoorPlus/CMP/Building/MaterialSavonnieresCMP.cs",
    "Manual Inflow Profile": "Outdoor/ManualInflowProfile.cs",
    "Uniform Flow": "Outdoor/CMP/UniformFlowCMP.cs",
    "Download Weather": "Outdoor/CMP/DownloadWeatherCMP.cs",
    "Translate Date To Hours": "Outdoor/CMP/AnalysisPeriodToHoursCMP.cs",
    "Wind Compass": "Outdoor/CMP/CompassCMP.cs",
    "Wind Rose Cluster": "Outdoor/CMP/WindRoseClusterCMP.cs",
    "Gmsh Mesh": "OutdoorPlus/CMP/Building/GMSHMeshingCMP.cs",
    "Tree": "Outdoor/CMP/TreesCMP.cs",
    "Watertight": "Outdoor/CMP/WatertightCMP.cs",
    "Cylinder Domain": "Outdoor/CylinderDomain.cs",
    "Cell Size": "Outdoor/CMP/CellSizeCMP.cs",
    "Mesh Settings": "Outdoor/CMP/MeshSettingsCMP.cs",
    "Refinement Region": "Outdoor/CMP/RefinementRegionCMP.cs",
    "Brep Grid Points": "Outdoor/CMP/BrepGridPointsCMP.cs",
    "Load Wind Case": "Outdoor/CMP/CleanCaseCMP.cs",
    "Outdoor Case": "Outdoor/OutdoorCase.cs",
    "Write Run Scripts": "Outdoor/CMP/WindScriptsCMP.cs",
    "Clean Case": "Outdoor/CMP/CleanCaseCMP.cs",
    "Run": "Radiance/CMP/MrtRunCMP.cs",
    "Run Settings": "Outdoor/CMP/RunSettingsCMP.cs",
    "Custom Function Object": "Outdoor/CMP/CustomFunctionObjectCMP.cs",
    "SLURM Runner": "Outdoor/CMP/SlurmRunnerCMP.cs",
    "Probe": "Outdoor/CMP/ProbeCMP.cs",
    "Analysis Period": "MetaFOAM.Lib/AnalysisPeriod.cs",
    "Date to HOY": "Outdoor/CMP/HoyCMP.cs",
    "Live Residuals": "Outdoor/CMP/LiveResidualsCMP.cs",
    "Meshing Progress": "Outdoor/CMP/MeshingProgressCMP.cs",
    "Plot Residuals": "Outdoor/CMP/PlotResidualsCMP.cs",
    "Flow Rates": "Outdoor/CMP/FlowRatesCMP.cs",
    "Pedestrian Wind Comfort": "Outdoor/CMP/WindComfortCMP.cs",
    "Velocity Amplification Factors (VAF)": "Outdoor/CMP/SpatialFactorsCMP.cs",
    "Wind Field Viewer": "Outdoor/CMP/WindFieldViewerCMP.cs",
    "Indoor Case": "Indoor/IndoorCase.cs",
    "Indoor Inlet": "Indoor/CMP/IndoorInletCMP.cs",
    "Indoor Outlet": "Indoor/CMP/IndoorOutletCMP.cs",
    "Indoor Sink": "Indoor/CMP/IndoorSinkCMP.cs",
    "Indoor Wall": "Indoor/CMP/IndoorCaseCMP.cs",
    "CO2 Emitter": "OutdoorPlus/CMP/Simulation/WeatherCMP.cs",
    "Heat Source": "Radiance/CMP/MrtSurfaceCMP.cs",
    "Momentum Source": "Radiance/CMP/MrtSurfaceCMP.cs",
    "Viral Emitter": "OutdoorPlus/CMP/Terrain/SurfaceMaterialCMP.cs",
    "CalcHeatIndex": "OutdoorPlus/CMP/Metrics/CalcHeatIndexCMP.cs",
    "CalcPET": "OutdoorPlus/CMP/Metrics/CalcPETCMP.cs",
    "UTCI (Weather)": "Radiance/CMP/UtciWeatherCMP.cs",
    "MRT Sensors": "Radiance/CMP/MrtSensorsCMP.cs",
    "MRT Surface": "Radiance/CMP/MrtSurfaceCMP.cs",
    "Surface Settings": "Radiance/CMP/SurfaceSettingsCMP.cs",
    "Thermal Comfort": "OutdoorPlus/CMP/Metrics/ThermalComfortCMP.cs",
    "Tree Settings": "Radiance/CMP/TreeSettingsCMP.cs",
    "Vegetation Settings": "Radiance/CMP/VegetationSettingsCMP.cs",
    "MRT": "Radiance/CMP/MrtRunCMP.cs",
    "MRT Settings": "Radiance.Core/Radiation/MrtSettings.cs",
    "Sky Exposure": "Radiance/CMP/SkyExposureCMP.cs",
    "UTCI (Simulation)": "Radiance/CMP/UtciCMP.cs",
    "FluidX3D Run Settings": "FluidX3D/CMP/FluidX3DRunSettingsCMP.cs",
    "FluidX3D Run": "FluidX3D/CMP/FluidX3DRunCMP.cs",
    "Dataset Reader": "Outdoor/ML/DatasetReaderCMP.cs",
    "ML Model": "Outdoor/ML/MLModelCMP.cs",
    "Wind Predictor": "Outdoor/ML/WindPredictorCMP.cs",
    "GAN Predict": "Outdoor/ML/GanPredictCMP.cs",
    "Interpolate UMag": "Outdoor/ML/InterpolateUMagCMP.cs",
    "Wind Comfort Predictor (ML)": "Outdoor/ML/WindComfortPredictorCMP.cs",
    "Grass": "OutdoorPlus/CMP/Terrain/GrassCMP.cs",
    "Air Region": "OutdoorPlus/CMP/Air/AirRegionCMP.cs",
    "Building Region": "OutdoorPlus/CMP/Building/BuildingRegionCMP.cs",
    "Terrain Region": "OutdoorPlus/CMP/Terrain/TerrainRegionCMP.cs",
    "Vegetation Region": "OutdoorPlus/CMP/Vegetation/VegetationRegionCMP.cs",
    "Building Material": "OutdoorPlus/CMP/Building/BuildingMaterialCMP.cs",
    "Soil Material": "OutdoorPlus/CMP/Terrain/SoilMaterialCMP.cs",
    "Terrain Surface Material": "OutdoorPlus/CMP/Terrain/SurfaceMaterialCMP.cs",
    "Vegetation Properties": "OutdoorPlus/CMP/Vegetation/VegetationPropertiesCMP.cs",
    "ABL Condition": "OutdoorPlus/CMP/Air/ABLConditionCMP.cs",
    "Advanced Terrain Mesh": "OutdoorPlus/CMP/Terrain/AdvancedTerrainCMP.cs",
    "Building Mesh Settings": "OutdoorPlus/CMP/Building/BuildingMeshSettingsCMP.cs",
    "Terrain Mesh Settings": "OutdoorPlus/CMP/Terrain/TerrainMeshSettingCMP.cs",
    "Vegetation Mesh Settings": "OutdoorPlus/CMP/Vegetation/VegetationMeshSettingsCMP.cs",
    "Case Run": "OutdoorPlus/CMP/Simulation/CaseRunCMP.cs",
    "OpenFOAM Dictionary": "OutdoorPlus/CMP/Obsolete/OFDictionaryCMP.cs",
    "OpenFOAM List": "MetaFOAM.Lib/Engines/OpenFoamStep.cs",
    "Read OpenFOAM Case": "OutdoorPlus/CMP/Obsolete/ReadCaseCMP.cs",
    "Outdoor+ Case": "Outdoor/OutdoorCase.cs",
    "Deconstruct Weather": "OutdoorPlus/CMP/Simulation/DeconstructCaseCMP.cs",
    "Box Domain": "OutdoorPlus/CMP/Simulation/BoxDomainCMP.cs",
    "Relative Humidity": "OutdoorPlus/CMP/Simulation/RelativeHumidityCMP.cs",
    "Simulation Mesh Settings": "OutdoorPlus/CMP/Simulation/SimulationMeshSettingsCMP.cs",
    "Simulation Settings": "OutdoorPlus/CMP/Simulation/SimulationSettingsCMP.cs",
    "Timing Parameters": "OutdoorPlus/CMP/Simulation/TimingParametersCMP.cs",
    "Weather": "OutdoorPlus/CMP/Simulation/WeatherCMP.cs",
    "CheckMesh": "OutdoorPlus/CMP/Simulation/CheckMeshCMP.cs",
    "Check Geometry": "OutdoorPlus/CMP/Simulation/CheckGeometryCMP.cs",
    "Parse Case Logs": "MetaFOAM.App/ParseCase.cs",
    "ViewFactors": "OutdoorPlus/CMP/Simulation/ViewFactorsCMP.cs",
    "Export to Visualizer": "Outdoor/CMP/StlExporterCMP.cs",
    "Open In ParaView": "Outdoor/CMP/ParaviewCMP.cs",
    "Deconstruct Case": "OutdoorPlus/CMP/Simulation/DeconstructCaseCMP.cs",
    "Deconstruct Region": "OutdoorPlus/CMP/Simulation/DeconstructCaseCMP.cs",
    "Face Warnings": "OutdoorPlus/CMP/Visualization/ReadTetWarningsCMP.cs",
    "Read Cells": "OutdoorPlus/CMP/Visualization/ReadCellZonesCMP.cs",
    "Read checkMesh": "OutdoorPlus/CMP/Visualization/ReadCheckMeshCMP.cs",
    "Create Mesh": "OutdoorPlus/CMP/Visualization/CreateMeshCMP.cs",
    "Create OBJ": "OutdoorPlus/CMP/Visualization/CreateOBJCMP.cs",
    "Cull Ground Mesh": "Outdoor/CMP/CullPointsCMP.cs",
}

CLEAN_OUTPUT_DIR = True
USE_CROPPED_IMAGES = True

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

def exportDescription(component, pluginName, githubFolder, githubRepo=None):
    originalName = component.Name
    bName = originalName.replace(pluginName + "_", "")
    name = getComponentName(component)
    
    components_dir = os.path.join(githubFolder, "components")
    os.makedirs(components_dir, exist_ok=True)

    lines = []
    lines.append(f"## ![](../images/icons/{name}.png) {bName}")
    if githubRepo:
        mapped_path = SOURCE_LINKS.get(originalName)
        if mapped_path:
            lines[-1] += f" - [[source code]]({githubRepo}/blob/dev/{mapped_path})\n"
        else:
            search_query = quote(f'"{originalName}"')
            lines[-1] += f" - [[source code]]({githubRepo}/search?q={search_query})\n"
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

if not workingDir: githubFolder = "C:/Users/Administrator/Documents/GitHub/%s-primer/" % pluginName
else: githubFolder = workingDir

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
