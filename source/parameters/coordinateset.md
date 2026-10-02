(s:coordinate.set.params)=
## CoordinateSetP:  Define Reference Coordinates

The `CoordinateSetP` parameter group defines a reference coordinate system that is used with the `BodyShiftP` 
parameter group to specify positioning with respect with respect to the reference coordinate system.

The elements that have a `CoordinateSetP` group are:
```{code} yaml
Fiducial
FloorShift
Girder
```
For other elements that have a `BodyShiftP` group, the reference coordinates are automatically the
branch coordinates of the element.

For a `FloorShift` or `Fiducial` element, `CoordinateSetP` with `BodyShiftP` sets the location of 
the exit end of the element.
For a `Fiducial` element, since this element has zero length, the exit end location is also
the entrance end location.

Components of this group are:
```{code} yaml
CoordinateSetP:
  origin_ele: GLOBAL_ORIGIN  # [string] Origin element name. GLOBAL_ORIGIN -> global coordinate origin.
  origin_ele_ref_pt: CENTER  # [enum] Reference point on origin_ele.
```
The calculation of the coordinate system is as follows:
Start with the reference coordinates at the `origin_ele` reference point (see
below). The coordinate system described by `CoordinateSetP` are these
coordinates [shifted](#wws) using the offset and rot parameters of the
`CoordinateSetP` group.

`origin_ele` is either an element name or one of
```{code} yaml
GLOBAL_ORIGIN             # Default.
PREVIOUS_ELEMENT
```
If `origin_ele` is set to `GLOBAL_ORIGIN` (the default), the origin of the global coordinate system is used.
If `origin_ele` is set to `PREVIOUS_ELEMENT`, the lattice element previous to the lattice element before
the "target" element where the target element is defined to be the element containing the `CoordinateSetP` group.
Since `Girder` elements are considered to exist outside of any lattice branches, a setting of 
`PREVIOUS_ELEMENT` is not allowed for this type of element.

If `origin_ele` is set to a lattice element, a PALS parser needs to be able to calculate the 
position of this element before the position of the target element is calculated.
For example, it is not generally possible to calculate the position of elements downstream of
the target element before the target element's position is calculated.

If the `origin_ele` has a finite length, the reference point may be chosen using the
`origin_ele_ref_pt` attribute which may be set to one of
```{code} yaml
  ENTRANCE_END
  CENTER               # Default
  EXIT_END
```
