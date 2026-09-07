# ![](/images/icons/WRF_ABL.png) WRF ABL - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20ABL%22)

![](/images/components/WRF_ABL-crop.png)

Build an atmospheric boundary layer from a WRF site series. The output plugs into the same socket as Outdoor's ABL, so it drives the wind study, Outdoor+, FluidX3D and LBM alike. Note this is uniform in plan: one log-law profile at the site, not a spatially varying inflow.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Series | S | The site series from WRF Weather. | `Generic Data` |
| Terrain | T | Aerodynamic roughness of the ground upwind of the site, as a Davenport class. WRF cannot supply this: its own land use describes cells kilometres across, while the CFD domain needs the roughness of the specific approach. Choose Custom to set z0 directly. | `Text` |
| Roughness | z0 | Aerodynamic roughness length in metres. Used only when Terrain is Custom. | `Number` |
| Ground Height | zG | Displacement height of the ABL profile, in metres. | `Number` |
| Mode | M | Average gives one boundary for the whole run — note the direction is a VECTOR mean, since averaging bearings arithmetically makes 350 and 10 degrees come out as 180. Sectors gives one per direction that actually occurred, which is what a multi-direction wind study wants. Hourly gives one per history frame. | `Text` |
| Sectors | N | How many direction sectors to bin into. Used only in sector mode. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary Conditions | BC | The ABL boundary. Wire to a wind study, Outdoor+, FluidX3D or LBM. | `Generic Data` |
| Wind Vectors | V | Unit vectors the wind blows TOWARD, one per boundary. | `Vector` |
| Speed | U | Reference speed at 10 m, one per boundary, m/s. | `Number` |
| Report | R | One line per boundary. | `Text` |