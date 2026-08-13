# ![](/images/icons/Window_Air_Exchange.png) Window Air Exchange - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Window%20Air%20Exchange%22)

![](/images/components/Window_Air_Exchange-crop.png)

Air exchange through an open window (Maas 1995) and the steady-state CO2 it supports.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Opening Area | A | Effective free opening area (m2). | `Number` |
| Wind Speed | U | Outdoor wind speed at 10 m (m/s). | `Number` |
| Sash Height | H | Height of the openable sash (m) — drives the buoyancy term. | `Number` |
| Temp Difference | dT | Indoor minus outdoor air temperature (K). Sign is ignored. | `Number` |
| Room Volume | V | Room volume (m3), for air changes per hour. | `Number` |
| CO2 Rate | Q | CO2 generation per occupant (L/s) — see the Occupant CO2 component. | `Number` |
| Occupants | N | Number of occupants. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Flow | Fl | Air exchange through the opening (m3/h). | `Number` |
| Air Changes | ACH | Air changes per hour. | `Number` |
| Steady CO2 | C | Steady-state indoor CO2 (ppm) at that flow and occupancy. | `Number` |