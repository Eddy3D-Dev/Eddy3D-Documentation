# ![](/images/icons/WRF_Animate.png) WRF Animate - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Animate%22)

![](/images/components/WRF_Animate-crop.png)

Loop through a WRF run's history frames while Play is on. Wire Frame into the WRF Probe's Frame input; each tick advances one frame and recomputes the display.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Folder | Dir | The case folder — WRF Run's Case Folder output; run_wrf is derived from it (a run_wrf path wired directly still works). Empty uses the document's session case. | `Text` |
| Domain | d | Which nest's frames to count: 1 for d01, 2 for d02. | `Integer` |
| Play | P | Loop through the frames while on. | `Boolean` |
| Seconds per Frame | s | How long each frame stays on screen. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Frame | i | The current frame index. Wire into WRF Probe's Frame input. | `Integer` |
| Instant | T | The current frame's instant, UTC. | `Text` |