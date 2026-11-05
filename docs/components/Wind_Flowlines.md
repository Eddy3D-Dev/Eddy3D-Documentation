# ![](/images/icons/Wind_Flowlines.png) Wind Flowlines - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Wind%20Flowlines%22)

![](/images/components/Wind_Flowlines-crop.png)

Record wind flowlines through an LBM case's velocity frames (or a steady Points + Vectors field), save the recording in the case folder, and play it back. Each emitter releases particles evenly in time; when the wind direction turns past the restart angle the lines start again from the emitters. Playback restyles with Range and Thickness without re-tracing.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | LBM case folder (OpenLB or FluidX3D). The recording is written here as flowlines.e3dflow, and played back from here. | `Text` |
| Emitters |  | Points the flowlines start from. Divide a curve for an even rake. | `Point` |
| Points |  | Optional steady field: sample points (e.g. an OpenFOAM result or LBM Field). Wired with Vectors, it replaces the case's VTK frames and records one frame. | `Point` |
| Vectors |  | Velocity per point (m/s), pairing 1:1 with Points. | `Vector` |
| Time Step | Step | Seconds between particle releases (and integration step). Point spacing along a line is speed x step. | `Number` |
| Line Points | Length | Particles kept per line; a line spans Line Points x Time Step seconds of travel. | `Integer` |
| Restart Angle | Restart | Degrees the mean wind direction at the emitters must turn between frames before every line restarts from its emitter. | `Number` |
| Frame |  | Recorded frame to show (0-based). While Play is on, playback starts here. | `Integer` |
| Play |  | Loop through the recorded frames at 10 frames per second. | `Boolean` |
| Range |  | Speed range (m/s) the colours span. Unset: the recording's own range. | `Domain` |
| Thickness |  | Line thickness in the viewport, in pixels. | `Integer` |
| Record |  | Trace the flowlines through every frame and save the recording. Playback needs no Record. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Flowlines | Lines | The shown frame's flowlines. | `Curve` |
| Speeds |  | Speed (m/s) at each flowline point, one branch per line. | `Number` |
| Frame |  | Index of the shown frame. | `Integer` |
| Frame Count | Count | Frames in the recording. | `Integer` |
| Time |  | Solver time of the shown frame (s); empty for a steady frame. | `Number` |
| Range |  | Speed range used for the colours, for a legend. | `Domain` |
| File |  | The recording file. | `Text` |