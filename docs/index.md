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
| Outdoor  | Decoupled wind + mean radiant temp                           | OpenFOAM; Radiance     | **Eddy3D**            | 8.27        | Windows / Mac     | 12 (Foundation) |  Auto (rad6R0P2)  |
| Outdoor+ | Fully coupled (wind, radiation, heat, moisture) | OpenFOAM   | **Eddy3D** | 8.27                  | Windows / Mac | 12 (Foundation) | —              |
| Indoor   | Airflow, moisture, passive scalars (indoor)                  | OpenFOAM               | **Eddy3D**            | 8.27        | Windows / Mac     | 12 (Foundation) | -              |

## Downloads

Install **Eddy3D** from the Rhino Package Manager (run `PackageManager` in Rhino 8 and search for **`Eddy3D`**). For the current version and release notes, see the [**Eddy3D download page**](https://eddy3d.com/download/){ target="_blank" rel="noopener noreferrer" aria-label="Eddy3D download page (opens in a new tab)" }.

!!! tip "Previous Versions"
    View the [**required Rhino 8.27 build details (8.27.26019.16022, en-us)**](https://rhinoversions.github.io/?version=8.27.26019.16022&locale=en-us){ target="_blank" rel="noopener noreferrer" aria-label="required Rhino 8.27 build details (8.27.26019.16022, en-us) (opens in a new tab)" }.

!!! note "One package"
    All modules &mdash; Outdoor, Outdoor+, Indoor, MRT, and FluidX3D &mdash; now ship in the single **`Eddy3D`** package on the Rhino Package Manager (`yak`). The former separate **`UMCF`** package (Outdoor+) has been retired.
