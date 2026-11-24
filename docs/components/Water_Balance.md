# ![](/images/icons/Water_Balance.png) Water Balance - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Water%20Balance%22)

![](/images/components/Water_Balance-crop.png)

Where the water was at every stored time: rain delivered, run off the site, standing on it and lost to the ground, with the storm's intensity alongside. The numbers behind a water-balance chart.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | A run from Stormwater Run. Needs a Full run — a Fast one routes no water. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Time |  | Minutes from the storm's start, one per stored snapshot. Output Interval in Stormwater Settings sets how many. | `Number` |
| Rain |  | Mean rain intensity (mm/h) over the interval ending at each time — the hyetograph on the same time axis. | `Number` |
| Rain Volume | RainVol | Water delivered to the model so far (m³): rain on the ground, roof runoff, and anything already standing at the start. The other three volumes add up to it. | `Number` |
| Runoff |  | Water that has left across the site boundary so far (m³). | `Number` |
| Ponded |  | Water on the surface at that time (m³). | `Number` |
| Infiltrated | Infil | Rain that never became runoff, so far (m³): infiltration, initial abstraction and what roofs retained. | `Number` |