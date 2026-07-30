# ![](/images/icons/Wind_Field_Viewer.png) Wind Field Viewer - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Field%20Viewer%22)

![](/images/components/Wind_Field_Viewer-crop.png)

Visualize a probed wind field: colored velocity arrows, a point cloud, a heatmap mesh, streamlines, or volumetric smoke (pick via Display Mode). Feed the Probe component's points + velocity vectors (Field = U), or any points + vectors.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | Sample points (e.g. the probe points). | `Point` |
| Velocity | V | Velocity vector per point. | `Vector` |
| Display Mode | M | How to render the field: Vector Field (arrows), Point Cloud, Heatmap Mesh (colors a supplied mesh), Streamlines, or Volumetric Smoke. | `Text` |
| Mesh | Msh | Surface to color for Heatmap Mesh mode (colored per vertex from the nearest sample). Ignored in the other modes. | `Mesh` |
| Scale | S | Arrow length scale (Vector Field mode). | `Number` |
| Min Speed | Min | Lower end of the color range / filter (m/s). Empty = data minimum. | `Number` |
| Max Speed | Max | Upper end of the color range / filter (m/s). Empty = data maximum. | `Number` |
| Color Map | CM | Color ramp for the speed coloring. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Geometry | G | Colored viz geometry for baking: arrow lines, points, or the colored mesh. | `Generic Data` |
| Colors | C | Color per element (aligned with Geometry). | `Colour` |