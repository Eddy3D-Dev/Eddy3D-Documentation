# ![](/images/icons/WRF_Run.png) WRF Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Run%22)

![](/images/components/WRF_Run-crop.png)

Run the WRF pipeline. Writes a script into the project folder and launches it. The script and command are always shown, even before you run, so a failing run can be reproduced by hand.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Working Directory | Dir | The root the case folder sits under; the case itself is <root>/<Case Name>. Empty uses ~/Eddy3D/WRF. A full project path with an empty Case Name is used as-is, which is what older definitions wire. | `Text` |
| WRF Distribution | WRF | Folder the WRF distribution is unpacked into — its main/ holds real.exe and wrf.exe. Leave empty on the Container engine: the published image carries its own, and a folder given here is mounted OVER it. | `Text` |
| WPS Distribution | WPS | Folder the WPS distribution is unpacked into. Leave empty on the Container engine — the published image carries its own. | `Text` |
| GRIB Folder | G | Folder of GRIB files to link as GRIBFILE.AAA, AAB, ... for ungrib. Auto uses the grib folder under the case — where WRF Met Data downloads with nothing wired. Clear it if they are already linked, or if you are running the WRF half only. | `Text` |
| Vtable | V | The ungrib variable table for your meteorological product. The list is every table the shipped WPS carries; a table you added yourself can be typed or wired in. Vtable.GFS is what WRF Met Data downloads for. | `Text` |
| Engine | E | Which backend runs WRF. Auto picks the first that works here, preferring WSL. Native needs the WRF-CMake Windows build and MS-MPI. Container runs the published Eddy3D image through Docker or Podman, and is the only backend on macOS. | `Text` |
| Image | Img | Container image, when the engine is Container. Auto uses the published Eddy3D image matching this machine's architecture; pull it from the Eddy3D Setup window. A third-party image can be typed or wired in — one without Eddy3D's version marker keeps the mount-the-host-distributions behaviour. | `Text` |
| Ranks | N | MPI ranks for wrf.exe. Only wrf.exe uses more than one: ungrib has no MPI build, and geogrid, metgrid and real are pinned to a single rank because their netCDF-4 output is not reliable in parallel. | `Integer` |
| Steps | S | Which half to run. WPS output does not change unless the domains or the met data do, so re-running the WRF half alone is the normal edit-and-retry loop. | `Text` |
| Run | R | Launch the run. The script is written and shown regardless. | `Boolean` |
| Case Name | Case | The case folder under Working Directory. Empty mints a friendly session name once per document — the same name every other WRF component resolves — and keeps it with the saved document. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Script | Sc | The generated run script. | `Text` |
| Command | C | The command that launches it, as it would be typed. | `Text` |
| Status | St | What the engine is, what it will run, and what happened. | `Text` |
| Case Folder | Out | The resolved case folder. Feed to WRF Weather, Probe, Map, Animate and Progress — each derives its run_wrf from it. | `Text` |