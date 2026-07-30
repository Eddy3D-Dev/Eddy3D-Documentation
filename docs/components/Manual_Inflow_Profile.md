# ![](/images/icons/Manual_Inflow_Profile.png) Manual Inflow Profile - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Manual%20Inflow%20Profile%22)

![](/images/components/Manual_Inflow_Profile-crop.png)

Define inflow boundary conditions from a manually entered vertical profile (z/zR, U/UR, k/UR^2) instead of the parametric ABL log-law. Writes fixedProfile inlet conditions for U, k and epsilon. epsilon is derived from the profile as epsilon(z) = Cmu^0.5 * k(z) * d(U)/dz.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Directions | Dirs | Wind directions as meteorological degrees (wind-from, clockwise from north, e.g. 0, 45, 90) or flow vectors. One solver case is created per direction; the profile magnitudes are rotated to each direction. Optional; default is flow toward +X. | `Generic Data` |
| Normalized Height (z/zR) | z/zR | List of normalized heights z/zR (z = height above ground, zR = boundary layer height). | `Number` |
| Normalized Velocity (U/UR) | U/UR | List of normalized streamwise velocities U/UR at each height (UR = reference velocity at zR). | `Number` |
| Normalized TKE (k/UR^2) | k/UR^2 | List of normalized turbulent kinetic energies k/UR^2 at each height. | `Number` |
| Boundary Layer Height (zR) | zR | Boundary layer height zR (m), used to de-normalize z/zR. Optional; default is 250. | `Number` |
| Reference Velocity (UR) | UR | Reference velocity UR at zR (m/s), used to de-normalize U/UR and k/UR^2. Optional; default is 7.8. | `Number` |
| Cmu |  | Turbulence model constant Cmu used to derive epsilon from the profile. Optional; default is 0.09. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Boundary Conditions | BC | Manual-profile inflow boundary conditions (single direction); plug into the wind case BC input. | `Generic Data` |
| Wind Vectors | Vectors | Resolved unit flow vector for the inflow direction. | `Vector` |