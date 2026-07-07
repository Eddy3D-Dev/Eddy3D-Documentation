# 07 MRT
#### Main Components
<div class="index-quicklink-container">
    <a href="../components/MRT_Sensors.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/MRT_Sensors.png" class="nav-gh-icon"> MRT Sensors
            </div>
            <div class="index-quicklink-text">Create comfort sensor probes from a mesh (face centers) or points.</div>
        </div>
    </a>
    <a href="../components/MRT_Surface.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/MRT_Surface.png" class="nav-gh-icon"> MRT Surface
            </div>
            <div class="index-quicklink-text">Mesh Breps into a tagged radiation surface for an MRT analysis.</div>
        </div>
    </a>
    <a href="../components/Surface_Settings.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Surface_Settings.png" class="nav-gh-icon"> Surface Settings
            </div>
            <div class="index-quicklink-text">Thermal + optical material properties for a building/ground MRT surface.</div>
        </div>
    </a>
    <a href="../components/Thermal_Comfort.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Thermal_Comfort.png" class="nav-gh-icon"> Thermal Comfort
            </div>
            <div class="index-quicklink-text">Compute a thermal comfort metric at a point: UTCI (Ta, RH, wind, MRT), PET (adds the personal inputs), or NOAA Heat Index (Ta, RH only). Pick the metric from the dropdown — the inputs adapt. Wire hourly lists (e.g. EPW series) to compute annual values.</div>
        </div>
    </a>
    <a href="../components/Tree_Settings.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Tree_Settings.png" class="nav-gh-icon"> Tree Settings
            </div>
            <div class="index-quicklink-text">Canopy material properties for an MRT tree surface.</div>
        </div>
    </a>
    <a href="../components/Vegetation_Settings.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Vegetation_Settings.png" class="nav-gh-icon"> Vegetation Settings
            </div>
            <div class="index-quicklink-text">Leaf/canopy material properties for an MRT vegetation surface.</div>
        </div>
    </a>
    <a href="../components/MRT.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/MRT.png" class="nav-gh-icon"> MRT
            </div>
            <div class="index-quicklink-text">Compute mean radiant temperature at the sensors. Direct-raycast shortwave by default; wire MRT Settings with reflections/diffuse radiation on to use the Radiance DDS engine.</div>
        </div>
    </a>
    <a href="../components/MRT_Settings.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/MRT_Settings.png" class="nav-gh-icon"> MRT Settings
            </div>
            <div class="index-quicklink-text">Configuration for the MRT + UTCI analysis.</div>
        </div>
    </a>
    <a href="../components/Sky_Exposure.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/Sky_Exposure.png" class="nav-gh-icon"> Sky Exposure
            </div>
            <div class="index-quicklink-text">Computes the Sky View Factor (SVF) for each input point using the Tregenza 145-patch sky subdivision. Casts 145 rays toward the upper hemisphere and returns the fraction of unobstructed sky directions (0 = fully obstructed, 1 = fully open sky).</div>
        </div>
    </a>
    <a href="../components/UTCI_Simulation.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/UTCI_Simulation.png" class="nav-gh-icon"> UTCI Simulation
            </div>
            <div class="index-quicklink-text">Compute annual per-probe UTCI from simulation outputs: MRT and wind-speed data trees, plus air temperature and relative humidity. For a weather-only calculator, use "UTCI (Weather)".</div>
        </div>
    </a>
    <a href="../components/CalcHeatIndex.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/CalcHeatIndex.png" class="nav-gh-icon"> CalcHeatIndex
            </div>
            <div class="index-quicklink-text">Calculate Heat Index using the NOAA/NWS equation (air temperature + relative humidity).</div>
        </div>
    </a>
    <a href="../components/CalcPET.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/CalcPET.png" class="nav-gh-icon"> CalcPET
            </div>
            <div class="index-quicklink-text">Calculate PET (Physiological Equivalent Temperature) from environmental and personal inputs.</div>
        </div>
    </a>
    <a href="../components/UTCI_Weather.md" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="../images/icons/UTCI_Weather.png" class="nav-gh-icon"> UTCI Weather
            </div>
            <div class="index-quicklink-text">Universal Thermal Climate Index from weather inputs. Connect an EPW (supplies wind, RH, ambient temp) and/or override Ambient Temp, RH, Wind, and MRT by hand. Item or list.</div>
        </div>
    </a>
</div>

