# ![](/images/icons/Vertical_Sky_Component.png) Vertical Sky Component - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vertical%20Sky%20Component%22)

![](/images/components/Vertical_Sky_Component-crop.png)

Vertical Sky Component per point, in percent: the diffuse illuminance a vertical plane receives directly from a CIE standard overcast sky, over the illuminance an unobstructed horizontal plane would receive under the same sky.  Geometry only — no weather, no orientation, no time of year. An unobstructed vertical plane reads 39.6%; BRE BR 209 reads 27% as the guideline for conventional window design.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Obstructing geometry: buildings, terrain, canopies. Obstructions are treated as perfectly black — VSC counts direct skylight only, so nothing here reflects. | `Geometry` |
| Points | P | Analysis points, on the plane whose sky access is wanted. Wire Facade Grid for a facade map, or place points at window centres for the BR 209 assessment. | `Point` |
| Normals | N | Outward normal at each point — REQUIRED. VSC is a property of a plane, not of a location: the same point facing two ways has two different VSCs. Facade Grid emits these alongside its points. | `Vector` |
| Offset | O | Distance to lift each point along its normal before tracing, so the plane it sits on does not occlude itself. | `Number` |
| Sky Bands | SB | Sky subdivision from zenith to horizon; cell count is about 4πN²/3, so the default 24 is ~2,400 cells. Raise it for a smoother map at proportionally more cost — 24 already sits within 0.02 points of the analytic answer for an open plane. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| VSC |  | Vertical Sky Component per point, PERCENT. 39.6 is a fully open vertical plane. | `Number` |
| Colors | Col | Per-point colours on BR 209's own bands — under 5%, 5-15%, 15-27%, 27% and over — so the guideline reads off the map rather than out of a legend. | `Colour` |
| Report | R | Range, band counts, rays and the assumptions used. | `Text` |