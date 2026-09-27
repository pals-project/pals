(s:floor.params)=
## FloorP: Floor Parameters

The `FloorP` parameter group holds parameters that describe the position and orientation 
(collectively called "placement") of some
coordinate system in [global coordinates](#s:floor). When this group is contained in an element, 
the coordinate system described is the branch coordinate system whose origin point is at the 
upstream edge of the element. That is, the position of the element without any `FloorShiftP` or
`Girder` alignment shifts.

The components of this group are:
```{code} yaml
FloorP:
  x: null                       # [m] Global x-coordinate.
  y: null                       # [m] Global y-coordinate.
  z: null                       # [m] Global z-coordinate.
  theta: null                   # [radians] Orientation angle.
  phi: null                     # [radians] Orientation angle.
  psi: null                     # [radians] Orientation angle.
  user_set: false               # [logical] Is placement set by the user or computed?
```

When this group is contained in an element, the placement can either be set by the creator
of the lattice if `user_set` is set to `true`, or can be computed based upon the placement
of the upstream lattice elements of the branch the element is in. That is `user_set`
determines whether the `FloorP` parameters are inputs or outputs.

Also see [`ShiftedFloorP`](#s:shifted.floor.params) parameter group.
