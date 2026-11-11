# ![](/images/icons/Terrain_Diagram.png) Terrain Diagram - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Terrain%20Diagram%22)

![](/images/components/Terrain_Diagram-crop.png)

The diagrams a grading is read by, off one raster of the ground: elevation or slope bands as a coloured mesh, contours with major lines and their level labels, and spot levels with a downhill arrow at any points you wire. Set Range to hold one colour scale while the ground is edited or design options are compared, and Slope Bands to the gradients that matter (2 % drainage, 5 % and 8.33 % access ramps, 33 % mowing).  The ground is sampled once at the centre of every cell; slope is Horn's 3 x 3 gradient in percent (100 % = 45°), and reads low in the outermost ring of cells, where a neighbour is missing. Contour levels are multiples of the interval counted from elevation 0, so a line keeps its level when the ground changes.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Terrain |  | The ground — meshes, Breps or surfaces (branches are flattened). | `Geometry` |
| Cell Size | Cell | Raster cell size (m). The ground is sampled once at each cell centre. | `Number` |
| Diagram |  | What the mesh is coloured by: Elevation (m) or Slope (the Slope Bands). | `Text` |
| Range |  | Elevation at the two ends of the colour scale (m), held fixed so the colours do not shift while the ground is edited or options are compared. Unset = this ground's lowest and highest level. | `Domain` |
| Slope Bands | Bands | Slope band edges (percent, ascending); the last band is open. Default 2, 5, 8.33, 20, 33. | `Number` |
| Contour Interval | Interval | Vertical distance between contours (m). 0 = no contours. | `Number` |
| Major Every | Major | Every n-th contour, counted from elevation 0, is a major line and gets a label. 0 = none. | `Integer` |
| Spots |  | Points to read a spot level and slope at (their height is ignored). | `Point` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh |  | The ground as cells coloured by the chosen diagram. | `Mesh` |
| Contours |  | The minor contour lines. | `Curve` |
| Major Contours | Major | The major contour lines. | `Curve` |
| Label Points | LabelPts | One point on each major contour line, for its label. | `Point` |
| Labels |  | The level (m) at each of Label Points. | `Text` |
| Cells |  | Centre of every rastered cell, on the ground. | `Point` |
| Slopes |  | Slope at each of Cells (percent). | `Number` |
| Band Areas | Areas | One line per slope band: label and plan area m² (tab-separated). | `Text` |
| Spot Levels | Levels | Ground level at each of Spots (m); null off the ground. | `Number` |
| Spot Slopes | SpotSlopes | Slope at each of Spots (percent). | `Number` |
| Spot Arrows | Arrows | From each spot on the ground, five cells downhill; none on level ground. | `Line` |