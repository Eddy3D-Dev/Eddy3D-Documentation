# ![](/images/icons/WRF_Run.png) WRF Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22WRF%20Run%22)

![](/images/components/WRF_Run-crop.png)

Run the WRF pipeline in the two launches it needs: the WPS half (geogrid, ungrib, metgrid), then run_wrf/namelist.input, built from that output, then the WRF half (real, wrf). Writes one script per launch into the project folder. The scripts and commands are always shown, even before you run, so a failing run can be reproduced by hand.

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
| Steps | S | Which half to run. Everything runs the WPS half, builds run_wrf/namelist.input from its output (WRF's own physics kept), then runs the WRF half. WPS output does not change unless the domains or the met data do, so re-running the WRF half alone is the normal edit-and-retry loop: it uses the namelist.input in run_wrf exactly as you left it (time step, physics, run length), and only builds one when there is none. Time Step and History Interval, when set, are the exception: they are written into that file. | `Text` |
| Case Name | Case | The case folder under Working Directory. Empty mints a friendly session name once per document — the same name every other WRF component resolves — and keeps it with the saved document. | `Text` |
| Time Step | Step | Model time step [s], written to namelist.input as time_step (1 to 3600). 0 or empty derives it from the grid: 6 s per km of the outermost domain's spacing, divided by the largest map factor when that exceeds 1. WRF stops with a CFL error on a step the grid cannot take, so pin a shorter one to retry. With Steps set to WRF only, the value is also written into the run_wrf/namelist.input already there; with 0 that file is used exactly as you left it. | `Integer` |
| History Interval | History | Minutes between history frames [min], one wrfout file per frame, written as history_interval for every domain (1 to 1440). 0 or empty keeps the base namelist's, which is hourly in WRF's own example. With Steps set to WRF only, the value is also written into the run_wrf/namelist.input already there; with 0 that file is used exactly as you left it. | `Integer` |
| Run | R | Launch the run. The script is written and shown regardless. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Script | Sc | The generated run script. | `Text` |
| Command | C | The command that launches it, as it would be typed. | `Text` |
| Status | St | What the engine is, what it will run, and what happened. | `Text` |
| Case Folder | Out | The resolved case folder. Feed to WRF Weather, Probe, Map, Animate and Progress — each derives its run_wrf from it. | `Text` |