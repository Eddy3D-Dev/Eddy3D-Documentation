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

[Watch tutorial ▶](#) https://www.loom.com/share/261d3503d6d146c18aab0e7e49736b48?sid=28bb6cd9-eb2f-4bf1-879d-e2f8bf8e6055

## Verify Installation

Use the **`Check Installation`** component in Grasshopper:

- Set `Check = True`
- Set `Install UrbanMicroclimateFoam = True` if it’s a new install

The console will automatically install the necessary files.

[Watch tutorial ▶](#) https://www.loom.com/share/74ba54889b7c42ecaf8a886b71be76f5?sid=a33de996-e061-4b14-94af-58dccf61f680

## Run a Template Simulation

### 1. Load Template

- Use the **`Templates`** component
- Right-click > select `UMCF.Templates.MicroclimateSimulation.gh`

[Watch tutorial ▶](#) https://www.loom.com/share/1cbf445327e24c86bf17e0a5a4f2a9f4?sid=727daac3-dbca-4b3d-b422-bc897d116c8b

### 2. Add Weather File

- Connect an **EPW file** to the **`Weather`** component  
- This enables time settings in the **`Timing`** component

[Watch tutorial ▶](#) https://www.loom.com/share/d2a3d374a8ae4fffa47f968059c92702?sid=8c4ad152-0a6a-4e9c-9119-7e35fd3a22aa

##  Define the Simulation Domain

### Air Region

Use the **`Air Region`** component to set:

- **ABL Conditions:** Wind speed, height, direction
- **Domain Dimensions:**
  - `Cell Size`
  - `Front Add`, `Back Add`, `Sides Add`, `Top Add`
  - `Refinement Box Add`

[Watch tutorial ▶](#) https://www.loom.com/share/ab660c5bd5154345b148778e1651a4ea?sid=ca591bb1-aab3-4229-bf0a-70e8574a6dd0

### Solid Region (Buildings)

Inputs:

- Building mesh geometry
- Material (default: `Hamstad5Brick`)
- Mesh refinement (optional)
- Indoor temperature (°C)

[Watch tutorial ▶](#) https://www.loom.com/share/62bce8d5337b4f86823ee778f2abcf18?sid=256497e1-b48e-4542-acd3-50c5a1562ea6

### Vegetation Region

Inputs:

- Vegetation mesh
- Leaf Area Density (LAD)
- Vegetation properties
- Mesh refinement (optional)

Default vegetation values are found in `constant/air/vegetationProperties`.

[Watch tutorial ▶](#) https://www.loom.com/share/c2beacc65e5945e69893898c3ed10cfb?sid=db9acc4b-e593-40ae-982c-8680b0f73c2a

## Simulation Settings

Configure with the **`Simulation Settings`** component:

- **Number of CPUs** (e.g., 10 recommended)
- **maxFluidIteration** (higher = better resolution)

[Watch tutorial ▶](#) https://www.loom.com/share/a0e206e4e7e04bf19bd6cca1b9c5e3d4?sid=f9371d46-0eb6-45f2-b632-2e57da444d72

[Watch tutorial ▶](#) https://www.loom.com/share/ecf5815466e047338b1efa50f9f769dc?sid=79abc77e-ec5c-439d-9f56-d5267ffe09f2

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

[Watch tutorial ▶](#) https://www.loom.com/share/d18a882ad68440f79dad2f59f7ebf9ed?sid=25d93fa6-3e8a-4110-bd4d-94ed8dc33e01 

[Watch tutorial ▶](#) https://www.loom.com/share/626a6e249e1d4fa08966331fdd14aecb?sid=27208bea-a6c8-43bf-a35f-b8af12145f6b

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

[Watch tutorial ▶](#) <!-- Add probing tutorial video link -->

## Output Types

- Velocity (U)
- Temperature (T)
- Humidity (w)

Visualizations are available both in Grasshopper and ParaView.


## Need Help?

Visit the [UMCF GitHub Issues](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam/issues) page or reach out to your instructor/supervisor for support.
