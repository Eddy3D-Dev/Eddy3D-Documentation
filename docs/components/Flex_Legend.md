# ![](/images/icons/Flex_Legend.png) Flex Legend - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Flex%20Legend%22)

![](/images/components/Flex_Legend-crop.png)

Create a metric-aware color legend and an optional colored mesh from point/value samples. Supports wind, solar, sun-hours, temperature and other environmental data.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Range | R | Optional value range the legend spans. Wire a viewer's resolved Range output, construct a domain manually, or leave empty to derive it from Values. | `Domain` |
| Plane | Pl | Placement plane: the bar rises along the plane's Y axis from its origin, labels sit to the +X side. Default: world XY at the origin. | `Plane` |
| Size | S | Bar height in model units (bar width and label offsets scale from it). Empty = 30% of the plotted Points' longest bounding-box dimension, then the Case bounds when no Points exist, then 10 units when neither has a usable extent. | `Number` |
| Steps | N | Number of labeled intervals along the bar (N+1 tick labels at exact fractions of the range). Empty = automatic ticks at round speed values (… 3.1, 3.2 … rather than 3.134). | `Integer` |
| Color Map | CM | Color ramp — pick the same map as the Vector Field Viewer. | `Text` |
| Location | L | Optional anchor point overriding the Plane's origin — e.g. a corner of the domain box (plus an offset) to place the legend outside the wind tunnel. The Plane input keeps controlling the bar's orientation. | `Point` |
| Case |  | Optional wind case (or its Domain Box output, or any geometry): places the legend just outside the domain's +X side at ground level, next to the wind tunnel, and scales it to the domain when Size is empty. Location still overrides the position; the Plane input still controls orientation. | `Generic Data` |
| Points | Pts | Optional sample points. Supply one Value per point to create a colored cell mesh. | `Point` |
| Normals |  | Optional orientation normal per Point. Supply one normal for all cells or one per point. Empty = orient every cell parallel to the legend Plane. | `Vector` |
| Offset |  | Distance to lift each generated mesh cell along its normalized surface normal. Default: 0.5 model units (0.5 m in Eddy3D's standard metre workflow). | `Number` |
| Values |  | Optional scalar values, one per Point. They also define Range when Range is empty. | `Number` |
| Metric Type | Metric | Metric preset controlling the legend title and units. Custom produces unitless labels. | `Text` |
| Cell Radius | Radius | Radius of each colored point cell in model units. Empty = inferred from point spacing. | `Number` |
| Units |  | Optional unit override for the selected Metric Type (for example lux, dB or kg/m²). | `Text` |
| Label Style | LS | How the tick labels draw in the viewport. Text is plain 3d text that bakes and exports the way it looks; Bubbles are the classic screen-sized text dots. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Legend Mesh | LM | Vertex-colored legend bar, for baking. | `Mesh` |
| Legend Points | LP | Anchor point per tick label (e.g. for a Text Tag component). | `Point` |
| Legend Values | LV | Tick label text with metric units, aligned with Legend Points. | `Text` |
| Field Mesh | Mesh | Vertex-colored mesh created from Points and Values (one polygonal cell per sample), oriented by the corresponding Normals and lifted by Offset. | `Mesh` |
| Colors |  | Color per finite input value, aligned with Points. | `Colour` |
| Resolved Range | Domain | Range used to color both the legend and field mesh. | `Domain` |