# ![](/images/icons/Atmospheric_Boundary_Layer.png) Atmospheric Boundary Layer - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Atmospheric%20Boundary%20Layer%22)

![](/images/components/Atmospheric_Boundary_Layer-crop.png)

Define atmospheric boundary layer inflow conditions for Eddy3D.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Directions | Dirs | Wind directions as meteorological degrees (wind-from, clockwise from north) or flow vectors. One solver case is created per direction. Optional; default is flow toward -Y (south). | `Generic Data` |
| Wind Speed | U | Wind speed at the reference height (m/s), one value per wind direction. A single value applies to all directions; a shorter list repeats its last value. Optional; default is 5. | `Number` |
| Reference Height | Zref | Reference height for wind speed (m). Optional; default is 10. | `Number` |
| Roughness Length (z0) | z0 | Aerodynamic roughness length (m). Higher values indicate rougher terrain. Optional; default is 1. | `Number` |
| Ground Height | Zgnd | Ground/displacement height for the ABL log-law profile (m). Optional; default is 0. | `Number` |
| Turbulent KE (k) | k | Inlet/initial turbulent kinetic energy k (m^2/s^2) for the ABL. Used by the k field and the turbulence transports; the inlet patch still uses the atmBoundaryLayer k profile. Optional; default is 0.015. | `Number` |
| Turbulent Epsilon (ε) | epsilon | Inlet/initial turbulent dissipation rate epsilon (m^2/s^3) for the k-epsilon family. The inlet patch still uses the atmBoundaryLayer epsilon profile. Optional; default is 0.135. | `Number` |
| Turbulent Omega (ω) | omega | Inlet/initial specific dissipation rate omega (1/s) for the k-omega SST model. Optional; default is 100. | `Number` |
| Terrain Type | Terrain | Upwind terrain class from the revised Davenport roughness classification (Davenport 1960; Wieringa 1992; Davenport, Grimmond, Oke & Wieringa 2000): 1 Sea 0.0002 m · 2 Smooth 0.005 m · 3 Open 0.03 m · 4 Roughly open 0.1 m · 5 Rough 0.25 m · 6 Very rough 0.5 m · 7 Skimming 1 m · 8 Chaotic 2 m. Picking a class sets the roughness length z0 from the table (shown on the banner); Custom uses the Roughness Length input instead. Describe the terrain the wind CROSSES upwind of the site, not the site itself. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary Conditions | BC | Atmospheric boundary layer inflow boundary conditions (including the wind directions); plug into the wind case BC input, or into the Outdoor+ Air Region (which uses the first direction/speed because one Air Region represents one UMCF case). | `Generic Data` |
| Wind Vectors | Vectors | Resolved unit flow vectors, one per wind direction. | `Vector` |