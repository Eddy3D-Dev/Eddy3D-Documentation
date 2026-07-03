## ![](../images/icons/Deconstruct_Case.png) Deconstruct Case

![](../images/components/Deconstruct_Case-crop.png)

Inspect any Eddy3D case: Outdoor wind study, Indoor case, or OutdoorPlus (UMF) case.

#### Input
* ##### C 
Any Eddy3D case: an Outdoor wind study, an Indoor case, or an OutdoorPlus (UMF) case.

#### Output
* ##### N
Case name.
* ##### T
Which plugin produced it (Outdoor / Indoor / OutdoorPlus).
* ##### G
Representative geometry (buildings / room / total mesh).
* ##### D
Simulation domain (wind tunnel box / indoor zone).
* ##### F
Case directories on disk (one per sub-result).
* ##### S
Sub-result labels (wind directions for Outdoor; the case name otherwise).
* ##### R
Regions available to probe (air, buildings, … for UMF; a single empty entry otherwise).