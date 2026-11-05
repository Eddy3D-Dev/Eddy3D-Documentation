# ![](/images/icons/Sun_Report.png) Sun Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Sun%20Report%22)

![](/images/components/Sun_Report-crop.png)

Assemble the Sunlight-results chapter for the Site Report from per-date sun results: wire one Sun Hours, Solar Irradiation and Shadow per report date (equinox, summer and winter solstice — the Date dropdown on each), one branch per date, and connect Report to Site Report's Results. Per date: the share of points per band of sun hours, per bin of kWh/m² and per shade pattern (sun all day, morning shade, afternoon shade, shade all day); then the % of the grid in shade at 9, 12, 15 and 18 h across the dates.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Labels | L | One label per date, in branch order. Default: Equinox, Summer solstice, Winter solstice. | `Text` |
| Sun Hours | H | Sun Hours' Sun Hours output, one branch per date (graft the three components' outputs together). | `Number` |
| Morning Hours | AM | Sun Hours' Morning Hours output, one branch per date. | `Number` |
| Afternoon Hours | PM | Sun Hours' Afternoon Hours output, one branch per date. | `Number` |
| Irradiation | E | Solar Irradiation's Total output (kWh/m²), one branch per date. | `Number` |
| Shadows | S | Shadow's Result output, one per date in date order — the source of the 9 / 12 / 15 / 18 h shadow grid. | `Generic Data` |
| Images | Img | PNG or JPEG file per date, in date order: a capture of the coloured sun-hours result, printed above its bars. | `Text` |
| Source | Src | Where the results came from (the weather file, the study), printed in the chapter's lead. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Report | Rep | The Sunlight-results chapter; wire it to Site Report's Results. | `Generic Data` |
| Summary | Sum | What the chapter carries per date. | `Text` |