# ![](/images/icons/Study_Report.png) Study Report - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Study%20Report%22)

![](/images/components/Study_Report-crop.png)

Generate a Markdown report documenting the wind case to the QA discipline of the ASCE/SEI CWE Prestandard (within its steady-RANS pedestrian-comfort allowance): solver and OpenFOAM version, domain and blockage, boundary conditions, numerics and the 2nd-order verdict, mesh quality, convergence, y+, Reynolds, an optional comfort section, limitations, and a compliance summary table.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | The wind case — from the Outdoor Case component (full report) or Load Wind Case (reads the case's manifest; cases written before it degrade to what disk carries). | `Generic Data` |
| Weather | W | Optional weather record — documents the EPW file, station and location as the study's climate source. | `Generic Data` |
| Annual Wind Field | Wind | Optional annual wind speed field from Velocity Amplification Factors — adds per-probe statistics and, with a Metric, the comfort classification. | `Generic Data` |
| Comfort Metric | Metric | Optional comfort criterion for the classification table — pick one from the dropdown. The same vocabulary as the Wind Comfort component; an older document wiring the bare enum name (LawsonGeneral) or an index still resolves. | `Text` |
| Report Path | Path | Optional .md file path to write the report to — leave it empty and the report goes to '<case folder>/<case name>-report.md', beside the case it describes. Wire or type a path to override that; the folder must exist. | `Text` |
| Write |  | Write the report to the resolved Path output. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Report | MD | The whole report as Markdown text. | `Text` |
| Path |  | The file the report will be written to: the autofilled default in the case folder, or Report Path when one is given. Populated whether or not Write has fired, so the destination is visible before it is used. | `Text` |