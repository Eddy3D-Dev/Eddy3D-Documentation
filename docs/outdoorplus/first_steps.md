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

<iframe src="https://www.loom.com/embed/aa80604bdf55468e89e213adfe3dfc03" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

## Verify Installation

Use the **`Check Installation`** component in Grasshopper:

- Set `Check = True`
- Set `Install UrbanMicroclimateFoam = True` if it’s a new install

The console will automatically install the necessary files.

<iframe src="https://www.loom.com/embed/f0de87f9dd5b417fbe9cb7dde28e5926" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

## Run a Template Simulation

### 1. Load Template

- Use the **`Templates`** component
- Right-click > select `UMCF.Templates.MicroclimateSimulation.gh`

<iframe src="https://www.loom.com/embed/3813d676223e4bf78790a688a9e64cf1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

### 2. Add Weather File

- Connect an **EPW file** to the **`Weather`** component  
- This enables time settings in the **`Timing`** component

<iframe src="https://www.loom.com/embed/5180a478450b476b825caf4a2712717b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

##  Define the Simulation Domain

### Air Region

Use the **`Air Region`** component to set:

- **ABL Conditions:** Wind speed, height, direction
- **Domain Dimensions:**
  - `Cell Size`
  - `Front Add`, `Back Add`, `Sides Add`, `Top Add`
  - `Refinement Box Add`

<iframe src="https://www.loom.com/embed/44d4138231ae4fd78759858ecb6c78a1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

### Solid Region (Buildings)

Inputs:

- Building mesh geometry
- Material (default: `Hamstad5Brick`)
- Mesh refinement (optional)
- Indoor temperature (°C)

<iframe src="https://www.loom.com/embed/c70e729726534ec9bc90065693b7d77e" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

### Vegetation Region

Inputs:

- Vegetation mesh
- Leaf Area Density (LAD)
- Vegetation properties
- Mesh refinement (optional)

Default vegetation values are found in `constant/air/vegetationProperties`.

<iframe src="https://www.loom.com/embed/fdcfff3c303847e7a05a756ea4196ec8" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

## Simulation Settings

Configure with the **`Simulation Settings`** component:

- **Number of CPUs** (e.g., 10 recommended)
- **maxFluidIteration** (higher = better resolution)

<iframe src="https://www.loom.com/embed/5eb25cafae004029b975992cf66af3ec" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

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

<iframe src="https://www.loom.com/embed/49ab3679676e4f728cd483f7fe2ddaaa" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

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

<iframe src="https://www.loom.com/embed/a896f09c862440ce8b9c247cd95ae838" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

<iframe src="https://www.loom.com/embed/3499df4c8a544cb59e2681c71ebca3c3" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>

## Output Types

- Velocity (U)
- Temperature (T)
- Humidity (w)

Visualizations are available both in Grasshopper and ParaView.


## Need Help?

Visit the [UMCF GitHub Issues](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam/issues) page or reach out to your instructor/supervisor for support.
