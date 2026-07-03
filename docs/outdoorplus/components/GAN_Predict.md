## ![](../images/icons/GAN_Predict.png) GAN Predict

![](../images/components/GAN_Predict-crop.png)

Predict a pedestrian wind-speed field from buildings using the Eddy3D GAN (no CFD run). Sends the geometry to the GAN API and returns wind speeds + a colored result mesh.  Version 1.0.0.827

#### Input
* ##### B 
Building meshes.
* ##### Pl 
Square analysis plane (defaults to a 512×512 box around the buildings).
* ##### Dir 
Wind direction in degrees (0=N, clockwise).
* ##### URL 
GAN API base URL.
* ##### V 
Geometry rasterization voxel size (m).
* ##### CS 
Result-mesh pixel size for coloring.
* ##### CM 
Color map: Viridis, Turbo, or Inferno.
* ##### Run 
Run the prediction. Momentary — resets when the result arrives.

#### Output
* ##### U
Predicted pedestrian wind speeds.
* ##### M
Colored wind-speed result mesh.