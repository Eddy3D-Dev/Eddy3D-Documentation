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
| Wind Direction | Direction | Hourly wind direction (deg). | `Integer` |