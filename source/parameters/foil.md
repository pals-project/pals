(s:foil.params)=
## FoilP: Foil Element Parameters

The `FoilP` parameter group contains parameters for describing foil elements.

The components of this group are:
```{code} yaml
FoilP:
  dE_ref      # [eV] Reference energy change.
```

The reference energy at the downstream end of the `Foil` element will be `E_tot_ref + dE_ref`
where `E_tot_ref` is the upstream reference energy.

In Construction...
