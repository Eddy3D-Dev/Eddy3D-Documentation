# ![](/images/icons/Stormwater_Settings.png) Stormwater Settings - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Stormwater%20Settings%22)

![](/images/components/Stormwater_Settings-crop.png)

Solver controls for Stormwater Run. The defaults suit a 1–5 m urban raster; leave this unconnected unless a run misbehaves.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Simulation Length | Sim | How long to simulate, in MINUTES. Should run well past the storm: peak ponding in a depression often arrives long after the rain stops, once the water has had time to travel there. A pond still standing when the run ends is itself a finding — it has nowhere to go. | `Number` |
| Output Interval | Out | Minutes between stored snapshots. Storage is cells × snapshots × two fields, so a fine interval on a large grid costs real memory. Peak depth and velocity are tracked every STEP regardless, so a coarse interval never misses the maximum. | `Number` |
| Boundary |  | Open (default): water leaves at the raster edge and wherever no ground was found, at the rate the local bed slope drives — an edge where the ground rises outward drains nothing. Closed: nothing leaves. For a genuinely bunded site, or to check that the model conserves water. | `Text` |
| CFL |  | Courant number for the adaptive timestep. 0.7 is the working value; lower it toward 0.4 if a run is unstable, which usually means the terrain has detail far below the cell size. | `Number` |
| Minimum Depth | MinD | Depth in MILLIMETRES below which a cell carries no flow. Not a fudge: the friction term divides by depth^(7/3), so without a floor the timestep collapses at the wetting front. 1 mm is negligible against any depth worth reporting. | `Number` |
| Debris Factor | DF | Added to the flood hazard rating HR = d·(v + 0.5) + DF. 0 is open ground with no debris source; UK guidance uses 0.5 to 1.0 where debris is expected. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Settings |  | Solver settings for Stormwater Run. | `Generic Data` |