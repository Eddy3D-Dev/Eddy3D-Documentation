# ![](/images/icons/Compare_Wind_Climates.png) Compare Wind Climates - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Compare%20Wind%20Climates%22)

![](/images/components/Compare_Wind_Climates-crop.png)

Puts two wind climates of one site side by side — a station record (ISD, EPW) against ERA5, or two stations — before one of them drives a study. Wire the Climate output of two Wind Climate components built with the same Sectors.  Rose Overlap is the share of the direction distribution the two have in common (1 = the same rose); Speed Ratio is B's mean speed over A's, over the non-calm hours. The report says which of the two differs and lists every sector. It measures the disagreement; it does not pick a source.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Climate A | A | A Wind Climate — usually the station record. | `Generic Data` |
| Climate B | B | The Wind Climate to hold against it — usually ERA5 at the site. | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Rose Overlap | Overlap | Shared share of the two direction distributions, 0-1. | `Number` |
| Speed Ratio | Ratio | Mean speed of B over A, non-calm hours. | `Number` |
| Agree |  | True when the overlap is at least 0.85 and the mean speeds are within 15 % (round thresholds, not a standard). | `Boolean` |
| Directions | Dir | Sector centres (degrees from north). | `Number` |
| Difference | Diff | Probability of B minus A in each sector (percentage points). | `Number` |
| Report |  | The verdict and the sector table (Markdown). | `Text` |