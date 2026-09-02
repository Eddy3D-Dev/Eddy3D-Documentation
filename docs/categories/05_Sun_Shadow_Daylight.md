{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="05_Sun_Shadow_Daylight"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 05 Sun Shadow Daylight
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Canopy/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Canopy.png" class="nav-gh-icon"> Canopy
            </div>
            <div class="index-quicklink-text">Vegetation that attenuates the sun instead of blocking it, with an optional leaf-on/leaf-off season. Feed the Canopy input of Sun Hours or Solar Irradiation.</div>
        </div>
    </a>
    <a href="/components/Facade_Grid/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Facade_Grid.png" class="nav-gh-icon"> Facade Grid
            </div>
            <div class="index-quicklink-text">Analysis points with outward normals and per-cell areas over surfaces, at a spacing suited to a building rather than a district.</div>
        </div>
    </a>
    <a href="/components/Sun_Path/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Path.png" class="nav-gh-icon"> Sun Path
            </div>
            <div class="index-quicklink-text">Daily sun arcs, analemmas and sun positions as curves and points — north-aware, drawn from the same solar geometry the sun studies use.</div>
        </div>
    </a>
    <a href="/components/Sun_Vectors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Vectors.png" class="nav-gh-icon"> Sun Vectors
            </div>
            <div class="index-quicklink-text">Sun positions for a period at a chosen time step (6-minute and finer), from site and clock rather than from an EPW's hourly rows.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_Shadow/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Shadow.png" class="nav-gh-icon"> Deconstruct Shadow
            </div>
            <div class="index-quicklink-text">Per-point sun exposure (and, for an explicit HOY selection, the per-instant trees) from a Shadow Result — without putting a whole year of lit flags on the canvas.</div>
        </div>
    </a>
    <a href="/components/Shadow/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Shadow.png" class="nav-gh-icon"> Shadow
            </div>
            <div class="index-quicklink-text">Lit or shaded at each analysis point for one or more sun instants — the shadow's position, not accumulated sun hours.</div>
        </div>
    </a>
    <a href="/components/Sun_Hours/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Hours.png" class="nav-gh-icon"> Sun Hours
            </div>
            <div class="index-quicklink-text">Direct sun hours and shadow by ray casting — an interactive preview, not a Radiance simulation.</div>
        </div>
    </a>
    <a href="/components/Daily_Light_Integral/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Daily_Light_Integral.png" class="nav-gh-icon"> Daily Light Integral
            </div>
            <div class="index-quicklink-text">Daily Light Integral per point in mol/m²/day — the photosynthetically active photons (400-700 nm) landing on each point per day, averaged over the analysed period.  Shares Solar Irradiation's geometry: beam plus isotropic sky plus a ground term, no interreflection. The ground albedo here is a PAR albedo and is much lower than the broadband one. Vegetation is deliberately not accepted — see the Canopy note in the docs.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_DLI/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_DLI.png" class="nav-gh-icon"> Deconstruct DLI
            </div>
            <div class="index-quicklink-text">Per-point daily light integral — period mean and worst month — and, for an explicit Month selection, the per-month tree, from a Daily Light Integral Result.</div>
        </div>
    </a>
    <a href="/components/Solar_Irradiation/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Solar_Irradiation.png" class="nav-gh-icon"> Solar Irradiation
            </div>
            <div class="index-quicklink-text">Cumulative incident solar energy per point in kWh/m² — beam plus isotropic sky plus ground reflection. An interactive preview, not a Radiance simulation.</div>
        </div>
    </a>
    <a href="/components/Annual_Daylight/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Annual_Daylight.png" class="nav-gh-icon"> Annual Daylight
            </div>
            <div class="index-quicklink-text">Climate-based annual daylight metrics from Radiance annual illuminance matrices:    sDA  spatial daylight autonomy — fraction of the grid daylit for at least half the occupied hours (LM-83 default sDA300/50%)   ASE  annual sunlight exposure — fraction of the grid seeing direct sun for more than 250 occupied hours (a glare proxy; LOWER is better)   UDI  useful daylight illuminance — fraction of occupied hours inside a useful band  ASE needs the DIRECT matrix. Without it, ASE is reported as zero and the Report says so — the total matrix would count bright overcast sky as glare.</div>
        </div>
    </a>
    <a href="/components/Daylight_Factor/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Daylight_Factor.png" class="nav-gh-icon"> Daylight Factor
            </div>
            <div class="index-quicklink-text">Daylight factor: interior illuminance under the CIE standard overcast sky as a percentage of the simultaneous unobstructed exterior horizontal illuminance.  Feed it the illuminance at each sensor and the exterior illuminance the sky was built for. The ratio is invariant to sky brightness, so the absolute value only has to MATCH the one used for the render — it does not have to be any particular number.</div>
        </div>
    </a>
    <a href="/components/Vertical_Sky_Component/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vertical_Sky_Component.png" class="nav-gh-icon"> Vertical Sky Component
            </div>
            <div class="index-quicklink-text">Vertical Sky Component per point, in percent: the diffuse illuminance a vertical plane receives directly from a CIE standard overcast sky, over the illuminance an unobstructed horizontal plane would receive under the same sky.  Geometry only — no weather, no orientation, no time of year. An unobstructed vertical plane reads 39.6%; BRE BR 209 reads 27% as the guideline for conventional window design.</div>
        </div>
    </a>
    <a href="/components/View_Target/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/View_Target.png" class="nav-gh-icon"> View Target
            </div>
            <div class="index-quicklink-text">Fraction of a target's surface each observer point can see — which seats see the park, which units see the water. The target is sampled by area; rays are blocked by the context and by the target's own body.</div>
        </div>
    </a>
    <a href="/components/Viewshed/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Viewshed.png" class="nav-gh-icon"> Viewshed
            </div>
            <div class="index-quicklink-text">Visual openness by ray casting: the unobstructed fraction of a view cone around each point's normal. A design-orientation tool for seats, windows and routes — how open does it FEEL here — not a daylight metric.</div>
        </div>
    </a>
    <a href="/components/Sun_Stats/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sun_Stats.png" class="nav-gh-icon"> Sun Stats
            </div>
            <div class="index-quicklink-text">Area-weighted min/mean/median/max over a sun result, plus the area and fraction reaching a threshold.</div>
        </div>
    </a>
    <a href="/components/Sunlight_Compliance/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sunlight_Compliance.png" class="nav-gh-icon"> Sunlight Compliance
            </div>
            <div class="index-quicklink-text">EN 17037 sunlight exposure and BRE amenity overshadowing / APSH against a sun-hours result. Design aid — thresholds are editable and not certified.</div>
        </div>
    </a>
</div>

