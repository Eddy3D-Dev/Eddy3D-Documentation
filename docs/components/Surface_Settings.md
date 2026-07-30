# ![](/images/icons/Surface_Settings.png) Surface Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Surface%20Settings%22)

![](/images/components/Surface_Settings-crop.png)

Thermal + optical material properties for a building/ground MRT surface.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Thickness | Thick | Material thickness (m). | `Number` |
| Conductivity | k | Thermal conductivity W/(m·K). Concrete ≈ 2.3. | `Number` |
| Density | rho | Density kg/m³. Concrete ≈ 2400. | `Number` |
| Specific Heat | Cp | Specific heat J/(kg·K). | `Number` |
| Thermal Absorptance | eT | Longwave emissivity 0–1. | `Number` |
| Solar Absorptance | aS | Solar absorptance 0–1 (light ~0.3, dark ~0.9). | `Number` |
| Visible Absorptance | aV | Visible absorptance 0–1. | `Number` |
| Radiance Material | RadMat | Optional custom Radiance material string. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | Material for the MRT Surface component. | `Generic Data` |