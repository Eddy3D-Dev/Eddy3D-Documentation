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
            <div class="index-quicklink-text">Solver controls for the FluidX3D GPU engine (memory, simulated time, export interval, an interactive real-time window, and an optional fixed lattice spacing). Memory 0 = detected from this machine's GPU.</div>
        </div>
    </a>
    <a href="/components/LBM_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Case.png" class="nav-gh-icon"> LBM Case
            </div>
            <div class="index-quicklink-text">Build a lattice-Boltzmann wind case from the ABL, the geometry and a settings object, and write it to disk. Wire 'LBM Run Settings' for OpenLB or 'FluidX3D Run Settings' for FluidX3D (nothing = OpenLB). Feed the Case output to LBM Run, then to Probe, LBM Field or FluidX3D Live View — the same Case → Run → Probe chain as the OpenFOAM wind study.</div>
        </div>
    </a>
    <a href="/components/LBM_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Run.png" class="nav-gh-icon"> LBM Run
            </div>
            <div class="index-quicklink-text">Launch a lattice-Boltzmann case from the LBM Case component (OpenLB in a container or natively, or FluidX3D on the GPU — whichever the case was built with). Writes the case first if it has not been written, then opens the solver in a terminal window. Read results with Probe (points), LBM Field (the probe layer) or FluidX3D Live View.</div>
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
    <a href="/components/LBM_Field/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/LBM_Field.png" class="nav-gh-icon"> LBM Field
            </div>
            <div class="index-quicklink-text">Read the time-averaged pedestrian wind field from an LBM case directory. Outputs world-frame points and velocity vectors — plug both into the Vector Field Viewer.</div>
        </div>
    </a>
</div>

