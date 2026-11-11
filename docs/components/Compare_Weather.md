# ![](/images/icons/Compare_Weather.png) Compare Weather - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Compare%20Weather%22)

![](/images/components/Compare_Weather-crop.png)

Puts two weather files of one site side by side before one of them drives a study: a station's typical year (an EPW from the climate browser) against a reanalysis year (ERA5, Open-Meteo, NASA POWER), or the same place from two providers. Dry-bulb temperature, relative humidity and wind speed as means, global horizontal radiation and precipitation as sums, for the year and each month.  An EPW's missing-value codes are left out, so a typical-year file without a rain column says it carries none instead of reading as a dry climate. It measures the difference; it does not pick a file. For the wind's DIRECTIONS use Compare Wind Climates.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Weather A | A | An EPW file path, or a Weather object — usually the station's typical year. | `Generic Data` |
| Weather B | B | The EPW file path or Weather object to hold against it — usually a reanalysis year at the site. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Quantities | Names | The quantities compared, with their units. | `Text` |
| Annual A | A | Each quantity over the year in file A (mean, or sum for radiation and precipitation). | `Number` |
| Annual B | B | The same in file B. | `Number` |
| Monthly Difference | Diff | B minus A for each month, one branch per quantity. | `Number` |
| Distance | Dist | Distance between the two files' stated locations (km). | `Number` |
| Report |  | The summary and the monthly tables (Markdown). | `Text` |