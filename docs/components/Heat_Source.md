# ![](/images/icons/Heat_Source.png) Heat Source - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Heat%20Source%22)

![](/images/components/Heat_Source-crop.png)

A volumetric heat source box for an indoor ventilation case (transported temperature scalar).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zone | Z | Box zone occupied by the heat source. | `Box` |
| Source Rate | Q | Temperature source rate injected into the zone (K/s, specific). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | S | Heat source for the Indoor Case component. | `Generic Data` |