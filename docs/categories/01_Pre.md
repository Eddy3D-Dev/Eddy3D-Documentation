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
    <a href="/components/Convert_Units/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Convert_Units.png" class="nav-gh-icon"> Convert Units
            </div>
            <div class="index-quicklink-text">Convert values between the units Eddy3D works in — any unit into any other of the same kind, a single value or a whole hourly list. Temperature (°C, K, °F), speed (m/s, km/h, mph, kn), length, area, volume, pressure (Pa, hPa, inHg, psi), radiation (W/m², Btu/h·ft², kWh/m²), energy and power (kWh, Btu, kW, TR), mass, air flow (m³/s, cfm), rain rate, illuminance, humidity ratio (g/kg, gr/lb), enthalpy, U-value and conductivity, angle and time. EPW and every Eddy3D comfort input are in SI, OpenFOAM temperature fields are Kelvin: wire the values in, pick From and To.</div>
        </div>
    </a>
    <a href="/components/Download_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Download_Weather.png" class="nav-gh-icon"> Download Weather
            </div>
            <div class="index-quicklink-text">Pick an EPW weather file from a bundled catalog of 60,867 climate files — every TMYx station on climate.onebuilding.org plus the EnergyPlus store (IWEC, TMY3, CWEC, SWERA, …) — with your own folders and Morph Weather results listed alongside them; its second list, Built for this site, holds the sources that build a file for your site (Open-Meteo, PVGIS, NASA POWER, Copernicus CDS, NSRDB). Click the Station widget and choose Weather file (catalog)… for a searchable table with a map, or type a name, WMO id or direct URL. The catalog is searched offline; only the chosen file is downloaded, once, into the weather cache. The catalog browser's unit setting (SI or Imperial) changes only what is displayed — the Message strip, the match list and the Info text; the EPW file and every number this component outputs stay SI, so wire them to other components as before.</div>
        </div>
    </a>
    <a href="/components/Morph_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Morph_Settings.png" class="nav-gh-icon"> Morph Settings
            </div>
            <div class="index-quicklink-text">Engine settings for Morph Weather: the method (Future Weather Generator or the World Bank CCKP anomalies), climate products, spatial interpolation, uncertainty case and solar methods. Every value left empty stays on the Future Weather Generator's own default; the CCKP methods ignore the generator-only settings.</div>
        </div>
    </a>
    <a href="/components/Morph_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Morph_Weather.png" class="nav-gh-icon"> Morph Weather
            </div>
            <div class="index-quicklink-text">Morph a present-day EPW into future-climate EPWs with the Future Weather Generator (future-weather-generator.adai.pt), then feed the result to any Eddy3D workflow. Needs Java 17+ and the generator's .jar, which Eddy3D does not ship: download the distribution you need (CMIP6 Global, CORDEX-CMIP5 Europe, …) into ~/Eddy3D/FWG. The tool is licensed CC BY-NC-SA 4.0 — noncommercial use, attribution required. Alternatively set Morph Settings' Method to a CCKP entry: the World Bank Climate Change Knowledge Portal's CMIP6 ensemble (0.25°, no key, no Java, no jar) is read for the site's grid cell and applied to the file as monthly shifts and stretches.</div>
        </div>
    </a>
    <a href="/components/Compare_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Compare_Weather.png" class="nav-gh-icon"> Compare Weather
            </div>
            <div class="index-quicklink-text">Puts two weather files of one site side by side before one of them drives a study: a station's typical year (an EPW from the climate browser) against a reanalysis year (ERA5, Open-Meteo, NASA POWER), or the same place from two providers. Dry-bulb temperature, relative humidity and wind speed as means, global horizontal radiation and precipitation as sums, for the year and each month.  An EPW's missing-value codes are left out, so a typical-year file without a rain column says it carries none instead of reading as a dry climate. It measures the difference; it does not pick a file. For the wind's DIRECTIONS use Compare Wind Climates.</div>
        </div>
    </a>
    <a href="/components/Compare_Wind_Climates/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Compare_Wind_Climates.png" class="nav-gh-icon"> Compare Wind Climates
            </div>
            <div class="index-quicklink-text">Puts two wind climates of one site side by side — a station record (ISD, EPW) against ERA5, or two stations — before one of them drives a study. Wire the Climate output of two Wind Climate components built with the same Sectors.  Rose Overlap is the share of the direction distribution the two have in common (1 = the same rose); Speed Ratio is B's mean speed over A's, over the non-calm hours. The report says which of the two differs and lists every sector. It measures the disagreement; it does not pick a source.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Weather.png" class="nav-gh-icon"> Deconstruct Weather
            </div>
            <div class="index-quicklink-text">Deconstruct a Weather object into hourly time series values. More outputs: zoom in and click + beside the outputs to pick any EPW column, derived series (solar angles, sun vector, absolute humidity) or monthly statistic; − removes one. OutdoorPlus</div>
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
    <a href="/components/Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Weather.png" class="nav-gh-icon"> Weather
            </div>
            <div class="index-quicklink-text">Read an EPW file and create a Weather object for the simulation. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Wind_Climate/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Wind_Climate.png" class="nav-gh-icon"> Wind Climate
            </div>
            <div class="index-quicklink-text">Long-term directional wind statistics for pedestrian comfort: for every direction sector (36 × 10° by default) and season (year + Dec-Feb, Mar-May, Jun-Aug, Sep-Nov, named for the hemisphere), the sector probability, the calm share and a Weibull c, k fitted by maximum likelihood to the non-calm hours of a MULTI-YEAR record — ERA5 via Open-Meteo (any coordinate, no key), the nearest NOAA ISD or GHCNh station, local EPW files or a CSV — or the City of London Annex A table. A typical year cannot carry a safety criterion: Lawson's 15 m/s for 0.022 % of the year is about two hours, and a TMY holds two hours of one composite year. Wire the Wind Climate output into Pedestrian Wind Comfort (with VAF's Speed Ratios) to classify from P(U > u) = Σ p·exp(−(u/(r·c))^k); the report says whether the record is long enough to measure the safety tail. Downloads run off the canvas and are cached per year in WeatherCache/WindRecords inside the Eddy3D folder of your local app data.Sources: ERA5 (Hersbach et al. 2020, Copernicus C3S) via Open-Meteo; NOAA NCEI Integrated Surface Database (ISD-Lite) and its successor GHCNh; City of London Wind Microclimate Guidelines (2019), Annex A.</div>
        </div>
    </a>
    <a href="/components/Geometry_Repair/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Geometry_Repair.png" class="nav-gh-icon"> Geometry Repair
            </div>
            <div class="index-quicklink-text">Check building geometry and repair it for snappyHexMesh: weld split vertices, remove degenerate and duplicate faces (and the shared walls of touching solids), orient every closed piece outward, optionally fill small holes and drop specks, then optionally rebuild it as a closed, manifold voxel WRAP — overlapping buildings fuse into one solid, courtyards open to the sky stay open, gaps narrower than about the wrap cell close. Runs in-process (no Python service). The case components already run the safe part automatically before meshing; use this to see what is wrong, to fill holes, or to wrap.</div>
        </div>
    </a>
    <a href="/components/Land_Cover_Roughness/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Land_Cover_Roughness.png" class="nav-gh-icon"> Land Cover Roughness
            </div>
            <div class="index-quicklink-text">Fetch land-cover polygons around a location from OpenStreetMap (open data, Overpass API) — plus surface car parks, pedestrian areas and bare ground — and classify each into an aerodynamic roughness length via the Davenport-Wieringa terrain classification, with the terrain elevation around the site (AWS Terrain Tiles, open data). Outputs ready-made ground roughness zones draped on a terrain mesh for the wind case.</div>
        </div>
    </a>
    <a href="/components/Site_Context/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Site_Context.png" class="nav-gh-icon"> Site Context
            </div>
            <div class="index-quicklink-text">One click from a location to the site's context: buildings with heights, bare-earth terrain, tree crowns, land-cover ground zones with their roughness, and the inlet z0 per wind direction — fetched in the background from open data and placed in a local frame centred on the location (Rhino model units). Sources: OpenStreetMap buildings (ODbL; height from the height tag or building:levels x 3 m, else the Fallback Height — never guessed silently: every building's height KIND is in the report), GEDTM30 bare-earth DTM (CC BY 4.0), the Meta/WRI 1 m canopy height map plus OSM street trees (CC BY 4.0 / ODbL), and ESA WorldCover 2021 (CC BY 4.0). Buildings come from GlobalBuildingAtlas LoD1 (TUM, CC BY-NC 4.0 — heights PREDICTED by a model, every one labelled so) or from OpenStreetMap (ODbL — the height tag or building:levels x 3 m, else the Fallback Height), chosen on Building Source. Results are cached on disk, so a reopened document shows its context without a new fetch; pressing Fetch again, or Refresh from the sources on the right-click menu, downloads anew.</div>
        </div>
    </a>
    <a href="/components/Site_Picker/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Site_Picker.png" class="nav-gh-icon"> Site Picker
            </div>
            <div class="index-quicklink-text">Pick a site on a satellite map: search an address or place (Nominatim / Photon, OpenStreetMap data), click or drag the pin, then "Use this location". The map window stays in front of Rhino and Grasshopper while it is open. Latitude and Longitude (WGS84 degrees) go into LiDAR Site, Site Context or any component that takes a site. The pick is saved with the document. The last 20 places you searched for or used are kept on this machine (~/Eddy3D/site-picker-recent.json): Recent in the map window, and "Recent sites" in this component's right-click menu sets one without opening the map. Imagery: Esri World Imagery; map: © OpenStreetMap contributors. Needs an internet connection.</div>
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
    <a href="/components/City_Surface/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/City_Surface.png" class="nav-gh-icon"> City Surface
            </div>
            <div class="index-quicklink-text">Build ONE watertight surface of terrain, buildings (LoD 1.2 boxes to LoD 2.2 roofs) and surface layers (water, roads, green) for urban CFD. Ground comes from points (wired, or class 2 of a LAS/XYZ cloud) and every footprint and layer outline is carried into its triangulation, so buildings stand IN the terrain with walls down to the ground on every side instead of boxes sunk through a plate. A roof is the footprint's Height above its median ground, or else the Roof Percentile of the roof points (class 6) inside it, or — with neither, typically a house the survey saw only as the tree canopy over it — a flat box at the median height of its five nearest reconstructed buildings (the Report counts them). Overlapping footprints are separated (the earlier one wins); flattened layers sit at one level. Outputs are split by part so each can be its own patch. Method: Pađen et al. (2022), Frontiers in Built Environment 8:899332, doi:10.3389/fbuil.2022.899332; Biljecki et al. (2016), Computers, Environment and Urban Systems 59, 25-37, doi:10.1016/j.compenvurbsys.2016.04.005.</div>
        </div>
    </a>
    <a href="/components/LiDAR_Site/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LiDAR_Site.png" class="nav-gh-icon"> LiDAR Site
            </div>
            <div class="index-quicklink-text">Fetch open LiDAR and building footprints for a site from its latitude and longitude, for City Surface: the footprints over a square of the given Size, the point cloud (the terrain) over a larger square, Terrain Size — the ground a CFD domain stands on reaches further than the buildings that matter. The Netherlands: AHN (Het Waterschapshuis, CC-BY 4.0) from its official sheets — a sheet is ~5 GB and is downloaded once into the cache, then every site in it is read from there — with BAG footprints (Kadaster, CC0). The United States: USGS 3DEP (public domain), only the point-cloud nodes over the site, with GlobalBuildingAtlas footprints (TUM, CC BY-NC 4.0; OpenStreetMap if it cannot be read). France (IGN LiDAR HD, Licence Ouverte), Switzerland (swissSURFACE3D, swisstopo), Bavaria (CC BY 4.0), Scotland (National LiDAR Programme, OGL), Estonia (Maa- ja Ruumiamet), Denmark (Danmarks Højdemodel), Spain (PNOA 2022-25: Aragon, Extremadura, the Canaries) and Slovenia (GURS CLSS), the last three from the open-lidar-data mirror: the 1 km tiles over the site, 65-250 MB each (Slovenia's 2024 flight up to 1 GB), cached once, with the same footprints. Everything comes out in metres around the site centre: wire Point Cloud, Footprints and Domain into City Surface. Tree Crowns are read from the cloud's own vegetation returns (one closed mesh per cluster, for the Tree component); Trees, Barriers and Furniture are for looking at and for a render (round trees; with Roads on, OpenStreetMap fences, walls, hedges and street furniture); Layer Outlines, Layer Names, Layer Roughness and Flatten are OpenStreetMap land cover (ODbL) with its Davenport z0, in the footprints' frame — wire them into the City Surface inputs of the same names. Rivers, streams and canals mapped as lines come with them as water ribbons (the OpenStreetMap width tag, else river 20 m, canal 8 m, stream 3 m).</div>
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

