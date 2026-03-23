(s:ref.params)=
## ReferenceP: Reference Parameters

The `ReferenceP` parameter group contains parameters for describing the reference energy,
species, and time. 
The components of this group and their defaults are:
```{code} yaml
ReferenceP:
  species_ref: ""   # [string] Reference species
  pc_ref: 0         # [momentum*c] Reference momentum times speed of light
  E_tot_ref: 0      # [eV] Reference total energy
  time_ref: 0       # [s] Reference time
  location: ""      # [string] Where reference parameters are evaluated
```

The `location` component records where the reference parameters are evaluated at.
Possible values are
```{code} yaml
  location: UPSTREAM_END    # Upstream end of the element
```
and
```{code} yaml
  location: DOWNSTREAM_END  # Downstream end of the element
```
Except for `time_ref`, the reference parameters are generally the same at the
upstream and downstream ends of the element. However, there are exceptions.
For example, the upstream and downstream `species_ref` for a `Foil` element 
will generally be different. And the reference energy will change if the
`dE_ref` component of the [`ReferenceChangeP`](#s:ref.change.params) group is nonzero.
See the [`ReferenceChangeP`](#s:ref.change.params) for details as how the reference
energy and time is computed.

For a `BeginningEle` element, parameters of this group are user settable.
For all other element kinds, the parameters of this
group are calculated (output parameters) and are not user settable. 
To shift reference parameters, use the ReferenceChangeP parameter group.
