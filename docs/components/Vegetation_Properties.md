# ![](../images/icons/Vegetation_Properties.png) Vegetation Properties - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Vegetation%20Properties%22)

![](../images/components/Vegetation_Properties-crop.png)

Define vegetation property coefficients for canopy modeling. OutdoorPlus

#### Input
* ##### Cd 
Vegetation drag coefficient (Cd). Used in momentum sink and turbulence model.
* ##### Aerodynamic Resistance (C) (C) 
Proportionality factor for aerodynamic resistance calculation.
* ##### l 
Characteristic leaf length (l) for aerodynamic resistance.
* ##### rsMin 
Minimum stomatal resistance (rsMin).
* ##### EvapSides 
Number of evaporation sides for transpiration calculation.
* ##### kc 
Radiation extinction coefficient (kc).

#### Output
* ##### Props
Vegetation properties as a Setting instance.