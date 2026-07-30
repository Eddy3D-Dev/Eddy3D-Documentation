# ![](/images/icons/MRT_Sensors.png) MRT Sensors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Sensors%22)

![](/images/components/MRT_Sensors-crop.png)

Create comfort sensor probes from a mesh (face centers) or points.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | Sensor mesh; one probe per face center. | `Mesh` |
| Points | P | Explicit sensor points. When connected, these take priority over Mesh. | `Point` |
| Normal | N | Sensor normal for point input (default world Z). | `Vector` |
| Height |  | Offset MRT sensors along their Normal vector. Default 1.1 m places the sensor at pedestrian body height and prevents it from being coplanar with the ground. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sensors | S | Sensor probes for the MRT component. | `Generic Data` |
| Points | P | Sensor positions (preview). | `Point` |