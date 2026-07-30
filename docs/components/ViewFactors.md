# ![](/images/icons/ViewFactors.png) ViewFactors - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22ViewFactors%22)

![](/images/components/ViewFactors-crop.png)

Configure the view-factor discretization for radiation modeling. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Domain Sides Coarse Faces | SideFaces | Number of faces in the coarsest level for domain side walls. | `Integer` |
| Domain Top Coarse Faces | TopFaces | Number of faces in the coarsest level for the domain top. | `Integer` |
| Terrain Coarse Faces | TerrainFaces | Number of faces in the coarsest level for terrain. | `Integer` |
| Building Coarse Faces | BuildingFaces | Number of faces in the coarsest level for buildings. | `Integer` |
| Vegetation Coarse Faces | VegFaces | Number of faces in the coarsest level for vegetation. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| View Factor Settings | ViewFactors | View-factor settings. | `Generic Data` |