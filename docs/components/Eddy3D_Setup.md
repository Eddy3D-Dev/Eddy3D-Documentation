# ![](/images/icons/Eddy3D_Setup.png) Eddy3D Setup - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Eddy3D%20Setup%22)

Opens a separate setup window reporting, per simulation capability, what it needs and what is missing on this machine, with instructions to install it. It replaces the two old Install Engines components, which stay hidden on the ribbon (not removed) so documents that still use them keep opening.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Open | O | Opens the setup window. Momentary — the component resets this toggle itself right after showing the window, so it behaves like a button rather than a persistent switch. | `Boolean` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Status | St | What the setup surface reports: the registered catalog's capability count when idle or after opening, or why the window could not open. | `Text` |

#### Notes

- Open is a momentary toggle, not a state: `Solve` calls `ResetToggle("Open")` right after showing the window, since the window then owns its own lifetime and a toggle left on would try to re-show it every recompute.
- Opening calls `Eddy3DSetupForm.ShowSetup()` — a window outside the Grasshopper canvas, not a canvas-drawn output. If it throws, the component posts a canvas Error and Status echoes the same message.
- The window's content comes from a capability catalog registered when the Radiance plugin loads. If that hasn't happened yet, Open does nothing useful: the component posts a Warning and Status explains that the Eddy3D plugins may not have finished loading, suggesting a Rhino restart.
