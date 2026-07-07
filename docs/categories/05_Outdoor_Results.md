# 05 Outdoor Results
#### Main Components
<div class="index-quicklink-container">
    <a href="../components/Probe.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Probe.png" class="nav-gh-icon"> Probe
            </div>
            <div class="index-quicklink-text">Sample fields at points on a solved case, post-hoc. With Run it writes a probes function and runs postProcess on the latest time, then reads the results; without Run it reads existing results. Works on a wind case (one sub-result per direction) or a loaded case.</div>
        </div>
    </a>
    <a href="../components/Live_Residuals.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Live_Residuals.png" class="nav-gh-icon"> Live Residuals
            </div>
            <div class="index-quicklink-text">Draws a wind case's residual convergence directly on the Grasshopper canvas, with lightweight timed updates. Wire the case and toggle 'Live' to monitor a running simulation without an external plotter window. When a warm-up ramp is enabled the solver restarts mid-run and writes a separate residual file per phase; all phases are stitched into one continuous curve so you see the full history (warm-up + main), not just the latest phase.</div>
        </div>
    </a>
    <a href="../components/Meshing_Progress.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Meshing_Progress.png" class="nav-gh-icon"> Meshing Progress
            </div>
            <div class="index-quicklink-text">Monitor blockMesh, surfaceFeatures, and snappyHexMesh progress from the mesh case logs.</div>
        </div>
    </a>
    <a href="../components/Plot_Residuals.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Plot_Residuals.png" class="nav-gh-icon"> Plot Residuals
            </div>
            <div class="index-quicklink-text">Open the web-based residual plotter for a wind case's convergence history (one trace per direction).</div>
        </div>
    </a>
    <a href="../components/Flow_Rates.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Flow_Rates.png" class="nav-gh-icon"> Flow Rates
            </div>
            <div class="index-quicklink-text">Compute volumetric flow rates (m³/s) across a mesh, treating its vertices as velocity probes. Per face: average vertex velocities × face area × cos(angle to face normal).</div>
        </div>
    </a>
    <a href="../components/Pedestrian_Wind_Comfort.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Pedestrian_Wind_Comfort.png" class="nav-gh-icon"> Pedestrian Wind Comfort
            </div>
            <div class="index-quicklink-text">Classifies pedestrian wind comfort per point from an annual hourly wind-speed series (the Wind Speed output of the Velocity Amplification Factors (VAF) component) against a comfort criterion (Lawson, Davenport, NEN8100). Returns the comfort category, class letter, and activity description for each point.</div>
        </div>
    </a>
    <a href="../components/Velocity_Amplification_Factors_VAF.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Velocity_Amplification_Factors_VAF.png" class="nav-gh-icon"> Velocity Amplification Factors VAF
            </div>
            <div class="index-quicklink-text">Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed.</div>
        </div>
    </a>
    <a href="../components/Wind_Field_Viewer.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Wind_Field_Viewer.png" class="nav-gh-icon"> Wind Field Viewer
            </div>
            <div class="index-quicklink-text">Visualize a probed wind field: colored velocity arrows, a point cloud, a heatmap mesh, streamlines, or volumetric smoke (pick via Display Mode). Feed the Probe component's points + velocity vectors (Field = U), or any points + vectors.</div>
        </div>
    </a>
    <a href="../components/Analysis_Period.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Analysis_Period.png" class="nav-gh-icon"> Analysis Period
            </div>
            <div class="index-quicklink-text">Define an analysis period (from/to day of year, start/end hour of day) and output the hour-of-year indices it covers, for filtering annual results.</div>
        </div>
    </a>
    <a href="../components/Date_to_HOY.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Date_to_HOY.png" class="nav-gh-icon"> Date to HOY
            </div>
            <div class="index-quicklink-text">Convert a date and time (month, day, hour) into a single hour-of-year integer (1–8760), for indexing annual hourly data.</div>
        </div>
    </a>
</div>

