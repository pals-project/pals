(s:ref.change.params)=
## ReferenceChangeP: Adjustment of Reference Parameters

The `ReferenceChangeP` parameter group can be used to adjust reference parameters.
For example, it is often convenient to adjust the reference time after a `Wiggler`
element to account for the extra transit time due to particle oscillations.

The components of this group are:
```{code} yaml
ReferenceChangeP:
  dtime_ref: null      # [sec] Reference time adjustment
  dE_ref: null         # [eV] Reference energy adjustment.
  dpc_ref: null        # [eV] Reference momentum adjustment.
  time_ref: null       # [eV] Set reference time.
  E_tot_ref: null      # [eV] Set reference energy.
  pc_ref: null         # [eV] Set reference momentum.
  species_ref: null    # [species] Set reference species.
```

Adjustments are only made if there are non-`null` parameters. Only one of `dE_ref`,
`dpc_ref`, `E_tot_ref`, and `pc_ref` may be present. 
Similarly, only one of  `dtime_ref` and `time_ref` may be present.

The `extra_dtime_ref` parameter in the above is ment as a correction to take into account
for particle motion that is not straight or acceleration that is not linear in energy. For example,
in a wiggler, `extra_dtime_ref` can be used to correct for the oscillatory nature of the
particle trajectories.
Since the PALS standard does not define how tracking is to be done, `extra_dtime_ref` and `dE_ref`
must be calculated by the User.
