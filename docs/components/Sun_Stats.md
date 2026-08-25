# ![](/images/icons/Sun_Stats.png) Sun Stats - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Stats%22)

![](/images/components/Sun_Stats-crop.png)

Area-weighted min/mean/median/max over a sun result, plus the area and fraction reaching a threshold.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Values | V | Per-point results: sun hours, irradiation, whatever is being summarised. | `Number` |
| Grid | G | Optional analysis mesh — cell areas are taken from its faces, one per point. Without it every point is weighted equally, which is only right for a uniform grid. | `Mesh` |
| Areas | A | Optional explicit area per point, overriding the mesh. | `Number` |
| Threshold | T | The value the 'how much area reaches this' question is asked about. Inclusive. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Min |  | Smallest value. | `Number` |
| Mean |  | Area-weighted mean. | `Number` |
| Median | Med | Area-weighted median. | `Number` |
| Max |  | Largest value. | `Number` |
| Area Above | AA | Area at or above the threshold, in model units squared. | `Number` |
| Fraction Above | FA | That area as a fraction of the total, 0-1. | `Number` |
| Report | R | The summary, including how it was weighted. | `Text` |