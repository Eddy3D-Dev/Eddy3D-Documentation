# ![](/images/icons/Wind_Comfort_Criteria.png) Wind Comfort Criteria - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Comfort%20Criteria%22)

![](/images/components/Wind_Comfort_Criteria-crop.png)

Builds a pedestrian wind-comfort criterion from lists — one class per item, best (most comfortable) first — so a jurisdiction's own standard can be classified without shipping code. Each class is a speed threshold, the share of the year it may be exceeded, an operator (< comfort class achieved when exceeded LESS than the share; > / >= hazard class tripped when exceeded MORE), and whether it reads the hourly mean or the 3-second gust. Wire the Criteria output into Pedestrian Wind Comfort or Study Report. Pick a Preset to start from a shipped table (e.g. Wellington) and edit it.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Preset |  | Optional shipped criterion to start from. Its rows are used wherever the lists below are empty, and echoed on the Table output so they can be copied and edited. | `Text` |
| Name |  | Name of the criterion, shown on the comfort component's banner and in reports. | `Text` |
| Speed | U | Speed threshold per class (m/s), best class first. | `Number` |
| Exceedance | % | Share of the period the threshold may be exceeded, per class, in PERCENT (5 = 5 %). 0 means never (an annual maximum). | `Number` |
| Activity | Act | Activity / class description per class ("Sitting", "Unsafe"). | `Text` |
| Letter | L | Class letter per class (A, B, …, S). Defaults to A, B, C… when empty. | `Text` |
| Operator | Op | Per class: < (comfort class, achieved when the exceedance stays BELOW the share), > or >= (hazard class, tripped when the exceedance is ABOVE the share). Defaults to <. | `Text` |
| Reference | Ref | Per class: Hourly mean (default) or Gust — the 3-second gust series from the comfort component's Gust Speed input or its Gust Factor fallback. | `Text` |
| Source | Src | Optional citation of the standard the table comes from. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Criteria |  | The criterion object for Pedestrian Wind Comfort / Study Report. | `Generic Data` |
| Table |  | One line per class, for a panel. | `Text` |