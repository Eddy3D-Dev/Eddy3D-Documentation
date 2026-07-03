# ![](../images/icons/Simulation_Settings.png) [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Simulation%20Settings%22)

![](../images/components/Simulation_Settings.png)

Configure simulation control settings for UMF. OutdoorPlus

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