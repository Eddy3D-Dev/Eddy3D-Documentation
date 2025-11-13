# Eddy3D - Comfort+

*A Grasshopper plugin for urban microclimate simulation with `urbanMicroclimateFoam` (UMCF)*

## Overview

`urbanMicroclimateFoam` (UMCF) is an open-source solver built on [OpenFOAM](https://openfoam.org/) for modeling urban microclimates. It simulates coupled physical processes including:

- **Turbulent airflow**
- **Heat and moisture transport in air**
- **Radiative heat exchange (shortwave and longwave)**
- **Heat and moisture storage in building materials (HAM model)**
- **Urban vegetation heat balance**

 Learn more at the official repository:  
🔗 [urbanMicroclimateFoam GitHub](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam)

## Prerequisites

### 1. Install OpenFOAM with blueCFD-Core 2020 (Windows)

- Download: [`blueCFD-Core-2020-1-win64-setup.exe`](https://bluecfd.github.io/Core/Downloads/#bluecfd-core-2020-1)  
- This version includes `OpenFOAM 8`.

### 2. Install UMCF Plugin for Grasshopper (Rhino)

- Open **Rhinoceros**
- Run the `PackageManager` command
- Search for **UMCF**
- Enable **"Include pre-releases"**  
- Click **Install** and restart Rhino

[Watch tutorial ▶](#) https://www.loom.com/share/aa80604bdf55468e89e213adfe3dfc03?sid=2f8b4bb0-5d0d-460c-aab9-2a3f61da8a36

## Verify Installation

Use the **`Check Installation`** component in Grasshopper:

- Set `Check = True`
- Set `Install UrbanMicroclimateFoam = True` if it’s a new install

The console will automatically install the necessary files.

[Watch tutorial ▶](#) https://www.loom.com/share/f0de87f9dd5b417fbe9cb7dde28e5926?sid=18fad817-4904-412f-a29a-fa2d4bab3109

## Run a Template Simulation

### 1. Load Template

- Use the **`Templates`** component
- Right-click > select `UMCF.Templates.MicroclimateSimulation.gh`

[Watch tutorial ▶](#) https://www.loom.com/share/3813d676223e4bf78790a688a9e64cf1?sid=ea27b135-e154-40a9-8b45-9973a7f2e1d2
### 2. Add Weather File

- Connect an **EPW file** to the **`Weather`** component  
- This enables time settings in the **`Timing`** component

[Watch tutorial ▶](#) https://www.loom.com/share/5180a478450b476b825caf4a2712717b?sid=9379a082-d0bf-4856-98ec-26d4fd406147
##  Define the Simulation Domain

### Air Region

Use the **`Air Region`** component to set:

- **ABL Conditions:** Wind speed, height, direction
- **Domain Dimensions:**
  - `Cell Size`
  - `Front Add`, `Back Add`, `Sides Add`, `Top Add`
  - `Refinement Box Add`

[Watch tutorial ▶](#) https://www.loom.com/share/44d4138231ae4fd78759858ecb6c78a1?sid=df6b1263-31fa-4783-9282-b7f201e48050

### Solid Region (Buildings)

Inputs:

- Building mesh geometry
- Material (default: `Hamstad5Brick`)
- Mesh refinement (optional)
- Indoor temperature (°C)

[Watch tutorial ▶](#) https://www.loom.com/share/c70e729726534ec9bc90065693b7d77e?sid=423ee098-2ce8-4c03-8f44-63e19b53f116

### Vegetation Region

Inputs:

- Vegetation mesh
- Leaf Area Density (LAD)
- Vegetation properties
- Mesh refinement (optional)

Default vegetation values are found in `constant/air/vegetationProperties`.

[Watch tutorial ▶](#) https://www.loom.com/share/fdcfff3c303847e7a05a756ea4196ec8?sid=f1d5a25b-3f34-4e55-a953-51d2f579e22d

## Simulation Settings

Configure with the **`Simulation Settings`** component:

- **Number of CPUs** (e.g., 10 recommended)
- **maxFluidIteration** (higher = better resolution)

[Watch tutorial ▶](#) https://www.loom.com/share/5eb25cafae004029b975992cf66af3ec?sid=175f86d9-c4fc-4a58-bada-026dfc76db8e

## Write and Run the Case

Use the **`UMCF Case`** component to prepare files and view logs.

1. **Prepare Simulation** – generate mesh  
2. **Run Simulation** – execute solver  

 Run both steps with the same processor mode (single/parallel).

After simulation:
- View results with `.foam` in **ParaView**
- `0` folder = initial conditions
- Output folders based on `controlDict`:
  - `startTime = 0`, `endTime = 43200`, `deltaT = 3600` (i.e., 12 hours)

[Watch tutorial ▶](#) https://www.loom.com/share/49ab3679676e4f728cd483f7fe2ddaaa?sid=da231058-8103-4d3c-a599-a0f32c48fedb


## Visualize Results (in Rhino/Grasshopper)

Use a quad mesh plane at desired height in the **`Probing`** section.

Probe for:
- **Temperature (T)**
- **Velocity (U)**
- **Humidity (w)**

Steps:

1. Generate mesh plane  
2. Click **Run**  
3. Enable **`Probing`** to load results  
4. Use **Hour Slider** to view time-based results

[Watch tutorial ▶] https://www.loom.com/share/a896f09c862440ce8b9c247cd95ae838?sid=1c0e523b-384e-40ac-87fe-f9988e8b998c


[Watch tutorial ▶](#) https://www.loom.com/share/3499df4c8a544cb59e2681c71ebca3c3?sid=bcc8d506-3130-4019-a96f-1337f368cd57

## Output Types

- Velocity (U)
- Temperature (T)
- Humidity (w)

Visualizations are available both in Grasshopper and ParaView.


## Need Help?

Visit the [UMCF GitHub Issues](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam/issues) page or reach out to your instructor/supervisor for support.
