# ![](/images/icons/Runoff_Zones.png) Runoff Zones - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Runoff%20Zones%22)

![](/images/components/Runoff_Zones-crop.png)

Tags an area of the site with how rough it is and how much rain it sheds.  Manning's n here is the OVERLAND FLOW value, several times the channel value for the same material — at the millimetre depths of sheet flow the surface texture is the whole channel, and using a channel roughness makes runoff arrive far too fast.  A Curve Number (1–100) models losses that grow through a storm as the ground wets up; leave it at 0 to use the flat runoff coefficient instead.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Areas |  | Closed curves outlining where this surface type applies, in plan. Curves are projected to the world XY plane, and a cell belongs to a zone when its CENTRE does. | `Curve` |
| Surface |  | A preset surface type. Choosing one fills in the Curve Number and Manning's n below; override either by wiring it, or pick Custom and set both. | `Text` |
| Curve Number | CN | SCS Curve Number, 1–100. Higher sheds more: 98 is sealed paving, 61 a healthy lawn on an average soil, 55 mature woodland. Unlike a flat coefficient it makes runoff GROW through a storm as the ground wets up, which is why it suits a design event.  0 disables it in favour of Runoff Coefficient. Wiring this overrides the preset. | `Number` |
| Runoff Coefficient | C | Fraction of rainfall that becomes runoff, 0–1, used only when Curve Number is 0. The cruder model, but the one most local guidance is written in. | `Number` |
| Manning's n | n | Overland-flow roughness (s/m^⅓). Wiring this overrides the preset. Typical: 0.012 smooth paving, 0.05 gravel, 0.24 short grass, 0.40 woodland litter. | `Number` |
| Initial Abstraction Ratio | Ia/S | Fraction of the soil's storage absorbed before ANY runoff starts. 0.05 is the default and the value re-analysis of the original gauge data supports for small, largely impervious urban catchments; the textbook TR-55 figure of 0.2 was fitted to agricultural watersheds and under-predicts urban runoff. Pass 0.2 to reproduce it. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zones |  | Runoff zones for Stormwater Grid. | `Generic Data` |
| Area |  | Total plan area covered (m²). | `Number` |