(s:ref.params)=
## ReferenceP: Reference Parameters

The `ReferenceP` parameter group contains parameters for describing the reference energy,
species, and time at the upstream end of the element. 
The components of this group and their defaults are:
```{code} yaml
ReferenceP:
  species_ref: ""   # [string] Reference species
  pc_ref: 0         # [momentum*c] Reference momentum times speed of light
  E_tot_ref: 0      # [eV] Reference total energy
  time_ref: 0       # [s] Reference time
```

Except for `time_ref`, the reference parameters are generally the same at the
upstream and downstream ends of the element. However, there are exceptions.
For example, the upstream and downstream `species_ref` for a `Foil` element 
will generally be different. And the reference energy will change if the element has a
`dE_ref` as in an `RFCavity` element.

For a `BeginningEle` element, parameters of this group are user settable.
For all other element kinds, the parameters of this
group are calculated (output parameters) and are not user settable. 
The reference parameters at the upstream end of any non-`BeginningEle` element will be the 
same as the reference parameters at the downstream end of the previous element.
To adjust reference parameters at any point in a lattice branch, use the `ReferenceChange` element.

The downstream reference time is calculated via
```{code} yaml
time_ref(downstream) = time_ref(upstream) + transit_time
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
change (no associated `dE_ref` element parameter), the transit time calculation simplifies to
```{code} yaml
transit_time = length / (beta_ref * c)
```
where `beta_ref` is the normalized particle reference velocity.

