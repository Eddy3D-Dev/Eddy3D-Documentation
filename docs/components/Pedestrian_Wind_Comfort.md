# ![](/images/icons/Pedestrian_Wind_Comfort.png) Pedestrian Wind Comfort - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Pedestrian%20Wind%20Comfort%22)

![](/images/components/Pedestrian_Wind_Comfort-crop.png)

Classifies pedestrian wind comfort per point from an annual hourly wind-speed series (the Wind Speed output of the Velocity Amplification Factors (VAF) component) against a comfort criterion (Lawson, Davenport, NEN8100). Returns the comfort category, class letter, and activity description for each point.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Speed | U | Annual wind field from the Velocity Amplification Factors (VAF) component (its Wind Speed output): a single object holding every point's 8760-hour wind-speed series. Passed as an object so the millions of values skip the Grasshopper data tree. | `Generic Data` |
| Comfort Metric | Metric | Comfort criterion: Lawson General, Lawson LDDC, Lawson 2001, Davenport, NEN8100 Comfort, or NEN8100 Safety. A wired integer 0-5 (the old convention) still selects by index. | `Text` |
| Color Scheme | Scheme | Categorical palette for the comfort classes: Classic (green through red, the standard wind-comfort plot), Colorblind Safe (Okabe-Ito derived), or Muted (desaturated, for underlays). | `Text` |
| Size | S | Marker half-size in model units for the comfort mesh (one quad per point). | `Number` |
| Period |  | Slice of the year to classify: Year (default), a season, or a single month. The exceedance criteria then apply to that period's hours only — winter comfort is usually worse than annual. Seasons are named by their months (Winter = Dec-Feb), so southern-hemisphere EPWs read unambiguously. | `Text` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Comfort Rank | Rank | Comfort category number per point (1 = most comfortable; higher = worse). | `Integer` |
| Class Letter | Letter | Comfort class letter per point (A, B, ... ; S = unsafe). | `Text` |
| Comfort Class | Class | Comfort activity description per point (e.g. Sitting, Walking). | `Text` |
| Mesh | M | Comfort mesh: one colored quad per probe point, class-colored by the selected scheme. Needs points inside the Wind Speed object — wire the probe points into the VAF component's Points input. | `Mesh` |
| Colors | C | Class color per point, aligned with the input series — for coloring custom geometry. | `Colour` |
| Legend Colors | LC | One color per class of the selected metric, best-to-worst — pairs with Legend Labels for annotation. | `Colour` |
| Legend Labels | LL | One label per class of the selected metric ("A — Sitting" style), aligned with Legend Colors. | `Text` |