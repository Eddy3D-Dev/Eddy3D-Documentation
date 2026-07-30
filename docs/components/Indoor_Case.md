# ![](/images/icons/Indoor_Case.png) Indoor Case - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Case%22)

![](/images/components/Indoor_Case-crop.png)

Build an isothermal indoor ventilation case (room + inlets + outlets + sinks) for OpenFOAM 12.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case Name | Name | Case name (no spaces). | `Text` |
| Working Directory | Dir | Working directory (default ~/Eddy3D/Indoor). | `Text` |
| Room | R | Closed room Brep. | `Brep` |
| Cell Size | C | Mesh cell size (m). | `Number` |
| Inlets | I | Inlet surface(s): Brep or Indoor Inlet component(s). | `Generic Data` |
| Outlets | O | Outlet surface(s): Brep or Indoor Outlet component(s). | `Generic Data` |
| Inlet Speed | U | Fallback inlet speed (m/s) when raw Breps are used. Ignored when Indoor Inlet components provide velocity. | `Number` |
| Sinks | S | Momentum sinks (Indoor Sink). | `Generic Data` |
| Sources | Src | Emitters: Momentum / Heat / CO2 / Viral Source components. | `Generic Data` |
| Wall Temp | WT | Optional wall temperature (K) for the transported temperature field (needs a Heat Source). | `Number` |
| Write | W | Click to write the case to disk. Resets automatically so it never re-writes on recompute. | `Boolean` |
| Clear | X | Click to delete the case folder. Resets automatically so it never re-deletes on recompute. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case | C | The indoor case (for the Run component). | `Generic Data` |
| Logs | L | Build / write logs. | `Text` |