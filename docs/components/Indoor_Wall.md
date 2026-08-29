# ![](/images/icons/Indoor_Wall.png) Indoor Wall - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Wall%22)

![](/images/components/Indoor_Wall-crop.png)

Set an indoor wall temperature (°C). Wire a room surface to give just that surface its own temperature patch; leave it empty for a single case-wide wall temperature.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Temperature | T | Wall temperature (°C). | `Number` |
| Surface | S | Optional room surface to give this temperature. Must be part of the room Brep's shell; leave empty to set one case-wide wall temperature instead. | `Brep` |
| Name | N | Optional patch name (letters/digits/underscore). Defaults to a positional name. | `Text` |
| Power | P | Optional heat load in WATTS this surface emits, instead of a fixed temperature — the nameplate figure for an occupant (~100 W) or a luminaire. OpenFOAM spreads the total over the surface's meshed area, so the wattage stays right however finely it meshes. When set, Temperature is ignored for this wall. A CLOSED Brep (a person, a cabinet) becomes an obstacle carved out of the room with the load on its skin. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wall Temperature | WT | Wall temperature in Kelvin for the Indoor Case component's Wall Temp input. | `Number` |
| Wall | W | Named wall patch for the Indoor Case component's Walls input. Only meaningful when a Surface is supplied. | `Generic Data` |