{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="12_CHT"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 12 CHT
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/CHT_Air_Cavity/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CHT_Air_Cavity.png" class="nav-gh-icon"> CHT Air Cavity
            </div>
            <div class="index-quicklink-text">A closed air cavity: solved as buoyant air (natural convection), coupled to the solids around it.</div>
        </div>
    </a>
    <a href="/components/CHT_Boundary/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CHT_Boundary.png" class="nav-gh-icon"> CHT Boundary
            </div>
            <div class="index-quicklink-text">Boundary condition on one face of the analysis box: fixed surface temperature, convective film (h + air temperature), or adiabatic. Unassigned faces are adiabatic.</div>
        </div>
    </a>
    <a href="/components/CHT_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CHT_Material.png" class="nav-gh-icon"> CHT Material
            </div>
            <div class="index-quicklink-text">Solid material for CHT heat transfer analysis. Catalog values (ISO 10456 / Incropera) seed the properties; wire a number to override one.</div>
        </div>
    </a>
    <a href="/components/CHT_Solid/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CHT_Solid.png" class="nav-gh-icon"> CHT Solid
            </div>
            <div class="index-quicklink-text">A solid region of the CHT assembly: closed Brep/Mesh + material. The union of all solids and cavities must fill a rectangular box (the analysis domain).</div>
        </div>
    </a>
    <a href="/components/CHT_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/CHT_Case.png" class="nav-gh-icon"> CHT Case
            </div>
            <div class="index-quicklink-text">Build a conjugate heat transfer case from solids, air cavities and boundaries. Wire the Case output into the Run component (Containerized engine). Method: Kastner & Dogan (2020), SimAUD 2020 405-412, http://simaud.org/2020/proceedings/37.pdf.</div>
        </div>
    </a>
    <a href="/components/HAM_Climate/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/HAM_Climate.png" class="nav-gh-icon"> HAM Climate
            </div>
            <div class="index-quicklink-text">Air conditions on one face of a HAM wall. One value per input is a constant; a list is a stepped schedule (one entry per step, hourly by default).</div>
        </div>
    </a>
    <a href="/components/HAM_Material/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/HAM_Material.png" class="nav-gh-icon"> HAM Material
            </div>
            <div class="index-quicklink-text">Porous material for a HAM wall: a hamFoam material model plus density, specific heat and conductivity. The five HAMSTAD benchmark models arrive with their published properties; the rest supply curves only, so wire rho, c and lambda1.</div>
        </div>
    </a>
    <a href="/components/HAM_Wall/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/HAM_Wall.png" class="nav-gh-icon"> HAM Wall
            </div>
            <div class="index-quicklink-text">Layered build-up for a HAM case, OUTSIDE layer first. Materials and thicknesses are read in parallel, so their counts must match.</div>
        </div>
    </a>
    <a href="/components/HAM_Case/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/HAM_Case.png" class="nav-gh-icon"> HAM Case
            </div>
            <div class="index-quicklink-text">Build a heat-and-moisture case for a layered wall. Wire the Case output into the Run component (Containerized engine — hamFoam ships only in the container). Pick a Preset to reproduce one of the two HAMSTAD benchmark tutorials.</div>
        </div>
    </a>
</div>

