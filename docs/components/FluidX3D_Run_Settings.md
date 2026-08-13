# ![](/images/icons/FluidX3D_Run_Settings.png) FluidX3D Run Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22FluidX3D%20Run%20Settings%22)

![](/images/components/FluidX3D_Run_Settings-crop.png)

Solver controls for the FluidX3D GPU engine (memory, simulated time, export interval, and an interactive real-time window).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Memory | M | GPU memory budget (MB). | `Integer` |
| Sim Time | T | Physical simulated time (s). | `Number` |
| Export Interval | E | VTK export interval (s). | `Number` |
| Ground Z | Z | Ground plane Z (model units). | `Number` |
| Source Dir | S | Optional override for the FluidX3D source folder. Leave empty to use the default install path. | `Text` |
| Interactive | I | Open FluidX3D's native real-time GPU window (live render, on-the-fly camera + mode keys) while continuing periodic VTK export for Eddy3D Live View and probes. Windows: full support; macOS: requires XQuartz (X11). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | FluidX3D run settings. | `Generic Data` |