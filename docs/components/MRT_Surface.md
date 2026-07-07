# ![](../images/icons/MRT_Surface.png) MRT Surface - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Surface%22)

![](../images/components/MRT_Surface-crop.png)

Mesh Breps into a tagged radiation surface for an MRT analysis.

#### Input
* ##### Geometry (G) 
Surface geometry to mesh.
* ##### Type (T) 
Surface type: 0 Building, 1 Ground, 2 Vegetation, 3 Tree.
* ##### Simulated (S) 
True if the surface temperature is solved; false treats it as ambient.
* ##### Patch Size (P) 
Target mesh patch edge length (m) for view-factor resolution.
* ##### Mat 
Optional material from a Surface / Vegetation / Tree Settings component; overrides the default reflectance / Radiance material for this surface.
* ##### Tsrf 
Optional fixed surface temperature (°C) for the longwave MRT — one value (held all year) or an 8760-hour series. When set, this surface uses the given temperature instead of the EnergyPlus solve or ambient (overrides Simulated). Leave empty to keep Simulated/Ambient.

#### Output
* ##### Surface (S)
Tagged radiation surface for the MRT component.
* ##### Mesh (M)
The meshed surface (preview).