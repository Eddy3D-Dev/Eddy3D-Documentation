# ![](/images/icons/Sunlight_Compliance.png) Sunlight Compliance - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sunlight%20Compliance%22)

EN 17037 sunlight exposure and BRE amenity overshadowing / APSH, evaluated against a Sun Hours result. A design aid, not a certified daylight and sunlight report — the thresholds are secondary-sourced (surveyors' summaries, not the standards themselves) and exposed as inputs precisely so they can be corrected once someone has the standards to hand.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Standard | S | Metric to evaluate: 0 = BRE amenity overshadowing (hours on the assessment date), 1/2/3 = EN 17037 sunlight exposure minimum/medium/high, 4 = BRE annual probable sunlight hours (needs Winter Hours). Default 0. | `Integer` |
| Sun Hours | H | Per-point sun hours. For the amenity and EN 17037 metrics this must be a single-day study on the assessment date, not an annual total. | `Number` |
| Winter Hours | WH | Per-point sun hours within the winter window (21 Sep – 21 Mar). APSH only. | `Number` |
| Areas | A | Optional area per point. Without it every point counts equally, which is only right for a uniform grid. | `Number` |
| Available Hours | AH | Total hours the sun was above the horizon over the study period — the APSH denominator. Take it from the Sun Hours report so it matches the study's own time base. Default 0. | `Number` |
| Available Winter Hours | AWH | The same, restricted to the winter window. APSH only. Default 0. | `Number` |
| Amenity Hours | AmH | Hours a point must receive to count as sunlit, for the amenity metric. Default 2.0. | `Number` |
| Amenity Area Fraction | AmF | Fraction of the area that must reach Amenity Hours. Default 0.5. | `Number` |
| APSH Annual Fraction | AaF | Fraction of available hours required annually. Default 0.25. | `Number` |
| APSH Winter Fraction | AwF | Fraction of available hours required in winter. Default 0.05. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Passes | P | Scheme-level verdict. | `Boolean` |
| Value | V | The metric's value. | `Number` |
| Threshold | T | The value it was judged against. | `Number` |
| Point Passes | PP | Per-point pass flags, for colouring the grid. | `Boolean` |
| Report | R | The metric, its criterion, and every assumption behind the number. | `Text` |

#### Notes

- The socket set is fixed on purpose. The source notes that the metric selector could instead be a standard dropdown that rebuilds outputs, but that would make the component an `IGH_VariableParameterComponent` with its own family of wire-migration hazards — judged not worth it for three metrics, so `Standard` is a plain integer (0–4) instead.
- `Standard = 4` (APSH) requires `Winter Hours` to carry the same point count as `Sun Hours`, and `Available Hours` to be greater than 0 (it's the fraction denominator) — the component errors out with a Remark otherwise.
- `Areas`, if supplied, must match the point count of `Sun Hours` or be left empty entirely.
