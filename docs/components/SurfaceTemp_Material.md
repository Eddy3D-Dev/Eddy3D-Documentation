# ![](/images/icons/SurfaceTemp_Material.png) SurfaceTemp Material - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22SurfaceTemp%20Material%22)

![](/images/components/SurfaceTemp_Material-crop.png)

Predefined multi-layer construction (assembly) for the SurfaceTemp admittance solve.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| MaterialList | MatList | Predefined SurfaceTemp material. | `Text` |
| Emissivity | Emis | Long-wave emissivity of the exterior face, above 0 to 1. The library's assemblies are 0.9; bare metal is 0.1-0.2 and runs hotter by day and by night for it. | `Number` |
| Wetness | Wet | How freely the surface evaporates, 0 (dry, every library assembly) to 1 (irrigated turf, a wet green roof): that share of the Priestley-Taylor latent heat is taken out of the sunlight the surface absorbs. | `Number` |
| Wind Exposure | Wind | The share of the weather file's wind that reaches the surface, 1 (open) to 0 (still air). A weather station's wind does not reach a courtyard wall; a wind factor from a wind study is the number to give here. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Material | Mat | SurfaceTemp material parameters for the SurfaceTemp component. | `Generic Data` |