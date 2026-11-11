# ![](/images/icons/Stormwater_Flowlines.png) Stormwater Flowlines - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Stormwater%20Flowlines%22)

![](/images/components/Stormwater_Flowlines-crop.png)

Traces where the runoff goes, as curves over the graded surface. From a full run these are the solved velocity paths; from a fast run they are steepest-descent paths down the depression-filled terrain.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | A run from Stormwater Run. | `Generic Data` |
| Seed Spacing | Spacing | Distance in metres between the points flowlines are started from. Smaller is denser and slower. | `Number` |
| Minimum Catchment | MinArea | Terrain mode only: seed a line only where at least this much upslope area already drains through (m²). Raising it turns a hairball of sheet flow into the drainage NETWORK, which is usually what you want to look at. 0 seeds everywhere. | `Number` |
| Maximum Length | MaxLen | Give up on a line after this many metres, so a slow eddy cannot spin forever. | `Number` |
| Time |  | Minutes from the storm's start. Full runs only — the velocity field at the nearest stored snapshot is traced. Leave at 0 to use the peak-velocity field. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Flowlines | Lines | One polyline per traced path. | `Curve` |
| Values |  | Sampled along each line, one branch per line: flow speed (m/s) in a Full run, contributing area (m²) in a Fast one. | `Number` |
| Colors |  | Colour per POINT, pairing 1:1 with Values. For drawing a coloured line use Segments + Segment Colors instead — there is one fewer segment than points. | `Colour` |
| Range |  | Value range used for the colours, for a legend. | `Domain` |
| Segments |  | Each flowline split into stretches of one display colour (8 bands), one branch per line. Pairs 1:1 with Segment Colors — wire both into a Custom Preview, or just use the component's own viewport preview, which draws exactly this. | `Curve` |
| Segment Colors | SegColors | One colour per stretch, from the midpoint of its band. Pairs exactly with Segments. | `Colour` |