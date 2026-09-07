# ![](/images/icons/WRF_Progress.png) WRF Progress - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Progress%22)

![](/images/components/WRF_Progress-crop.png)

Progress of the WRF pipeline in the working directory, with an expected time to completion once wrf.exe is stepping. Toggle Live to re-poll once a second.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — WRF Run's Case Folder output, the one holding run_wps and run_wrf. Empty uses the document's session case, the same folder WRF Run resolves. | `Text` |
| Live | L | Re-poll the run once a second while on. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Progress | P | 0 to 1 across the whole pipeline, weighted so wrf.exe owns 80 % of the bar. | `Number` |
| Phase | Ph | The step currently running: geogrid, ungrib, metgrid, real, wrf, done or failed. | `Text` |
| Done | D | True once SUCCESS COMPLETE WRF is in the log and wrfout files exist. | `Boolean` |
| Status | St | One line: phase, percentage, and the expected time to completion when known. | `Text` |