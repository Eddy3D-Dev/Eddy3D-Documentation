{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="01_Pre"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 01 Pre
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Download_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Download_Weather.png" class="nav-gh-icon"> Download Weather
            </div>
            <div class="index-quicklink-text">Pick an EPW weather file from a bundled catalog of 60,868 climate files — every TMYx station on climate.onebuilding.org plus the EnergyPlus store (IWEC, TMY3, CWEC, SWERA, …) — with your own folders and Morph Weather results listed alongside them. Click the Station widget and choose Browse library… for a searchable table with a map, or type a name, WMO id or direct URL. The catalog is searched offline; only the chosen file is downloaded, once, into the weather cache.</div>
        </div>
    </a>
    <a href="/components/Morph_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Morph_Settings.png" class="nav-gh-icon"> Morph Settings
            </div>
            <div class="index-quicklink-text">Engine settings for Morph Weather: climate products, spatial interpolation, uncertainty case and solar methods. Every value left empty stays on the Future Weather Generator's own default.</div>
        </div>
    </a>
    <a href="/components/Morph_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Morph_Weather.png" class="nav-gh-icon"> Morph Weather
            </div>
            <div class="index-quicklink-text">Morph a present-day EPW into future-climate EPWs with the Future Weather Generator (future-weather-generator.adai.pt), then feed the result to any Eddy3D workflow. Needs Java 17+ and the generator's .jar, which Eddy3D does not ship: download the distribution you need (CMIP6 Global, CORDEX-CMIP5 Europe, …) into ~/Eddy3D/FWG. The tool is licensed CC BY-NC-SA 4.0 — noncommercial use, attribution required.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Weather.png" class="nav-gh-icon"> Deconstruct Weather
            </div>
            <div class="index-quicklink-text">Deconstruct a Weather object into hourly time series values. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Monthly_Climate_Chart/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Monthly_Climate_Chart.png" class="nav-gh-icon"> Monthly Climate Chart
            </div>
            <div class="index-quicklink-text">Visualize monthly dry-bulb temperature and relative humidity from Eddy3D Weather as two aligned min/mean/max charts.</div>
        </div>
    </a>
    <a href="/components/Relative_Humidity/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Relative_Humidity.png" class="nav-gh-icon"> Relative Humidity
            </div>
            <div class="index-quicklink-text">Convert specific humidity (w) and temperature (T) to relative humidity (%). OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Weather.png" class="nav-gh-icon"> Weather
            </div>
            <div class="index-quicklink-text">Read an EPW file and create a Weather object for the simulation. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Land_Cover_Roughness/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Land_Cover_Roughness.png" class="nav-gh-icon"> Land Cover Roughness
            </div>
            <div class="index-quicklink-text">Fetch land-cover polygons around a location from OpenStreetMap (open data, Overpass API) and classify each into an aerodynamic roughness length via the Davenport-Wieringa terrain classification — plus the terrain elevation around the site (AWS Terrain Tiles, open data). Outputs ready-made ground roughness zones and a terrain mesh for the wind case.</div>
        </div>
    </a>
    <a href="/components/Watertight/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Watertight.png" class="nav-gh-icon"> Watertight
            </div>
            <div class="index-quicklink-text">Combine a multi-part building mesh into a single watertight, CFD-ready solid via the bundled Python mesh service (trimesh/manifold3d/pymeshfix). The server auto-starts locally on the first run (uv-managed Python environment; first start installs it, 1-2 minutes) and is reused afterwards.</div>
        </div>
    </a>
    <a href="/components/Wind_Compass/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Wind_Compass.png" class="nav-gh-icon"> Wind Compass
            </div>
            <div class="index-quicklink-text">Visualize a wind direction on a compass circle. Direction is meteorological degrees (0=N, 90=E, 180=S, 270=W); outputs the flow vector and the 16-point cardinal name.</div>
        </div>
    </a>
    <a href="/components/Wind_Rose_Cluster/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Wind_Rose_Cluster.png" class="nav-gh-icon"> Wind Rose Cluster
            </div>
            <div class="index-quicklink-text">Cluster annual wind conditions into a budget of representative directions using k-means over hourly wind vectors (speed x direction): frequent, strong conditions attract the budget, and each cluster reports an observed direction/speed pair plus its frequency. Without wired speeds, clusters directions alone (unit vectors). Method: Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639; Kastner & Dogan (2019), Building Simulation 2019, Rome 621-628, doi:10.26868/25222708.2019.210458.</div>
        </div>
    </a>
    <a href="/components/Analysis_Period/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Analysis_Period.png" class="nav-gh-icon"> Analysis Period
            </div>
            <div class="index-quicklink-text">Define an analysis period (from/to day of year, start/end hour of day) and output the hour-of-year indices it covers, for filtering annual results.</div>
        </div>
    </a>
    <a href="/components/Calendar/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Calendar.png" class="nav-gh-icon"> Calendar
            </div>
            <div class="index-quicklink-text">Interactively select a month, day, and hour for annual analysis. Click the controls on the component to change the date and time.</div>
        </div>
    </a>
    <a href="/components/Hour_of_Year/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Hour_of_Year.png" class="nav-gh-icon"> Hour of Year
            </div>
            <div class="index-quicklink-text">Convert a start date/time and optional end date/time into hour-of-year values (1–8760) for indexing annual hourly data.</div>
        </div>
    </a>
    <a href="/components/Translate_Date_To_Hours/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Translate_Date_To_Hours.png" class="nav-gh-icon"> Translate Date To Hours
            </div>
            <div class="index-quicklink-text">Translate a Ladybug analysis period to hours of the year.</div>
        </div>
    </a>
    <a href="/components/STL_Exporter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/STL_Exporter.png" class="nav-gh-icon"> STL Exporter
            </div>
            <div class="index-quicklink-text">Export geometry to STL format for OpenFOAM or other CFD tools. Supports meshes and Breps (auto-meshed); binary or ASCII, single or multiple files.</div>
        </div>
    </a>
    <a href="/components/Safety_Toggle/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Safety_Toggle.png" class="nav-gh-icon"> Safety Toggle
            </div>
            <div class="index-quicklink-text">A boolean toggle that is always FALSE when a file is opened. Useful for preventing automatic execution of heavy work. When Run is connected to several component inputs, they run one Grasshopper solution at a time in canvas order. Double-click to toggle.</div>
        </div>
    </a>
    <a href="/components/Settle_Data/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Settle_Data.png" class="nav-gh-icon"> Settle Data
            </div>
            <div class="index-quicklink-text">Hold the last output while the left mouse button is pressed, then publish the newest value when the button is released. Useful between an MD Slider and an expensive component.</div>
        </div>
    </a>
</div>

