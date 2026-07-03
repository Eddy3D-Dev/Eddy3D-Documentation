## ![](../images/icons/Thermal_Comfort.png) [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Thermal%20Comfort%22)

![](../images/components/Thermal_Comfort.png)

Compute a thermal comfort metric at a point: UTCI (Ta, RH, wind, MRT), PET (adds the personal inputs), or NOAA Heat Index (Ta, RH only). Pick the metric from the dropdown — the inputs adapt. Wire hourly lists (e.g. EPW series) to compute annual values.

#### Input
* ##### Metric 
Comfort metric to compute; the inputs adapt to the choice.
* ##### Ta 
Air temperature [°C].
* ##### Relative Humidity (RH) 
Relative humidity [%].
* ##### Wind 
Wind speed at the subject [m/s].
* ##### MRT 
Mean radiant temperature [°C].

#### Output
* ##### Value
Metric value [°C].
* ##### Stress
Thermal stress category.
* ##### Details
Calculation details.