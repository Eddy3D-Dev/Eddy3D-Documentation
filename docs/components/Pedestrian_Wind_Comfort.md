# ![](/images/icons/Pedestrian_Wind_Comfort.png) Pedestrian Wind Comfort - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Pedestrian%20Wind%20Comfort%22)

![](/images/components/Pedestrian_Wind_Comfort-crop.png)

Classifies pedestrian wind comfort per point from an annual hourly wind-speed series (the Wind Speed output of the Velocity Amplification Factors (VAF) component) against a comfort criterion (Lawson, Davenport, NEN8100). Returns the comfort category, class letter, and activity description for each point.

#### Input

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Wind Speed | U | Annual wind field from the Velocity Amplification Factors (VAF) component (its Wind Speed output): a single object holding every point's 8760-hour wind-speed series. Passed as an object so the millions of values skip the Grasshopper data tree. |
| Metric |  | Comfort criterion: 0 Lawson General, 1 Lawson LDDC, 2 Lawson 2001, 3 Davenport, 4 NEN8100 Comfort, 5 NEN8100 Safety. |

#### Output

| Name | Nickname | Description |
| ---- | -------- | ----------- |
| Rank |  | Comfort category number per point (1 = most comfortable; higher = worse). |
| Letter |  | Comfort class letter per point (A, B, ... ; S = unsafe). |
| Class |  | Comfort activity description per point (e.g. Sitting, Walking). |
