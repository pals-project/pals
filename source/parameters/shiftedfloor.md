(s:shifted.floor.params)=
## ShiftedFloorP: Shifted Floor Parameters

The `ShiftedFloorP` parameter group holds parameters that describe the position and orientation,
taking into account any `BodyShiftP` and/or `Girder` shifts,
of the upstream end of a lattice element in the [global coordinate system](#s:floor).
Like `FloorP`, all of the `ShiftedFloorP` parameters are output parameters.

The components of this group are:
```{code} yaml
ShiftedFloorP:
  x                       # [m] Global x-coordinate.
  y                       # [m] Global y-coordinate.
  z                       # [m] Global z-coordinate.
  theta                   # [radians] Orientation angle.
  phi                     # [radians] Orientation angle.
  psi                     # [radians] Orientation angle.
```
All of these parameters are output parameters.
