(s:rf.params)=
## RFP: RF Parameters

The components of this group and their defaults are:
```{code} yaml
RFP:
  frequency: 0                  # [Hz] RF frequency
  harmon: 0                     # [unitless] RF frequency harmonic number
  voltage: 0                    # [V] RF voltage
  gradient: 0                   # [V/m] RF gradient
  phase: 0                      # [unitless] RF phase in 0 to 2*pi
  multipass_phase: 0            # [unitless] RF Phase added to multipass elements
  cavity_type: STANDING_WAVE    # [string] Cavity type
  n_cell: 1                     # [unitles] Number of cavity cells
  zero_phase: ACCELERATING      # [enum] Sets what phase = 0 means.
```

Whether `voltage` or `gradient` is kept constant with length changes is determined by
the setting of `field_master` ([](#s:non.params)). If `field_master` is `true`, the
`gradient` is kept constant and vice versa.

The `zero_phase` parameter sets what zero `phase` is in reference to. Possible settings are:
```{code} yaml
ACCELERATING              # Default. Zero phase is the maximum accelerating phase.
BELOW_TRANSITION          # Zero phase is at the stable zero crossing for particles below transition.
ABOVE_TRANSITION          # Zero phase is at the stable zero crossing for particles above transition.
```