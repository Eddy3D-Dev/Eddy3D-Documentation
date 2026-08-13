# ![](/images/icons/Wind_Rose_Cluster.png) Wind Rose Cluster - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Rose%20Cluster%22)

![](/images/components/Wind_Rose_Cluster-crop.png)

Cluster annual wind directions into representative directions using k-means.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Directions | Dirs | Wind directions in degrees (e.g. hourly values from an EPW). | `Number` |
| Budget |  | Maximum number of representative directions (clusters). | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Centroids |  | Representative centroid direction of each cluster. | `Number` |
| Wind Directions | Dirs | Distinct representative wind directions in degrees, sorted ascending; plug into the ABL or Uniform Flow component's Wind Directions input. | `Number` |
| Clusters |  | Clustered direction vectors as points, one branch per cluster. | `Point` |
| Breaks |  | Jenks-Fisher natural breaks of the input directions. | `Number` |
| Distance | Dist | Total clustering distance (error). | `Number` |