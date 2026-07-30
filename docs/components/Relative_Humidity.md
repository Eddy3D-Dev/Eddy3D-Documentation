# ![](/images/icons/Relative_Humidity.png) Relative Humidity - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Relative%20Humidity%22)

![](/images/components/Relative_Humidity-crop.png)

Convert specific humidity (w) and temperature (T) to relative humidity (%). OutdoorPlus

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Specific Humidity | w | Specific humidity in kg/kg (from OpenFOAM field 'w'). | `Number` |
| Temperature | T | Air temperature in Kelvin (from OpenFOAM field 'T'). | `Number` |
| Pressure | P | Atmospheric pressure in Pa. Optional; default is 101325 Pa. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Relative Humidity | RH | Relative humidity in percent (0–100%). | `Number` |