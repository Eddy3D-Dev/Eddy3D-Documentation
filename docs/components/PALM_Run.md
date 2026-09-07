# ![](/images/icons/PALM_Run.png) PALM Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22PALM%20Run%22)

![](/images/components/PALM_Run-crop.png)

Run PALM-4U. Writes a launch script into the case PALM Case wrote, then starts the published PALM container. The script and command are always shown, even before you run, so a failing run can be reproduced by hand.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Driver | Dr | PALM Case's Driver output. It carries the case folder, the grid and the settings the case was written with — one wire, nothing to keep consistent. | `Generic Data` |
| Engine | E | Which backend runs PALM. Container (Docker or Podman) is the only backend in this release, on every platform. | `Text` |
| Image | Img | Container image. Auto uses the published Eddy3D PALM image matching this machine's architecture; pull it from the Eddy3D Setup window. A custom image can be typed or wired in. | `Text` |
| Run | R | Write the launch script and start the container against the case PALM Case wrote. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Namelist | Nl | The _p3d this run will read, as it sits on disk. PALM Case writes it; empty means it is not there yet. | `Text` |
| Script | Sc | The generated run script. | `Text` |
| Command | C | The command that launches it, as it would be typed. | `Text` |
| Status | St | Engine, files, and what happened. | `Text` |
| Case Folder | Out | The resolved case folder. Feed to PALM Progress and PALM Results. | `Text` |