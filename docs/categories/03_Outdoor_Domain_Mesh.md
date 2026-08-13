{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="03_Outdoor_Domain_Mesh"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 03 Outdoor Domain Mesh
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Cylinder_Domain/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Cylinder_Domain.png" class="nav-gh-icon"> Cylinder Domain
            </div>
            <div class="index-quicklink-text">Define a cylindrical simulation domain for Eddy3D. One cylindrical mesh serves all wind directions; the cylinder side faces switch between inlet and outlet per direction. The auto radius targets the 3% frontal-blockage limit of ASCE/SEI CWE Prestandard AC 6-8b, which the case component verifies. Model surrounding buildings within ~240 m of the study area (ASCE 49 proximity guidance) before trusting results near the context edge.</div>
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
            <div class="index-quicklink-text">Add a custom snappyHexMesh refinement region (a box, solid or surface) to a written case's mesh. Refines the cells inside/near the geometry to the chosen level; re-run meshing separately afterward to apply it.</div>
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
</div>

