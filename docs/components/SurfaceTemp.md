# ![](/images/icons/SurfaceTemp.png) SurfaceTemp - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22SurfaceTemp%22)

![](/images/components/SurfaceTemp-crop.png)

Solves outdoor surface temperature per analysis point via the frequency-domain admittance method (no thermal mesh, no warm-up). Feeds a future MRT component alongside Sky Exposure.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | Pts | Analysis points. | `Point` |
| Vectors | Vec | Normal vector at each analysis point (e.g. from Eddy3D's Brep Grid Points), one per point. | `Vector` |
| EPW |  | Path to an EPW weather file. | `Text` |
| Material | Mat | SurfaceTemp material (from the SurfaceTemp Material component). | `Generic Data` |
| HOY |  | Hour(s) of year (1-8760) to output — one value, a list (e.g. a whole month), or leave unconnected for the full year. | `Integer` |
| Indoor Temp | Tin | Indoor design temperature (°C) for wall/roof materials. Ignored for ground materials, which use the EPW annual mean air temperature instead. | `Number` |
| Sky View | Sky | Optional sky view factor (0-1) per analysis point, from Sky Exposure. One value per point, or a single value for all points. Unconnected points fall back to the ideal tilt-based value (no context occlusion). | `Number` |
| Run |  | Enable the surface-temperature calculation. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| SurfaceTemp |  | Surface temperature (°C) at each requested HOY (or the full 8760-hour year, if HOY is unconnected) — one branch per HOY, each holding every analysis point's value {hoy}(point count). | `Number` |