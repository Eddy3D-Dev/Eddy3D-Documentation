{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="08_Post_Comfort"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 08 Post Comfort
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/PET_Simulation/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PET_Simulation.png" class="nav-gh-icon"> PET Simulation
            </div>
            <div class="index-quicklink-text">Compute annual probe-specific PET (Höppe) from simulation outputs: MRT and wind-speed data trees, plus air temperature, relative humidity and the person. Solves in the background; cancel from the right-click menu. For a single point, use "Thermal Comfort".</div>
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
    <a href="/components/UTCI_Simulation/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/UTCI_Simulation.png" class="nav-gh-icon"> UTCI Simulation
            </div>
            <div class="index-quicklink-text">Compute annual probe-specific UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)". Method: Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639; Kastner & Dogan (2019), Building Simulation 2019, Rome 621-628, doi:10.26868/25222708.2019.210458.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_UTCI/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_UTCI.png" class="nav-gh-icon"> Deconstruct UTCI
            </div>
            <div class="index-quicklink-text">Probe-specific statistics and comfort hours/% from a UTCI or PET (Simulation) Result, without putting the full 8760-hour year on the canvas. Data only — wire the Result (or these outputs) into the Thermal Comfort Legend to draw a map.</div>
        </div>
    </a>
    <a href="/components/Pedestrian_Wind_Comfort/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Pedestrian_Wind_Comfort.png" class="nav-gh-icon"> Pedestrian Wind Comfort
            </div>
            <div class="index-quicklink-text">Classifies pedestrian wind comfort per point from an annual hourly wind-speed series (the Wind Speed output of the Velocity Amplification Factors (VAF) component) against a comfort criterion (Lawson, Davenport, NEN8100). Returns the comfort category, class letter, and activity description for each point.</div>
        </div>
    </a>
    <a href="/components/Comfort_Hours/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Comfort_Hours.png" class="nav-gh-icon"> Comfort Hours
            </div>
            <div class="index-quicklink-text">Bin an hourly point-specific series (e.g. UTCI) into a comfort range or the UTCI thermal-stress categories, per analysis period, and report hours/percent in each band. Feed it a point-specific DataTree (e.g. the UTCI component's output) and, optionally, one Analysis Period per branch (see the Analysis Period / Analysis Period To Hours components); an unwired period covers the whole series as one implicit Annual period.</div>
        </div>
    </a>
    <a href="/components/Thermal_Comfort_Legend/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Thermal_Comfort_Legend.png" class="nav-gh-icon"> Thermal Comfort Legend
            </div>
            <div class="index-quicklink-text">Color UTCI, PET or NOAA Heat Index temperatures by their thermal-stress categories, or a comfort share by its own bands, and create a matching legend.</div>
        </div>
    </a>
</div>

