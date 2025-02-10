# Eddy3D - Comfort+

![UMCF](./images/comfort+/umcf.gif)
[![Language](https://img.shields.io/badge/language-C%23-gray)](https://github.com/your-repo/umcf)
[![Status](https://img.shields.io/badge/status-beta-brightgreen)](https://github.com/your-repo/umcf)

## Overview

**UMCF** (`urbanMicroclimateFoam`) is an open-source solver for coupled physical processes modeling urban microclimate based on `OpenFOAM`. 

### Key Features

🌊 **CFD** - Computational fluid dynamics model 

- Solves turbulent, convective airflow
- Handles heat and moisture transport in the `air` subdomain

🏗️ **HAM** - Heat moisture transport model

- Manages absorption and transport
- Controls storage of heat and moisture in porous building materials

☀️ **RAD** - Radiation model

- Calculates net longwave and shortwave radiative heat fluxes
- Uses view factor approach

🌳 **VEG** - Vegetation model

- Solves heat balance for urban trees
- Handles green surfaces

## Installation

### Prerequisites
- `bluecfd core 2020`
- `UMCF` plugin from `PackageManager`
- `CheckInstallation` component

### Step-by-Step Guide

1. **Install blueCFD-Core**
   - Download `blueCFD-Core-2020-1-win64-setup.exe` from [bluecfd.github.io](https://bluecfd.github.io/Core/Downloads/#bluecfd-core-2020-1)
   - This provides `OpenFOAM 8`

2. **Install UMCF Plugin**
   - In `Rhinoceros`, execute `PackageManager` command
   - Search for `UMCF` and click Install ([View on RhinoPackages](https://www.rhinopackages.com/?search=umcf))
   - Optional: Check `Include pre-releases` for all versions
   - Restart `Rhinoceros` to complete installation

   ![PackageManager](images/comfort+/PackageManager.png)

3. **Verify Installation**
   - Navigate to `UMCF` tab in `Grasshopper` ribbon
   - Find `Check Installation` under `Meta` subcategory
   - Set `Check` input to `True`
   - This verifies integrity of `blueCDF-Core 2020` and `urbanMicroclimateFoam` files

   ![InstallationCheck](images/comfort+/InstallationCheck.png)

## Features & Workflow

### 1. Simulation Domain Configuration
- The simulation domain consists of three regions:
   1. `air` region
   2. `solid` region
   3. `vegetation` region

### 2. Air Region Setup
- Managed by `UMCF.AirRegion` class
- Determined by `Box Domain Dimensions`
- Includes `Atmospheric Boundary Layer` (`ABL`) condition:
  - `Wind Speed`
  - `Height`
  - `Wind Direction`

![Air Region Configuration](images/comfort+/1.png)

### 3. Solid Region Setup
- Managed by `UMCF.SolidRegion` class
- Requires `mesh` geometry input
- Stores:
  - `region name`
  - `material`
  - Optional `thickness` value
  - `mesh parameters`
  - `building temperature`

![Solid Region Setup](images/comfort+/2.png)

### 4. Vegetation Region Configuration
- Managed by `UMCF.VegetationRegion`
- Requirements:
  - `mesh` geometry input
  - `Leaf Area Density` (`LAD`)
  - `vegetation properties`
  - `mesh parameters`

![Vegetation Region Configuration](images/comfort+/3.png)

### 5. Timing Parameters
- Uses `EnergyPlus Weather` file (`.EPW`)
- Requires:
  - `Start Day` (365-day based)
  - `start time`
  - `duration`
  - `end time` is calculated by adding the `start time` and `duration`

![Timing Configuration](images/comfort+/4.png)

### 6. Simulation Settings
- Key parameters include:  
   - `Number of CPUs` (`N`)  
   - `maxFluidIterations` (`F`)  
   - `Write Interval` (`W`)  
   - `Initial Solid Timestep Factor` (`I`)  
   - `minDeltaT` (`T`)  
   - `maxDeltaT` (`T`)  
   - `minFluidIteration` (`F`)  
   - `pcEqnForm` (`p`)  
   - `dampingThickness` (`d`)  
   - `alphaCoefU` (`U`)  
   - `alphaCoefT` (`T`)  

![Simulation Settings](images/comfort+/5.png)

### 7. Case Generation
- Connect all configured components
- Set `Write Case` to `True`
- Outputs `UMCF.UMCFCase` which must be connected to the `Case Run` component

![Case Generation](images/comfort+/6.png)

### 8. Simulation Execution
- Two-step process:
  1. Prepare simulation
     - Set `Prepare Simulation` or `Prepare Simulation in Parallel` to `True`
  3. Run simulation
     - Set `Run Simulation` or `Run Simulation in Parallel` to `True`

Note: Use consistent parallel settings for preparation and execution

![Simulation Execution](images/comfort+/7.png)

### 9. Analysis & Visualization
- Uses `probing` component
- Samples field values at point locations
- Writes results to file using input fields
- Enables value analysis and visualization by running the `probes` function

![Analysis & Visualization](images/comfort+/8.png)

## Documentation

📚 Visit [docs.eddy3d.com](https://docs.eddy3d.com/) for detailed documentation *(Work in Progress)*

## Presentation

<a href="https://www.youtube.com/watch?v=PuFVGLvi_Xo" target="_blank" rel="noopener noreferrer">
    <img src="https://img.youtube.com/vi/PuFVGLvi_Xo/maxresdefault.jpg" width="480" alt="Final Presentation --- 24Fa --- Microclimate-LSTM-Kriging" class="off-glb">
</a>

## Team


| Name | Seniority | Major | Department | GitHub |
|------|-----------|--------|------------|---------|
| Marcelo Alvarez | Masters | Architecture (DC) | ARCH | [@alvarezdmarch](https://github.com/alvarezdmarch) |
| Gonzalo Vegas | PhD | Architecture | ARCH | [@gvegasol](https://github.com/gvegasol) |
| Shruti Jadhav | Masters | Architecture (HBP) | ARCH | [@ShrutiJadhav27](https://github.com/ShrutiJadhav27) |
| Rui Shen | Masters | Architecture (DC) | ARCH | [@ShiRo-25](https://github.com/ShiRo-25) |
| Chinmay Rothe | Masters | Architecture (HPB) | ARCH | [@ChinmayR5](https://github.com/ChinmayR5) |