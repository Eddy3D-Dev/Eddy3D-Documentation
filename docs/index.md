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

| Module   | Overview                                                     | Core engine                                           | Rhino / Grasshopper | OS support | OpenFOAM (ver) | Radiance (ver) | Other deps            | Docs                                               |
|----------|--------------------------------------------------------------|-------------------------------------------------------|---------------------|------------|----------------|----------------|-----------------------|----------------------------------------------------|
| Outdoor  | Decoupled microclimate (wind + mean radiant temp)            | OpenFOAM; Radiance                                    | 8.15                | Win 10/11  | 8              |  Radiance 5.3              | —                     | [Learn more](https://docs.eddy3d.com/outdoor/)     |
| Outdoor+ | Fully coupled microclimate (wind, radiation, heat, moisture) | OpenFOAM | 8.15                | Win 10/11  | 8              | —              | `urbanMicroclimateFoam` (ETH Zurich Building Physics) | [Learn more](https://docs.eddy3d.com/outdoorplus/) |
| Indoor   | Airflow, moisture, passive scalars (indoor)                  |                                                       | 8.15                | Win 10/11  | 8              | -              | —                     | [Learn more](https://docs.eddy3d.com/indoor/)      |

