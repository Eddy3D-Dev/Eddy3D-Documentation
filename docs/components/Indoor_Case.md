## ![](../images/icons/Indoor_Case.png) [[source code]](https://github.com/Eddy3D-Dev/Eddy3D/search?q=%22Indoor%20Case%22)

![](../images/components/Indoor_Case.png)

Build an isothermal indoor ventilation case (room + inlets + outlets + sinks) for OpenFOAM 12.

#### Input
* ##### Name 
Case name (no spaces).
* ##### Dir 
Working directory (default ~/Eddy3D/Indoor).
* ##### Room (R) 
Closed room Brep.
* ##### Cell Size (C) 
Mesh cell size (m).
* ##### Inlets (I) 
Inlet surface(s): Brep or Indoor Inlet component(s).
* ##### Outlets (O) 
Outlet surface(s): Brep or Indoor Outlet component(s).
* ##### Inlet Speed (U) 
Fallback inlet speed (m/s) when raw Breps are used. Ignored when Indoor Inlet components provide velocity.
* ##### Sinks (S) 
Momentum sinks (Indoor Sink).
* ##### Src 
Emitters: Momentum / Heat / CO2 / Viral Source components.
* ##### Wall Temp (WT) 
Optional wall temperature (K) for the transported temperature field (needs a Heat Source).
* ##### Write (W) 
Click to write the case to disk. Resets automatically so it never re-writes on recompute.
* ##### Clear (X) 
Click to delete the case folder. Resets automatically so it never re-deletes on recompute.

#### Output
* ##### Case (C)
The indoor case (for the Run component).
* ##### Logs (L)
Build / write logs.