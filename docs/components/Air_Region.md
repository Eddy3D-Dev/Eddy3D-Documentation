# ![](/images/icons/Air_Region.png) Air Region - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Air%20Region%22)

![](/images/components/Air_Region-crop.png)

Create an air region for the UMF case. OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| ABL Settings | ABL | Optional atmospheric boundary layer inflow for the air region: wire the Atmospheric Boundary Layer component's Boundary Conditions output (the first direction/speed is used — one Air Region is one UMCF case). | `Generic Data` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Air Region | Air | Air region object for the case. | `Generic Data` |