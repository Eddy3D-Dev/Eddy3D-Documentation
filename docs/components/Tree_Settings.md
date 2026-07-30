# ![](/images/icons/Tree_Settings.png) Tree Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Tree%20Settings%22)

![](/images/components/Tree_Settings-crop.png)

Canopy material properties for an MRT tree surface.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Reflectivity | R | Canopy shortwave reflectivity 0–1. | `Number` |
| Emissivity | E | Canopy longwave emissivity 0–1. | `Number` |
| Radiance Material | RadMat | Optional custom Radiance material string for the tree canopy. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | Tree/canopy material for the MRT Surface component's Material input. | `Generic Data` |