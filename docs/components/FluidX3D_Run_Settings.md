# ![](/images/icons/FluidX3D_Run_Settings.png) FluidX3D Run Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22FluidX3D%20Run%20Settings%22)

![](/images/components/FluidX3D_Run_Settings-crop.png)

Solver controls for the FluidX3D GPU engine (memory, simulated time, export interval, and an interactive real-time window).

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Memory | M | GPU memory budget (MB). |
| Sim Time | T | Physical simulated time (s). |
| Export Interval | E | VTK export interval (s). |
| Ground Z | Z | Ground plane Z (model units). |
| Source Dir | S | Optional override for the FluidX3D source folder. Leave empty to use the default install path. |
| Interactive | I | Open FluidX3D's native real-time GPU window (live render, on-the-fly camera + mode keys) instead of headless batch VTK export. No VTK is written in interactive mode — use batch mode to probe results. Windows: full support; macOS: requires XQuartz (X11). |
| Window Size | W | Interactive real-time window size (macOS X11). "Fullscreen" sizes it to the display. Only applies in interactive mode; on Windows the window is always full-screen. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Settings | S | FluidX3D run settings. |
