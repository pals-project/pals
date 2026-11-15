%---------------------------------------------------------------------------------------------------
(s:particle.params)=
## ParticleP: Particle Coordinates Parameters

The `ParticleP` parameter group contains parameters for describing single particle coordinates
or a beam particle distribution that is Gaussian distributed.
For a [BeginningEle](#s:beginningele) element, `ParticleP` is an input parameter group that sets the
particle coordinates at the start of a branch.
For all other element kinds that have a [ReferenceP](#s:ref.params) group, `ParticleP` is an
[output parameter](#s:io.params) group.

Note that PALS itself does not define how any `ParticleP` component is calculated: that is outside
the scope of PALS.
A program is free to track particles and write the resulting coordinates out for each element of an
expanded lattice so that other programs may read them back in.

The components of this group are:
```{code} yaml
ParticleP:                    # <> denotes average over distribution
  x:             0            # <x>  x  phase space component
  px:            0            # <px> px phase space component
  y:             0            # <y>  y  phase space component
  py:            0            # <py> py phase space component
  z:             0            # <z>  z  phase space component
  pz:            0            # <pz> pz phase space component
  spin_x:        0            # <Sx> Spin x-component
  spin_y:        0            # <Sy> Spin y-component
  spin_z:        0            # <Sz> Spin z-component
  sigma_xx:      null         # <x_bar^2>
  sigma_xpx:     null         # <x_bar*px_bar> 
  sigma_xy:      null         # <x_bar*y_bar> 
  sigma_xpy:     null         # <x_bar*py_bar> 
  sigma_xz:      null         # <x_bar*z_bar> 
  sigma_xpz:     null         # <x_bar*pz_bar> 
  sigma_pxpx:    null         # <px_bar^2>
  sigma_pxy:     null         # <px_bar*y_bar> 
  sigma_pxpy:    null         # <px_bar*py_bar> 
  sigma_pxz:     null         # <px_bar*z_bar> 
  sigma_pxpz:    null         # <px_bar*pz_bar> 
  sigma_yy:      null         # <y_bar^2>
  sigma_ypy:     null         # <y_bar*py_bar>
  sigma_yz:      null         # <y_bar*z_bar>
  sigma_ypz:     null         # <y_bar*pz_bar>
  sigma_pypy:    null         # <py_bar^2>
  sigma_pyz:     null         # <py_bar*z_bar>
  sigma_pypz:    null         # <py_bar*pz_bar>
  sigma_zz:      null         # <z_bar^2>
  sigma_zpz:     null         # <z_bar*pz_bar>
  sigma_pzpz:    null         # <pz_bar^2>
```
where `x_bar = x - <x>` is the deviation from the average, etc.
When describing a single particle, the `sigma` parameters are not relevant. 
