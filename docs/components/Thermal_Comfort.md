# ![](/images/icons/Thermal_Comfort.png) Thermal Comfort - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Thermal%20Comfort%22)

![](/images/components/Thermal_Comfort-crop.png)

Compute a thermal comfort metric at a point: UTCI (Ta, RH, wind, MRT), PET (adds the personal inputs), or NOAA Heat Index (Ta, RH only). Pick the metric from the dropdown — the inputs adapt. Wire hourly lists (e.g. EPW series) to compute annual values.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Metric |  | Comfort metric to compute; the inputs adapt to the choice. | `Text` |
| Air Temperature | Ta | Air temperature [°C]. | `Number` |
| Relative Humidity | RH | Relative humidity [%]. | `Number` |
| Wind Speed | Wind | Wind speed at the subject [m/s]. | `Number` |
| MRT |  | Mean radiant temperature [°C]. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Value |  | Metric value [°C]. | `Number` |
| Stress |  | Thermal stress category. | `Text` |
| Details |  | Calculation details. | `Text` |