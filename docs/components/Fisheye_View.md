# ![](/images/icons/Fisheye_View.png) Fisheye View - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Fisheye%20View%22)

![](/images/components/Fisheye_View-crop.png)

Equal-angle fisheye of the hemisphere above one sensor, as a colored mesh — a flat disk or a 3D dome (Display dropdown): sky, building, ground and vegetation per direction, plus the sensor's cosine-weighted sky view fraction.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| VF Model | VF | Solved model from MRT View Factors (geometry + sensors). | `Generic Data` |
| Sensor | i | Sensor index (0-based, in MRT Sensors order). | `Integer` |
| Plane | P | Where to draw the disk. Unconnected: horizontal at the sensor, +Y = north. | `Plane` |
| Radius | R | Disk radius in model units. | `Number` |
| Rings | N | Zenith rings of the fisheye grid (sectors are 4x this). More rings = crisper silhouettes, more rays. Pick a preset or type/wire any number (clamped to 4-90). | `Text` |
| Display | D | How to draw the view: Disk (flat equal-angle fisheye — center zenith, rim horizon) or Dome (the same cells on a 3D hemisphere of the given Radius over the plane, so each patch sits in the actual direction the sensor sees it). | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Fisheye | F | The colored fisheye disk: light blue = sky, gray = building, tan = ground, green = vegetation/tree. | `Mesh` |
| SVF | svf | Cosine-weighted sky view fraction of the hemisphere (1 = fully open sky). | `Number` |