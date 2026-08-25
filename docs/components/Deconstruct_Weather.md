# ![](/images/icons/Deconstruct_Weather.png) Deconstruct Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20Weather%22)

![](/images/components/Deconstruct_Weather-crop.png)

Deconstruct a Weather object into hourly time series values. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather |  | Weather object, or an EPW file path (e.g. from Download Weather), to deconstruct. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Dry Bulb Temperature | Temp | Hourly dry-bulb temperature (deg C). | `Number` |
| Relative Humidity | Humidity | Hourly relative humidity (%). | `Number` |
| Wind Speed | Wind | Hourly wind speed (m/s). | `Number` |
| Wind Direction | Direction | Hourly wind direction (deg clockwise from north; 0 means calm). | `Integer` |
| Solar Elevation | Elevation | Hourly solar elevation (deg above the horizon). Night hours are 0, not negative — the sun is either up or it is not, and downstream components read 0 as night. | `Number` |
| Solar Azimuth | Azimuth | Hourly solar azimuth (deg clockwise from north), aligned hour for hour with Solar Elevation. 0 at night, where azimuth is meaningless. | `Number` |
| Hour of Year | HOY | 0-based hour-of-year index, aligned with every other series — feed it to the HOY-driven components. | `Integer` |