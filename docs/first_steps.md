# Eddy3D - Outdoor+

*The urban microclimate module of the **Eddy3D** plugin, using `urbanMicroclimateFoam` (uMFoam)*

## Overview

`urbanMicroclimateFoam` (uMFoam) is an open-source solver built on [OpenFOAM](https://openfoam.org/){ target="_blank" rel="noopener noreferrer" aria-label="OpenFOAM (opens in a new tab)" } for modeling urban microclimates. It simulates coupled physical processes including:

- **Turbulent airflow**
- **Heat and moisture transport in air**
- **Radiative heat exchange (shortwave and longwave)**
- **Heat and moisture storage in building materials (HAM model)**
- **Urban vegetation heat balance**

 Learn more at the official repository:  
🔗 [urbanMicroclimateFoam GitHub](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam){ target="_blank" rel="noopener noreferrer" aria-label="urbanMicroclimateFoam GitHub (opens in a new tab)" }

## Prerequisites

### 1. Install an OpenFOAM engine

Eddy3D runs OpenFOAM through one of these engines (pick one):

- **Docker (Windows & macOS, recommended):** [Install Docker Desktop](https://www.docker.com/products/docker-desktop/){ target="_blank" rel="noopener noreferrer" aria-label="Install Docker Desktop (opens in a new tab)" }. Eddy3D pulls a pre-configured OpenFOAM 12 image automatically.
- **blueCFD-Core 2024 (Windows):** [Download blueCFD-Core](https://bluecfd.github.io/Core/Downloads/){ target="_blank" rel="noopener noreferrer" aria-label="Download blueCFD-Core (opens in a new tab)" }. **Install into a folder without spaces in the name** (e.g. `C:\blueCFD-Core\2024`) — a location like `C:\Program Files\...` breaks the OpenFOAM toolchain and the UMF solver can never be built or found.
- **WSL (Windows):** [WSL installation guide](https://learn.microsoft.com/en-us/windows/wsl/install){ target="_blank" rel="noopener noreferrer" aria-label="WSL installation guide (opens in a new tab)" }.

### 2. Install the Eddy3D Plugin for Grasshopper (Rhino)

- Open **Rhinoceros**
- Run the `PackageManager` command
- Search for **Eddy3D**
- Click **Install** and restart Rhino

<iframe loading="lazy" title="Loom video: Install Eddy3D Plugin" src="https://www.loom.com/embed/aa80604bdf55468e89e213adfe3dfc03" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Verify Installation

Use the **`Check Installation`** component in Grasshopper:

- Set `Check = True`
- Set `Install UrbanMicroclimateFoam = True` if it’s a new install

The console will automatically install the necessary files.

<iframe loading="lazy" title="Loom video: Verify Installation" src="https://www.loom.com/embed/f0de87f9dd5b417fbe9cb7dde28e5926" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Run a Template Simulation

### 1. Load Template

- Use the **`Templates`** component
- Right-click > select `UMCF.Templates.MicroclimateSimulation.gh`

<iframe loading="lazy" title="Loom video: Load Template" src="https://www.loom.com/embed/3813d676223e4bf78790a688a9e64cf1" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### 2. Add Weather File

- Connect an **EPW file** to the **`Weather`** component  
- This enables time settings in the **`Timing`** component

<iframe loading="lazy" title="Loom video: Add Weather File" src="https://www.loom.com/embed/5180a478450b476b825caf4a2712717b" width="640" height="360" frameborder="0" allowfullscreen></iframe>

##  Define the Simulation Domain

### Air Region

Use the **`Air Region`** component to set:

- **ABL Conditions:** Wind speed, height, direction
- **Domain Dimensions:**
  - `Cell Size`
  - `Front Add`, `Back Add`, `Sides Add`, `Top Add`
  - `Refinement Box Add`

<iframe loading="lazy" title="Loom video: Air Region" src="https://www.loom.com/embed/44d4138231ae4fd78759858ecb6c78a1" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Solid Region (Buildings)

Inputs:

- Building mesh geometry
- Material (default: `Hamstad5Brick`)
- Mesh refinement (optional)
- Indoor temperature (°C)

<iframe loading="lazy" title="Loom video: Solid Region (Buildings)" src="https://www.loom.com/embed/c70e729726534ec9bc90065693b7d77e" width="640" height="360" frameborder="0" allowfullscreen></iframe>

### Vegetation Region

Inputs:

- Vegetation mesh
- Leaf Area Density (LAD)
- Vegetation properties
- Mesh refinement (optional)

Default vegetation values are found in `constant/air/vegetationProperties`.

<iframe loading="lazy" title="Loom video: Vegetation Region" src="https://www.loom.com/embed/fdcfff3c303847e7a05a756ea4196ec8" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Simulation Settings

Configure with the **`Simulation Settings`** component:

- **Number of CPUs** (e.g., 10 recommended)
- **maxFluidIteration** (higher = better resolution)

<iframe loading="lazy" title="Loom video: Simulation Settings" src="https://www.loom.com/embed/5eb25cafae004029b975992cf66af3ec" width="640" height="360" frameborder="0" allowfullscreen></iframe>

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

<iframe loading="lazy" title="Loom video: Write and Run the Case" src="https://www.loom.com/embed/49ab3679676e4f728cd483f7fe2ddaaa" width="640" height="360" frameborder="0" allowfullscreen></iframe>

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

<iframe loading="lazy" title="Loom video: Visualize Results Part 1" src="https://www.loom.com/embed/a896f09c862440ce8b9c247cd95ae838" width="640" height="360" frameborder="0" allowfullscreen></iframe>

<iframe loading="lazy" title="Loom video: Visualize Results Part 2" src="https://www.loom.com/embed/3499df4c8a544cb59e2681c71ebca3c3" width="640" height="360" frameborder="0" allowfullscreen></iframe>

## Output Types

- Velocity (U)
- Temperature (T)
- Humidity (w)

Visualizations are available both in Grasshopper and ParaView.


## Need Help?

Visit the [UMCF GitHub Issues](https://github.com/OpenFOAM-BuildingPhysics/urbanMicroclimateFoam/issues){ target="_blank" rel="noopener noreferrer" aria-label="UMCF GitHub Issues (opens in a new tab)" } page or reach out to your instructor/supervisor for support.
