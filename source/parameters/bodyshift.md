(s:bodyshift.params)=
## BodyShiftP: Element Body Orientation and Position Parameters

Parameters describing the alignment of the physical element with respect to the element's nominal 
position. The nominal position is set by the [branch coordinate system](#c:coords).
This parameter group can be used to simulate positional errors. See section [](#s:lab.body.transform)
for documentation on the body shift transformation equations.

The components of this group and their defaults are:
```{code} yaml
BodyShiftP:
  x_offset: 0       # [m] Offset along x-axis
  y_offset: 0       # [m] Offset along y-axis
  z_offset: 0       # [m] Offset along z-axis
  x_rot: 0          # [rad] Rotation around x-axis
  y_rot: 0          # [rad] Rotation around y-axis
  z_rot: 0          # [rad] Rotation around z-axis
```

```{figure} figures/straight-align.svg
:width: 90%
:name: f:straight-align

Figures illustrating how alignment parameters affect the position of straight-line
elements. A) Effect of `x_offset` and `y_rot`, B) Effect of `z_rot`.
```

For straight-line elements, that is for all elements where the curvilinear coordinate system
through the element is a straight line, 
positioning is measured using a with respect to the center of the element.
This is illustrated in figure {numref}`f:straight-align`. {numref}`f:straight-align`A shows the
effect of `x_offset` and `y_rot` parameters. {numref}`f:straight-align`B shows the effect of `z_rot`.

```{figure} figures/bend-align.svg
:width: 40%
:name: f:bend-align

For a bend element, the coordinate system used for positioning has origin at the center of the 
bend chord with the `z`-axis along the chord. Shown is the situation where, with `tilt_ref` zero,
the plane of the bend is the {math}`x-z` plane.
```

For a bend element, the coordinate system used for positioning has origin at the center of the 
bend chord with the `z`-axis along the chord as shown in {numref}`f:bend-align`. If the
[`tilt_ref`](#s:bend.params) parameter (which does not shift the element with respect to the branch
coordinate system but rather shifts the branch coordinate system itself) is zero, the plane
of the bend corresponds to the `x-z` plane.

Note: Using the center of the arc for the origin of the alignment coordinate system is also a
possible logical choice. The center of the chord was chosen for the center for a practical reason:
A very common misalignment for bends is a rotation of the bend along the chord axis. That is,
with the present choice, a pure `z_rot` misalignment. If the center of the arc were chosen,
such a misalignment would need offsets added to keep the bend end points invariant.