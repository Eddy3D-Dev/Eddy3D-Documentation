# ![](/images/icons/Wind_Rose_Cluster.png) Wind Rose Cluster - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Rose%20Cluster%22)

![](/images/components/Wind_Rose_Cluster-crop.png)

Cluster annual wind conditions into a budget of representative directions using k-means over hourly wind vectors (speed x direction): frequent, strong conditions attract the budget, and each cluster reports an observed direction/speed pair plus its frequency. Without wired speeds, clusters directions alone (unit vectors). Method: Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639; Kastner & Dogan (2019), Building Simulation 2019, Rome 621-628, doi:10.26868/25222708.2019.210458.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Directions | Dirs | Wind directions in degrees (e.g. hourly values from an EPW). | `Number` |
| Budget |  | Maximum number of representative directions (clusters), e.g. 8 or 16. | `Integer` |
| Wind Speeds | U | Hourly wind speeds (m/s) paired with Directions (optional). When wired, the clustering runs over wind VECTORS (speed x direction), so speed and frequency both shape the representative set; calm hours (< 0.5 m/s) are excluded. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Directions | Dirs | Distinct representative wind directions in degrees, sorted ascending; plug into the ABL or Uniform Flow component's Wind Directions input. | `Number` |
| Wind Speeds | U | Representative wind speed (m/s) per cluster — the observed speed of the cluster's medoid hour, aligned with Wind Directions; plug into the ABL component's Wind Speed input. Requires wired input speeds. | `Number` |
| Frequencies | Freq | Fraction of (non-calm) hours in each cluster, aligned with Wind Directions — the per-direction weights for annual wind-comfort statistics. Sums to 1. | `Number` |