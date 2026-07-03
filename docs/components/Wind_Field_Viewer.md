## ![](../images/icons/Wind_Field_Viewer.png) Wind Field Viewer

![](../images/components/Wind_Field_Viewer-crop.png)

Visualize a probed wind field: colored velocity arrows, a point cloud, or a heatmap mesh. Feed the Probe component's points + velocity (or any points + vectors).  Version 1.0.0.827

#### Input
* ##### P 
Sample points (e.g. the probe points).
* ##### V 
Velocity vector per point.
* ##### M 
How to render the field: Vector Field (arrows), Point Cloud, Heatmap Mesh (colors a supplied mesh), Streamlines, or Volumetric Smoke.
* ##### Msh 
Surface to color for Heatmap Mesh mode (colored per vertex from the nearest sample). Ignored in the other modes.
* ##### S 
Arrow length scale (Vector Field mode).
* ##### Min 
Lower end of the color range / filter (m/s). Empty = data minimum.
* ##### Max 
Upper end of the color range / filter (m/s). Empty = data maximum.
* ##### CM 
Color ramp for the speed coloring.

#### Output
* ##### G
Colored viz geometry for baking: arrow lines, points, or the colored mesh.
* ##### C
Color per element (aligned with Geometry).