# ![](/images/icons/Water_Surface.png) Water Surface - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Water%20Surface%22)

![](/images/components/Water_Surface-crop.png)

Coupled evaporating water surface for urbanMicroclimateFoam. The water geometry becomes a named air patch that exchanges sensible heat and moisture with the air; water motion and a moving free surface are not solved. Requires an UMF build that includes the simpleWater model.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Water Surface | Surface | Planar or meshed water surface. It should coincide with an exposed terrain/ground boundary; model terrain with an opening beneath the water when possible. | `Geometry` |
| Mixed Depth | Depth | Effective thermally mixed water depth in metres. | `Number` |
| Albedo |  | Short-wave reflectivity of the water surface (0–1). | `Number` |
| Emissivity |  | Long-wave emissivity of the water surface (0–1). | `Number` |
| Aerodynamic Resistance | Resistance | Surface aerodynamic resistance in s/m. Use -1 to derive it from local wind speed. | `Number` |
| Refinement Level | Refine | SnappyHexMesh refinement level at the water surface. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Water Settings | Water | Connect directly to the Water Surface input on Outdoor+ Case. | `Generic Data` |