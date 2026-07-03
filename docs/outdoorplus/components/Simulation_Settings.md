## ![](../images/icons/Simulation_Settings.png) Simulation Settings

![](../images/components/Simulation_Settings-crop.png)

Configure simulation control settings for UMF. OutdoorPlus  Version 1.0.0.827

#### Input
* ##### WriteInt 
Write interval in time steps. Optional; uses solver default if omitted.
* ##### Format 
Write format: 0=ascii, 1=binary, 2=compressed.
* ##### CPU 
Number of CPUs/subdomains to use. Optional; default is 1.
* ##### SolidStep 
Initial solid time step factor for UMF controlDict. Optional.
* ##### MinDT 
Minimum time step between iterations. Optional.
* ##### MaxDT 
Maximum time step between iterations. Optional.
* ##### MinFI 
Minimum fluid iterations per time step. Optional.
* ##### MaxFI 
Maximum fluid iterations per time step. Optional.
* ##### PcForm 
'pc-based' or 'mixed' (default is pc-based).
* ##### DampThk 
Blending coefficients: damping thickness. Optional.
* ##### AlphaU 
Blending coefficients: alphaCoeffU. Optional.
* ##### AlphaT 
Blending coefficients: alphaCoeffT. Optional.

#### Output
* ##### Settings
Simulation control settings.