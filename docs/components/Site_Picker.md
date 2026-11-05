# ![](/images/icons/Site_Picker.png) Site Picker - [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Site%20Picker%22)

![](/images/components/Site_Picker-crop.png)

Pick a site on a satellite map: search an address or place (Nominatim / Photon, OpenStreetMap data), click or drag the pin, then "Use this location". The map window stays in front of Rhino and Grasshopper while it is open. Latitude and Longitude (WGS84 degrees) go into LiDAR Site, Site Context or any component that takes a site. The pick is saved with the document. The last 20 places you searched for or used are kept on this machine (~/Eddy3D/site-picker-recent.json): Recent in the map window, and "Recent sites" in this component's right-click menu sets one without opening the map. Imagery: Esri World Imagery; map: © OpenStreetMap contributors. Needs an internet connection.

#### Input

*None*

#### Output

| Name | Nickname | Description | Type |
| ---- | -------- | ----------- | ---- |
| Latitude | Lat | The picked site's latitude (WGS84, degrees). | `Number` |
| Longitude | Lon | The picked site's longitude (WGS84, degrees). | `Number` |
| Address | Addr | The address the map found at the pick (empty when the lookup failed). | `Text` |