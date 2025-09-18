## ![](../../images/icons/Advanced_Terrain_Mesh.png) Advanced Terrain Mesh

![](../../images/components/Advanced_Terrain_Mesh.png)

Generates a multi-resolution terrain mesh from input geometry with a solid base.

#### Input
* ##### T 
Input terrain geometry (Meshes, Breps, or Surfaces).
* ##### IS 
Scale factor for the high-detail inner region.
* ##### OS 
Scale factor for the low-detail outer region.
* ##### H 
The height of the solid base below the terrain.

#### Output
* ##### M
The final generated terrain mesh.