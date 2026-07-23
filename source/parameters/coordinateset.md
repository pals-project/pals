(s:coordinate.set.params)=
## CoordinateSetP:  Floor Shifting Parameters

The `CoordinateSetP` parameter group describes the position and orientation of the branch coordinates
at some location. With a `FloorShift` element, this location is the exit end of the element.
For a `Fiducial` element, this location is the whole element itself (since this element has no length).
Components of this group are:
```{code} yaml
CoordinateSetP:
  x_offset: 0                # [m] Offset in x-direction.
  y_offset: 0                # [m] Offset in y-direction.
  z_offset: 0                # [m] Offset in z-direction.
  x_rot: 0                   # [rad] Rotation around x-axis.
  y_rot: 0                   # [rad] Rotation around y-axis.
  z_rot: 0                   # [rad] Rotation around z-axis.
  origin_ele: null           # [string] Origin element name.
  origin_ele_ref_pt: CENTER  # [enum] Reference point on origin_ele.
```
The calculation of the coordinate system is as follows:
Start with the reference coordinates at the `origin_ele` reference point (see
below). The coordinate system described by `CoordinateSetP` are these
coordinates [shifted](#wws) using the offset and rot parameters of the
`CoordinateSetP` group.

If an `origin_ele` is not specified or `null`, the `origin_ele` is the lattice element before
the "target" element where the target element is defined to be the element containing the `CoordinateSetP` group.
If the `origin_ele` value is set to `GLOBAL_ORIGIN`, the origin of the global coordinate system is used.
If an `origin_ele` is specified and is not `GLOBAL_ORIGIN`, a PALS parser needs to be able to
calculate the position of this lattice element before the position of the target element is calculated.
For example, it is not generally possible to calculate the postion of elements downstream of
the target element before the target element's position is calculated

If the `origin_ele` has a finite length, the reference point may be chosen using the
`origin_ele_ref_pt` attribute which may be set to one of
```{code} yaml
  ENTRANCE_END
  CENTER               # Default
  EXIT_END 
```
