## ![Building Surface Icon](../images/icons/Building_Surface.png) Building Surface

![Building Surface Component](../images/components/Building_Surface-crop.png)

Building Material

 Assigns thermal and optical properties to building geometries. Affects how buildings reflect sunlight and emit heat.


 Eddy3D 1.0.0.827

#### Input
* ##### Geo 
Building facade geometry (Breps). Will be meshed into analysis patches.
* ##### Patch 
Size of analysis mesh patches. Units: meters. Smaller = more accurate but slower. Default: 3m
* ##### Set 
Optional: Material and property settings from Surface Settings component.
* ##### Src 
Surface temperature data source for MRT calculation.
* ##### Temp 
Optional: User-defined surface temperatures. Units: °C

#### Output
* ##### Srf
Radiation surface for MRT Simulation component