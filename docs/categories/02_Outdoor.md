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
    <a href="/components/Mesh_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Mesh_Settings.png" class="nav-gh-icon"> Mesh Settings
            </div>
            <div class="index-quicklink-text">Configure mesh refinement, layers, and grading for Eddy3D.</div>
        </div>
    </a>
    <a href="/components/Refinement_Region/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Refinement_Region.png" class="nav-gh-icon"> Refinement Region
            </div>
            <div class="index-quicklink-text">Define a custom snappyHexMesh refinement region (a box, solid or surface) — refines the cells inside/near the geometry to the chosen level. Wire Extras into a case component so the region is written every time the case is written; or wire a written Case in and press Apply to edit the dictionaries in place (which a later re-write undoes).</div>
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
            <div class="index-quicklink-text">Define a custom OpenFOAM function object the solver runs at runtime — fieldAverage, yPlus, wallShearStress, forces, surfaceFieldValue, a coded FO, etc. Wire Extras into a case component so it is written every time the case is written; or wire a written Case in and press Apply to edit controlDict in place (which a later re-write undoes).</div>
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
    <a href="/components/Run_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Run_Settings.png" class="nav-gh-icon"> Run Settings
            </div>
            <div class="index-quicklink-text">Configure solver run controls for Eddy3D.</div>
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
    <a href="/components/Write_Run_Scripts/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Write_Run_Scripts.png" class="nav-gh-icon"> Write Run Scripts
            </div>
            <div class="index-quicklink-text">Writes meshing and simulation scripts (.bat / .sh) into a Scripts/ folder under the wind study, so the workflow can be launched manually outside Grasshopper. The scripts match what the Run component executes. Write the study to disk first (Wind Case 'Write').</div>
        </div>
    </a>
</div>

