# Eddy3D Modules

The Grasshopper plugin currently contains three modules, please see below.

<div class="grid cards" markdown>

- __Eddy3D Outdoor__

    ---

    Decoupled microclimate simulations, via wind and mean radiant temperature simulations. Driven by OpenFOAM and Radiance.

    ---

    [:octicons-arrow-right-24: Learn more](https://docs.eddy3d.com/outdoor/)

- __Eddy3D Outdoor+__

    ---

    Fully coupled microclimate simulations, including wind, radiation, heat, and moisture transfer, driven by `urbanMicroclimateFoam` by ETH Zurich Building Physics.

    ---

    [:octicons-arrow-right-24: Learn more](https://docs.eddy3d.com/outdoorplus/)

- __Eddy3D Indoor__

    ---

    Modeling airflow, moisture content, and passive scalars in indoor spaces.

    ---

    [:octicons-arrow-right-24: Learn more](https://docs.eddy3d.com/indoor/)

</div>

<style>
    /* Application header should be static for the landing page */
    .md-header {
      position: initial;
    }
    /* Hide navigation */
    @media screen and (min-width: 76.25em) {
      .md-sidebar--primary {
        display: none;
      }
    }
      .md-content__button {
    display: none;
  }
</style>

## Requirements

| Module   | Overview                                                     | Core engine          | Package | Rhino (ver) | OS support | OpenFOAM (ver) | Radiance (ver) |
|----------|--------------------------------------------------------------|----------------------|----------------------|-------------|------------|----------------|----------------|
| Outdoor  | Decoupled wind + mean radiant temp                           | OpenFOAM; Radiance   | **Eddy3D**           | 8.21        | Windows (Mac via manual install)     | 8              |  Radiance 5.3  |
| Outdoor+ | Fully coupled (wind, radiation, heat, moisture) | OpenFOAM             | **Eddy3D-OutdoorPlus** | 8.21      | Windows/Mac | 8              | —              |
| Indoor   | Airflow, moisture, passive scalars (indoor)                  | OpenFOAM             | **Eddy3D**           | 8.21        | Windows (Mac via manual install)     | 8              | -              |

## Downloads

| Plugin | Platform | Link |
|----------|----------|----------------|
| **Eddy3D** (Outdoor / Indoor) | Windows | [Download Installer](https://github.com/Eddy3D-Dev/Eddy3D/releases/latest) |
| **Eddy3D-OutdoorPlus** (Outdoor+) | Windows / Mac | [Install `UMCF` via Rhino Package Manager (`yak`)](https://rhinopackages.github.io/?search=Umcf&sort=2 ) |

!!! tip "Previous Versions"
    Official previous Rhino versions can be found at [**rhinoversions.github.io**](https://rhinoversions.github.io/).

!!! note "Plugin Naming"
    The **Outdoor+** module is currently distributed under the package name **`UMCF`** via the Rhino Package Manager (`yak`). Ensure you enable **"Include pre-releases"** in the Package Manager.

