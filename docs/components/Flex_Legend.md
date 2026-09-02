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
| Contours |  | Contour presentation. Off keeps one colored cell per sample. Bands re-meshes the samples into flat-filled contour bands; Lines adds isolines over the cells; Bands + Lines gives the classic contour map; Lines Only draws isolines alone. | `Text` |
| Bands |  | Number of contour bands (and therefore isolines) across the Range. Empty = bands at round values, matching the legend's automatic ticks. | `Integer` |
| Smoothing | Smooth | Laplacian smoothing passes applied to the Values before contouring, for rounder isolines. This CHANGES the plotted numbers (the Values output is untouched) and is reported as a Remark. Default: 0 = contour the data as measured. | `Integer` |
| Analysis Mesh | AMesh | Optional mesh carrying the field, with one Value per mesh vertex or per mesh face. Use it for facades, terrain and any sample set whose connectivity cannot be inferred from the Points alone. Empty = derive topology from Points. | `Mesh` |
| Max Edge | MaxEdge | Longest triangle edge kept when Points have to be tessellated — this is what leaves courtyards and building footprints as holes instead of bridging them. Empty = 1.8x the detected sample spacing. Ignored for a regular sample grid. | `Number` |
| Bin Size | Bin | Hexagon size (centre to corner, in model units) for the Hexbins styles. Empty = about 40 hexagons across the sampled area, never finer than the sample spacing. | `Number` |
| Aggregate | Agg | How the samples inside one hexagon become the value it draws. Count maps sampling density rather than the measured quantity. | `Text` |
| Highlight Top | Top | Circle the N highest-valued hexagons and output those circles. 0 = none. | `Integer` |
| Boundary |  | Optional closed, planar boundary (a district or site outline): hexagons whose centre falls outside it are dropped, and the outline is drawn dashed over the map. | `Curve` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Legend Mesh | LM | Vertex-colored legend bar, for baking. | `Mesh` |
| Legend Points | LP | Anchor point per tick label (e.g. for a Text Tag component). | `Point` |
| Legend Values | LV | Tick label text with metric units, aligned with Legend Points. | `Text` |
| Field Mesh | Mesh | Vertex-colored mesh created from Points and Values (one polygonal cell per sample), oriented by the corresponding Normals and lifted by Offset. | `Mesh` |
| Colors |  | Color per finite input value, aligned with Points. | `Colour` |
| Resolved Range | Domain | Range used to color both the legend and field mesh. | `Domain` |
| Contours |  | Isoline polylines at each band edge, empty unless a line-drawing Contours style is selected. | `Curve` |
| Contour Values | CValues | Field value of each contour curve, aligned with Contours. | `Number` |
| Bin Centers | Centers | Centre of each drawn hexagon, empty unless a Hexbins style is selected. | `Point` |
| Bin Values | BinValues | Aggregated value per hexagon, aligned with Bin Centers. | `Number` |
| Highlights |  | Circles around the Highlight Top hexagons, highest first. | `Curve` |