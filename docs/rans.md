# Wind CFD: the RANS approach

The **02 | Outdoor** workflow (Atmospheric Boundary Layer → Outdoor Case → Run → Probe) solves
pedestrian-level wind with **steady Reynolds-averaged Navier–Stokes (RANS)** in
[OpenFOAM 12](https://openfoam.org/). Eddy3D writes the case — geometry, mesh controls, boundary
conditions, turbulence model, numerics — and OpenFOAM solves it. The physics is OpenFOAM's; this
page explains what Eddy3D chooses on your behalf, what you can change, and where the approach
stops being trustworthy.

!!! warning "Install the engine before you run"
    Nothing on this page solves until an OpenFOAM engine is installed. Open **Eddy3D Setup**
    (ribbon `00 | Setup`, or the standalone installer) and install the row
    **(U)RANS CFD (OpenFOAM)**. It offers three routes:

    - **Containerized** — macOS and Windows, through Podman (preferred) or Docker. Pulls a
      digest-pinned OpenFOAM 12 image; needs the *Container runtime (Podman · Docker)* row first.
    - **BlueCFD** — Windows, native. Parallel runs also need a 64-bit MS-MPI; Eddy3D refuses a
      parallel blueCFD launch without one and says so.
    - **WSL** — Windows, OpenFOAM inside a Linux distribution.

    The engine is chosen on **Outdoor Case**. Every template's description names the Setup row it
    needs under *Needs*.

## When steady RANS is the right tool

Eddy3D offers several ways to get a wind field. Steady RANS is the workhorse: it gives the
**time-averaged** flow around buildings at a cost a design team can afford for 8–16 wind
directions.

| Question | Use | Engine |
|---|---|---|
| Mean wind speed, wind comfort classes, facade Cp, mean pollutant concentration | **Steady RANS** (this page) | OpenFOAM, 02 \| Outdoor |
| Mean flow where the wake sheds periodically, or a time-averaged field you trust more than one steady solve | **URANS** — same components, Run Settings → Solver Algorithm `PIMPLE` | OpenFOAM, 02 \| Outdoor |
| Gusts, peak loads, turbulence statistics resolved in time | **Large-eddy simulation** on a lattice-Boltzmann solver | OpenLB or FluidX3D, 11 \| LBM |
| Air temperature, humidity and surface heat exchange coupled with the flow | **Coupled microclimate** | urbanMicroclimateFoam, 03 \| Outdoor+ |
| A first look in seconds, before any CFD | **Machine-learning screening** — never a substitute for CFD | Wind Predictor, 12 \| ML |

## The model Eddy3D writes

### Equations

OpenFOAM's `incompressibleFluid` solver module solves the steady, incompressible RANS equations
with an eddy-viscosity closure:

```
∇·U = 0
∇·(U U) = −∇p + ∇·[(ν + ν_t)(∇U + ∇Uᵀ)]
```

`U` is the mean velocity, `p` the kinematic pressure, `ν` the molecular and `ν_t` the turbulent
(eddy) viscosity, which the turbulence model supplies. Pressure–velocity coupling is **SIMPLE**.
Whether the run is steady or transient is decided by the time-derivative scheme, which Run
Settings writes for you (see [Transient runs](#transient-runs-urans)).

### Turbulence models

Run Settings → **Turbulence Model**. All four are OpenFOAM 12 RAS models.

| Model | Notes |
|---|---|
| **Realizable k-ε** (default) | Shih et al. 1995. The AIJ and COST 732 recommendation for pedestrian-level wind; robust on coarse urban meshes, and over-predicts turbulence at stagnation points less than standard k-ε. |
| Standard k-ε | Launder & Spalding 1974. Cheapest and most tolerant; over-produces turbulence at building corners and under-predicts recirculation. |
| RNG k-ε | Yakhot et al. 1992. Better in separated and swirling flow at the same cost. |
| SST k-ω | Menter 1994. Best near-wall behaviour, needs a finer mesh near walls. **In OpenFOAM 12 its ω inlet is uniform**, not a boundary-layer profile, so the approaching flow loses most of its turbulence before it reaches the buildings. Mean velocities stay good; anything driven by inflow turbulence (dispersion, gust estimates) does not. Prefer a k-ε model unless you need SST specifically. |

### The atmospheric boundary layer (inflow)

The **Atmospheric Boundary Layer** component sets the inlet as the equilibrium neutral boundary
layer of Richards & Hoxey (1993), which OpenFOAM's `atmBoundaryLayer` conditions implement:

```
u*        = κ · U_ref / ln((Z_ref + z0) / z0)
U(z)      = (u* / κ) · ln((z − z_g + z0) / z0)
k         = u*² / √C_μ                          (constant with height)
ε(z)      = u*³ / (κ · (z − z_g + z0))
κ = 0.41,  C_μ = 0.09
```

- **U_ref at Z_ref** — the reference speed and its height (default 10 m).
- **z0** — aerodynamic roughness length of the terrain upstream. One value, or one per wind
  direction (`z0 per Direction`), for example from **Land Cover Roughness**, which derives z0 from
  OpenStreetMap land cover over the upstream fetch.
- **Station versus site.** A weather station measures at 10 m over open terrain. Feeding that speed
  straight into an urban profile tells the model the urban 10 m wind equals the open-country one,
  which overstates pedestrian wind by up to about 2×. **Wind Conditions** (with `Site Terrain` set)
  applies the EN 1991-1-4 §4.3 terrain transfer (×0.54 for category IV, ×0.84 for III), and
  Velocity Amplification Factors applies the same factor to the hourly series. The default is
  "None": no transfer.

### Boundary conditions

| Patch | Velocity | Pressure | Turbulence |
|---|---|---|---|
| Inlet | ABL log profile (`atmBoundaryLayerInletVelocity`) | zero gradient | ABL k and ε |
| Outlet | `inletOutlet` | fixed 0 | `inletOutlet` |
| Top and sides | `slip` | `slip` | `slip` |
| Ground | no slip | zero gradient | rough wall function `nutkAtmRoughWallFunction` with the same z0 as the inlet |
| Buildings | no slip | zero gradient | `nutUSpaldingWallFunction` |

Using the inlet's z0 on the ground keeps the approaching profile from changing along the empty
fetch, the "horizontal homogeneity" condition. Check it with the **ABL_Verification** template:
some decay is normal, a profile that changes shape completely is not.

### Domain

Two shapes, both on **Outdoor Case**:

- **Box Domain.** Automatic extents follow COST 732 best practice: 5 H upstream, 15 H downstream
  and 5 H to the sides and top (H = tallest building). The inlet is one fixed face, so an
  8-direction study builds and meshes one rotated box per direction.
- **Cylinder Domain.** One mesh serves every direction. The side wall is split into segments, and
  each direction decides which segments are inlet and which are outlet (Kastner & Dogan 2020). An
  8-direction study meshes once instead of eight times. Each direction is still solved from
  scratch.

Outdoor Case checks the **frontal blockage** against the 3 % limit of the ASCE/SEI CWE
Prestandard. Model the surrounding buildings within about 240 m of the study area before
trusting results near the edge of the context.

### Mesh

`blockMesh` writes a uniform background mesh and `snappyHexMesh` refines it towards buildings,
terrain and any refinement regions. Each refinement level halves the cell size and costs about
eight times the cells in that region. **Cell Size** shows the size each level actually produces
(for example `L3 · 1.25 m`), and the Wind Study banner estimates the cell count *as a range*
before you mesh, because a single number would claim more precision than the estimate has.
**Height Bands** refines by height above ground without any geometry: finest near pedestrian
level, coarser above.

### Numerics

Run Settings → **Numerics** is a point on a triangle with three corners: **Accuracy**, **Robustness**
and **Speed**. The default sits towards Robustness. It sets the convection schemes,
under-relaxation, corrector counts and linear-solver tolerances together. A few other controls
matter on their own:

- **Warm-up Iterations** — run the first iterations with first-order upwind and heavy relaxation,
  then switch to the chosen numerics. The default (−1) picks this from the numerics point.
- **Potential Flow** — initialise velocity and pressure with a quick `potentialFoam` solve instead
  of a uniform field. Measured on test cases, this and other "better initial fields" do **not**
  reliably converge faster; the effect changes sign between cases.
- **Velocity cap** — every wind case carries an `fvConstraints` limit of |U| ≤ 100 m/s. It keeps a
  diverging start finite and logs when it bites. A run whose maximum |U| sits at the cap has
  diverged; it has not converged.
- The pressure equation always uses the GAMG solver; the Laplacian scheme defaults to
  `limited 0.5`.

### Convergence

- **Convergence** (default 1e-4) stops the run once the initial residuals of **p, U and k** (plus
  **ω** for SST) are all below the tolerance. **ε is never in that list.** Its residual stalls
  around 10⁻² even when the field has settled, because of how the wall functions fix ε next to
  walls, so it would hold every k-ε run to the iteration limit.
- **Auto-stop on plateau** ends a run cleanly once every residual has been flat for about 100
  iterations. Some wind directions, often the oblique ones, settle into a small limit cycle
  instead of converging; their residuals never reach the tolerance however long they run.
- **Live Residuals** shows the run's progress, rate and estimated time to finish. Field
  monitors (default on) also log the domain's maximum |U| every iteration. This is the earliest
  sign of a cold-start overshoot.
- Flat residuals are not proof of a settled field. Eddy3D tests the residual history for
  stationarity (the KPSS test) and can run a grid-convergence study (Roache GCI) through the
  foamgci toolkit.

## Transient runs (URANS)

Choose **PIMPLE** as Solver Algorithm on Run Settings to make the same case transient. The controls
change meaning: you set **Duration** and **Time Step** in seconds, a **Max Courant** number, and an
**Averaging Window** for the time-averaged fields. Iteration counts, the residual stop and the
plateau stop do not apply to a transient run and are not written. The component says so on the
canvas, because treating 1000 iterations as 1000 seconds would give a wrong answer that looks
right.

## From a solved case to results

- **Probe** samples velocity (or any field: Cp, a pollutant, TKE) at points, usually a grid about
  1.5–2 m above ground. **Wind Field Viewer** and **Streamlines** draw it.
- **Velocity Amplification Factors** turns each direction's U / U_ref into an hourly field by
  scaling with the weather file's hourly speed and direction. This is the annual wind every
  comfort assessment reads. Its optional TKE input gives a gust estimate for gust-referenced
  criteria.
- **Wind Comfort** classifies that annual field against Lawson, Davenport, NEN 8100 or Wellington
  criteria, for the year, a season or a month.
- With **Pressure Coefficient** on, Run Settings writes facade Cp. Airflow Network Cp exports it
  to EnergyPlus.

## Validation

Eddy3D checks that the cases it *writes* let OpenFOAM reproduce measured data. The benchmarks run
through the same case writer as the canvas. Headline results (2026-09-27, OpenFOAM 12; the full
tables and their caveats are in the repository's
[VALIDATION.md](https://github.com/Eddy3D-Dev/Eddy3D/blob/dev/docs/VALIDATION.md)):

| Benchmark | Result |
|---|---|
| AIJ Case I — surface-mounted cube, three closures | Velocity hit rate q 0.77–0.81, correlation R ≥ 0.99 for every closure; SST loses its inflow turbulence (see above) |
| CODASC street canyon, wind perpendicular to the street | Concentration FAC2 0.90–0.96, \|FB\| ≤ 0.21 on 1400 points; the leeward-wall profile is too flat |
| AIJ Case H — 1:1:2 building, point source | Outer flow right (q 0.91 above the roof); the wake is 1.9× too long and peak concentrations 2.6–4.3× too high |
| CEDVAL A1-5 — isolated block | Recirculation length 3.26 H |

These are typical RANS strengths and weaknesses. Mean speeds away from the wake are reliable;
wake lengths and concentrations in the wake are not.

## Limitations

- **Steady RANS gives the mean, not the gust.** Gust-referenced criteria rely on a gust *estimate*
  from the modelled turbulence, not on resolved gusts. For peak values use LES (`11 | LBM`).
- **Wakes are typically too long and recirculation too weak** with k-ε closures. Results directly
  behind buildings deserve the least trust.
- **Not every direction converges to a tolerance.** Some, especially oblique ones, end in a limit
  cycle. Check the residuals and the field monitors before reading a direction's result.
- **This is not a structural-load tool.** Eddy3D results are for pedestrian comfort, ventilation and
  dispersion screening. They do not demonstrate compliance with a wind-load standard.
- **The physics belongs to OpenFOAM.** Cite OpenFOAM, the turbulence model, and the Eddy3D method
  papers you relied on (see [Methods & Citations](methods.md)).

## References

- Richards, P. J., & Hoxey, R. P. (1993). Appropriate boundary conditions for computational wind
  engineering models using the k-ε turbulence model. *Journal of Wind Engineering and Industrial
  Aerodynamics*, 46–47, 145–153.
- Franke, J., Hellsten, A., Schlünzen, H., & Carissimo, B. (Eds.) (2007). *Best practice guideline
  for the CFD simulation of flows in the urban environment*. COST Action 732.
- Tominaga, Y., et al. (2008). AIJ guidelines for practical applications of CFD to pedestrian wind
  environment around buildings. *Journal of Wind Engineering and Industrial Aerodynamics*, 96,
  1749–1761.
- Shih, T.-H., et al. (1995). A new k-ε eddy viscosity model for high Reynolds number turbulent
  flows. *Computers & Fluids*, 24(3), 227–238.
- Launder, B. E., & Spalding, D. B. (1974). The numerical computation of turbulent flows.
  *Computer Methods in Applied Mechanics and Engineering*, 3(2), 269–289.
- Yakhot, V., et al. (1992). Development of turbulence models for shear flows by a double expansion
  technique. *Physics of Fluids A*, 4(7), 1510–1520.
- Menter, F. R. (1994). Two-equation eddy-viscosity turbulence models for engineering
  applications. *AIAA Journal*, 32(8), 1598–1605.
- EN 1991-1-4:2005+A1:2010, *Eurocode 1: Actions on structures — Part 1-4: Wind actions*.
- ASCE/SEI, *Prestandard for Computational Wind Engineering*.
- Kastner, P., & Dogan, T. (2020). A cylindrical meshing methodology for annual urban computational
  fluid dynamics simulations. *Journal of Building Performance Simulation*, 13(1), 59–68.
