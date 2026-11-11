(s:foil.params)=
## FoilP: Foil Element Parameters

The `FoilP` parameter group contains parameters for describing foil elements.

The components of this group and their defaults are:
```{code} yaml
FoilP:
  dE_ref: 0                # [eV] Reference energy change.
  material: ""             # [string] Foil material. Elemental or compound.
  thickness: 0             # [m] Material thickness at (x, y) = (0, 0).
  dthickness_dx: 0         # [-] Thickness slope for a wedge shaped foil.
  density: []              # [kg/m^3] Material density.
  area_density: []         # [kg/m^2] Material area density at (x, y) = (0, 0).
  radiation_length: []     # [kg/m^2] Material radiation length.
  final_charge: null       # [-] Charge state after stripping. null means fully stripped.
  x_min: null              # [m] Foil edge in the -x direction.
  x_max: null              # [m] Foil edge in the +x direction.
  y_min: null              # [m] Foil edge in the -y direction.
  y_max: null              # [m] Foil edge in the +y direction.
```

The reference energy at the downstream end of the `Foil` element will be `E_tot_ref + dE_ref`
where `E_tot_ref` is the upstream reference energy.

### Material

The `material` is the name of the foil material. This may be an element (for example `"Cu"`)
or a compound (for example `"B4C"`). A compound has one component for each element in its formula.
In the `"B4C"` example, the components are Boron and Carbon, in that order.

The `density`, `area_density` and `radiation_length` parameters may each be a single number
or a list with one value per component, in the order the components appear in `material`.
For `density` and `area_density`, a single value for a compound is the sum of the component values.
`radiation_length` for a compound must be a list with one value per component.
Example:
```{code} yaml
- f1:
    kind: Foil
    FoilP:
      material: "B4C"
      thickness: 1.0e-2
      density: [2.0e3, 1.0e3]           # Boron: 2e3, Carbon: 1e3
      radiation_length: [527, 427]      # Boron: 527, Carbon: 427
```

The amount of material a particle passes through is given by the area density.
If `thickness` or `dthickness_dx` is non-zero, the area density is `density * thickness`
(with `thickness` given by the equation below) and `area_density` is not used.
If both are zero, the `area_density` value is used.

When `density` or `radiation_length` is not set, a program may use tabulated values for
an elemental material. For a compound, either `density` or `area_density` must be set.

### Thickness

The `dthickness_dx` parameter describes a wedge shaped foil. The thickness `t` at a
point `(x, y)` in body coordinates is
```{code}
  t = thickness + x * dthickness_dx
```
To orient the wedge in the transverse plane, use the `z_rot` parameter of
[`BodyShiftP`](#s:bodyshift.params). If `dthickness_dx` is non-zero and `area_density` is set
instead of `density`, `thickness` must be non-zero.

### Charge stripping

A particle that passes through the foil is stripped to the charge state given by `final_charge`.
If `final_charge` is not set, the particle is fully stripped.
A particle with no electrons to strip does not change charge state.

### Foil edges

The foil is rectangular. A particle hits the foil if
```{code}
  x_min < x < x_max  and  y_min < y < y_max
```
where `(x, y)` is the particle position in body coordinates. A `null` edge value means the
foil does not end on that side. A particle that misses the foil passes through
the element with no change in charge or trajectory.
These edges are separate from any [`ApertureP`](#s:aperture.params) limits.
A particle outside an aperture is lost. A particle outside the foil edges is not affected by the foil.

In Construction...
