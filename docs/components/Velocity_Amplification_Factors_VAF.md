# ![](../images/icons/Velocity_Amplification_Factors_VAF.png) Velocity Amplification Factors VAF - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Velocity%20Amplification%20Factors%20%28VAF%29%22)

![](../images/components/Velocity_Amplification_Factors_VAF-crop.png)

Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed.

#### Input
* ##### Boundary Conditions (BC) 
OutdoorBoundaryConditions object from the ABL or Uniform Flow component.
* ##### Wind Velocity (U) 
DataTree of velocity vectors {direction}[probe] from the probe results.
* ##### EPW 
Path to the EPW weather file.
* ##### Height 
Probing/pedestrian height in meters.
* ##### Interp 
Interpolate between bracketing wind directions.

#### Output
* ##### Wind
Annual wind field object (every point's 8760-hour wind-speed series) for the Pedestrian Wind Comfort component. A single object rather than a data tree, so a few thousand probes stay fast.
* ##### VAF
DataTree {direction}[probe] of Velocity Amplification Factors (VAF) — local wind speed normalized by the reference (undisturbed) speed.