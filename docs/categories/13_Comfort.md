{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="13_Comfort"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 13 Comfort
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
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
            <div class="index-quicklink-text">Compute annual probe-specific UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".</div>
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
            <div class="index-quicklink-text">Color UTCI, PET or NOAA Heat Index values by their thermal-stress categories and create a matching legend.</div>
        </div>
    </a>
</div>

