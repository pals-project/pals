(s:beambeam.params)=
## BeamBeamP: BeamBeam Parameters

The `BeamBeamP` parameter group describes a particle beam element
from the opposite moving colliding beam.
Without explicit input specification, the hourglass effect is turned off. 

The inputs of `BeamBeamP` are:
```{code} yaml
BeamBeamP:
  sigma_x: null   # [m] The horizontal beam size of the opposite beam. 
  sigma_y: null   # [m] The vertical beam size of the opposite beam. 
  sigma_z: null   # [m] The longitudinal beam size of the opposite beam. 
  alpha_x: null   # [unitless] The horizontal Twiss parameter alpha at interaction point. 
  beta_x:  null   # [m] The horizontal Twiss parameter beta at interaction point. 
  alpha_y: null   # [unitless] The vertical Twiss parameter alpha at interaction point. 
  beta_y: null    # [m] The vertical Twiss parameter beta at interaction point. 
  charge: null    # [unitless] The charge of the opposite beam. 
  energy: null    # [eV] The total energy in eV of the opposite beam. 
  N_particle: null  # [unitless] Number of particles in the opposite beam. 
```

