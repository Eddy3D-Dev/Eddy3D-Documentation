{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="07_MRT"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 07 MRT
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/MRT_Sensors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Sensors.png" class="nav-gh-icon"> MRT Sensors
            </div>
            <div class="index-quicklink-text">Create comfort sensor probes from a mesh (face centers) or points.</div>
        </div>
    </a>
    <a href="/components/MRT_Surface/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Surface.png" class="nav-gh-icon"> MRT Surface
            </div>
            <div class="index-quicklink-text">Mesh Breps into a tagged radiation surface for an MRT analysis.</div>
        </div>
    </a>
    <a href="/components/SurfaceTemp/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp.png" class="nav-gh-icon"> SurfaceTemp
            </div>
            <div class="index-quicklink-text">Solves outdoor surface temperature per analysis point via the frequency-domain admittance method (no thermal mesh, no warm-up). Feeds a future MRT component alongside Sky Exposure.</div>
        </div>
    </a>
    <a href="/components/SurfaceTemp_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp_Material.png" class="nav-gh-icon"> SurfaceTemp Material
            </div>
            <div class="index-quicklink-text">Predefined multi-layer construction (assembly) for the SurfaceTemp admittance solve.</div>
        </div>
    </a>
    <a href="/components/Surface_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Surface_Settings.png" class="nav-gh-icon"> Surface Settings
            </div>
            <div class="index-quicklink-text">Thermal + optical material properties for a building/ground MRT surface.</div>
        </div>
    </a>
    <a href="/components/Thermal_Comfort/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Thermal_Comfort.png" class="nav-gh-icon"> Thermal Comfort
            </div>
            <div class="index-quicklink-text">Compute a thermal comfort metric at a point: UTCI (Ta, RH, wind, MRT), PET (adds the personal inputs), or NOAA Heat Index (Ta, RH only). Pick the metric from the dropdown — the inputs adapt. Wire hourly lists (e.g. EPW series) to compute annual values.</div>
        </div>
    </a>
    <a href="/components/Tree_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Tree_Settings.png" class="nav-gh-icon"> Tree Settings
            </div>
            <div class="index-quicklink-text">Canopy material properties for an MRT tree surface.</div>
        </div>
    </a>
    <a href="/components/Vegetation_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vegetation_Settings.png" class="nav-gh-icon"> Vegetation Settings
            </div>
            <div class="index-quicklink-text">Leaf/canopy material properties for an MRT vegetation surface.</div>
        </div>
    </a>
    <a href="/components/MRT/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT.png" class="nav-gh-icon"> MRT
            </div>
            <div class="index-quicklink-text">Compute mean radiant temperature at the sensors. Direct-raycast shortwave by default; wire MRT Settings with reflections/diffuse radiation on to use the Radiance DDS engine.</div>
        </div>
    </a>
    <a href="/components/MRT_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Settings.png" class="nav-gh-icon"> MRT Settings
            </div>
            <div class="index-quicklink-text">Configuration for the MRT + UTCI analysis.</div>
        </div>
    </a>
    <a href="/components/Sky_Exposure/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sky_Exposure.png" class="nav-gh-icon"> Sky Exposure
            </div>
            <div class="index-quicklink-text">Computes the Sky View Factor (SVF) for each input point using the Tregenza 145-patch sky subdivision. Casts 145 rays toward the upper hemisphere and returns the fraction of unobstructed sky directions (0 = fully obstructed, 1 = fully open sky).</div>
        </div>
    </a>
    <a href="/components/UTCI_Simulation/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/UTCI_Simulation.png" class="nav-gh-icon"> UTCI Simulation
            </div>
            <div class="index-quicklink-text">Compute annual per-probe UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".</div>
        </div>
    </a>
    <a href="/components/Comfort_Hours/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Comfort_Hours.png" class="nav-gh-icon"> Comfort Hours
            </div>
            <div class="index-quicklink-text">Bin an hourly per-point series (e.g. UTCI) into a comfort range or the UTCI thermal-stress categories, per analysis period, and report hours/percent in each band. Feed it a per-point DataTree (e.g. the UTCI component's output) and, optionally, one Analysis Period per branch (see the Analysis Period / Analysis Period To Hours components); an unwired period covers the whole series as one implicit Annual period.</div>
        </div>
    </a>
    <a href="/components/UTCI_Legend/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/UTCI_Legend.png" class="nav-gh-icon"> UTCI Legend
            </div>
            <div class="index-quicklink-text">Color UTCI values by the official thermal-stress categories and create a matching legend.</div>
        </div>
    </a>
</div>

