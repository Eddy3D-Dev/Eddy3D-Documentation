# ![](/images/icons/Flow_Rates.png) Flow Rates - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Flow%20Rates%22)

![](/images/components/Flow_Rates-crop.png)

Compute volumetric flow rates (m³/s) across a mesh, treating its vertices as velocity probes. Per face: average vertex velocities × face area × cos(angle to face normal).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Velocity | U | Velocity vectors, one per mesh vertex (e.g. probed pedestrian-height wind). | `Vector` |
| Mesh |  | Mesh whose faces the flow is integrated over. | `Mesh` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Flow Rates | Q | Volumetric flow rate per face (m³/s). | `Number` |
| Centers | C | Face centers. | `Point` |
| Flow Velocity | Vel | Average velocity vector per face. | `Vector` |