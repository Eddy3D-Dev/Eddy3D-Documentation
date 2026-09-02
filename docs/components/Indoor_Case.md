# ![](/images/icons/Indoor_Case.png) Indoor Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Case%22)

![](/images/components/Indoor_Case-crop.png)

Build an isothermal indoor ventilation case (room + inlets + outlets + sinks) for OpenFOAM 12. Method: De Simone, Kastner & Dogan (2021), Building Simulation 2021, Bruges, doi:10.26868/25222708.2021.30632.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case name (no spaces). Leave empty for an auto-generated name (same convention as Outdoor). | `Text` |
| Working Directory | Dir | Working directory (default ~/Eddy3D/Indoor). | `Text` |
| Room | R | Closed room Brep. | `Brep` |
| Cell Size | C | Mesh cell size (m). | `Number` |
| Inlets | I | Inlet surface(s): Brep or Indoor Inlet component(s). | `Generic Data` |
| Outlets | O | Outlet surface(s): Brep or Indoor Outlet component(s). | `Generic Data` |
| Inlet Speed | U | Fallback inlet speed (m/s) when raw Breps are used. Ignored when Indoor Inlet components provide velocity. | `Number` |
| Sinks | S | Momentum sinks (Indoor Sink). | `Generic Data` |
| Sources | Src | Emitters: Momentum / Heat / CO2 / Viral Source components. | `Generic Data` |
| Wall Temp | WT | Optional wall temperature (K) for the transported temperature field (needs a Heat Source). | `Number` |
| Walls | W | Optional Indoor Wall components with a Surface: each gets its own patch and temperature. Room faces not covered by one keep the case-wide Wall Temp. | `Generic Data` |
| Age of Air | AoA | Solve the mean age of air (OpenFOAM 'age' function object) during the run. Age [s] is the time since the air at each point entered the room — the ventilation map: low = well flushed, high = trapped in a corner the supply never reaches. Unlike an air-change rate, which is one number for the whole room, it says WHERE the ventilation fails. Adds a cheap scalar transport solved at each write; probe the 'age' field to read it. Optional; default is off. | `Boolean` |
| Extras |  | Optional user additions from the Refinement Region and Custom Function Object components. Applied every time the case is written, so they survive a re-write. The indoor mesh dict is built programmatically and has no refinementRegions block of its own — one is created for a user region. | `Generic Data` |
| Write | W | Click to write the case to disk. Resets automatically so it never re-writes on recompute. | `Boolean` |
| Clear | X | Click to delete the case folder. Resets automatically so it never re-deletes on recompute. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | The indoor case (for the Run component). | `Generic Data` |
| Logs | L | Build / write logs. | `Text` |