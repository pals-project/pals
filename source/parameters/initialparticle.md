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
  sigma_xpx:     null         # <x*px> 
  sigma_xy:      null         # <x*y> 
  sigma_xpy:     null         # <x*py> 
  sigma_xz:      null         # <x*z> 
  sigma_xpz:     null         # <x*pz> 
  sigma_pxy:     null         # <px*y> 
  sigma_pxpy:    null         # <px*py> 
  sigma_pxz:     null         # <px*z> 
  sigma_pxpz:    null         # <px*pz> 
  sigma_ypy:     null         # <y*py>
  sigma_yz:      null         # <y*z>
  sigma_ypz:     null         # <y*pz>
  sigma_pyz:     null         # <py*z>
  sigma_pypz:    null         # <py*pz>
  sigma_zpz:     null         # <z*pz>
```

