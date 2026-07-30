# ![](/images/icons/UTCI_Legend.png) UTCI Legend - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22UTCI%20Legend%22)

![](/images/components/UTCI_Legend-crop.png)

Color UTCI values by the official thermal-stress categories and create a matching legend.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| UTCI |  | UTCI values to categorize and color. | `Number` |
| Plane |  | Legend base plane. | `Plane` |
| Size |  | Width of each legend color block. | `Number` |
| Mesh |  | Optional mesh to color with the UTCI values. Supports one value per face or per vertex. | `Mesh` |
| Ground Surface | Ground | Optional ground geometry used to place the legend at its bottom center. | `Geometry` |
| Offset |  | Distance between the bottom edge of the ground bounding box and the legend. | `Number` |
| Smooth Colors | Smooth | Use a continuous UTCI color ramp. Face values remain unchanged; vertex-based inputs interpolate naturally across the mesh. | `Boolean` |
| Circle Radius | Radius | Radius of each colored UTCI sensor disk. | `Number` |
| Sensor Points | Points | Optional UTCI sensor points. When their count matches UTCI, one colored disk is created per point; the Mesh face/vertex count does not need to match. | `Point` |
| Scale |  | Uniform scale factor for the legend bar, label spacing, and centered text. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Colors |  | Category color for every UTCI input value. | `Colour` |
| Categories |  | Thermal-stress category for every UTCI value. | `Text` |
| Legend Mesh | LM | Ten-color UTCI legend mesh. | `Mesh` |
| Label Points | LP | Text anchor for each legend block. | `Point` |
| Labels |  | UTCI ranges and thermal-stress labels. | `Text` |
| UTCI Mesh | Mesh | Colored sensor disks for face-based UTCI data, or a colored mesh for vertex-based data. | `Mesh` |
| Centered Labels | Text | Three-line UTCI label text, middle-center aligned and positioned at Label Points. | `Geometry` |