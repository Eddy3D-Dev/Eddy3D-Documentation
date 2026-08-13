# ![](/images/icons/Thermal_Comfort_Legend.png) Thermal Comfort Legend - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Thermal%20Comfort%20Legend%22)

![](/images/components/Thermal_Comfort_Legend-crop.png)

Color UTCI, PET or NOAA Heat Index values by their thermal-stress categories and create a matching legend.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Values |  | UTCI, PET or Heat Index values to categorize and color. | `Number` |
| Plane |  | Legend base plane. | `Plane` |
| Size |  | Width of each legend color block. | `Number` |
| Mesh |  | Optional mesh to color with the UTCI values. Supports one value per face or per vertex. | `Mesh` |
| Ground Surface | Ground | Optional ground geometry used to place the legend at its bottom center. | `Geometry` |
| Offset |  | Distance between the bottom edge of the ground bounding box and the legend. | `Number` |
| Smooth Colors | Smooth | Use a continuous UTCI color ramp. Face values remain unchanged; vertex-based inputs interpolate naturally across the mesh. When the legend is scaled to actual values (right-click), this blends the ramp instead of quantizing it into discrete bands. | `Boolean` |
| Circle Radius | Radius | Radius of each colored UTCI sensor disk. | `Number` |
| Sensor Points | Points | Optional UTCI sensor points. When their count matches UTCI, one colored disk is created per point; the Mesh face/vertex count does not need to match. | `Point` |
| Scale |  | Uniform scale factor for the legend bar, label spacing, and centered text. | `Number` |
| Metric |  | Metric Type from Thermal Comfort: UTCI, PET (Temperate), PET (Humid), or Heat Index. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Colors |  | Color drawn for every input value: the thermal-stress category color, or the ramp color when the legend is scaled to actual values. | `Colour` |
| Categories |  | Thermal-stress category for every UTCI value. | `Text` |
| Legend Mesh | LM | Legend bar: one block per thermal-stress category, or a value ramp when scaled to actual values. | `Mesh` |
| Label Points | LP | Text anchors for the metric title followed by each legend block or tick. | `Point` |
| Labels |  | Metric title followed by its ranges and thermal-stress labels, or by its numeric ticks when scaled to actual values. | `Text` |
| UTCI Mesh | UM | Colored sensor disks for face-based UTCI data, or a colored mesh for vertex-based data. | `Mesh` |
| Centered Labels | Text | Centered metric title and thermal-stress label text. | `Geometry` |