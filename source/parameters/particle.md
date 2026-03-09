%---------------------------------------------------------------------------------------------------
(s:particle.params)=
## ParticleP: Particle Coordinates Parameters

The `ParticleP` parameter group contains parameters for describing single particle coordinates
or a beam particle distribution that is Gaussian distributed.
The components of this group are:
```{code} yaml
ParticleP:                    # <> denotes average over distribution
  x:             0            # <x>  x  phase space component
  px:            0            # <px> px phase space component
  y:             0            # <y>  y  phase space component
  py:            0            # <py> py phase space component
  z:             0            # <z>  z  phase space component
  pz:            0            # <pz> pz phase space component
  spin_x         0            # <Sx> Spin x-component
  spin_y         0            # <Sy> Spin y-component
  spin_z         0            # <Sz> Spin z-component
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
When describing a single particle, the `sigma` parameters are not relavent. 
