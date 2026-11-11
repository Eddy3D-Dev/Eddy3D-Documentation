# ![](/images/icons/Analysis_Results.png) Analysis Results - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Analysis%20Results%22)

![](/images/components/Analysis_Results-crop.png)

Reads any Eddy3D result object as points and values: an annual wind field or VAF, an MRT, UTCI or PET result, a surface temperature, shadow or daily-light-integral result, a noise result or a stormwater run. One branch per field, with the analysis, the quantity and the unit beside it, so one definition can colour, filter or compare any of them, and it updates when the analysis re-runs.  A result that is a series over hours is reduced to its mean per point (stormwater: the peak); use the result's own Deconstruct component to pick hours or a statistic.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Results |  | Result objects — the Wind Speed or Annual VAF of the VAF component, an MRT, UTCI or PET Result, a Surface Temperature, Shadow or DLI Result, a Noise Run result, a Stormwater Run result (branches are flattened). | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points |  | Where each value is, one branch per field. Empty when the result carries no positions. | `Point` |
| Values |  | The value at each of Points, one branch per field. | `Number` |
| Analysis |  | The analysis each branch comes from (Wind, MRT, UTCI, Noise, Stormwater). | `Text` |
| Quantity |  | What each branch's values are. | `Text` |
| Unit |  | The unit of each branch's values; empty when dimensionless. | `Text` |