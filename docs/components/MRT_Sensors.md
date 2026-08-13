# ![](/images/icons/MRT_Sensors.png) MRT Sensors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Sensors%22)

![](/images/components/MRT_Sensors-crop.png)

Create comfort sensor probes from meshes (one probe per face center, facing the face normal) and/or points (facing corresponding Normals), mixed freely on one input.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sensors | S | Sensor geometry: meshes (one probe per face center, facing the face normal) and/or points (one probe each, facing the Normal input). | `Geometry` |
| Normal | N | Sensor normals for POINT inputs: one vector per point (for example, Vectors from Brep Grid Points), or one vector shared by every point. Default world Z. Mesh probes always face their face normal. | `Vector` |
| Height |  | Offsets every sensor along its own normal by this many meters. Point sensors use their corresponding Normal input; mesh sensors use their face normal. Default 1.1 m places upward-facing ground sensors at pedestrian body height. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sensors | S | Sensor probes for the MRT component. | `Generic Data` |
| Points | P | Sensor positions (preview). | `Point` |