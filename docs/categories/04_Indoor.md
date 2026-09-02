{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="04_Indoor"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 04 Indoor
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Facade_Wind_Pressure/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Facade_Wind_Pressure.png" class="nav-gh-icon"> Facade Wind Pressure
            </div>
            <div class="index-quicklink-text">External wind pressure on a facade per EN 1991-1-4, and the opening flow it drives.</div>
        </div>
    </a>
    <a href="/components/Indoor_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Case.png" class="nav-gh-icon"> Indoor Case
            </div>
            <div class="index-quicklink-text">Build an isothermal indoor ventilation case (room + inlets + outlets + sinks) for OpenFOAM 12. Method: De Simone, Kastner & Dogan (2021), Building Simulation 2021, Bruges, doi:10.26868/25222708.2021.30632.</div>
        </div>
    </a>
    <a href="/components/Occupant_CO2/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Occupant_CO2.png" class="nav-gh-icon"> Occupant CO2
            </div>
            <div class="index-quicklink-text">CO2 generation rate of one occupant by age, activity and sex (Persily & de Jonge 2017).</div>
        </div>
    </a>
    <a href="/components/Window_Air_Exchange/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Window_Air_Exchange.png" class="nav-gh-icon"> Window Air Exchange
            </div>
            <div class="index-quicklink-text">Air exchange through an open window (Maas 1995) and the steady-state CO2 it supports.</div>
        </div>
    </a>
    <a href="/components/Indoor_Inlet/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Inlet.png" class="nav-gh-icon"> Indoor Inlet
            </div>
            <div class="index-quicklink-text">Ventilation inlet — defines where air enters the room (diffuser, window, door). Direction is computed perpendicular to the surface, pointing into the room.</div>
        </div>
    </a>
    <a href="/components/Indoor_Outlet/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Outlet.png" class="nav-gh-icon"> Indoor Outlet
            </div>
            <div class="index-quicklink-text">Ventilation outlet — defines where air exhausts from the room (return grille, open window).</div>
        </div>
    </a>
    <a href="/components/Indoor_Wall/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Wall.png" class="nav-gh-icon"> Indoor Wall
            </div>
            <div class="index-quicklink-text">Set an indoor wall temperature (°C). Wire a room surface to give just that surface its own temperature patch; leave it empty for a single case-wide wall temperature.</div>
        </div>
    </a>
    <a href="/components/Manikin/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Manikin.png" class="nav-gh-icon"> Manikin
            </div>
            <div class="index-quicklink-text">A breathing occupant (LOD-0 body with a separate mouth patch) for the Indoor Species Case.</div>
        </div>
    </a>
    <a href="/components/CO2_Emitter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CO2_Emitter.png" class="nav-gh-icon"> CO2 Emitter
            </div>
            <div class="index-quicklink-text">A CO2 passive-scalar source box for an indoor ventilation case.</div>
        </div>
    </a>
    <a href="/components/Heat_Source/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Heat_Source.png" class="nav-gh-icon"> Heat Source
            </div>
            <div class="index-quicklink-text">A volumetric heat source box for an indoor ventilation case (transported temperature scalar).</div>
        </div>
    </a>
    <a href="/components/Indoor_Sink/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Sink.png" class="nav-gh-icon"> Indoor Sink
            </div>
            <div class="index-quicklink-text">A Darcy-Forchheimer momentum sink (filter/screen) box for an indoor ventilation case.</div>
        </div>
    </a>
    <a href="/components/Momentum_Source/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Momentum_Source.png" class="nav-gh-icon"> Momentum Source
            </div>
            <div class="index-quicklink-text">A fan/jet momentum source (mean velocity) box for an indoor ventilation case.</div>
        </div>
    </a>
    <a href="/components/Viral_Emitter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Viral_Emitter.png" class="nav-gh-icon"> Viral Emitter
            </div>
            <div class="index-quicklink-text">An airborne-pathogen passive-scalar source box for an indoor ventilation case. Method: De Simone, Kastner & Dogan (2021), Building Simulation 2021, Bruges, doi:10.26868/25222708.2021.30632.</div>
        </div>
    </a>
    <a href="/components/Indoor_Species_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Indoor_Species_Case.png" class="nav-gh-icon"> Indoor Species Case
            </div>
            <div class="index-quicklink-text">Build a CO2 species case (OpenFOAM 12 multicomponentFluid) with a breathing manikin.</div>
        </div>
    </a>
    <a href="/components/CO2_Air_Quality/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CO2_Air_Quality.png" class="nav-gh-icon"> CO2 Air Quality
            </div>
            <div class="index-quicklink-text">Grade indoor CO2 (ppm) against EN 16798-1 or another CO2-based IAQ standard.</div>
        </div>
    </a>
    <a href="/components/Sleep_Comfort/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Sleep_Comfort.png" class="nav-gh-icon"> Sleep Comfort
            </div>
            <div class="index-quicklink-text">Sleep-adapted Gagge two-node model (Yan et al. 2022) for bedrooms.</div>
        </div>
    </a>
    <a href="/components/Two-Node_Comfort/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Two-Node_Comfort.png" class="nav-gh-icon"> Two-Node Comfort
            </div>
            <div class="index-quicklink-text">Gagge two-node thermal comfort: SET, ET, PMV, TSENS and DISC.</div>
        </div>
    </a>
</div>

