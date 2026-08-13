# ![](/images/icons/MRT_Surface.png) MRT Surface - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Surface%22)

![](/images/components/MRT_Surface-crop.png)

Tags Breps or Meshes as a radiation surface for an MRT analysis. Breps are meshed at Patch Size; Meshes are used face-for-face as given.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Surface geometry: Breps (meshed at Patch Size) or Meshes (used as given — their faces ARE the view-factor patches, so refine coarse meshes upstream). | `Geometry` |
| Type | T | Surface type. Drives the default reflectance, the EnergyPlus construction, and the type-specific view-factor totals. | `Text` |
| Simulated | S | True if the surface temperature is solved; false treats it as ambient. | `Boolean` |
| Patch Size | P | Target mesh patch edge length (m) for view-factor resolution. | `Number` |
| Material | Mat | Optional material from a Surface / Vegetation / Tree Settings component; overrides the default reflectance / Radiance material for this surface. | `Generic Data` |
| Temperature | Tsrf | Optional surface temperature (°C) for longwave MRT. Connect SurfaceTemp directly: both {hour}(surface points) and {surface point}(hours) trees are accepted. A single value or one shared 8760-hour series is also supported. Overrides Simulated. | `Number` |
| Temperature Points | TempPts | Optional points used to calculate SurfaceTemp. When their count differs from the MRT mesh polygon count, each polygon uses its nearest temperature sample. | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surface | S | Tagged radiation surface for the MRT component. | `Generic Data` |
| Mesh | M | The meshed surface (preview). | `Mesh` |