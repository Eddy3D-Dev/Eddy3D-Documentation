# ![](/images/icons/Indoor_Sink.png) Indoor Sink - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Sink%22)

![](/images/components/Indoor_Sink-crop.png)

A Darcy-Forchheimer momentum sink (filter/screen) box for an indoor ventilation case.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zone | Z | Box zone occupied by the sink. | `Box` |
| Viscous | d | Darcy viscous resistance (1/m²) per axis. | `Vector` |
| Inertial | f | Forchheimer inertial resistance (1/m) per axis. | `Vector` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Sink | S | Momentum sink for the indoor case. | `Generic Data` |