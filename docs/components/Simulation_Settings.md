# ![](/images/icons/Simulation_Settings.png) Simulation Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Simulation%20Settings%22)

![](/images/components/Simulation_Settings-crop.png)

Configure simulation control settings for UMF. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Write Interval | WriteInt | Write interval in time steps. Optional; uses solver default if omitted. | `Integer` |
| Write Format | Format | Write format: 'ascii', 'binary', or 'compressed'. | `Text` |
| CPU Count | CPU | Number of CPUs/subdomains to use. Optional; default is 1. | `Integer` |
| Initial Solid Time Step Factor | SolidStep | Initial solid time step factor for UMF controlDict. Optional. | `Number` |
| Min Delta T | MinDT | Minimum time step between iterations. Optional. | `Number` |
| Max Delta T | MaxDT | Maximum time step between iterations. Optional. | `Number` |
| Min Fluid Iterations | MinFI | Minimum fluid iterations per time step. Optional. | `Number` |
| Max Fluid Iterations | MaxFI | Maximum fluid iterations per time step. Optional. | `Number` |
| PC Equation Form | PcForm | 'pc-based' or 'mixed' (default is pc-based). | `Text` |
| Damping Thickness | DampThk | Blending coefficients: damping thickness. Optional. | `Number` |
| Alpha Coeff U | AlphaU | Blending coefficients: alphaCoeffU. Optional. | `Number` |
| Alpha Coeff T | AlphaT | Blending coefficients: alphaCoeffT. Optional. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Simulation Settings | SimSettings | Simulation control settings. | `Generic Data` |