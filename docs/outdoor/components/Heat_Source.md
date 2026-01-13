## ![](../images/icons/Heat_Source.png) Heat Source

![](../images/components/Heat_Source-crop.png)

Heat Source  Models a heat-generating object within the indoor space, such as equipment, electronics, or a cluster of people. Can be defined by total power (W) or power density (W/m³).   Eddy3D 0.5.0.815

#### Input
* ##### Geo 
Heat source volume (Mesh).
* ##### P 
Heat output. Units: W (absolute) or W/m³ (specific).
* ##### Name 
Identifier for this heat source.
* ##### Type 
0: Absolute [W], 1: Specific [W/m³]

#### Output
* ##### FObj
Heat source for Indoor Simulation component