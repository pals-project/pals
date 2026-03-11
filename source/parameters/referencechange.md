(s:ref.change.params)=
## ReferenceChangeP: Change in Reference Parameters

The `ReferenceChangeP` parameter group contains parameters for describing how the reference energy,
and time deviate from the nominal values from one end of an element to the other end.
The components of this group are:
```{code} yaml
ReferenceChangeP:
  extra_dtime_ref: 0   # [sec] Reference time deviation from nominal.
  dE_ref: null         # [eV] Change in reference energy.
  E_tot_ref: null      # [eV] Reference energy at exit end.
  species_ref: null    # [species] Species at exit end.
```
Note: The reference energy, time, and species are stored in the [`ReferenceP`](#s:ref.params) group.

The exit end reference energy is calculated in one of two ways. 
If `E_tot_ref` is set, that is the exit reference energy.
If `dE_ref` is set, the exit reference energy is calculated from the entrance value via
```{code} yaml
E_tot_ref(exit) = E_tot_ref(entrance) + dE_ref
```
Notice that this formula is formulated with respect to the entrance and exit ends of the
element as opposed to the upstream and downstream ends. This is done so that reversing
an element longitudinally reverses the change in reference energy.
It is not permitted to set both `E_tot_ref` and `dE_ref`.

The downstream reference time is calculated via
```{code} yaml
time_ref(downstream) = time_ref(upstream) + transit_time + extra_dtime_ref
```
where `transit_time` is the time to transit the element assuming a straight line trajectory
and a linear energy change throughout the element. The formula
for the transit time is
```{code} yaml
transit_time = length * (E_tot_ref(upstream) + E_tot_ref(downstream)) / 
                            (c * (pc_ref(upstream) + pc_ref(downstream)))
```
where `length` is the length of the element and `c` is the speed of light.
For elements where there is no energy
change (`dE_ref` = 0), the transit time calculation simplifies to
```{code} yaml
transit_time = length / (beta_ref * c)
```
where `beta_ref` is the normalized particle velocity.

The `species_ref` parameter can be used to set the outgoing reference species. This is
typically used in elements in things like `Foil` elements where the outgoing particles of interest
are not the same as the incoming. If `species_ref` is set, the transit time calculation uses
the species set by `species_ref`. 

The `extra_dtime_ref` parameter in the above is ment as a correction to take into account
for particle motion that is not straight or acceleration that is not linear in energy. For example,
in a wiggler, `extra_dtime_ref` can be used to correct for the oscillatory nature of the
particle trajectories.
Since the PALS standard does not define how tracking is to be done, `extra_dtime_ref` and `dE_ref`
must be calculated by the User.
