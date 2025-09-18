## ![](../../images/icons/CalcPET.png) CalcPET

![](../../images/components/CalcPET.png)

Calculate PET.

#### Input
* ##### Ta 
Air temperature in Celsius (°C)
* ##### MRT 
Mean radiant temperature in Celsius (°C)
* ##### rh 
Relative humidity in percent (%)
* ##### ws 
Wind speed in meters per second (m/s)
* ##### P 
Atmospheric pressure in hPa
* ##### age 
Age in years
* ##### sex 
Sex of the person ('Male', 'Female', or 'Average')
* ##### H 
Height in meters (m)
* ##### W 
Weight in kilograms (kg)
* ##### pos 
Body position ('Standing', 'Sitting', or 'Crouching')
* ##### Icl 
Clothing insulation value in clo
* ##### M 
Metabolic rate / activity in Watts (W)
* ##### climate 
Climate type ('Temperate' or 'Humid')

#### Output
* ##### PET
Physiological Equivalent Temperature (°C)
* ##### Stress
Thermal stress level based on PET
* ##### Comfort
Indicates if the condition is thermally comfortable
* ##### D
Detailed results from the PET calculation