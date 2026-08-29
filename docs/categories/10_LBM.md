{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="10_LBM"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 10 LBM
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/FluidX3D_Run_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/FluidX3D_Run_Settings.png" class="nav-gh-icon"> FluidX3D Run Settings
            </div>
            <div class="index-quicklink-text">Solver controls for the FluidX3D GPU engine (memory, simulated time, export interval, and an interactive real-time window).</div>
        </div>
    </a>
    <a href="/components/LBM_Field/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Field.png" class="nav-gh-icon"> LBM Field
            </div>
            <div class="index-quicklink-text">Read the time-averaged pedestrian wind field from an LBM case directory. Outputs world-frame points and velocity vectors — plug both into the Vector Field Viewer.</div>
        </div>
    </a>
    <a href="/components/LBM_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Run.png" class="nav-gh-icon"> LBM Run
            </div>
            <div class="index-quicklink-text">Prepare and launch a container-based OpenLB wind simulation (Smagorinsky LES, time-averaged pedestrian wind field). Uses the same ABL inflow object as the OpenFOAM and FluidX3D engines. Needs Docker Desktop or podman; the solver image is pulled on first run.</div>
        </div>
    </a>
    <a href="/components/LBM_Run_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Run_Settings.png" class="nav-gh-icon"> LBM Run Settings
            </div>
            <div class="index-quicklink-text">Solver controls for the container-based LBM wind engine (grid spacing, warmup and averaging windows, probe layer, GPU, container runtime).</div>
        </div>
    </a>
    <a href="/components/FluidX3D_Live_View/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/FluidX3D_Live_View.png" class="nav-gh-icon"> FluidX3D Live View
            </div>
            <div class="index-quicklink-text">Watch a FluidX3D wind solve live in the viewport: colors an analysis mesh with the velocity magnitude of the newest exported frame while the GPU solver runs, updating as each frame lands. Also shows the final field of a completed run.  Wire either the Run component's Case or Folder output into Case, and supply the mesh to read the wind on (e.g. a pedestrian-level plane).</div>
        </div>
    </a>
</div>

