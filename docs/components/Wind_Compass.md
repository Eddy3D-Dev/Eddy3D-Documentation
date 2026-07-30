# ![](/images/icons/Wind_Compass.png) Wind Compass - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Compass%22)

![](/images/components/Wind_Compass-crop.png)

Visualize a wind direction on a compass circle. Direction is meteorological degrees (0=N, 90=E, 180=S, 270=W); outputs the flow vector and the 16-point cardinal name.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Direction | Dir | Wind direction in degrees (0=N, 90=E, 180=S, 270=W). | `Number` |
| Radius | R | Radius of the compass circle. | `Number` |
| Base Point | P | Center of the compass. | `Point` |
| Color | C | Display color. | `Colour` |
| Arrow Scale | S | Scale of the directional arrow. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Vector | Vec | Wind direction (flow) vector. | `Vector` |
| Direction Name | Name | 16-point cardinal name (e.g. NNE). | `Text` |