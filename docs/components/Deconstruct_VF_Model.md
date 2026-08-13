# ![](/images/icons/Deconstruct_VF_Model.png) Deconstruct VF Model - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20VF%20Model%22)

![](/images/components/Deconstruct_VF_Model-crop.png)

Colors the model's surfaces by view factor: the mean each face receives from all sensors, or one chosen sensor's view factors to every face. Values output is per face, in mesh face order, for custom gradients.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| VF Model | VF | Solved model from MRT View Factors. | `Generic Data` |
| Mode |  | Seen by sensors: each face colored by the mean view factor it receives across ALL sensors — the aggregate visibility the thermal solve filters surfaces by. From one sensor: each face colored by the selected sensor's view factor to it — the weights that sensor's longwave MRT is built from. | `Text` |
| Sensor | i | Sensor index (0-based, in MRT Sensors order). Only used by "From one sensor". | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mesh | M | Scene mesh with one independently colored face per radiation polygon (jet ramp, blue = lowest, red = highest view factor). | `Mesh` |
| Values | V | View factor per face, in the mesh's face order. | `Number` |