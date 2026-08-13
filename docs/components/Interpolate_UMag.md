# ![](/images/icons/Interpolate_UMag.png) Interpolate UMag - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Interpolate%20UMag%22)

![](/images/components/Interpolate_UMag-crop.png)

Resample direction-specific wind-magnitude fields onto a new point grid (nearest-neighbour average, with direction-specific rotation). Prepares grids for GAN applications.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Current Points | CP | Source points, one branch per direction. | `Point` |
| Current UMag | UMag | Source wind magnitudes, one branch per direction. | `Number` |
| New Points | NP | Target points to resample onto. | `Point` |
| Average By | AB | Number of nearest source points to average. | `Integer` |
| Center Point | C | Rotation center. | `Point` |
| Wind Directions | WDir | Wind direction (deg) per branch. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Points | P | The new points. | `Point` |
| U Mag | UMag | Resampled wind magnitudes, one branch per direction. | `Number` |