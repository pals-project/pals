(s:matter.params)=
## MatterP:  Definition of materials

```{code} yaml
MatterP:
- thickness:         # [m] Thickness in meter
- area_density:      # [kg/m^2] Density times thickness
- MaterialP:          # [MatterP or name] the material
```
Only one of the parameters `thickness` or `area_density` is required.