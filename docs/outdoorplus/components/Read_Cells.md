## ![](../images/icons/Read_Cells.png) Read Cells

![](../images/components/Read_Cells-crop.png)

Read cell connectivity and cell zones for a region. OutdoorPlus 0.0.20.0

#### Input
* ##### Case 
UMCF case containing the region data.
* ##### Region 
Region name to read.
* ##### Chunk 
Chunk size for reading owner/neighbour files. Optional; default is 500.
* ##### Offset 
Chunk offset for reading owner/neighbour files. Optional; default is 0.

#### Output
* ##### Cells
Tree of cells containing face indices.
* ##### Zones
Cell zone names.
* ##### ZoneIndices
Indices for each cell zone.