# ![](/images/icons/Indoor_Inlet.png) Indoor Inlet - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Inlet%22)

![](/images/components/Indoor_Inlet-crop.png)

Ventilation inlet — defines where air enters the room (diffuser, window, door). Direction is computed perpendicular to the surface, pointing into the room.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Surface | S | Planar surface on the room wall marking the inlet opening. | `Brep` |
| Speed | V | Inlet supply speed (m/s). Direction is auto-computed from the surface normal. | `Number` |
| Temperature | T | Inlet air temperature (°C). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Inlet | I | Indoor inlet for the case component. | `Generic Data` |