# ![](/images/icons/Vegetation_Settings.png) Vegetation Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vegetation%20Settings%22)

![](/images/components/Vegetation_Settings-crop.png)

Leaf/canopy material properties for an MRT vegetation surface.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Height Plants | HP | Height of plants (m). | `Number` |
| LeafAreaIndex | LAI | Leaf area index (dimensionless). | `Number` |
| LeafReflectivity | LR | Leaf reflectivity 0–1. | `Number` |
| LeafEmissivity | LE | Leaf emissivity 0–1. | `Number` |
| MinStomatalResistance | MSR | Minimum stomatal resistance (s/m). | `Number` |
| Radiance Material | RadMat | Optional custom Radiance material string. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | Vegetation material for the MRT Surface component's Material input. | `Generic Data` |