# ![](/images/icons/Wind_Compass.png) Wind Compass - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Compass%22)

![](/images/components/Wind_Compass-crop.png)

Visualize a wind direction on a compass circle. Direction is meteorological degrees (0=N, 90=E, 180=S, 270=W); outputs the flow vector and the 16-point cardinal name.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Dir |  | Wind direction in degrees (0=N, 90=E, 180=S, 270=W). |
| Radius | R | Radius of the compass circle. |
| Base Point | P | Center of the compass. |
| Color | C | Display color. |
| Arrow Scale | S | Scale of the directional arrow. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Vec |  | Wind direction (flow) vector. |
| Name |  | 16-point cardinal name (e.g. NNE). |
