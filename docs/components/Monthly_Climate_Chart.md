# ![](/images/icons/Monthly_Climate_Chart.png) Monthly Climate Chart - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Monthly%20Climate%20Chart%22)

![](/images/components/Monthly_Climate_Chart-crop.png)

Visualize monthly dry-bulb temperature and relative humidity from Eddy3D Weather as two aligned min/mean/max charts.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather |  | Eddy3D Weather object. | `Generic Data` |
| Base Point | BasePoint | Lower-left chart location. | `Point` |
| Width |  | Chart width in model units. | `Number` |
| Height |  | Combined chart height in model units. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Months |  | January through December. | `Text` |
| Temperature Minimum | TempMin | Monthly minimum dry-bulb temperature (°C). | `Number` |
| Temperature Mean | TempMean | Monthly mean dry-bulb temperature (°C). | `Number` |
| Temperature Maximum | TempMax | Monthly maximum dry-bulb temperature (°C). | `Number` |
| Humidity Minimum | HumidityMin | Monthly minimum relative humidity (%). | `Number` |
| Humidity Mean | HumidityMean | Monthly mean relative humidity (%). | `Number` |
| Humidity Maximum | HumidityMax | Monthly maximum relative humidity (%). | `Number` |