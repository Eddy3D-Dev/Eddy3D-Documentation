# ![](/images/icons/GAN_Predict.png) GAN Predict - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22GAN%20Predict%22)

![](/images/components/GAN_Predict-crop.png)

Predict a pedestrian wind-speed field from buildings using the Eddy3D GAN (no CFD run). Sends the geometry to the GAN API and returns wind speeds + a colored result mesh.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Buildings | B | Building meshes. | `Mesh` |
| Analysis Plane | Pl | Square analysis plane (defaults to a 512×512 box around the buildings). | `Rectangle` |
| Wind Direction | Dir | Wind direction in degrees (0=N, clockwise). | `Integer` |
| API URL | URL | GAN API base URL. | `Text` |
| Voxel Size | V | Geometry rasterization voxel size (m). | `Number` |
| Color Size | CS | Result-mesh pixel size for coloring. | `Number` |
| Color Map | CM | Color map: Viridis, Turbo, or Inferno. | `Text` |
| Run |  | Run the prediction. Momentary — resets when the result arrives. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Speed | U | Predicted pedestrian wind speeds. | `Number` |
| Result Mesh | M | Colored wind-speed result mesh. | `Mesh` |