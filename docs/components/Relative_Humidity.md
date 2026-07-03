## ![](../images/icons/Relative_Humidity.png) Relative Humidity

![](../images/components/Relative_Humidity-crop.png)

Convert specific humidity (w) and temperature (T) to relative humidity (%). OutdoorPlus

#### Input
* ##### w 
Specific humidity in kg/kg (from OpenFOAM field 'w').
* ##### T 
Air temperature in Kelvin (from OpenFOAM field 'T').
* ##### P 
Atmospheric pressure in Pa. Optional; default is 101325 Pa.

#### Output
* ##### RH
Relative humidity in percent (0–100%).