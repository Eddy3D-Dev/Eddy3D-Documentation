{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="03_Outdoor+"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 03 Outdoor+
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Advanced_Terrain_Mesh/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Advanced_Terrain_Mesh.png" class="nav-gh-icon"> Advanced Terrain Mesh
            </div>
            <div class="index-quicklink-text">Generate a multi-resolution terrain mesh from input geometry with a solid base. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Case_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Case_Run.png" class="nav-gh-icon"> Case Run
            </div>
            <div class="index-quicklink-text">Prepare and run a UMF case. OutdoorPlus</div>
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
    <a href="/components/Outdoor+_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Outdoor+_Case.png" class="nav-gh-icon"> Outdoor+ Case
            </div>
            <div class="index-quicklink-text">Create, read, and manage an Outdoor+ (UMF microclimate) case. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Water_Surface/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Water_Surface.png" class="nav-gh-icon"> Water Surface
            </div>
            <div class="index-quicklink-text">Coupled evaporating water surface for urbanMicroclimateFoam. The water geometry becomes a named air patch that exchanges sensible heat and moisture with the air; water motion and a moving free surface are not solved. Requires an UMF build that includes the simpleWater model.</div>
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
    <a href="/components/Air_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Air_Region.png" class="nav-gh-icon"> Air Region
            </div>
            <div class="index-quicklink-text">Create an air region for the UMF case. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Building_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Building_Material.png" class="nav-gh-icon"> Building Material
            </div>
            <div class="index-quicklink-text">Select a building material from the list and override its properties.</div>
        </div>
    </a>
    <a href="/components/Building_Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Building_Mesh_Settings.png" class="nav-gh-icon"> Building Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure mesh refinement for building regions.</div>
        </div>
    </a>
    <a href="/components/Building_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Building_Region.png" class="nav-gh-icon"> Building Region
            </div>
            <div class="index-quicklink-text">Build a solid building region for the UMF case: from the façade surface meshes, two material wall layers (outer + inner) are extruded inward to model heat and moisture transport through the building envelope.</div>
        </div>
    </a>
    <a href="/components/Terrain_Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Terrain_Mesh_Settings.png" class="nav-gh-icon"> Terrain Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure mesh settings for terrain and underground regions. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Terrain_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Terrain_Region.png" class="nav-gh-icon"> Terrain Region
            </div>
            <div class="index-quicklink-text">Create a terrain region with materials and depth settings. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Terrain_Surface_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Terrain_Surface_Material.png" class="nav-gh-icon"> Terrain Surface Material
            </div>
            <div class="index-quicklink-text">Select a terrain surface material from the list and override its properties. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Vegetation_Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vegetation_Mesh_Settings.png" class="nav-gh-icon"> Vegetation Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure mesh refinement for vegetation regions. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Vegetation_Properties/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vegetation_Properties.png" class="nav-gh-icon"> Vegetation Properties
            </div>
            <div class="index-quicklink-text">Define vegetation property coefficients for canopy modeling. Shows the recommended coefficients (Leaf Length, rsMin, kc) by default; right-click to show all coefficients (Cd, C, nEvapSides). OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Vegetation_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vegetation_Region.png" class="nav-gh-icon"> Vegetation Region
            </div>
            <div class="index-quicklink-text">Create a vegetation region from tree crown solids. Pick a Tree Type preset for a typical leaf area density and foliage drag coefficient, or choose Custom and wire your own LAD. The output drives BOTH the Outdoor+ (OpenFOAM/UMF) case and the LBM Run component's Vegetation input, with consistent canopy drag.  Library sources — LAD (crown-average, m²/m³): Sjöman et al. (2021) Arboricult. Urban For. 47(6), plant area index of 64 urban species; Klingberg et al. (2017) Urban For. Urban Green. 26, Gothenburg leaf area mapping; ENVI-met Albero plant database conventions; Zhang et al. (2018) Atmosphere 9(5):198 and Beijing For. Univ. J. (2017) ENVI-met validations for subtropical evergreens. Cd (per frontal leaf area, 0.1–0.3): Katul et al. (2004) Boundary-Layer Meteorol. 113; Mayhead (1973) Agric. Meteorol. 12, conifer wind-tunnel drag; Gillies et al. (2002) J. Geophys. Res. 107(D24), drag vs. wind speed and crown streamlining. Note: NIST TN 2039 (2019) reports Cd ≈ 2.8 against total projected area per volume — a different normalization; do not mix it with the Cd·LAD convention used here. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Box_Domain/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Box_Domain.png" class="nav-gh-icon"> Box Domain
            </div>
            <div class="index-quicklink-text">Define simulation domain extents and refinement padding. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Simulation_Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Simulation_Mesh_Settings.png" class="nav-gh-icon"> Simulation Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure snappyHexMesh settings for the simulation. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Simulation_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Simulation_Settings.png" class="nav-gh-icon"> Simulation Settings
            </div>
            <div class="index-quicklink-text">Configure simulation control settings for UMF. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/Timing_Parameters/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Timing_Parameters.png" class="nav-gh-icon"> Timing Parameters
            </div>
            <div class="index-quicklink-text">Define simulation timing and optional weather-driven time series. OutdoorPlus</div>
        </div>
    </a>
    <a href="/components/ViewFactors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/ViewFactors.png" class="nav-gh-icon"> ViewFactors
            </div>
            <div class="index-quicklink-text">Configure the view-factor discretization for radiation modeling. OutdoorPlus</div>
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
    <a href="/components/Check_Geometry/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Check_Geometry.png" class="nav-gh-icon"> Check Geometry
            </div>
            <div class="index-quicklink-text">Tests for buildings and trees for Eddy3D-OutdoorPlus simulation.</div>
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
    <a href="/components/Deconstruct_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_Region.png" class="nav-gh-icon"> Deconstruct Region
            </div>
            <div class="index-quicklink-text">Deconstruct a MetaFOAM Region instance.</div>
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
    <a href="/components/Relative_Humidity/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Relative_Humidity.png" class="nav-gh-icon"> Relative Humidity
            </div>
            <div class="index-quicklink-text">Convert specific humidity (w) and temperature (T) to relative humidity (%). OutdoorPlus</div>
        </div>
    </a>
</div>

