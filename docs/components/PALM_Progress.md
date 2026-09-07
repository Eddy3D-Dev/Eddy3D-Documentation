# ![](/images/icons/PALM_Progress.png) PALM Progress - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Progress%22)

![](/images/components/PALM_Progress-crop.png)

Progress of the PALM run in the case folder, from its RUN_CONTROL table. Toggle Live to re-poll once a second.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — PALM Run's Case Folder output. Empty uses the document's session case. | `Text` |
| Live | L | Re-poll the run once a second while on. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Progress | P | 0 to 1 of the simulated window. | `Number` |
| Simulated Time | t | Seconds of simulated time completed (spin-up excluded). | `Number` |
| Done | D | True once the launch script's completion marker exists. | `Boolean` |
| Status | St | One line: phase and percentage. | `Text` |