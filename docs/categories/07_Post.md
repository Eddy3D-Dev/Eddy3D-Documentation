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
    <a href="/components/Probe/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Probe.png" class="nav-gh-icon"> Probe
            </div>
            <div class="index-quicklink-text">Sample fields at points on a solved case, post-hoc. With Run it writes a probes function and runs postProcess on the requested Time (latest by default), then reads the results; without Run it reads existing results. Works on a wind case (one sub-result per direction) or a loaded case.</div>
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
    <a href="/components/Read_Cells/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Read_Cells.png" class="nav-gh-icon"> Read Cells
            </div>
            <div class="index-quicklink-text">Read cell connectivity and cell zones for a region. OutdoorPlus</div>
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
    <a href="/components/Read_checkMesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Read_checkMesh.png" class="nav-gh-icon"> Read checkMesh
            </div>
            <div class="index-quicklink-text">Read and visualize sets produced by checkMesh. OutdoorPlus</div>
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
            <div class="index-quicklink-text">Write probed wind results as a CSV for the Eddy3D Visualizer (viz.eddy3d.com): columns X, Y, Z_relative, U_at_z, mag_U — one row per probe point. Upload the file at https://viz.eddy3d.com to view the 3D field, coloured by velocity magnitude.</div>
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
    <a href="/components/Study_Report/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Study_Report.png" class="nav-gh-icon"> Study Report
            </div>
            <div class="index-quicklink-text">Generate a Markdown report documenting the wind case to the QA discipline of the ASCE/SEI CWE Prestandard (within its steady-RANS pedestrian-comfort allowance): solver and OpenFOAM version, domain and blockage, boundary conditions, numerics and the 2nd-order verdict, mesh quality, convergence, y+, Reynolds, an optional comfort section, limitations, and a compliance summary table.</div>
        </div>
    </a>
</div>

