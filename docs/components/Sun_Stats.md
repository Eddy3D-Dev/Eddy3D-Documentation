# ![](/images/icons/Sun_Stats.png) Sun Stats - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Stats%22)

Area-weighted min/mean/median/max over a per-point sun result, plus the area and fraction reaching a threshold. Weighting matters: an analysis grid trimmed to a site boundary is rarely uniform, and averaging the points instead of the area over-counts wherever the grid is dense — silently, because the answer still looks plausible.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Values | V | Per-point results to summarise: sun hours, irradiation, or anything else. | `Number` |
| Grid | G | Optional analysis mesh. Cell areas are taken from its faces, one per point. Without it every point is weighted equally, which is only correct for a uniform grid. | `Mesh` |
| Areas | A | Optional explicit area per point, overriding the mesh. | `Number` |
| Threshold | T | The value the "how much area reaches this" question is asked about. Inclusive (≥). Default `2.0`. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Min | Min | Smallest value. | `Number` |
| Mean | Mean | Area-weighted mean. | `Number` |
| Median | Med | Area-weighted median. | `Number` |
| Max | Max | Largest value. | `Number` |
| Area Above | AA | Area at or above the threshold, in model units squared. | `Number` |
| Fraction Above | FA | That area as a fraction of the total, 0–1. | `Number` |
| Report | R | The summary text, including how the values were weighted. | `Text` |

#### Notes

- **Weighting is chosen automatically, in this priority order**: explicit **Areas** wins if supplied (must match **Values** count exactly, or the component errors); otherwise **Grid** face areas are used, one per value; otherwise every point is weighted equally. If a **Grid** is wired but its face count doesn't match **Values**, the component does *not* silently fall back — it raises a runtime Warning ("falling back to equal weighting. Wire the mesh the points came from") because a mismatched grid is treated as a wiring mistake, not something to paper over.
- Quad mesh faces are measured as two triangles rather than assumed planar, since an analysis grid draped over terrain routinely has warped quads that a parallelogram formula would over-report.
- An empty **Values** list is a runtime Error, not a zero result.
- The component's canvas message shows the headline number at a glance, e.g. `82% ≥ 2`.
