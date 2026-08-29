# ![](/images/icons/Deconstruct_DLI.png) Deconstruct DLI - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20DLI%22)

![](/images/components/Deconstruct_DLI-crop.png)

Per-point daily light integral — period mean and worst month — and, for an explicit Month selection, the per-month tree, from a Daily Light Integral Result.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | Res | Result output of the Daily Light Integral component. | `Generic Data` |
| Month | M | Month(s) to expand, 1-12. Left empty, the per-point outputs still cover the whole solved period and the monthly tree stays empty — which is the tree this component exists to avoid building unasked. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | The analysis points the solve covered, in their original order. | `Point` |
| Mean DLI | DLI | Mean daily light integral per point over the whole analysed period, mol/m²/day. | `Number` |
| Worst Month | Min | The LOWEST monthly mean each point sees across the covered months, mol/m²/day — what a planting palette has to survive. Equals Mean DLI when only one month was solved. | `Number` |
| Best Month | Max | The highest monthly mean each point sees, mol/m²/day. | `Number` |
| Colors | Col | Colour ramp over the Worst Month value — the limiting case is what the map should show. | `Colour` |
| Months | Mo | The calendar months the solve actually covered, in order. | `Text` |
| Days | D | Days of each covered month the solve analysed, parallel to Months. A month analysed for three days is not a month. | `Integer` |
| Monthly DLI | MDLI | Per-point DLI for each SELECTED month, one branch per month. Populated only when Month is connected. | `Number` |