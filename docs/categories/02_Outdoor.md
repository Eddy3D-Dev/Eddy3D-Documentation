{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="02_Outdoor"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 02 Outdoor
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Atmospheric_Boundary_Layer/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Atmospheric_Boundary_Layer.png" class="nav-gh-icon"> Atmospheric Boundary Layer
            </div>
            <div class="index-quicklink-text">Define atmospheric boundary layer inflow conditions for Eddy3D.</div>
        </div>
    </a>
    <a href="/components/Download_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Download_Weather.png" class="nav-gh-icon"> Download Weather
            </div>
            <div class="index-quicklink-text">Download an EPW weather file from a direct URL, or search climate.onebuilding.org by station name, WMO ID, or dataset year.</div>
        </div>
    </a>
    <a href="/components/Manual_Inflow_Profile/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Manual_Inflow_Profile.png" class="nav-gh-icon"> Manual Inflow Profile
            </div>
            <div class="index-quicklink-text">Define inflow boundary conditions from a manually entered vertical profile (z/zR, U/UR, k/UR^2) instead of the parametric ABL log-law. Writes fixedProfile inlet conditions for U, k and epsilon. epsilon is derived from the profile as epsilon(z) = Cmu^0.5 * k(z) * d(U)/dz.</div>
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
    <a href="/components/Outdoor_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Outdoor_Case.png" class="nav-gh-icon"> Outdoor Case
            </div>
            <div class="index-quicklink-text">Create, write, and manage an Eddy3D outdoor wind simulation case.</div>
        </div>
    </a>
    <a href="/components/Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Run.png" class="nav-gh-icon"> Run
            </div>
            <div class="index-quicklink-text">Mesh and run an OpenFOAM case on the selected engine (wind / indoor / UMF).</div>
        </div>
    </a>
    <a href="/components/Uniform_Flow/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Uniform_Flow.png" class="nav-gh-icon"> Uniform Flow
            </div>
            <div class="index-quicklink-text">Create a uniform (constant velocity) inflow boundary condition for Eddy3D.</div>
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
            <div class="index-quicklink-text">Cluster annual wind conditions into a budget of representative directions using k-means over hourly wind vectors (speed x direction): frequent, strong conditions attract the budget, and each cluster reports an observed direction/speed pair plus its frequency. Without wired speeds, clusters directions alone (unit vectors).</div>
        </div>
    </a>
    <a href="/components/Cell_Size/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Cell_Size.png" class="nav-gh-icon"> Cell Size
            </div>
            <div class="index-quicklink-text">Compute the snappyHexMesh refinement level needed to reach a target cell size (each level halves the cell size).</div>
        </div>
    </a>
    <a href="/components/Cylinder_Domain/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Cylinder_Domain.png" class="nav-gh-icon"> Cylinder Domain
            </div>
            <div class="index-quicklink-text">Define a cylindrical simulation domain for Eddy3D. One cylindrical mesh serves all wind directions; the cylinder side faces switch between inlet and outlet per direction. The auto radius targets the 3% frontal-blockage limit of ASCE/SEI CWE Prestandard AC 6-8b, which the case component verifies. Model surrounding buildings within ~240 m of the study area (ASCE 49 proximity guidance) before trusting results near the context edge.</div>
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
    <a href="/components/Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Mesh_Settings.png" class="nav-gh-icon"> Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure mesh refinement, layers, and grading for Eddy3D.</div>
        </div>
    </a>
    <a href="/components/Velocity_Amplification_Factors_VAF/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Velocity_Amplification_Factors_VAF.png" class="nav-gh-icon"> Velocity Amplification Factors VAF
            </div>
            <div class="index-quicklink-text">Compute Velocity Amplification Factors (VAF) and annual wind speed at probes from CFD or ML wind-prediction results and EPW weather data. VAF (the term used in the wind-engineering literature for what Eddy3D historically called "wind factors") is the local wind speed normalized by the reference speed.</div>
        </div>
    </a>
    <a href="/components/Brep_Grid_Points/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Brep_Grid_Points.png" class="nav-gh-icon"> Brep Grid Points
            </div>
            <div class="index-quicklink-text">Generate centered surface samples on the actual faces of Brep, surface, or mesh geometry.</div>
        </div>
    </a>
    <a href="/components/Ground_Roughness/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Ground_Roughness.png" class="nav-gh-icon"> Ground Roughness
            </div>
            <div class="index-quicklink-text">Assign a multi-face ground plate to the wind tunnel: each face gets its own aerodynamic roughness length z0 and becomes its own ground patch (nutkAtmRoughWallFunction). Feed into the wind case component's Ground Roughness input.</div>
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
    <a href="/components/Pedestrian_Wind_Comfort/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Pedestrian_Wind_Comfort.png" class="nav-gh-icon"> Pedestrian Wind Comfort
            </div>
            <div class="index-quicklink-text">Classifies pedestrian wind comfort per point from an annual hourly wind-speed series (the Wind Speed output of the Velocity Amplification Factors (VAF) component) against a comfort criterion (Lawson, Davenport, NEN8100). Returns the comfort category, class letter, and activity description for each point.</div>
        </div>
    </a>
    <a href="/components/Pollutant_Source/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Pollutant_Source.png" class="nav-gh-icon"> Pollutant Source
            </div>
            <div class="index-quicklink-text">Define a pollutant emission source for the wind study: a closed volume (stack tip, traffic corridor box, exhaust vent) releasing a named species at a mass rate. Wire into the Eddy3D Case component's Sources input; the species is transported as a passive scalar with turbulent diffusivity (Sct) on every direction case, and the concentration field (kg/m3) is read back by probing the species name.</div>
        </div>
    </a>
    <a href="/components/Tree/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Tree.png" class="nav-gh-icon"> Tree
            </div>
            <div class="index-quicklink-text">Represents a tree as a porous zone for wind blocking (Darcy-Forchheimer). Feed into the wind case component.</div>
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
    <a href="/components/Custom_Function_Object/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Custom_Function_Object.png" class="nav-gh-icon"> Custom Function Object
            </div>
            <div class="index-quicklink-text">Inject a custom OpenFOAM function object into a written case so the solver runs it at runtime — fieldAverage, yPlus, wallShearStress, forces, surfaceFieldValue, a coded FO, etc.</div>
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
    <a href="/components/Refinement_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Refinement_Region.png" class="nav-gh-icon"> Refinement Region
            </div>
            <div class="index-quicklink-text">Add a custom snappyHexMesh refinement region (a box, solid or surface) to a written case's mesh. Refines the cells inside/near the geometry to the chosen level; re-run meshing separately afterward to apply it.</div>
        </div>
    </a>
    <a href="/components/Run_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Run_Settings.png" class="nav-gh-icon"> Run Settings
            </div>
            <div class="index-quicklink-text">Configure solver run controls for Eddy3D.</div>
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
    <a href="/components/Plot_Residuals/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Plot_Residuals.png" class="nav-gh-icon"> Plot Residuals
            </div>
            <div class="index-quicklink-text">Open the web-based residual plotter for a wind case's convergence history (one trace per direction).</div>
        </div>
    </a>
    <a href="/components/Write_Run_Scripts/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Write_Run_Scripts.png" class="nav-gh-icon"> Write Run Scripts
            </div>
            <div class="index-quicklink-text">Writes meshing and simulation scripts (.bat / .sh) into a Scripts/ folder under the wind study, so the workflow can be launched manually outside Grasshopper. The scripts match what the Run component executes. Write the study to disk first (Wind Case 'Write').</div>
        </div>
    </a>
    <a href="/components/Airflow_Network_Cp/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Airflow_Network_Cp.png" class="nav-gh-icon"> Airflow Network Cp
            </div>
            <div class="index-quicklink-text">Export probed facade pressure coefficients into the EnergyPlus AirflowNetwork as an .idf snippet: WindPressureCoefficientArray (the simulated directions), per-node WindPressureCoefficientValues and ExternalNode objects, ready to paste/merge into a Ladybug Tools (or hand-built) AirflowNetwork model. Enable Pressure Coefficient in Run Settings, probe the Cp field at facade points, and wire the probe tree here.</div>
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
    <a href="/components/Deconstruct_Wind/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Wind.png" class="nav-gh-icon"> Deconstruct Wind
            </div>
            <div class="index-quicklink-text">Probe-specific statistics, per-hour values, a colored probe mesh and an inline legend from an annual wind field or Annual VAF object, without putting the full 8760-hour year on the canvas.</div>
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
</div>

