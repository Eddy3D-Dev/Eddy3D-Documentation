# ![](/images/icons/Vegetation_Properties.png) Vegetation Properties - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vegetation%20Properties%22)

![](/images/components/Vegetation_Properties-crop.png)

Define vegetation property coefficients for canopy modeling. Shows the recommended coefficients (Leaf Length, rsMin, kc) by default; right-click to show all coefficients (Cd, C, nEvapSides). OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Leaf Length (l) | l | Characteristic leaf length (l) for aerodynamic resistance. | `Number` |
| Stomatal Resistance Min | rsMin | Minimum stomatal resistance (rsMin). | `Number` |
| Radiation Extinction (kc) | kc | Radiation extinction coefficient (kc). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Vegetation Properties | Props | Vegetation properties as a Setting instance. | `Generic Data` |