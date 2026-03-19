(s:rf.params)=
## RFP: RF Parameters

The components of this group and their defaults are:
```{code} yaml
RFP:
  frequency: 0                  # [Hz] RF frequency
  harmon: 0                     # [unitless] RF frequency harmonic number
  voltage: 0                    # [V] RF voltage
  gradient: 0                   # [V/m] RF gradient
  phase: 0                      # [rad/2pi] RF phase in 0 to 2*pi
  multipass_phase: 0            # [rad/2pi] RF Phase added to multipass elements
  cavity_type: STANDING_WAVE    # [enum] Cavity type
  num_cells: null               # [-] Number of cavity cells
  zero_phase: ACCELERATING      # [enum] Sets what phase = 0 means.
  L_active: L                   # [m] Active acceleration length.
```
Either `frequency` or `harmon` should be set but not both. To translate between the two 
the 1-turn reference time `t1_ref` must be known using the relationship `frequency = harmon / t1_ref`.

The `L_active` length is the longitudinal length over which there is an RF field. The active
length can be different from the element length `L` since `L` can include the entire RF vessel.
Especially with cryo-modules, `L_active` can be quite different from `L`. 
If not given, the value of `L_active` defaults to the value of `L`.

Either `voltage` or `gradient` should be set but not both. The two are related by the active length
`voltage = gradient * L_active`.

The `cavity_type` parameters sets the kind of cavity under consideration. Possible settings are:
```{code} yaml
STANDING_WAVE             # Default
TRAVELING_WAVE
``` 

The `zero_phase` parameter sets what zero `phase` is in reference to. Possible settings are:
```{code} yaml
ACCELERATING              # Default. Zero phase is the maximum accelerating phase.
BELOW_TRANSITION          # Zero phase is at the stable zero crossing for particles below transition.
ABOVE_TRANSITION          # Zero phase is at the stable zero crossing for particles above transition.
```
