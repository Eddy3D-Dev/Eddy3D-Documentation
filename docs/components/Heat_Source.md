# ![](/images/icons/Heat_Source.png) Heat Source - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Heat%20Source%22)

![](/images/components/Heat_Source-crop.png)

A volumetric heat source box for an indoor ventilation case (transported temperature scalar).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zone | Z | Box zone occupied by the heat source. | `Box` |
| Heat Output | Q | Total heat output of the source, in WATTS (OpenFOAM heatSource Q). A seated person is about 100 W, a desktop workstation 150 W, a domestic heater 1000-2000 W. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | S | Heat source for the Indoor Case component. | `Generic Data` |