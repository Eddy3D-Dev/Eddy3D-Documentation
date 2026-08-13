# ![](/images/icons/Two-Node_Comfort.png) Two-Node Comfort - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Two-Node%20Comfort%22)

![](/images/components/Two-Node_Comfort-crop.png)

Gagge two-node thermal comfort: SET, ET, PMV, TSENS and DISC.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Air Temperature | Ta | Dry-bulb air temperature (°C). | `Number` |
| Radiant Temperature | Tr | Mean radiant temperature (°C). | `Number` |
| Air Speed | V | Air speed (m/s). Floored at 0.1 — the model is not valid in perfectly still air. | `Number` |
| Relative Humidity | RH | Relative humidity (%). | `Number` |
| Metabolic Rate | M | Metabolic rate (met). | `Number` |
| Clothing | Clo | Clothing insulation (clo). | `Number` |
| Sitting | St | True for a seated occupant (smaller radiating area). | `Boolean` |
| Body Surface Area | BSA | Body surface area (m2). Default is the ASHRAE standard person. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| SET |  | Standard Effective Temperature (°C). | `Number` |
| ET |  | Effective Temperature (°C). | `Number` |
| PMV |  | PMV from the two-node energy balance. | `Number` |
| Sensation | TS | Predicted thermal sensation (TSENS). | `Number` |
| Discomfort | DISC | Thermal discomfort. | `Number` |
| Skin Temp | Tsk | Mean skin temperature (°C). | `Number` |
| Core Temp | Tcr | Core temperature (°C). | `Number` |
| Wettedness | W | Skin wettedness (0-1). | `Number` |
| Sweat Rate | SW | Regulatory sweat rate (g/h/m2). | `Number` |