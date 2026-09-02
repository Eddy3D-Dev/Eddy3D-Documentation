# ![](/images/icons/Viral_Emitter.png) Viral Emitter - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Viral%20Emitter%22)

![](/images/components/Viral_Emitter-crop.png)

An airborne-pathogen passive-scalar source box for an indoor ventilation case. Method: De Simone, Kastner & Dogan (2021), Building Simulation 2021, Bruges, doi:10.26868/25222708.2021.30632.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Zone | Z | Box zone occupied by the viral source. | `Box` |
| Injection Rate | IR | Viral tracer injection rate (specific). | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Source | S | Viral source for the Indoor Case component. | `Generic Data` |