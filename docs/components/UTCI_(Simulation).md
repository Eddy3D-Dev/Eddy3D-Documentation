## ![](../images/icons/UTCI_(Simulation).png) UTCI (Simulation)

![](../images/components/UTCI_(Simulation)-crop.png)

Compute annual per-probe UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".

#### Input
* ##### M 
DataTree of annual MRT values {probe}(8760). Each branch = one probe.
* ##### V 
Annual per-probe wind field from the Wind Factors component (its Wind Speed output). Pedestrian-height speeds are lifted to the 10 m UTCI reference. Defaults to calm (0.5 m/s) when not connected.
* ##### T 
Annual hourly ambient air temperature (8760 values, °C).
* ##### RH 
Annual hourly relative humidity (8760 values, %).

#### Output
* ##### U
DataTree {probe}(8760 hourly UTCI values).
* ##### H
No-thermal-stress hours per probe.
* ##### %
Comfort percentage per probe.