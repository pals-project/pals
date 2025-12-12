%---------------------------------------------------------------------------------------------------
(s:init.particle.params)=
## InitialParticleP: Initial Particle Coordinates Parameters

The `InitialParticleP` parameter group contains parameters for describing the 
initial beam particle distribution based on its first two moments.
The components of this group are:
```{code} yaml
InitialParticleP:
  distribution_type: ""    # [string] name of initial distribution type
  x_off:         null         # <x>, <> denotes average over distribution
  px_off:        null         # <px>
  y_off:         null         # <y>
  py_off:        null         # <py>
  z_off:         null         # <z>
  pz_off:        null         # <pz>
  sigma_xx:      null         # <x^2>
  sigma_pxpx:    null         # <px^2>
  sigma_yy:      null         # <y^2>
  sigma_pypy:    null         # <py^2>
  sigma_zz:      null         # <z^2>
  sigma_pzpz:    null         # <pz^2>
  sigma_xpx:     null         # <xpx> 
  sigma_xy:      null         # <xy> 
  sigma_xpy:     null         # <xpy> 
  sigma_xz:      null         # <xz> 
  sigma_xpz:     null         # <xpz> 
  sigma_pxy:     null         # <pxy> 
  sigma_pxpy:    null         # <pxpy> 
  sigma_pxz:     null         # <pxz> 
  sigma_pxpz:    null         # <pxpz> 
  sigma_ypy:     null         # <ypy>
  sigma_yz:      null         # <yz>
  sigma_ypz:     null         # <ypz>
  sigma_pyz:     null         # <pyz>
  sigma_pypz:    null         # <pypz>
  sigma_zpz:     null         # <zpz>
```

