# ![](/images/icons/Wind_Predictor_Cloud.png) Wind Predictor (Cloud) - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Predictor%20%28Cloud%29%22)

![](/images/components/Wind_Predictor_Cloud-crop.png)

Predict a pedestrian wind-speed field from buildings without running CFD, using the hosted Eddy3D model (Yel 1.0, a 512x512 image GAN). Rasterizes the buildings and the analysis plane into the model's input image, sends it to the API, and returns the predicted wind speeds plus a colored result mesh. Runs on Eddy3D's server: needs internet, no GPU and no model download, and the free server may need a minute to wake up. For a local GPU run over arbitrary points and multiple wind directions, use Wind Predictor with a model from ML Model instead.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Buildings | B | Building meshes. | `Mesh` |
| Analysis Plane | Pl | Square analysis plane (defaults to a 512x512 box around the buildings). | `Rectangle` |
| Wind Direction | Dir | Wind direction in degrees (0=N, clockwise). | `Integer` |
| API URL | URL | Prediction API base URL. | `Text` |
| Voxel Size | V | Geometry rasterization voxel size (m). | `Number` |
| Color Size | CS | Result-mesh pixel size for coloring. | `Number` |
| Color Map | CM | Color map: Viridis, Turbo, or Inferno. | `Text` |
| Run |  | Run the prediction. Momentary - resets when the result arrives. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Speed | U | Predicted pedestrian wind speeds. | `Number` |
| Result Mesh | M | Colored wind-speed result mesh. | `Mesh` |