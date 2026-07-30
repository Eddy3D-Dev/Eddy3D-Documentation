# ![](/images/icons/Timing_Parameters.png) Timing Parameters - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Timing%20Parameters%22)

![](/images/components/Timing_Parameters-crop.png)

Define simulation timing and optional weather-driven time series. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather |  | Optional Weather object or EPW file path for weather-driven time series. | `Generic Data` |
| Start Day | StartDay | Day-of-year index to start (0-based). Optional; default is 0. | `Integer` |
| Start Hour | StartHour | Hour of day to start (0-23). Optional; default is 0. | `Integer` |
| Duration (Hours) | Hours | Simulation duration in hours. Optional; default is 24. | `Integer` |
| Hour of Year | HOY | Optional 1-based start hour of year (1-8760). When connected, overrides Start Day and Start Hour. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Timing Settings | Timing | Simulation timing settings. | `Generic Data` |
| Hours of Year | HOY | Resolved 1-based hour-of-year sequence for the simulated period. | `Integer` |
| Air Temperature | Tair | EPW dry-bulb temperature (°C) for the resolved hours; useful as a weather fallback for UTCI. | `Number` |
| Relative Humidity | RH | EPW relative humidity (%) for the resolved hours; useful as a weather fallback for UTCI. | `Number` |