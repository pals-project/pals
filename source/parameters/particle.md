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
  sigma_xx:      null         # <dx^2>
  sigma_xpx:     null         # <dx*dpx> 
  sigma_xy:      null         # <dx*dy> 
  sigma_xpy:     null         # <dx*dpy> 
  sigma_xz:      null         # <dx*dz> 
  sigma_xpz:     null         # <dx*dpz> 
  sigma_pxpx:    null         # <dpx^2>
  sigma_pxy:     null         # <dpx*dy> 
  sigma_pxpy:    null         # <dpx*dpy> 
  sigma_pxz:     null         # <dpx*dz> 
  sigma_pxpz:    null         # <dpx*dpz> 
  sigma_yy:      null         # <dy^2>
  sigma_ypy:     null         # <dy*dpy>
  sigma_yz:      null         # <dy*dz>
  sigma_ypz:     null         # <dy*dpz>
  sigma_pypy:    null         # <dpy^2>
  sigma_pyz:     null         # <dpy*dz>
  sigma_pypz:    null         # <dpy*dpz>
  sigma_zz:      null         # <dz^2>
  sigma_zpz:     null         # <dz*dpz>
  sigma_pzpz:    null         # <dpz^2>
```
where `dx = x - <x>` is the deviation from the average, etc.
When describing a single particle, the `sigma` parameters are not relevant. 
