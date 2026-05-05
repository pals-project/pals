(s:converter.params)=
## ConverterP: converter Element Parameters

The `ConverterP` parameter group contains parameters for describing `Converter` elements.

The components of this group are:
```{code} yaml
ConverterP:
  species_out:      # [species] Species produced.
  E_tot_ref_out     # [eV] Output (downstream) reference energy
```

The `species_out` parameter gives the species produced. This will be the reference species 
of the element downstream to the `Converter`.

In Construction...
