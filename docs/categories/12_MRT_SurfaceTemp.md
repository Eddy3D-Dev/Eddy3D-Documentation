{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="12_MRT_SurfaceTemp"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 12 MRT SurfaceTemp
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/SurfaceTemp_EnergyPlus/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp_EnergyPlus.png" class="nav-gh-icon"> SurfaceTemp EnergyPlus
            </div>
            <div class="index-quicklink-text">Surface temperatures via EnergyPlus, mapped onto a solved VF Model. The counterpart of the FFT SurfaceTemp component for the staged MRT pipeline: it consumes MRT View Factors' output (the E+ surface selection depends on the view factors) and its output feeds MRT Solve. Skipping this stage leaves surfaces at ambient temperature unless they carry FFT temperatures from MRT Surface.</div>
        </div>
    </a>
    <a href="/components/SurfaceTemp_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp_Material.png" class="nav-gh-icon"> SurfaceTemp Material
            </div>
            <div class="index-quicklink-text">Predefined multi-layer construction (assembly) for the SurfaceTemp admittance solve.</div>
        </div>
    </a>
    <a href="/components/SurfaceTemp_FFT/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp_FFT.png" class="nav-gh-icon"> SurfaceTemp FFT
            </div>
            <div class="index-quicklink-text">Solves outdoor surface temperature per analysis point via the frequency-domain admittance method (no thermal mesh, no warm-up). Feeds a future MRT component alongside Sky Exposure.  Method: Beckett, O., Owens, S. and Acred, A. (2026). Applying Frequency Domain Methods for Calculating Outdoor Surface Temperatures. Proceedings of the 12th National Conference of IBPSA-USA, Minneapolis, MN. https://publications.ibpsa.org/conference/paper/?id=simbuild2026_1312</div>
        </div>
    </a>
    <a href="/components/Deconstruct_SurfaceTemp/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_SurfaceTemp.png" class="nav-gh-icon"> Deconstruct SurfaceTemp
            </div>
            <div class="index-quicklink-text">Point-specific statistics (and optionally the raw hours) from a SurfaceTemp Result, without putting the full 8760-hour year on the canvas.</div>
        </div>
    </a>
</div>

