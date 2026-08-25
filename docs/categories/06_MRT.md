{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="06_MRT"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 06 MRT
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/MRT_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Settings.png" class="nav-gh-icon"> MRT Settings
            </div>
            <div class="index-quicklink-text">Configuration for the MRT + UTCI analysis.</div>
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
    <a href="/components/Surface_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Surface_Settings.png" class="nav-gh-icon"> Surface Settings
            </div>
            <div class="index-quicklink-text">Thermal + optical material properties for a building/ground MRT surface.</div>
        </div>
    </a>
    <a href="/components/Tree_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Tree_Settings.png" class="nav-gh-icon"> Tree Settings
            </div>
            <div class="index-quicklink-text">Canopy material properties for an MRT tree surface.</div>
        </div>
    </a>
    <a href="/components/Vegetation_Settings/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Vegetation_Settings.png" class="nav-gh-icon"> Vegetation Settings
            </div>
            <div class="index-quicklink-text">Leaf/canopy material properties for an MRT vegetation surface.</div>
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
    <a href="/components/Sky_Exposure/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sky_Exposure.png" class="nav-gh-icon"> Sky Exposure
            </div>
            <div class="index-quicklink-text">Computes the Sky View Factor (SVF) for each input point using the Tregenza 145-patch sky subdivision. Casts 145 rays toward the upper hemisphere and returns the fraction of unobstructed sky directions (0 = fully obstructed, 1 = fully open sky).</div>
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
    <a href="/components/MRT_Sensors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Sensors.png" class="nav-gh-icon"> MRT Sensors
            </div>
            <div class="index-quicklink-text">Create comfort sensor probes from meshes (one probe per face center, facing the face normal) and/or points (facing corresponding Normals), mixed freely on one input.</div>
        </div>
    </a>
    <a href="/components/MRT_Surface/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Surface.png" class="nav-gh-icon"> MRT Surface
            </div>
            <div class="index-quicklink-text">Tags Breps or Meshes as a radiation surface for an MRT analysis. Breps are meshed at Patch Size; Meshes are used face-for-face as given.</div>
        </div>
    </a>
    <a href="/components/MRT/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT.png" class="nav-gh-icon"> MRT
            </div>
            <div class="index-quicklink-text">Mean radiant temperature at each sensor, hour by hour. MRT = shortwave + longwave.  SHORTWAVE — what the sensor absorbs from sun and sky. Either a direct raycast (default, pure C#) or the Radiance DDS chain (MRT Settings -> Radiance Reflections), which adds diffuse sky and interreflection off the surroundings. Radiance returns annual total and direct illuminance per sensor, which are mapped onto the probes' shortwave series.  LONGWAVE — what the sensor exchanges with everything around it, weighted by view factors traced from each sensor against the scene and the sky dome.  SURFACE TEMPERATURES come from ENERGYPLUS, not Radiance — Radiance is a light transport engine and computes no temperatures at all. With MRT Settings -> EnergyPlus Surfaces on, Eddy3D builds an epJSON from the polygons that actually matter to the sensors (those inside the cumulative view-factor percentile and above the small-face cutoff; everything else is demoted to a shading surface), runs EnergyPlus against the EPW, and maps the surface-specific temperatures out of the ESO back onto the geometry. With it off, every surrounding surface is simply assumed to sit at air temperature.  SKY TEMPERATURE is always Clark-Allen from dew point, dry bulb, opaque cloud cover and relative humidity — it needs no engine.</div>
        </div>
    </a>
    <a href="/components/MRT_Solve/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_Solve.png" class="nav-gh-icon"> MRT Solve
            </div>
            <div class="index-quicklink-text">Solves MRT on a prepared VF Model: shortwave (direct raycast, or Radiance DDS when MRT Settings enables reflections) + view-factor longwave. Wire the VF Model straight from MRT View Factors for ambient/FFT surface temperatures, or through SurfaceTemp (EnergyPlus) for E+ temperatures. Result feeds Deconstruct MRT and UTCI.</div>
        </div>
    </a>
    <a href="/components/MRT_View_Factors/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/MRT_View_Factors.png" class="nav-gh-icon"> MRT View Factors
            </div>
            <div class="index-quicklink-text">Assembles tagged surfaces + sensors into a radiation model, builds the sky dome, and solves probe-to-polygon view factors. Feed the VF Model to SurfaceTemp (EnergyPlus) and/or MRT Solve. The sweep is the expensive part of an MRT run — solving it once here lets the downstream stages re-run without repeating it.</div>
        </div>
    </a>
    <a href="/components/SurfaceTemp_EnergyPlus/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/SurfaceTemp_EnergyPlus.png" class="nav-gh-icon"> SurfaceTemp EnergyPlus
            </div>
            <div class="index-quicklink-text">Surface temperatures via EnergyPlus, mapped onto a solved VF Model. The counterpart of the FFT SurfaceTemp component for the staged MRT pipeline: it consumes MRT View Factors' output (the E+ surface selection depends on the view factors) and its output feeds MRT Solve. Skipping this stage leaves surfaces at ambient temperature unless they carry FFT temperatures from MRT Surface.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_MRT/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_MRT.png" class="nav-gh-icon"> Deconstruct MRT
            </div>
            <div class="index-quicklink-text">Probe-specific statistics (and optionally the raw hours) from an MRT Result, without putting the full 8760-hour year on the canvas.</div>
        </div>
    </a>
    <a href="/components/Deconstruct_VF_Model/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Deconstruct_VF_Model.png" class="nav-gh-icon"> Deconstruct VF Model
            </div>
            <div class="index-quicklink-text">Colors the model's surfaces by view factor: the mean each face receives from all sensors, or one chosen sensor's view factors to every face. Values output is per face, in mesh face order, for custom gradients.</div>
        </div>
    </a>
    <a href="/components/Fisheye_View/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Fisheye_View.png" class="nav-gh-icon"> Fisheye View
            </div>
            <div class="index-quicklink-text">Equal-angle fisheye of the hemisphere above one sensor, as a colored mesh — a flat disk or a 3D dome (Display dropdown): sky, building, ground and vegetation per direction, plus the sensor's cosine-weighted sky view fraction.</div>
        </div>
    </a>
</div>

