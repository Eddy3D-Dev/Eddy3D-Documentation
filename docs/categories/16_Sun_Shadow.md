{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="16_Sun_Shadow"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 16 Sun Shadow
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Sun_Vectors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Vectors.png" class="nav-gh-icon"> Sun Vectors
            </div>
            <div class="index-quicklink-text">Builds a set of sun positions for a date-and-hour window at a chosen time step (6 minutes and finer), computed from site and clock rather than read from an EPW's hourly rows. Feeds Sun Path; the Sun Hours, Shadow and Solar Irradiation analysis components read a weather record directly and no longer need this wired in.</div>
        </div>
    </a>
    <a href="/components/Sun_Path/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Path.png" class="nav-gh-icon"> Sun Path
            </div>
            <div class="index-quicklink-text">Draws the sun's daily arcs, hourly analemmas and sampled sun positions as curves and points on a dome — pure geometry built from the same solar calculation the sun studies use, with no new physics. It exists to let a wrong north, a southern-hemisphere sign error, or an off-by-one time zone show up visually instead of hiding in a table of numbers.</div>
        </div>
    </a>
    <a href="/components/Sun_Stats/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Stats.png" class="nav-gh-icon"> Sun Stats
            </div>
            <div class="index-quicklink-text">Area-weighted min/mean/median/max over a per-point sun result, plus the area and fraction reaching a threshold. Weighting matters: an analysis grid trimmed to a site boundary is rarely uniform, and averaging the points instead of the area over-counts wherever the grid is dense — silently, because the answer still looks plausible.</div>
        </div>
    </a>
    <a href="/components/Shadow/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Shadow.png" class="nav-gh-icon"> Shadow
            </div>
            <div class="index-quicklink-text">Lit or shaded at each analysis point for one or more sun instants, by ray casting against the context — the shadow's position at a moment, not Sun Hours' accumulation over a period. It shares Sun Hours' solver, so a point counted lit here is exactly one Sun Hours would credit for that same sample.</div>
        </div>
    </a>
    <a href="/components/Solar_Irradiation/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Solar_Irradiation.png" class="nav-gh-icon"> Solar Irradiation
            </div>
            <div class="index-quicklink-text">Cumulative incident solar energy at each point, in kWh/m² — beam plus an isotropic sky term plus a single-albedo ground reflection. An interactive preview, not a Radiance simulation: no interreflection, no material response, no spectral detail, so use MRT/UTCI when the number has to be defensible and this component to compare orientations while the design is still moving.</div>
        </div>
    </a>
    <a href="/components/Sunlight_Compliance/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sunlight_Compliance.png" class="nav-gh-icon"> Sunlight Compliance
            </div>
            <div class="index-quicklink-text">EN 17037 sunlight exposure and BRE amenity overshadowing / APSH, evaluated against a Sun Hours result. A design aid, not a certified daylight and sunlight report — the thresholds are secondary-sourced (surveyors' summaries, not the standards themselves) and exposed as inputs precisely so they can be corrected once someone has the standards to hand.</div>
        </div>
    </a>
    <a href="/components/Canopy/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Canopy.png" class="nav-gh-icon"> Canopy
            </div>
            <div class="index-quicklink-text">Vegetation that dims the sun rather than blocking it — a crown passes part of the beam, and can optionally lose that effect outside its leaf season. Wire its Canopy output into the Canopy input of Sun Hours or Solar Irradiation; putting the same geometry in a study's plain Context socket instead makes it fully opaque year-round, with no seasonal or partial-transmittance behavior.</div>
        </div>
    </a>
    <a href="/components/Facade_Grid/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Facade_Grid.png" class="nav-gh-icon"> Facade Grid
            </div>
            <div class="index-quicklink-text">Grids surfaces into analysis points with outward normals and per-cell areas, at a spacing suited to a single building rather than a district. Normals come from mesh face winding after Rhino's `UnifyNormals` — consistent across the mesh, but not provably outward for an open surface, which is why the Flip input exists.</div>
        </div>
    </a>
</div>
