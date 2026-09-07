# ![](/images/icons/Stormwater_Run.png) Stormwater Run - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Stormwater%20Run%22)

![](/images/components/Stormwater_Run-crop.png)

Routes a design storm over the graded terrain and reports ponding depth, flow velocity and flood hazard.  Two modes. FAST is terrain analytics only — slope, flow direction, contributing area and the capacity of every depression — which recomputes between grading edits and answers most of a grading review. FULL adds a shallow-water solve for the depths and velocities a design storm actually produces.  SURFACE ROUTING ONLY: no pipe network, no soakaways, no evapotranspiration. Use it for design-storm and cloudburst checks, not for hydraulic sizing.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Grid |  | The rasterised site from Stormwater Grid. | `Generic Data` |
| Storm |  | The design storm from Design Storm. Not needed in Fast mode, which reads the terrain alone. | `Generic Data` |
| Settings |  | Solver settings. Leave unconnected for defaults suited to a 1–5 m urban raster. | `Generic Data` |
| Mode |  | Fast: terrain analytics only — instant, and enough for most grading questions. Full: adds the shallow-water solve for depth and velocity under the design storm. | `Text` |
| Run |  | Route the storm. Works as an inline button or as a wired toggle — with a wire held true, the run relaunches whenever the inputs change. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result |  | The whole run as ONE item, for Deconstruct Stormwater, Ponding Report and Stormwater Flowlines. It is not a tree on purpose — a run holds millions of values, and emitting them here would freeze the canvas. | `Generic Data` |
| Summary |  | Peak depth and velocity, ponding capacity, the mass balance, and the caveats that belong with any number taken from this run. | `Text` |
| Peak Depth | Peak | Deepest ponding anywhere on the site (mm). | `Number` |