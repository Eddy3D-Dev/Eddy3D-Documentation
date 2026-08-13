# ![](/images/icons/SurfaceTemp_FFT.png) SurfaceTemp (FFT) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22SurfaceTemp%20%28FFT%29%22)

![](/images/components/SurfaceTemp_FFT-crop.png)

Solves outdoor surface temperature per analysis point via the frequency-domain admittance method (no thermal mesh, no warm-up). Feeds a future MRT component alongside Sky Exposure.  Method: Beckett, O., Owens, S. and Acred, A. (2026). Applying Frequency Domain Methods for Calculating Outdoor Surface Temperatures. Proceedings of the 12th National Conference of IBPSA-USA, Minneapolis, MN. https://publications.ibpsa.org/conference/paper/?id=simbuild2026_1312

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | Analysis points. | `Point` |
| Vectors | Vec | Normal vector at each analysis point (e.g. from Eddy3D's Brep Grid Points), one per point. | `Vector` |
| EPW | W | Path to an EPW weather file. | `Text` |
| Material | Mat | SurfaceTemp material (from the SurfaceTemp Material component). | `Generic Data` |
| Indoor Temp | Tin | Indoor design temperature (°C) for wall/roof materials. Ignored for ground materials, which use the EPW annual mean air temperature instead. | `Number` |
| Sky View | Sky | Optional sky view factor (0-1) per analysis point, from Sky Exposure. One value per point, or a single value for all points. Unconnected points fall back to the ideal tilt-based value (no context occlusion). | `Number` |
| Run | R | Enable the surface-temperature calculation. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | R | The complete solve — every analysis point's full 8760-hour series — as a single item, so it costs one wire instead of a tree. Feed it to Deconstruct SurfaceTemp for point-specific annual mean/min/max, or for the hours of any subset. | `Generic Data` |