# ![](/images/icons/MRT_Sensors.png) MRT Sensors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Sensors%22)

![](/images/components/MRT_Sensors-crop.png)

Create comfort sensor probes from a mesh (face centers) or points.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Mesh | M | Sensor mesh; one probe per face center. |
| Points | P | Explicit sensor points (used if no mesh). |
| Normal | N | Sensor normal for point input (default world Z). |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Sensors | S | Sensor probes for the MRT component. |
| Points | P | Sensor positions (preview). |
