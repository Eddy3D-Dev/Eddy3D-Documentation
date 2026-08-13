{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="02_Outdoor_Setup"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 02 Outdoor Setup
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
            <div class="index-quicklink-text">Download an EPW weather file from a direct URL, or search climate.onebuilding.org by station name, WMO ID, or dataset year.</div>
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
            <div class="index-quicklink-text">Fetch land-cover polygons around a location from OpenStreetMap (open data, Overpass API) and classify each into an aerodynamic roughness length via the Davenport-Wieringa terrain classification. Outputs ready-made ground roughness zones for the wind case.</div>
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

