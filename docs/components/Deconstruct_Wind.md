# ![](/images/icons/Deconstruct_Wind.png) Deconstruct Wind - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Deconstruct%20Wind%22)

Unpacks an annual wind field — the VAF component's Wind Speed or Annual VAF output, probes × 8760 hours carried as one item — into probe-specific Mean/Min/Max statistics, per-hour raw values for an explicit HOY selection, a colored probe mesh, and the value range that mesh was colored over. It exists specifically to avoid ever materializing the full annual tree: with HOY left unconnected, only the three reduced statistics and the mesh get computed, not 8760 branches of values. It does not draw a legend itself — wire Range into the Wind Legend component, which owns that.

#### Input

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Wind Field | W | Annual field object from the VAF component — its Wind Speed output (m/s) or its Annual VAF output (dimensionless factors). One item, probes × hours. | `Generic` |
| HOY | HOY | Hour(s) of year (1-8760) to restrict to. Leave unconnected for the whole year; statistics are then reduced over exactly these hours, so a July-afternoon list gives July-afternoon wind with no re-solve needed. | `Integer` |
| Statistic | Stat | Value used to color the probe mesh and scale the Range output: the Mean, Min or Max of each probe's series over the selected hours. Defaults to Mean. | `Text` |
| Radius | Radius | Half-width of each colored square centered on a probe point. Defaults to 0.75. | `Number` |

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Mean | Avg | Mean value per probe over the selected hours — the annual average when HOY is unconnected. | `Number` |
| Min | Min | Lowest value per probe over the selected hours. | `Number` |
| Max | Max | Highest value per probe over the selected hours. | `Number` |
| Values | V | The field at each selected hour — one branch per HOY, each holding every probe's value. Populated only when HOY is connected; with HOY unconnected this would be the entire year, which is the tree this component exists to avoid. | `Number` |
| Points | P | Probe positions carried inside the field (the VAF component's Points input). | `Point` |
| Mesh | Mesh | Colored probe mesh for the selected statistic. Requires the field to carry probe positions (wire Points into the VAF component). | `Mesh` |
| Range | Range | Minimum and maximum of the selected statistic — the range the Mesh was colored over. Wire it into the Wind Legend component's Range input so the legend labels exactly the scale this mesh uses. | `Interval` |

#### Notes

- **Statistic** renders as an on-canvas dropdown (Mean / Min / Max), not a plain text box. It only changes which series colors the Mesh and sets Range — Mean, Min and Max are always all computed and output regardless of this setting.
- **One Wind Field per solve.** If more than one item reaches Wind Field, Grasshopper iterates the component once per item; from the second iteration on it raises a Runtime Error asking you to connect a single field or graft deliberately, and that iteration produces no outputs.
- HOY values outside 1-8760, or past the hours the field actually holds, are clamped into range with a Runtime Warning rather than failing outright.
- **Points and Mesh stay empty** if the field's probe positions were never carried through — i.e. the VAF component's own Points input was left unwired — with a Remark explaining why.
- Asking for a lot of hours over a lot of probes (Values exceeding 2,000,000 raw numbers) triggers a Remark that the raw output itself, not the underlying solve, is now the slow part; narrowing HOY or reading the Mean/Min/Max statistics avoids materializing that tree.
- An empty field (no probes or no hours) is reported with a Runtime Warning and produces no outputs.
