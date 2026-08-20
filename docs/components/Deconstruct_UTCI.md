# ![](/images/icons/Deconstruct_UTCI.png) Deconstruct UTCI - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20UTCI%22)

Reduces the annual UTCI field carried in a UTCI (Simulation) Result into probe-specific statistics — mean/min/max, comfort hours and comfort % — over any hour selection, without putting all 8760 hours per probe on the canvas. It draws nothing itself: wire its Points (or the Result) into the Thermal Comfort Legend to get a colored map.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Result | R | Result output of the UTCI (Simulation) component — the whole solved annual UTCI field, passed as a single item. | `Generic` |
| HOY | HOY | Hour(s) of year (1-8760) to restrict to. Leave unconnected for the whole year. Statistics and comfort hours/% are reduced over exactly these hours, so a July-afternoon list gives the July-afternoon comfort — no re-solve needed. | `Integer` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mean | Avg | Mean UTCI (°C) per probe over the selected hours — the annual average when HOY is unconnected. | `Number` |
| Min | Min | Lowest UTCI (°C) per probe over the selected hours. | `Number` |
| Max | Max | Highest UTCI (°C) per probe over the selected hours. | `Number` |
| Comfort Hours | H | No-thermal-stress hours per probe, counted over the selected hours. | `Integer` |
| Comfort % | % | No-thermal-stress share (%) of the selected hours, per probe. | `Number` |
| UTCI | U | UTCI (°C) at each selected hour — one branch per HOY, each holding every probe's value. Populated only when HOY is connected; with HOY unconnected this would be the entire year, which is the tree this component exists to avoid. | `Number` |
| Points | P | Probe positions carried inside the Result, aligned by index with every list above. Wire these into the Thermal Comfort Legend's Sensor Points to draw a map — or wire the Result straight into that component, which takes the positions itself. | `Point` |

#### Notes

- **This component only reduces — it no longer draws.** An older version also carried the false-color legend directly (Statistic, Radius, Legend Plane/Size/Text inputs; Mesh, Legend Mesh/Points/Labels/Text outputs). That drawing responsibility moved to the **Thermal Comfort Legend** component. Opening a document saved before the split triggers Remarks naming which inputs/outputs moved and where to reconnect them.
- **Result must arrive as a single item.** Feeding a list of Results makes Grasshopper iterate the component once per item; on the second item it raises an Error instead of silently re-running the reduction per Result.
- **HOY is clamped, not rejected.** Values outside 1-8760, or beyond the hours this particular Result actually holds (e.g. a partial-year weather series), are clamped into range with a Warning rather than failing the solve.
- **Large HOY selections get a performance Remark.** Once HOY-hours × probe-count exceeds 2,000,000 values, a Remark suggests narrowing HOY or using the statistics outputs, which read the same hours without materializing them onto the canvas.
