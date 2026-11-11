{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="09_Stormwater"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 09 Stormwater
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Design_Storm/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Design_Storm.png" class="nav-gh-icon"> Design Storm
            </div>
            <div class="index-quicklink-text">Builds a design-storm hyetograph from an IDF (Intensity-Duration-Frequency) curve, with an optional climate allowance. Feed it to Stormwater Run.  Give it EITHER the three coefficients of an i = a/(t+b)^c fit, OR a published depth-duration table (the form NOAA Atlas 14, KOSTRA and FEH actually distribute). The alternating-block and Chicago patterns reproduce the IDF depth at every sub-duration, which is what makes the result a design event rather than a shape.  Drainage Depth takes the share the piped drainage carries off the storm before it reaches the surface model: the total depth of the storm the sewers were designed for (2-year, 24-hour in the source study), removed in proportion from every block, after the climate allowance. It is a volume allowance, not a pipe network.  Method: Shrestha et al. (2026), Urban Systems Lab, urban-flood-modeling-workflows, https://github.com/UrbanSystemsLab/urban-flood-modeling-workflows.</div>
        </div>
    </a>
    <a href="/components/Land_Cover_Runoff/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Land_Cover_Runoff.png" class="nav-gh-icon"> Land Cover Runoff
            </div>
            <div class="index-quicklink-text">Fetches land-cover polygons around a lat/lon from OpenStreetMap (open data, no key) and classifies each into a Curve Number and an overland Manning's n.  This is the same Overpass query the Land Cover Roughness component makes, read for runoff instead of for wind — so wiring both on one site costs one fetch, not two. Unmapped tags are skipped rather than guessed at.</div>
        </div>
    </a>
    <a href="/components/Layer_Runoff/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Layer_Runoff.png" class="nav-gh-icon"> Layer Runoff
            </div>
            <div class="index-quicklink-text">Runoff zones from the ground layers a site model already has: wire LiDAR Site's Layer Outlines and Layer Kinds, and every outline becomes a zone with the Curve Number and overland Manning's n of what the ground there is (grass, park, forest, residential, paved…). The rain then falls on the same polygons the wind study's roughness and City Surface's layers were built from, with no second fetch.  A kind takes the hydrology of its typical OpenStreetMap tag, for the chosen soil group. Roads, paved areas and paths read as paved (CN 98). An outline whose name is not a ground kind (a roughness class such as roughly_open) is skipped and counted: wire Layer Kinds, not Layer Names. Put hand-drawn Runoff Zones after these to override them.</div>
        </div>
    </a>
    <a href="/components/Runoff_Zones/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Runoff_Zones.png" class="nav-gh-icon"> Runoff Zones
            </div>
            <div class="index-quicklink-text">Assigns a surface MATERIAL to an area of the site. The material's runoff coefficient is the share of the rain landing there that enters the surface flow, and it brings an overland Manning's n — change the material and both swap. Wire the zones into Stormwater Grid's Zones for the ground, or its Roof Zones for roofs; a zone with no Areas is the Default for every cell no other zone covers (or, as a roof zone, every roof).  Manning's n here is the OVERLAND FLOW value, several times the channel value for the same material — at the millimetre depths of sheet flow the surface texture is the whole channel, and using a channel roughness makes runoff arrive far too fast.  A Curve Number (1–100) replaces the coefficient with losses that grow through a storm as the ground wets up.  A Soil replaces both with Green-Ampt infiltration: all the rain reaches the ground and the soil takes water from whatever stands on it — run-on from upslope included, and ponds after the rain has stopped — at a rate that falls from unlimited toward the soil's saturated conductivity as it wets. Solved on the CPU.  Overland Manning's n after Engman (1986), J. Irrig. Drain. Eng. 112(1):39-53. Green-Ampt soil parameters as tabulated in the HEC-RAS 2D User's Manual, ported with the source study's workflow.  Method: DIN 1986-100:2016-12 (2016), DIN Media, Berlin Table 9, doi:10.31030/2586228; Green & Ampt (1911), Journal of Agricultural Science 4(1):1-24, doi:10.1017/S0021859600001441; Shrestha et al. (2026), Urban Systems Lab, urban-flood-modeling-workflows, https://github.com/UrbanSystemsLab/urban-flood-modeling-workflows.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_Stormwater/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Stormwater.png" class="nav-gh-icon"> Deconstruct Stormwater
            </div>
            <div class="index-quicklink-text">Turns a stormwater result into meshes and numbers. This is the ONLY component that materialises the field — a run holds millions of values and emitting them all as a tree would freeze the canvas, so ask here for the field and the time you want.</div>
        </div>
    </a>
    <a href="/components/Stormwater_Grid/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Stormwater_Grid.png" class="nav-gh-icon"> Stormwater Grid
            </div>
            <div class="index-quicklink-text">Rasterises the graded terrain into the DEM the solver runs on.  Buildings become no-flow WALLS rather than raised ground: raising them fabricates a ridge at the footprint edge that sheds water in whatever direction the rasterised edge happens to face, and lets water pond on roofs.  Breaklines are how a 1 m grid stays usable. A kerb, a swale invert or a threshold is sub-cell at 1 m and every one of them controls where the water goes — sampling the terrain at cell centres averages them away. Burning them along the cell path keeps the control without paying for a fine raster over the whole site.  Surfaces: Zones set the ground cells, Roof Zones the building footprints — a roof's material wins over whatever ground is drawn under it, and with "Roofs drain to grade" its runoff coefficient decides how much of the roof's rain reaches the downpipes. Cells no zone covers take the Default.</div>
        </div>
    </a>
    <a href="/components/Stormwater_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Stormwater_Run.png" class="nav-gh-icon"> Stormwater Run
            </div>
            <div class="index-quicklink-text">Routes a design storm over the graded terrain and reports ponding depth, flow velocity and flood hazard.  Two modes. FAST is terrain analytics only — slope, flow direction, contributing area and the capacity of every depression — which recomputes between grading edits and answers most of a grading review. FULL adds a shallow-water solve for the depths and velocities a design storm actually produces.  SURFACE ROUTING ONLY: no pipe network, no soakaways, no evapotranspiration. Use it for design-storm and cloudburst checks, not for hydraulic sizing.</div>
        </div>
    </a>
    <a href="/components/Stormwater_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Stormwater_Settings.png" class="nav-gh-icon"> Stormwater Settings
            </div>
            <div class="index-quicklink-text">Solver controls for Stormwater Run. The defaults suit a 1–5 m urban raster; leave this unconnected unless a run misbehaves.</div>
        </div>
    </a>
    <a href="/components/Stormwater_Flowlines/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Stormwater_Flowlines.png" class="nav-gh-icon"> Stormwater Flowlines
            </div>
            <div class="index-quicklink-text">Traces where the runoff goes, as curves over the graded surface. From a full run these are the solved velocity paths; from a fast run they are steepest-descent paths down the depression-filled terrain.</div>
        </div>
    </a>
    <a href="/components/Stormwater_Legend/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Stormwater_Legend.png" class="nav-gh-icon"> Stormwater Legend
            </div>
            <div class="index-quicklink-text">A legend for a stormwater mesh: swatches, labels and a title, placed on a plane.</div>
        </div>
    </a>
</div>

