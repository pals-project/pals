(s:shifted.floor.params)=
## ShiftedFloorP: Shifted Floor Parameters

The `ShiftedFloorP` parameter group holds parameters that describe the position and orientation,
taking into account any `BodyShiftP` and/or `Girder` shifts,
of the upstream end of a lattice element in the [global coordinate system](#s:floor).
Unlike `FloorP`, whose parameters can be user set, all of the `ShiftedFloorP` parameters are output parameters.

The components of this group are:
```{code} yaml
ShiftedFloorP:
  X:                      # [m] Global X-coordinate.
  Y:                      # [m] Global Y-coordinate.
  Z:                      # [m] Global Z-coordinate.
  theta:                  # [rad] Orientation angle.
  phi:                    # [rad] Orientation angle.
  psi:                    # [rad] Orientation angle.
```
