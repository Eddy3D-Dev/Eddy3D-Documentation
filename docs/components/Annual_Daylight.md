# ![](/images/icons/Annual_Daylight.png) Annual Daylight - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Annual%20Daylight%22)

![](/images/components/Annual_Daylight-crop.png)

Climate-based annual daylight metrics from Radiance annual illuminance matrices:    sDA  spatial daylight autonomy — fraction of the grid daylit for at least half the occupied hours (LM-83 default sDA300/50%)   ASE  annual sunlight exposure — fraction of the grid seeing direct sun for more than 250 occupied hours (a glare proxy; LOWER is better)   UDI  useful daylight illuminance — fraction of occupied hours inside a useful band  ASE needs the DIRECT matrix. Without it, ASE is reported as zero and the Report says so — the total matrix would count bright overcast sky as glare.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Total Matrix | Total | Path to the annual TOTAL illuminance matrix (annual_total.ill), rows = hours, columns = sensors. | `Text` |
| Direct Matrix | Direct | Path to the annual DIRECT-beam illuminance matrix (annual_dir.ill). Required for ASE; leave empty to skip it. | `Text` |
| Start Hour | From | First occupied hour of the day, inclusive. LM-83 default 8. | `Integer` |
| End Hour | To | Last occupied hour of the day, exclusive. LM-83 default 18. | `Integer` |
| Autonomy Threshold | Ea | Illuminance a sensor must reach to count as daylit, lux. LM-83 default 300. | `Number` |
| Sun Threshold | Es | Direct illuminance above which an hour counts toward ASE, lux. LM-83 default 1000. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| sDA |  | Spatial daylight autonomy, 0-1. | `Number` |
| ASE |  | Annual sunlight exposure, 0-1. Lower is better. | `Number` |
| Daylight Autonomy | DA | Per-sensor fraction of occupied hours at or above the threshold, 0-1. | `Number` |
| UDI |  | Per-sensor fraction of occupied hours inside the useful band, 0-1. | `Number` |
| Sun Hours | SH | Per-sensor count of occupied hours above the direct-sun threshold. | `Integer` |
| Report | R | Thresholds, schedule and sensor count these numbers were produced under — a metric quoted without them cannot be reproduced. | `Text` |