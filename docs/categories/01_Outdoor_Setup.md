{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="01_Outdoor_Setup"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 01 Outdoor Setup
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
    <a href="/components/Manual_Inflow_Profile/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Manual_Inflow_Profile.png" class="nav-gh-icon"> Manual Inflow Profile
            </div>
            <div class="index-quicklink-text">Define inflow boundary conditions from a manually entered vertical profile (z/zR, U/UR, k/UR^2) instead of the parametric ABL log-law. Writes fixedProfile inlet conditions for U, k and epsilon. epsilon is derived from the profile as epsilon(z) = Cmu^0.5 * k(z) * d(U)/dz.</div>
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
    <a href="/components/Download_Weather/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Download_Weather.png" class="nav-gh-icon"> Download Weather
            </div>
            <div class="index-quicklink-text">Download an EPW weather file from climate.onebuilding.org nearest to your project location. Use the Search input to filter by station name, WMO ID, or dataset year.</div>
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
            <div class="index-quicklink-text">Cluster annual wind directions into representative directions using k-means.</div>
        </div>
    </a>
    <a href="/components/Gmsh_Mesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Gmsh_Mesh.png" class="nav-gh-icon"> Gmsh Mesh
            </div>
            <div class="index-quicklink-text">Creates a STL mesh from geometry using the gmsh application. Useful to create healthy mesh topologies for building elements.</div>
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
</div>

