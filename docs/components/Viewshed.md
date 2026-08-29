# ![](/images/icons/Viewshed.png) Viewshed - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Viewshed%22)

![](/images/components/Viewshed-crop.png)

Visual openness by ray casting: the unobstructed fraction of a view cone around each point's normal. A design-orientation tool for seats, windows and routes — how open does it FEEL here — not a daylight metric.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Context | C | Obstructing geometry: buildings, terrain, walls. Meshes, Breps and Surfaces are accepted; branches are flattened into one scene. | `Geometry` |
| Points | P | Observer points. | `Point` |
| Normals | N | Optional per-point view directions — the cone axis (e.g. a facade normal, or a seat's facing). Default is straight up, the plan-view openness question. | `Vector` |
| Cone Half-Angle | A | Half-angle of the view cone in degrees. 60 approximates the human comfortable field of view; 90 is the full hemisphere around the axis. | `Number` |
| Rays | R | Rays traced per cone. More rays, smoother numbers; cost is linear. | `Integer` |
| Offset | O | Distance to lift each point along its axis before tracing, so a point sitting ON geometry does not see only itself. | `Number` |
| Max Distance | D | Optional view distance cap in metres — geometry beyond it counts as OPEN, turning the answer into "openness within this range". | `Number` |
| Color Scheme | Ramp | Colour ramp for the Colors output. Viridis is perceptually uniform and colourblind-safe (use it in a figure); Grayscale suits a monochrome print. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Openness | Op | Unobstructed fraction of each point's view cone, 0-1. | `Number` |
| Colors | Col | Point-specific colour ramp over openness, for a mesh or point preview. | `Colour` |
| Report | R | Rays traced, cone directions, and elapsed time. | `Text` |
| Cones | VC | All view cones joined into ONE mesh (a mesh per point made the canvas crawl), each sector coloured by its point's openness — the axis actually used (including the straight-up fallback for an unusable normal) and the half-angle actually sampled. The surface is TRUNCATED by the context: each direction is drawn to the first building it hits, so the shape shows what the rays saw. Unobstructed directions reach Max Distance when one is set, and otherwise the context's bounding-box diagonal, which is a display length and not a traced distance; the Report says which was used. | `Mesh` |