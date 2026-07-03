## ![Plot Residuals Icon](../images/icons/Plot_Residuals.png) Plot Residuals

![Plot Residuals Component](../images/components/Plot_Residuals-crop.png)

Convergence Monitor

 Visualizes the definition of simulation convergence (residuals) in real-time. Helps verify if the simulation has reached a stable solution.


 Eddy3D 1.0.0.827

#### Input
* ##### Res 
Simulation result from Wind Simulation component.
* ##### X 
Iteration axis range. Format: 'min:max'. Example: '0:5000'
* ##### Y 
Residual axis range (log scale). Format: 'min:max'. Example: '0.00001:1'
* ##### Ver 
0: BlueCFD Gnuplot, 1: Windows Gnuplot
* ##### Run! 
Set True to display residual plot.

#### Output