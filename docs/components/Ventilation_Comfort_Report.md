# ![](/images/icons/Ventilation_Comfort_Report.png) Ventilation & Comfort Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Ventilation%20%26%20Comfort%20Report%22)

![](/images/components/Ventilation_Comfort_Report-crop.png)

One page per room: thermal comfort (EN ISO 7730 / EN 16798-1 category shares, ASHRAE 55, draught, stratification, ADPI), ventilation effectiveness (age of air, air change effectiveness, contaminant removal) and airborne infection risk (Wells–Riley) with the ASHRAE 241 equivalent-clean-airflow check — each number beside the reference it is read against, and the caveats that belong to it. Always outputs the Markdown and HTML text; Write saves <Room>.md and a self-contained <Room>.html (no external assets) into the Folder. Sections left unwired are reported as not evaluated.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Folder | Dir | Where Write saves the report. | `Text` |
| Room Name | Room | Room name for the title and the file names. | `Text` |
| Comfort Map | Map | Indoor Comfort Map's Comfort Map output. | `Generic Data` |
| Ventilation | Vent | Ventilation Effectiveness's Ventilation output. | `Generic Data` |
| Infection Risk | Risk | Infection Risk's Infection Risk output. | `Generic Data` |
| Notes |  | Extra lines for the caveats (probe grid, solver mode, …). | `Text` |
| Write | W | Write the .md and .html files to the Folder. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Markdown | MD | The report as Markdown. | `Text` |
| HTML |  | The report as a self-contained HTML page. | `Text` |
| Files |  | Paths written by the last Write. | `Text` |