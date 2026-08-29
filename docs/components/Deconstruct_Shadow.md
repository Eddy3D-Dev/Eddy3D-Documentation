# ![](/images/icons/Deconstruct_Shadow.png) Deconstruct Shadow - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20Shadow%22)

![](/images/components/Deconstruct_Shadow-crop.png)

Per-point sun exposure (and, for an explicit HOY selection, the per-instant trees) from a Shadow Result — without putting a whole year of lit flags on the canvas.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | Res | Result output of the Shadow component. | `Generic Data` |
| HOY | H | Hour(s) of the year [1-8760] to restrict to — wire the Hour Of Year component. Left empty, the per-point outputs cover every instant the study solved and the per-instant trees stay empty, which is the tree this component exists to avoid. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | The analysis points the study solved, in their original order — so a preview needs one wire from here rather than a second reference to the grid. | `Point` |
| Lit Fraction | LF | Share of the SELECTED instants each point was lit for, 0-1. Unweighted: this is "how often", which is what a shadow study reads as. One value per point. | `Number` |
| Sun Hours | SH | Hours of direct sun each point received over the selected instants — the same number Sun Hours reports, recovered from the solved field instead of re-traced. | `Number` |
| Colors | Col | Point-specific ramp over Lit Fraction, matching Sun Hours' blue-to-yellow endpoints. | `Colour` |
| Lit | L | Lit or shaded at each SELECTED instant — one branch per HOY, each holding every point's flag. Populated only when HOY is connected. | `Boolean` |
| Sunlit Points | SP | Just the lit points at each selected instant, one branch per HOY. Populated only when HOY is connected. | `Point` |
| Instants | I | The local date and time of each selected instant, in branch order. | `Text` |