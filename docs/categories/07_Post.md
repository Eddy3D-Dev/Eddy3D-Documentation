{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="07_Post"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 07 Post
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Deconstruct_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Case.png" class="nav-gh-icon"> Deconstruct Case
            </div>
            <div class="index-quicklink-text">Inspect any Eddy3D case: Outdoor wind study, Indoor case, or OutdoorPlus (UMF) case.</div>
        </div>
    </a>
    <a href="/components/Load_Wind_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Load_Wind_Case.png" class="nav-gh-icon"> Load Wind Case
            </div>
            <div class="index-quicklink-text">Reference an existing wind case folder (mesh/ + case_NNN) for post-processing.</div>
        </div>
    </a>
    <a href="/components/Probe/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Probe.png" class="nav-gh-icon"> Probe
            </div>
            <div class="index-quicklink-text">Sample fields at points on a solved case, post-hoc. With Run it writes a probes function and runs postProcess on the requested Time (latest by default), then reads the results; without Run it reads existing results. Works on a wind case (one sub-result per direction) or a loaded case.</div>
        </div>
    </a>
    <a href="/components/Streamlines/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Streamlines.png" class="nav-gh-icon"> Streamlines
            </div>
            <div class="index-quicklink-text">Extract solver-side streamlines from a solved case with OpenFOAM's streamlines function object (particles tracked through the actual mesh — accurate in refined near-building cells, unlike tracing a probed field). With Run it writes the function-object dict and runs postProcess on the requested Time, then reads the tracks; without Run it reads existing tracks.</div>
        </div>
    </a>
    <a href="/components/Airflow_Network_Cp/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Airflow_Network_Cp.png" class="nav-gh-icon"> Airflow Network Cp
            </div>
            <div class="index-quicklink-text">Export probed facade pressure coefficients into the EnergyPlus AirflowNetwork as an .idf snippet: WindPressureCoefficientArray (the simulated directions), per-node WindPressureCoefficientValues and ExternalNode objects, ready to paste/merge into a Ladybug Tools (or hand-built) AirflowNetwork model. Enable Pressure Coefficient in Run Settings, probe the Cp field at facade points, and wire the probe tree here. Method: Dogan & Kastner (2021), Building Simulation 14(4):1189-1200, doi:10.1007/s12273-020-0727-x; Dogan & Kastner (2018), IBPC 2018, Syracuse NY 1139-1144, doi:10.14305/ibpc.2018.ms-5.05.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_Wind/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Wind.png" class="nav-gh-icon"> Deconstruct Wind
            </div>
            <div class="index-quicklink-text">Probe-specific statistics, per-hour values, a colored probe mesh and an inline legend from an annual wind field or Annual VAF object, without putting the full 8760-hour year on the canvas.</div>
        </div>
    </a>
    <a href="/components/Flow_Rates/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Flow_Rates.png" class="nav-gh-icon"> Flow Rates
            </div>
            <div class="index-quicklink-text">Compute volumetric flow rates (m³/s) across a mesh, treating its vertices as velocity probes. Per face: average vertex velocities × face area × cos(angle to face normal).</div>
        </div>
    </a>
    <a href="/components/Velocity_Amplification_Factors_VAF/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Velocity_Amplification_Factors_VAF.png" class="nav-gh-icon"> Velocity Amplification Factors VAF
            </div>
            <div class="index-quicklink-text">Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD or ML wind-prediction results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed. Method: Kastner & Dogan (2022), Building and Environment 212:108639, doi:10.1016/j.buildenv.2021.108639; Kastner & Dogan (2019), Building Simulation 2019, Rome 621-628, doi:10.26868/25222708.2019.210458.</div>
        </div>
    </a>
    <a href="/components/Create_Mesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Create_Mesh.png" class="nav-gh-icon"> Create Mesh
            </div>
            <div class="index-quicklink-text">Create a visualization mesh from polyMesh point/face data. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Cull_Ground_Mesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Cull_Ground_Mesh.png" class="nav-gh-icon"> Cull Ground Mesh
            </div>
            <div class="index-quicklink-text">Remove ground mesh faces that intersect buildings, creating an analysis ground mesh with building footprints cut out.</div>
        </div>
    </a>
    <a href="/components/Flex_Legend/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Flex_Legend.png" class="nav-gh-icon"> Flex Legend
            </div>
            <div class="index-quicklink-text">Create a metric-aware color legend and an optional colored mesh from point/value samples. Supports wind, solar, sun-hours, temperature and other environmental data.</div>
        </div>
    </a>
    <a href="/components/Read_Cells/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Read_Cells.png" class="nav-gh-icon"> Read Cells
            </div>
            <div class="index-quicklink-text">Read cell connectivity and cell zones for a region. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Scalar_Field_Viewer/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Scalar_Field_Viewer.png" class="nav-gh-icon"> Scalar Field Viewer
            </div>
            <div class="index-quicklink-text">Visualize a probed scalar field — CO2, temperature, age of air, Cp, pressure — as a colored point cloud, a heatmap mesh, or a translucent volumetric cloud. Feed the Probe component's points and one value per point. For velocity, use the Vector Field Viewer.</div>
        </div>
    </a>
    <a href="/components/Vector_Field_Viewer/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vector_Field_Viewer.png" class="nav-gh-icon"> Vector Field Viewer
            </div>
            <div class="index-quicklink-text">Visualize a probed vector field: colored velocity arrows, a point cloud, a heatmap mesh, streamlines, or volumetric smoke (pick via Display Mode). Feed the Probe component's points + velocity vectors (Field = U), or any points + vectors. For a field without direction — CO2, temperature, age of air, Cp — use the Scalar Field Viewer.</div>
        </div>
    </a>
    <a href="/components/Create_OBJ/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Create_OBJ.png" class="nav-gh-icon"> Create OBJ
            </div>
            <div class="index-quicklink-text">Export an OBJ mesh from a polyMesh description. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Export_to_Visualizer/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Export_to_Visualizer.png" class="nav-gh-icon"> Export to Visualizer
            </div>
            <div class="index-quicklink-text">Write probed wind results as a CSV for the Eddy3D Visualizer (https://viz.eddy3d.com/): columns X, Y, Z_relative, U_at_z, mag_U, U_x, U_y, U_z — one row per probe point. Upload the file at https://viz.eddy3d.com/ to view the 3D field, coloured by velocity magnitude, with the vector components powering the viewer's particle-flow overlay.</div>
        </div>
    </a>
    <a href="/components/Open_In_ParaView/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Open_In_ParaView.png" class="nav-gh-icon"> Open In ParaView
            </div>
            <div class="index-quicklink-text">Open a wind case's direction cases in ParaView. All directions are added to the ParaView pipeline browser; click Apply on the ones you want to load (nothing is loaded automatically).</div>
        </div>
    </a>
    <a href="/components/CheckMesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CheckMesh.png" class="nav-gh-icon"> CheckMesh
            </div>
            <div class="index-quicklink-text">Run the OpenFOAM checkMesh command for a case region. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Face_Warnings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Face_Warnings.png" class="nav-gh-icon"> Face Warnings
            </div>
            <div class="index-quicklink-text">Visualize faces that fail tet decomposition during topoSet. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Live_Residuals/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Live_Residuals.png" class="nav-gh-icon"> Live Residuals
            </div>
            <div class="index-quicklink-text">Draws a wind case's residual convergence directly on the Grasshopper canvas, with lightweight timed updates. Wire the case and toggle 'Live' to monitor a running simulation without an external plotter window. When a warm-up ramp is enabled the solver restarts mid-run and writes a separate residual file per phase; all phases are stitched into one continuous curve so you see the full history (warm-up + main), not just the latest phase.</div>
        </div>
    </a>
    <a href="/components/Meshing_Progress/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Meshing_Progress.png" class="nav-gh-icon"> Meshing Progress
            </div>
            <div class="index-quicklink-text">Monitor blockMesh, surfaceFeatures, and snappyHexMesh progress from the mesh case logs.</div>
        </div>
    </a>
    <a href="/components/Parse_Case_Logs/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Parse_Case_Logs.png" class="nav-gh-icon"> Parse Case Logs
            </div>
            <div class="index-quicklink-text">Parses log files in a case folder and reports any FOAM errors. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Plot_Residuals/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Plot_Residuals.png" class="nav-gh-icon"> Plot Residuals
            </div>
            <div class="index-quicklink-text">Open the web-based residual plotter for a wind case's convergence history (one trace per direction).</div>
        </div>
    </a>
    <a href="/components/Read_checkMesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Read_checkMesh.png" class="nav-gh-icon"> Read checkMesh
            </div>
            <div class="index-quicklink-text">Read and visualize sets produced by checkMesh. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Study_Report/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Study_Report.png" class="nav-gh-icon"> Study Report
            </div>
            <div class="index-quicklink-text">Generate a Markdown report documenting the wind case to the QA discipline of the ASCE/SEI CWE Prestandard (within its steady-RANS pedestrian-comfort allowance): solver and OpenFOAM version, domain and blockage, boundary conditions, numerics and the 2nd-order verdict, mesh quality, convergence, y+, Reynolds, an optional comfort section, limitations, and a compliance summary table.</div>
        </div>
    </a>
</div>

