{!toolbar.md!}

<style>
.Main-GhToolbar-Container .SubGroup-Container:not([data-category="16_Earthworks"]) {
  filter: grayscale(1);
  opacity: 0.35;
}
</style>

# 16 Earthworks
<h4 id="main-components">Main Components</h4>
<div class="index-quicklink-container">
    <a href="/components/Cut_Fill/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Cut_Fill.png" class="nav-gh-icon"> Cut Fill
            </div>
            <div class="index-quicklink-text">Cut and fill between the existing ground and a proposed grading: where the proposed surface sits below the ground is CUT (red), where it sits above is FILL (blue), and the volumes come with the mesh. Compare design options on one depth scale (Depth Range), read the balance (Net: positive = material to bring in), and the bands say how deep the work goes.  Both surfaces are sampled at the centre of every raster cell inside the proposed surface's footprint; a cell's volume is depth × cell area, so halve the cell size where the grading is finer than the cells. Ground the proposed surface does not reach is not earthworks; a cell the existing ground misses is left out and counted. Depths within 5 mm of zero are unchanged.</div>
        </div>
    </a>
    <a href="/components/Terrain_Diagram/" style="text-decoration: none;">
        <div class="index-quicklink">
            <div class="index-quicklink-title">
                <img src="/images/icons/Terrain_Diagram.png" class="nav-gh-icon"> Terrain Diagram
            </div>
            <div class="index-quicklink-text">The diagrams a grading is read by, off one raster of the ground: elevation or slope bands as a coloured mesh, contours with major lines and their level labels, and spot levels with a downhill arrow at any points you wire. Set Range to hold one colour scale while the ground is edited or design options are compared, and Slope Bands to the gradients that matter (2 % drainage, 5 % and 8.33 % access ramps, 33 % mowing).  The ground is sampled once at the centre of every cell; slope is Horn's 3 x 3 gradient in percent (100 % = 45°), and reads low in the outermost ring of cells, where a neighbour is missing. Contour levels are multiples of the interval counted from elevation 0, so a line keeps its level when the ground changes.</div>
        </div>
    </a>
</div>

