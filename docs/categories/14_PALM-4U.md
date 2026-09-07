{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="14_PALM-4U"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 14 PALM-4U
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/PALM_Domain/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Domain.png" class="nav-gh-icon"> PALM Domain
            </div>
            <div class="index-quicklink-text">Define the PALM-4U grid: cells, spacing and the site's latitude/longitude. The domain's lower-left corner sits at the Origin point in the Rhino model (world origin by default), with y pointing north. Feed the output to PALM Case and PALM Run.</div>
        </div>
    </a>
    <a href="/components/PALM_Land_Cover/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Land_Cover.png" class="nav-gh-icon"> PALM Land Cover
            </div>
            <div class="index-quicklink-text">Fetch OpenStreetMap land cover over the PALM domain and classify it into PALM surface types. Feed the output into PALM Case's Land Cover input. Urban block polygons are skipped and reported — paint those by hand.</div>
        </div>
    </a>
    <a href="/components/PALM_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Case.png" class="nav-gh-icon"> PALM Case
            </div>
            <div class="index-quicklink-text">Write the PALM-4U case: the static driver (terrain, buildings, tree canopies and the ground surface mosaic, rasterized onto the domain grid) and the _p3d namelist that runs it. Geometry inputs take trees of meshes/Breps; branches are flattened — everything wired belongs to ONE scene. Ground not covered by any input takes the Ground Cover class. The viewport shows the domain, its boundary conditions and the rasterized surface the solver will actually see.</div>
        </div>
    </a>
    <a href="/components/PALM_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Settings.png" class="nav-gh-icon"> PALM Settings
            </div>
            <div class="index-quicklink-text">Steer the PALM-4U run: duration, wind, temperature and outputs. Forcing is idealized (constant wind, cyclic boundaries). Comfort switches on radiation and the biometeorology module, whose PET/UTCI/MRT maps are PALM-4U's point.</div>
        </div>
    </a>
    <a href="/components/PALM_Progress/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Progress.png" class="nav-gh-icon"> PALM Progress
            </div>
            <div class="index-quicklink-text">Progress of the PALM run in the case folder, from its RUN_CONTROL table. Toggle Live to re-poll once a second.</div>
        </div>
    </a>
    <a href="/components/PALM_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Run.png" class="nav-gh-icon"> PALM Run
            </div>
            <div class="index-quicklink-text">Run PALM-4U. Writes a launch script into the case PALM Case wrote, then starts the published PALM container. The script and command are always shown, even before you run, so a failing run can be reproduced by hand.</div>
        </div>
    </a>
    <a href="/components/PALM_Results/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/PALM_Results.png" class="nav-gh-icon"> PALM Results
            </div>
            <div class="index-quicklink-text">Read a PALM output field: one variable, one time frame, as values and a colored mesh over the domain. Variables and times available in the case are listed on every solve.</div>
        </div>
    </a>
</div>

