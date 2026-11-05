{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="15_Noise"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 15 Noise
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Noise_Area_Emitter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Area_Emitter.png" class="nav-gh-icon"> Noise Area Emitter
            </div>
            <div class="index-quicklink-text">A fixed AREA source of sound for Noise Run, to ask "what if": a car park, a courtyard, a loading yard, a market. Give it a closed curve (its z is the source height, m) and a sound power level dB(A) PER SQUARE METRE — or a data sheet's eight octave levels per square metre — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). The area is cut into point sources that share it, so the total power is the area times the level, whatever the grid. No directivity, no reflection off the walls round it. For one unit use Noise Emitter, for a line Noise Line Emitter.</div>
        </div>
    </a>
    <a href="/components/Noise_Emitter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Emitter.png" class="nav-gh-icon"> Noise Emitter
            </div>
            <div class="index-quicklink-text">A fixed point source of sound for Noise Run, to ask "what if": a rooftop plant, a generator, a car park gate, an event stage. Give it a point (its z is the source height, m) and a sound power level dB(A) — or a data sheet's eight octave levels, 63 Hz to 8 kHz, which win — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). It radiates equally in every direction, with no reflection off the wall or roof beside it. Wire it next to the road sources and compare two runs, with and without it.</div>
        </div>
    </a>
    <a href="/components/Noise_Line_Emitter/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Line_Emitter.png" class="nav-gh-icon"> Noise Line Emitter
            </div>
            <div class="index-quicklink-text">A fixed LINE source of sound for Noise Run, to ask "what if": a conveyor, a rail spur, a row of loading bays, a queue. Give it a curve (its z is the source height, m) and a sound power level dB(A) PER METRE — or a data sheet's eight octave levels per metre — and the hours it runs in the day (12 h), evening (4 h) and night (8 h). It is cut into point sources like a road, with no directivity and no reflection off the wall beside it. For one unit at one place use Noise Emitter.</div>
        </div>
    </a>
    <a href="/components/Noise_Receivers/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Receivers.png" class="nav-gh-icon"> Noise Receivers
            </div>
            <div class="index-quicklink-text">Where the levels are asked for: a ground grid inside a disc at pedestrian height (1.5 m; set 4 m to match an END strategic map), and a point in front of every facade at every storey of the buildings wired in. Facade levels are free-field, without the reflection off the facade they stand before, as CNOSSOS and the END define them.</div>
        </div>
    </a>
    <a href="/components/Road_Source/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Road_Source.png" class="nav-gh-icon"> Road Source
            </div>
            <div class="index-quicklink-text">A road as a CNOSSOS-EU line source: its centreline, a daily traffic total, the heavy-vehicle share and a speed. One item per curve, or one value for all of them. Feed the sources to Noise Run.  The daily total is split 70/20/10 % over day (07-19), evening (19-23) and night (23-07), and heavies half-and-half between two-axle and multi-axle trucks — the neutral defaults when a count says no more.</div>
        </div>
    </a>
    <a href="/components/Roads_From_OSM/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Roads_From_OSM.png" class="nav-gh-icon"> Roads From OSM
            </div>
            <div class="index-quicklink-text">Every driveable road around a site from OpenStreetMap, as Road Sources with STREET-TYPE DEFAULTS for traffic: a residential street a few hundred vehicles a day, a primary road fifteen thousand, a motorway sixty thousand. A posted maxspeed wins over the class speed; four lanes carry twice the two-lane default. These are placeholders for a count — override the roads that matter with Road Source. Roads are placed in metres east/north of the site, at z = 0.</div>
        </div>
    </a>
    <a href="/components/Noise_Run/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Run.png" class="nav-gh-icon"> Noise Run
            </div>
            <div class="index-quicklink-text">Road-traffic noise after CNOSSOS-EU (Directive 2015/996, 2021/1226 coefficients): the emission of every road and the propagation to every receiver — divergence, air absorption, the ground effect on the mean plane, diffraction over roofs and crests — summed per octave band and period into Lday, Levening, Lnight and Lden. Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours.  PROTOTYPE LIMITS: homogeneous atmospheric conditions only (no favourable-propagation share, so distant levels run a little low); no facade reflections; no path around a corner (a receiver behind a block gets the over-the-roof path only, which reads low); one ground factor for the whole site; no rail, aircraft or industry. Not a compliance calculation.  Method: CNOSSOS-EU, Commission Directive (EU) 2015/996 Annex II (road emission §2.2, propagation §2.5), coefficients per Delegated Directive (EU) 2021/1226, https://eur-lex.europa.eu/eli/dir/2015/996/oj — pinned against NoiseModelling (Université Gustave Eiffel) on the ISO/TR 17534-4 cases.</div>
        </div>
    </a>
    <a href="/components/Noise_Map/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Noise_Map.png" class="nav-gh-icon"> Noise Map
            </div>
            <div class="index-quicklink-text">Colours a run's receivers in the END 5 dB bands (yellow from 50-55, orange at 60, red at 65, blue above 80): a ground mesh of the grid, a vertical quad per facade receiver, and the points, values and colours behind them for custom tagging. Pick Lden or a single period. Lden (L_den) is the day-evening-night level of the EU Environmental Noise Directive 2002/49/EC: the long-term A-weighted level in dB(A) over a whole day, with the 4 h evening counted +5 dB and the 8 h night +10 dB (the day is 12 h), so night and evening noise weigh more than their hours.</div>
        </div>
    </a>
</div>

