(s:foil.params)=
## FoilP: Foil Element Parameters

The `FoilP` parameter group contains parameters for describing foil elements.

The components of this group and their defaults are:
```{code} yaml
FoilP:
  dE_ref: 0                # [eV] Reference energy change.
  thickness: 0             # [m] Material thickness at (x, y) = (0, 0).
  dthickness_dx: 0         # [-] Thickness slope for a wedge shaped foil.
  final_charge: null       # [-] Charge state after stripping. null means fully stripped.
  x_min: null              # [m] Foil edge in the -x direction.
  x_max: null              # [m] Foil edge in the +x direction.
  y_min: null              # [m] Foil edge in the -y direction.
  y_max: null              # [m] Foil edge in the +y direction.
```

The reference energy at the downstream end of the `Foil` element will be `E_tot_ref + dE_ref`
where `E_tot_ref` is the upstream reference energy.

### Material

The foil material is given by the [`MaterialP`](#s:material.params) group of the `Foil` element.
`FoilP` gives the geometry. For a `Foil`, `MaterialP.area_density` is the area density at
`(x, y) = (0, 0)`.
Example:
```{code} yaml
- stripper:
    kind: Foil
    FoilP:
      thickness: 1.0e-6
      x_min: -0.03
    MaterialP:
      name: "C"
      density: 2.0e3
```

### Thickness

The `dthickness_dx` parameter describes a wedge shaped foil. The thickness `t` at a
point `(x, y)` in body coordinates is
```{code}
  t = thickness + x * dthickness_dx
```
To orient the wedge in the transverse plane, use the `z_rot` parameter of
[`BodyShiftP`](#s:bodyshift.params).

The amount of material a particle passes through is given by the area density at the
particle position:
- If `thickness` is non-zero, the area density is `density * t`. If `MaterialP.area_density`
  is set instead of `MaterialP.density`, the density is `area_density / thickness`.
- If `thickness` is zero and `dthickness_dx` is non-zero, `MaterialP.density` must be set
  and the area density is `density * t`.
- If `thickness` and `dthickness_dx` are both zero, `MaterialP.area_density` must be set
  and is used everywhere on the foil.

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
