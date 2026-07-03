## ![](../images/icons/MRT_Settings.png) MRT Settings

![](../images/components/MRT_Settings-crop.png)

Configuration for the MRT + UTCI analysis.

#### Input
* ##### W 
Factor applied to weather wind speed when a probe has no CFD wind.
* ##### F 
Faces below this area (m²) are ignored by the thermal model.
* ##### Rad 
High-fidelity shortwave via the Radiance DDS chain (true) vs the pure-C# raycast (false). Requires a Radiance install (or Use Docker).
* ##### EP 
Surface temperatures from EnergyPlus (true) vs ambient (false). Requires an EnergyPlus install (or the Docker engine on the MRT component).

#### Output
* ##### S
MRT settings for the MRT component.