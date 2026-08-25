# ![](/images/icons/Facade_Wind_Pressure.png) Facade Wind Pressure - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Facade%20Wind%20Pressure%22)

![](/images/components/Facade_Wind_Pressure-crop.png)

External wind pressure on a facade per EN 1991-1-4, and the opening flow it drives.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Basic Wind Speed | Vb | Fundamental basic wind velocity v_b,0 (m/s) from the National Annex map. | `Number` |
| Height | z | Height above ground of the opening (m). | `Number` |
| Building Height | h | Building height (m). | `Number` |
| Building Depth | d | Plan dimension along the wind (m). h/d must be <= 5. | `Number` |
| Opening Area | A | Loaded area of the opening (m2). | `Number` |
| Zone | Z | Facade zone: 0 A, 1 B, 2 C (side bands from the windward corner), 3 D (windward), 4 E (leeward). | `Integer` |
| Terrain | T | Terrain category: 0 sea, 1 open flat, 2 low vegetation, 3 suburban, 4 urban. | `Integer` |
| Facade Zone | ZoneN | EN 1991-1-4 facade pressure zone by name. Picking one sets the Zone input; Custom uses the wired integer. | `Text` |
| Terrain Category | TerrN | EN 1991-1-4 Table 4.1 terrain category by name. Picking one sets the Terrain input; Custom uses the wired integer. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Pressure | we | External surface pressure (Pa). Positive pushes onto the facade. | `Number` |
| Cpe |  | External pressure coefficient. | `Number` |
| Peak Pressure | qp | Peak velocity pressure (Pa). | `Number` |
| Mean Wind | Vm | Mean wind speed at that height (m/s). | `Number` |
| Turbulence | Iv | Turbulence intensity. | `Number` |