# ![](/images/icons/Stormwater_Legend.png) Stormwater Legend - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Stormwater%20Legend%22)

![](/images/components/Stormwater_Legend-crop.png)

A legend for a stormwater mesh: swatches, labels and a title, placed on a plane.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Style |  | Which map this legend belongs to. Flood hazard uses discrete FD2320 bands rather than a ramp, because the band boundaries are the regulated quantity. | `Text` |
| Range |  | The value range being shown — wire the Range output of Deconstruct Stormwater so the legend and the map can never disagree. Ignored for flood hazard, whose bands are fixed. | `Domain` |
| Plane |  | Where to draw it. | `Plane` |
| Size |  | Height of one swatch in model units. | `Number` |
| Steps |  | Number of swatches in a continuous legend. Ignored for flood hazard. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Swatches |  | One coloured quad per band. | `Mesh` |
| Labels |  | Label for each swatch. | `Text` |
| Label Planes | LabelPlanes | Where to place each label — feed with Labels into a Text Tag 3D. | `Plane` |
| Title |  | Title for the legend, including the unit. | `Text` |