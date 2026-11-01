# Outdoor+ Solver Troubleshooting

Field notes for runs of the Outdoor+ (`urbanMicroclimateFoam`) case that mesh fine but stop during the
solve. For installation problems see [Setup Troubleshooting](setup_troubleshooting.md); for the workflow
itself see [First Steps](first_steps.md).

## Where to look first

Everything the solver prints lands in the case folder (the *Working Directory* of the **Outdoor+ Case**
component, one sub-folder per case name):

- the solve log — the last `Solving for solid region <name>` line before the error tells you **which
  region** diverged (`buildings`, `terrain`, or a vegetation region);
- `checkMesh_<region>.txt` — one per meshed region, written at the end of meshing;
- the `*_dump` fields (`Ts_dump`, `pc_dump`, `ws_dump`, `Crel_dump`) written into the last time folder when
  the solid solver gives up — load them in ParaView to see *where* the field ran away.

## `This is going to crash (Ts)!` … `Cannot decrease time step further`

The solid regions (buildings, terrain) are solved with an adaptive sub-time-step inside each hourly
fluid step. After every solid iteration the solver checks that the solid temperature `Ts` stays within
0 K < Ts < 423.15 K (150 °C) and that the capillary pressure `pc` stays negative. If not, it prints
`This is going to crash (Ts)!` (or `(pc)!`), reverts the fields, halves the time step and retries.
When the time step reaches `minDeltaT` (default 1 s) it aborts with `Cannot decrease time step further`.

The message says nothing about the cause. In practice it is one of the following, in this order of
likelihood:

### 1. A light hygroscopic wall material

Materials with a moisture model and a very low density/conductivity — `CalciumSilicate` (ρ 270 kg/m³,
λ 0.06 W/mK) and `Hamstad5Insulation` (ρ 130) — diverge in the coupled heat-and-moisture solve as soon
as the air field has converged and the surface starts receiving solar radiation. Typical signature: the
run survives the first one or two hours and dies around sunrise.

!!! warning "Integer-wired Material inputs"
    The *Material* input of **Building Material**, **Terrain Surface Material** and **Soil Material**
    expects a material **name**. Older documents wire a *Number Slider* into it; the plugin then
    resolves the number by **position** in the dropdown list, so slider `1` silently means
    `CalciumSilicate`. Prefer the dropdown (right-click the input) or a panel with the name.

| index | name | ρ (kg/m³) | λ (W/mK) | moisture model |
|---|---|---|---|---|
| 0 | AsphaltConcrete | 2100 | 0.75 | yes |
| 1 | CalciumSilicate | 270 | 0.06 | yes, strongly hygroscopic |
| 2 | Hamstad5Brick | 1600 | 0.68 | yes (plugin default) |
| 3 | Hamstad5Insulation | 130 | 0.04 | yes, strongly hygroscopic |
| 4 | Hamstad5Mortar | 1900 | 0.82 | yes |
| 5 | HamstadBrick | 2005 | 0.5 | yes |
| 6 | HamstadCase2 | 1600 | 0.68 | yes |
| 7 | HamstadConcrete | 2400 | 1.6 | yes |
| 8 | HamstadPlaster | 790 | 0.2 | yes |
| 9 | Impermeable | 2400 | 1.0 | **none** — heat conduction and storage only |
| 10 | PorousAsphalt | 2000 | 0.7 | yes |
| 11 | SabaBrick | 1608 | 0.73 | yes |
| 12 | SabaBrickMod | 1608 | 0.73 | yes |
| 13 | Savonnieres (buildings) / Soil (terrain) | 1830 / 1150 | 1.2 / 1.5 | yes |
| 14 | Soil (buildings) / VanGenuchten (terrain) | 1150 / 1500 | 1.5 / 1.0 | yes |

**Remedy:** use `Impermeable` for both wall layers (stable, models heat storage and conduction, no
moisture in the wall), or a heavy hygroscopic material such as `Hamstad5Brick` or `HamstadConcrete`.
To bisect, set *every* material (walls, terrain surface, soil) to `Impermeable` once; if that run
finishes, bring the moisture models back one region at a time.

### 2. Inverted cells from the wall extrusion

The solid buildings and terrain are made by extruding the surface **inwards** (two layers, 0.1 m each by
default, 10 cells per layer at expansion ratio 1.2). Wherever the surface has a feature narrower than
roughly twice the wall thickness — a 20 cm ledge, a fin, a thin parapet, sliver triangles between
unwelded faces — the offset prisms cross and `checkMesh_buildings.txt` reports **negative cell
volumes**. The solver then fails on the very first solid step, at `t` of a few seconds, with the same
message as above.

The plugin reads the `checkMesh` logs and raises a warning on **Run** when it finds negative volumes
(since 1.14). Remedy: remove or thicken the thin features in Rhino, pass the façades through **Gmsh
Mesh**, and re-mesh.

!!! note "Small determinants are expected"
    `checkMesh -allGeometry` always reports many cells with *small determinant (< 0.001)* in the
    building and terrain regions. The thinnest extruded cell is about 4 mm thick under a face that is
    1–3 m wide; that aspect ratio gives tiny determinants by construction and does **not** affect the
    one-dimensional conduction through the wall. Only *negative volumes*, *incorrectly oriented faces*
    or *severely non-orthogonal faces* in a solid region are a problem.

### 3. An air field that has not converged

The air region is solved to steady state inside every hourly step, from whatever field it has. The
first ~100 iterations of a cold start are a violent transient — the log shows `Min/max T:` pinned to
273.15 / 373.15 K and very large `|U|` — that has died out by iteration ~100 and converged by ~500.
*Max Fluid Iterations* below 300 freezes that transient into hour 1 and hands the solid regions a
garbage boundary condition. Keep it at 300 or more; 500–1000 for the first hour is cheap insurance.

### 4. Time-step controls

Only after the three points above: *Simulation Settings → Min Delta T* (default 1 s) can be lowered to
`0.1`, and *Initial Solid Time Step Factor* reduced, to give the solid solver more room. This delays a
material-driven divergence rather than curing it.

## `This is going to crash (pc)!`

Same mechanism, but the moisture equation overshoots `pc ≥ 0` (saturation). Seen with the `Soil` and
Hamstad models from a cold start; cases written by plugin 1.10 or later carry a floor on the moisture
capacity (`minCrel`) that removed it in all tested cases. If it still appears, switch the affected
region to `Impermeable` and report the case.

## Need help?

Open a thread in the [Eddy3D Discussions](https://github.com/orgs/Eddy3D-Dev/discussions){ target="_blank" rel="noopener noreferrer" aria-label="Eddy3D Discussions (opens in a new tab)" }
and attach the `.gh`, the tail of the solve log (from the last `Solving for solid region` line) and
the `checkMesh_*.txt` files.
