# ![](/images/icons/Read_Cells.png) Read Cells - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Read%20Cells%22)

![](/images/components/Read_Cells-crop.png)

Read cell connectivity and cell zones for a region. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | UMF case containing the region data. | `Generic Data` |
| Region |  | Region name to read. | `Text` |
| Chunk Size | Chunk | Chunk size for reading owner/neighbour files. Optional; default is 500. | `Integer` |
| Chunk Offset | Offset | Chunk offset for reading owner/neighbour files. Optional; default is 0. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Cells by Face Indices | Cells | Tree of cells containing face indices. | `Generic Data` |
| Cell Zone Names | Zones | Cell zone names. | `Text` |
| Cell Zone Indices | ZoneIndices | Indices for each cell zone. | `Generic Data` |