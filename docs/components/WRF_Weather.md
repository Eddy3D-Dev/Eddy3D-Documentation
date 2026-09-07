# ![](/images/icons/WRF_Weather.png) WRF Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Weather%22)

![](/images/components/WRF_Weather-crop.png)

Read a WRF run at a site and build the weather an Eddy3D case needs. Feed the Weather output to Timing Parameters and urbanMicroclimateFoam runs on WRF instead of an EPW. Start HOY and Duration describe the window the run actually covers — wire them too, because every hour outside it is deliberately NaN and will stop OpenFOAM rather than quietly simulate a day of 0 degC.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — WRF Run's Case Folder output; run_wrf is derived from it (a run_wrf path wired directly still works). Empty uses the document's session case. | `Text` |
| Domain | d | Which nest to read: 1 for d01, 2 for d02. The innermost domain that covers your site is usually the one you want. | `Integer` |
| Latitude | Lat | Site latitude in decimal degrees. The nearest WRF cell centre answers. | `Number` |
| Longitude | Lon | Site longitude in decimal degrees. | `Number` |
| Time Zone | TZ | Standard-time offset from UTC, in hours. Leave unwired to derive it from longitude, which is right to within an hour almost everywhere and wrong at every political zone boundary. WRF writes UTC; this is only used to place the hours in the year. | `Number` |
| Solar Split | Sp | How to split WRF's global horizontal irradiance into beam and diffuse. This is a MODELLING CHOICE, not a conversion: urbanMicroclimateFoam consumes IDN and Idif separately and they drive surface temperatures differently. Erbs (1982) is the standard hourly correlation. WRF's own diagnostics are exact but exist only when the run enabled them; the component falls back to Erbs and says so. | `Text` |
| Cloud Cover | Cl | How to obtain sky cover for 0/air/cloudCover. The clearness index inverts Kasten-Czeplak on the ratio of WRF's SWDOWN to a clear sky — it works with the fields every run writes but is blind at night, where the nearest daylight value is carried across. CLDFRA is available only when the run wrote it. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather | W | The weather. Wire this to Timing Parameters' Weather input. | `Generic Data` |
| Start HOY | H | Hour of year of the run's first hour. Wire to Timing Parameters' Hour of Year. | `Integer` |
| Duration | D | How many hours the run covers. Wire to Timing Parameters' Duration. | `Integer` |
| Series | S | The extracted site series. Feed to WRF ABL, or deconstruct it. | `Generic Data` |
| Report | R | What was read, which cell answered, and which methods actually ran. | `Text` |