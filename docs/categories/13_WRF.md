{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="13_WRF"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 13 WRF
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/WRF_Geo_Data/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Geo_Data.png" class="nav-gh-icon"> WRF Geo Data
            </div>
            <div class="index-quicklink-text">Check and download the WPS static geographical data geogrid needs. Reports what is installed against the mandatory field list, and fetches the bundle that closes the gap.</div>
        </div>
    </a>
    <a href="/components/WRF_Met_Data/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Met_Data.png" class="nav-gh-icon"> WRF Met Data
            </div>
            <div class="index-quicklink-text">Download the meteorological GRIB files that drive a WRF run. The file list and the Vtable are shown before you fetch anything, so a window can be checked first.</div>
        </div>
    </a>
    <a href="/components/WRF_Domain/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Domain.png" class="nav-gh-icon"> WRF Domain
            </div>
            <div class="index-quicklink-text">Define a WRF domain and the parent grids nested around it. Domains are specified INNERMOST-FIRST: the grid you set here is the finest one, and each nest ratio adds a coarser parent around it. Outputs the project the WRF Namelist component writes, and the domain extents as rectangles centred on the innermost domain.</div>
        </div>
    </a>
    <a href="/components/WRF_Namelist/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Namelist.png" class="nav-gh-icon"> WRF Namelist
            </div>
            <div class="index-quicklink-text">Write namelist.wps for a WRF project. The text is produced on every solve; the Write toggle saves it to <Working Directory>/run_wps/namelist.wps.</div>
        </div>
    </a>
    <a href="/components/WRF_Progress/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Progress.png" class="nav-gh-icon"> WRF Progress
            </div>
            <div class="index-quicklink-text">Progress of the WRF pipeline in the working directory, with an expected time to completion once wrf.exe is stepping. Toggle Live to re-poll once a second.</div>
        </div>
    </a>
    <a href="/components/WRF_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Run.png" class="nav-gh-icon"> WRF Run
            </div>
            <div class="index-quicklink-text">Run the WRF pipeline. Writes a script into the project folder and launches it. The script and command are always shown, even before you run, so a failing run can be reproduced by hand.</div>
        </div>
    </a>
    <a href="/components/WRF_Animate/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Animate.png" class="nav-gh-icon"> WRF Animate
            </div>
            <div class="index-quicklink-text">Loop through a WRF run's history frames while Play is on. Wire Frame into the WRF Probe's Frame input; each tick advances one frame and recomputes the display.</div>
        </div>
    </a>
    <a href="/components/WRF_Map/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Map.png" class="nav-gh-icon"> WRF Map
            </div>
            <div class="index-quicklink-text">Lat/lon graticule with labels, the run's own coastline from LANDMASK, and a site marker — in the same plane as the WRF Probe points and WRF Domain rectangles. Wire Labels + Label Points (and Site Label + Site Point) to a Text Tag to draw the annotations.</div>
        </div>
    </a>
    <a href="/components/WRF_Probe/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Probe.png" class="nav-gh-icon"> WRF Probe
            </div>
            <div class="index-quicklink-text">Sample a surface field of a WRF run over the whole domain, one point per grid cell. Points are in metres about the domain centre, matching the WRF Domain rectangles. Wire Points + Values into the Scalar Field Viewer, or Points + Vectors into the Vector Field Viewer, for the display.</div>
        </div>
    </a>
    <a href="/components/WRF_ABL/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_ABL.png" class="nav-gh-icon"> WRF ABL
            </div>
            <div class="index-quicklink-text">Build an atmospheric boundary layer from a WRF site series. The output plugs into the same socket as Outdoor's ABL, so it drives the wind study, Outdoor+, FluidX3D and LBM alike. Note this is uniform in plan: one log-law profile at the site, not a spatially varying inflow.</div>
        </div>
    </a>
    <a href="/components/WRF_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/WRF_Weather.png" class="nav-gh-icon"> WRF Weather
            </div>
            <div class="index-quicklink-text">Read a WRF run at a site and build the weather an Eddy3D case needs. Feed the Weather output to Timing Parameters and urbanMicroclimateFoam runs on WRF instead of an EPW. Start HOY and Duration describe the window the run actually covers — wire them too, because every hour outside it is deliberately NaN and will stop OpenFOAM rather than quietly simulate a day of 0 degC.</div>
        </div>
    </a>
</div>

