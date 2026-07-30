# ![](/images/icons/MRT_Settings.png) MRT Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22MRT%20Settings%22)

![](/images/components/MRT_Settings-crop.png)

Configuration for the MRT + UTCI analysis.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Scaling | W | Factor applied to weather wind speed when a probe has no CFD wind. | `Number` |
| Small Face Cutoff | F | Faces below this area (m²) are ignored by the thermal model. | `Number` |
| Radiance Reflections | Rad | High-fidelity shortwave via the Radiance DDS chain (true, default) vs the pure-C# raycast (false). Requires a Radiance install (or Use Docker). | `Boolean` |
| EnergyPlus Surfaces | EP | Surface temperatures from EnergyPlus (true, default) vs ambient (false). Requires an EnergyPlus install (or the Docker engine on the MRT component). | `Boolean` |
| Engine Timeout | T | Wall-clock cap in minutes for each external engine run (Radiance DDS, EnergyPlus). Raise for large urban scenes. | `Integer` |
| Sky Dome Subdivisions | SkyDiv | Resolution of the internal MRT sky hemisphere. Higher values produce smoother view factors but take longer. Recommended range 8-24; default 16. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings | S | MRT settings for the MRT component. | `Generic Data` |