# ![](/images/icons/Sunlight_Compliance.png) Sunlight Compliance - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sunlight%20Compliance%22)

![](/images/components/Sunlight_Compliance-crop.png)

EN 17037 sunlight exposure and BRE amenity overshadowing / APSH against a sun-hours result. Design aid — thresholds are editable and not certified.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Standard | S | 0 = BRE amenity overshadowing (hours on the assessment date) 1/2/3 = EN 17037 sunlight exposure, minimum / medium / high 4 = BRE annual probable sunlight hours (needs Winter Hours) | `Integer` |
| Sun Hours | H | Per-point sun hours. For the amenity and EN 17037 metrics this must be a SINGLE-DAY study on the assessment date, not an annual total. | `Number` |
| Winter Hours | WH | Per-point sun hours within the winter window (21 Sep - 21 Mar). APSH only. | `Number` |
| Areas | A | Optional area per point. Without it every point counts equally, which is only right for a uniform grid. | `Number` |
| Available Hours | AH | Total hours the sun was above the horizon over the study period — the APSH denominator. Take it from the Sun Hours report so it matches the study's own time base. | `Number` |
| Available Winter Hours | AWH | The same, restricted to the winter window. APSH only. | `Number` |
| Amenity Hours | AmH | Hours a point must receive to count as sunlit, for the amenity metric. | `Number` |
| Amenity Area Fraction | AmF | Fraction of the area that must reach Amenity Hours. | `Number` |
| APSH Annual Fraction | AaF | Fraction of available hours required annually. | `Number` |
| APSH Winter Fraction | AwF | Fraction of available hours required in winter. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Passes | P | Scheme-level verdict. | `Boolean` |
| Value | V | The metric's value. | `Number` |
| Threshold | T | The value it was judged against. | `Number` |
| Point Passes | PP | Per-point pass flags, for colouring the grid. | `Boolean` |
| Report | R | The metric, its criterion, and every assumption behind the number. | `Text` |