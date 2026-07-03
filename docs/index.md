# Eddy3D Modules

The Grasshopper plugin currently contains three modules, please see below.

<div class="grid cards" markdown>

- __Eddy3D Outdoor__

    ---

    Decoupled microclimate simulations, via wind and mean radiant temperature simulations. Driven by OpenFOAM and Radiance.

    ---

    [:octicons-arrow-right-24: View Eddy3D Outdoor Documentation](outdoor/index.md)

- __Eddy3D Outdoor+__

    ---

    Fully coupled microclimate simulations, including wind, radiation, heat, and moisture transfer, driven by `urbanMicroclimateFoam` by ETH Zurich Building Physics.

    ---

    [:octicons-arrow-right-24: View Eddy3D Outdoor+ Documentation](outdoorplus/index.md)

- __Eddy3D Indoor__

    ---

    Modeling airflow, moisture content, and passive scalars in indoor spaces.

    ---

    [:octicons-arrow-right-24: View Eddy3D Indoor Documentation](indoor/index.md)

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

| Module   | Overview                                                     | Core engine            | Package | Rhino (ver) | OS support  | OpenFOAM (ver) | Radiance (ver) |
|----------|--------------------------------------------------------------|------------------------|-----------------------|-------------|----------------|----------------|----------------|
| Outdoor  | Decoupled wind + mean radiant temp                           | OpenFOAM; Radiance     | **Eddy3D**            | 8.27        | Windows / Mac     | 12              |  Auto (rad6R0P2)  |
| Outdoor+ | Fully coupled (wind, radiation, heat, moisture) | OpenFOAM   | **Eddy3D** | 8.27                  | Windows / Mac | 12              | —              |
| Indoor   | Airflow, moisture, passive scalars (indoor)                  | OpenFOAM               | **Eddy3D**            | 8.27        | Windows / Mac     | 12              | -              |

## Downloads

| Plugin | Platform | Link |
|----------|----------|----------------|
| **Eddy3D** (Outdoor, Outdoor+, Indoor, MRT, FluidX3D) | Windows / Mac | [Install via the Rhino Package Manager &mdash; search **`Eddy3D`**](https://rhinopackages.github.io/?search=eddy3d&sort=2&p=Eddy3D){ target="_blank" rel="noopener noreferrer" aria-label="Install Eddy3D via the Rhino Package Manager (opens in a new tab)" } &nbsp;·&nbsp; Windows also has a [standalone installer](https://github.com/Eddy3D-Dev/Eddy3D/releases/latest){ target="_blank" rel="noopener noreferrer" aria-label="Download Eddy3D installer for Windows (opens in a new tab)" } |

!!! tip "Previous Versions"
    View the [**required Rhino 8.27 build details (8.27.26019.16022, en-us)**](https://rhinoversions.github.io/?version=8.27.26019.16022&locale=en-us){ target="_blank" rel="noopener noreferrer" aria-label="required Rhino 8.27 build details (8.27.26019.16022, en-us) (opens in a new tab)" }.

!!! note "One package"
    All modules &mdash; Outdoor, Outdoor+, Indoor, MRT, and FluidX3D &mdash; now ship in the single **`Eddy3D`** package on the Rhino Package Manager (`yak`). The former separate **`UMCF`** package (Outdoor+) has been retired.
