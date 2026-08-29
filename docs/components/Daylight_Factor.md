# ![](/images/icons/Daylight_Factor.png) Daylight Factor - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Daylight%20Factor%22)

![](/images/components/Daylight_Factor-crop.png)

Daylight factor: interior illuminance under the CIE standard overcast sky as a percentage of the simultaneous unobstructed exterior horizontal illuminance.  Feed it the illuminance at each sensor and the exterior illuminance the sky was built for. The ratio is invariant to sky brightness, so the absolute value only has to MATCH the one used for the render — it does not have to be any particular number.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Illuminance | E | Interior illuminance at each sensor under the overcast sky, lux. | `Number` |
| Sky Illuminance | Esky | Unobstructed exterior horizontal illuminance of the sky the render used, lux. The BRE/CIE convention is 10000; it must match the sky actually rendered. | `Number` |
| Target | T | Target daylight factor in percent, for the compliance fraction. BRE's common value is 2 %. | `Number` |
| Areas | A | Optional per-sensor areas for an area-weighted average. Leave empty for a regular grid, where every weight is equal anyway. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Daylight Factor | DF | Daylight factor at each sensor, percent. | `Number` |
| Average | Avg | Mean daylight factor over the grid, percent. | `Number` |
| Minimum | Min | Lowest daylight factor on the grid, percent. | `Number` |
| Uniformity | U | Minimum divided by average — a space can meet an average target while leaving its depth dark, and this is what shows that. | `Number` |
| Above Target | %>T | Fraction of sensors at or above the target, 0-1. | `Number` |
| Report | R | The sky, sensor count and target these numbers were produced under. | `Text` |