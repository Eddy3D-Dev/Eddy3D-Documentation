# ![](/images/icons/Momentum_Source.png) Momentum Source - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Momentum%20Source%22)

![](/images/components/Momentum_Source-crop.png)

A fan/jet momentum source (mean velocity) box for an indoor ventilation case.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zone | Z | Box zone occupied by the source. | `Box` |
| Mean Velocity | U | Target mean velocity in the zone (m/s). | `Vector` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | S | Momentum source for the Indoor Case component. | `Generic Data` |