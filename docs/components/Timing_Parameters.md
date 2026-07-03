# ![](../images/icons/Timing_Parameters.png) [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Timing%20Parameters%22)

![](../images/components/Timing_Parameters.png)

Define simulation timing and optional weather-driven time series. OutdoorPlus

#### Input
* ##### Weather 
Optional Weather object or EPW file path for weather-driven time series.
* ##### StartDay 
Day-of-year index to start (0-based). Optional; default is 0.
* ##### StartHour 
Hour of day to start (0-23). Optional; default is 0.
* ##### Hours 
Simulation duration in hours. Optional; default is 24.

#### Output
* ##### Timing
Simulation timing settings.