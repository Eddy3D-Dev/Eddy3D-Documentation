# ![](/images/icons/HAM_Climate.png) HAM Climate - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22HAM%20Climate%22)

![](/images/components/HAM_Climate-crop.png)

Air conditions on one face of a HAM wall. One value per input is a constant; a list is a stepped schedule (one entry per step, hourly by default).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Temperature | T | Air temperature (°C). One value or one per step. | `Number` |
| Relative Humidity | RH | Relative humidity (%). One value or one per step. Converted to the vapour pressure hamFoam reads, using the solver's own saturation relation. | `Number` |
| Vapour Pressure | pv | Vapour pressure (Pa). Wire this to bypass Relative Humidity — the HAMSTAD cases state their loads this way (case 4's exterior is a constant 1150 Pa while its temperature swings). | `Number` |
| Heat Transfer | alpha | Surface heat transfer coefficient α (W/m²K). 25 exterior, 8 interior are the benchmark values. | `Number` |
| Vapour Transfer | beta | Surface vapour transfer coefficient β (s/m). 1.8382e-7 exterior, 5.8823e-8 interior are the benchmark values. | `Number` |
| Rain Flux | gl | Wind-driven rain reaching the face (kg/m²s). One value or one per step. Interior faces are 0. | `Number` |
| Radiation | rad | Absorbed shortwave radiation (W/m²). One value or one per step. | `Number` |
| Step | S | Length of one schedule step (hours). Only read when an input is a list. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Climate | C | Climate for one side of the HAM Case component. | `Generic Data` |
| Vapour Pressure | pv | The vapour pressure actually written (Pa) — one value, or the schedule. | `Number` |