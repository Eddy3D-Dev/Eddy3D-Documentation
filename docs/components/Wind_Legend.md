# ![](/images/icons/Wind_Legend.png) Wind Legend - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Legend%22)

![](/images/components/Wind_Legend-crop.png)

Color-scale legend for wind speed: a colored bar with labeled ticks matching the Wind Field Viewer's ramp. Wire the viewer's Range output into Range so the legend always shows the span the colors actually map, and pick the same Color Map.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Range | R | Speed range the legend spans (m/s). Wire the Wind Field Viewer's Range output — that is the resolved range its colors actually map — or construct a domain to set the scale manually. | `Domain` |
| Plane | Pl | Placement plane: the bar rises along the plane's Y axis from its origin, labels sit to the +X side. Default: world XY at the origin. | `Plane` |
| Size | S | Bar height in model units (bar width and label offsets scale from it). Empty = 10 units, or scaled to the wind tunnel when Case is wired. | `Number` |
| Steps | N | Number of labeled intervals along the bar (N+1 tick labels at exact fractions of the range). Empty = automatic ticks at round speed values (… 3.1, 3.2 … rather than 3.134). | `Integer` |
| Color Map | CM | Color ramp — pick the same map as the Wind Field Viewer. | `Text` |
| Location | L | Optional anchor point overriding the Plane's origin — e.g. a corner of the domain box (plus an offset) to place the legend outside the wind tunnel. The Plane input keeps controlling the bar's orientation. | `Point` |
| Case |  | Optional wind case (or its Domain Box output, or any geometry): places the legend just outside the domain's +X side at ground level, next to the wind tunnel, and scales it to the domain when Size is empty. Location still overrides the position; the Plane input still controls orientation. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Legend Mesh | LM | Vertex-colored legend bar, for baking. | `Mesh` |
| Legend Points | LP | Anchor point per tick label (e.g. for a Text Tag component). | `Point` |
| Legend Values | LV | Tick label text (m/s), aligned with Legend Points. | `Text` |