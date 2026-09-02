# ![](/images/icons/Custom_Function_Object.png) Custom Function Object - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Custom%20Function%20Object%22)

![](/images/components/Custom_Function_Object-crop.png)

Define a custom OpenFOAM function object the solver runs at runtime — fieldAverage, yPlus, wallShearStress, forces, surfaceFieldValue, a coded FO, etc. Wire Extras into a case component so it is written every time the case is written; or wire a written Case in and press Apply to edit controlDict in place (which a later re-write undoes).

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Case |  | Optional. An already-written case to edit in place — any Eddy3D OpenFOAM case (wind, Outdoor+ microclimate, indoor, CHT) or a loaded study. Leave it empty and wire the Extras output into the case component instead, which is the durable route: a function object applied here is erased the next time the case is written. | `Generic Data` |
| Name |  | Function object key (a valid OpenFOAM word, e.g. "fieldAverage1"). | `Text` |
| Definition | Def | The function object body — the contents between its braces, as text (from a panel) or a Foamonary. Example:   type            fieldAverage;   libs            ("libfieldFunctionObjects.so");   fields          ( U p ); The component wraps it as Name { ... } inside controlDict functions. | `Generic Data` |
| Region |  | Optional OpenFOAM region for a MULTI-region solver (Outdoor+ microclimate: air, buildings, vegetation, terrain; CHT: one per solid/cavity). Those solvers scope every function object by region and nest its output under postProcessing/<region>/, so an unscoped one never runs. Leave empty for single-region cases (wind, indoor). | `Text` |
| Bake | Apply | Write the function object into the wired Case's already-written controlDict (idempotent). Momentary button. Not needed for the Extras route, which writes it with the case. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Status |  | What was written, and where. | `Text` |
| Extras |  | The function object as case data. Wire this into a case component's Extras input so it is written into controlDict every time the case is written — including after a re-write, which is what editing controlDict in place cannot survive. | `Generic Data` |