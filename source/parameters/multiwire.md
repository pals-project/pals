(s:multiwire.params)=
## MultiWireP: Multi-Wire Parameters

The `MultiWireP` parameter group describes a multi-wire profile monitor, also called a harp. A
harp is a fixed grid of thin wires that intercepts a particle beam to measure, in a single shot,
one-dimensional projections of the beam's transverse distribution.
The components of this group and their defaults are:
```{code} yaml
MultiWireP:
  n_wires_x: 0        # [integer] Number of wires that measure the horizontal profile.
  n_wires_y: 0        # [integer] Number of wires that measure the vertical profile.
  wire_spacing_x: 0   # [m] Spacing between the wires that measure the horizontal profile.
  wire_spacing_y: 0   # [m] Spacing between the wires that measure the vertical profile.
  width: 0            # [m] Wire width (diameter).
  mirror_x: false     # [logical] Is the horizontal wire ordering reversed?
  mirror_y: false     # [logical] Is the vertical wire ordering reversed?
```

All parameters are in the transverse plane of the element's [body coordinates](#s:coords).
The wires that measure the horizontal profile are parallel to the {math}`y`-axis and are spaced
`wire_spacing_x` apart, center to center, along the {math}`x`-axis. The wires that measure the
vertical profile are parallel to the {math}`x`-axis and are spaced `wire_spacing_y` apart along
the {math}`y`-axis. Each set of wires is centered on the {math}`x = y = 0` axis. A harp that
measures only one profile has zero wires in the other set. A harp whose wires are rotated in the
transverse plane can be described using the `z_rot` parameter of
[`BodyShiftP`](#s:bodyshift.params).

If `mirror_x` is `false`, the index of the horizontal profile wires increases in the {math}`+x`
direction. If `mirror_x` is `true`, the index increases in the {math}`-x` direction. `mirror_y`
does the same for the vertical profile wires and the {math}`y`-axis. These parameters let a
simulated profile be compared wire by wire with a measured one.
