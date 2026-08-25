# ![](/images/icons/Streamlines.png) Streamlines - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Streamlines%22)

![](/images/components/Streamlines-crop.png)

Extract solver-side streamlines from a solved case with OpenFOAM's streamlines function object (particles tracked through the actual mesh — accurate in refined near-building cells, unlike tracing a probed field). With Run it writes the function-object dict and runs postProcess on the requested Time, then reads the tracks; without Run it reads existing tracks.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Solved wind case or loaded study to extract streamlines from. | `Generic Data` |
| Seed Line | Line | Line to seed uniformly with Seed Count particles (e.g. a vertical line upstream of the site). Ignored when Seed Points are wired. | `Line` |
| Seed Points | Pts | Explicit seed points. Takes precedence over Seed Line when wired. | `Point` |
| Seed Count | N | Number of seeds along Seed Line. Default 24. | `Integer` |
| Fields |  | Fields to sample along the tracks. U is always included (needed for speed coloring); add p, k, … for extra data. | `Text` |
| Direction | Dir | Tracking direction from each seed: Both (upstream + downstream, longest lines), Forward (with the flow), or Backward. | `Text` |
| Region |  | Region to track in; leave empty for single-region (wind) cases. | `Text` |
| Time |  | Result time to track at: empty = latest written time, a number = that written time. | `Text` |
| Color Map | CM | Color ramp for the speed coloring — pick the same map as the Vector Field Viewer / Wind Legend. | `Text` |
| Range | R | Optional speed range [min, max] (m/s) to lock the color scale. Empty = the tracks' own min/max. Wire the Vector Field Viewer's Range output (or another Streamlines component's) to color both on one comparable scale. | `Domain` |
| Run |  | True: write the streamlines function object and run postProcess, then read the tracks. False: read existing tracks only (the dict is still written so external runs pick it up). | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Streamlines | SL | Traced streamline polylines; branch = {sub-result}, items = one curve per track. | `Curve` |
| Speeds | Spd | Velocity magnitude along each track; branch = {sub-result, track}, items = one per vertex (feed with Streamlines into Vector Field Viewer or a gradient for coloring). | `Number` |
| Sub-Results | Subs | Sub-result labels matching the first branch index (e.g. wind direction case names). | `Text` |
| Colors | C | One color per track (its mean speed on the ramp); branch = {sub-result}, aligned with Streamlines — wire both into a Custom Preview to bake the coloring. The viewport preview drawn by the component itself is finer: per-segment gradients. | `Colour` |
| Range | R | The speed range the colors span (m/s): the Range input where wired, else the tracks' min/max. Feed it to the Wind Legend component for a matching legend. | `Domain` |