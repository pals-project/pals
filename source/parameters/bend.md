(s:bend.params)=
## BendP: Bend Parameters

The `BendP` group stores the parameters that characterize the shape of a [`Bend`](#s:bend) element. 
The only relevant shape parameter that is not in the `BendP` is the
length `length` parameter.

```{code} yaml
BendP:
  angle_ref: 0             # [radian] Reference bend angle
  bend_field_ref: 0        # [T] Reference bend field
  bend_field_actual:       # [T] Output param. Actual bend field perpendicular to the reference plane. 
  e1: 0                    # [radian] Entrance end pole face rotation with respect to a sector geometry
  e2: 0                    # [radian] Exit end pole face rotation with respect to a sector geometry
  e1_rect: 0               # [radian] Entrance end pole face rotation with respect to a rectangular geometry
  e2_rect: 0               # [radian] Exit end pole face rotation with respect to a rectangular geometry
  edge1_int: 0             # [T*m] Entrance end fringe field integral
  edge2_int: 0             # [T*m] Exit end fringe field integral
  g_ref: 0                 # [1/m] Reference bend strength = 1/radius_ref
  g_actual:                 # [1/m] Output param. Actual bending strength corresponding to `bend_field_actual`.
  multipole_type: vertically_pure # [enum] Only relavent if `ref_coords` is set to `arc`.
  h1: 0                    # [1/m] Entrance end pole face curvature
  h2: 0                    # [1/m] Exit end pole face curvature
  L_chord: 0               # [m] Chord length. 
  L_sagitta: 0             # [m] Sagitta length. Output parameter.
  L_rectangle: 0           # [m] Rectangular length. 
  ref_coords: arc          # [enum] Reference coordinates type.
  rho_ref: null            # [m] Reference bend radius.
  tilt_ref: 0              # [radian] Reference tilt
```

The geometry of a bend in [body](#s:coords).  coordinates is shown in {numref}`f:bend`. 
In body coordinates the rotation axis is, by definition, always the {math}`y`-axis.
Note that in general the rotation axis in branch coordinates will not be the {math}`y`-axis.
An exception to this is if `tilt_ref` is zero for all bends so that the
machine lies in the "horizontal" plane.

Note: In the equations below, {math}`q` is the charge of the reference particle 
and {math}`p_0` is the reference momentum.

Note: The attributes `g_ref`, `angle_ref`, `rho_ref` and `length` are mutually dependent. Specifying
more than two of these can be contradictory.

```{figure} figures/bend.svg
:width: 90%
:name: f:bend
 
Bend geometry in body coordinates.
The red curve is the reference curve.
Red dots mark the entry {math}`(z_1, x_1)` and exit {math}`(z_2, x_2)` coordinate points.
The rotation axis is parallel to the (out of the page) {math}`y`-axis.

A) Bend geometry for `ref_coords` set to `arc` or `chord`. For the geometry shown,
`g_ref`, `angle_ref`, `rho_ref`, `e1`, `e2`, `e1_rect`, and `e2_rect` are all positive.

B) Same as (A) but with a negative bend angle. For the geometry shown,
`g_ref`, `angle_ref`, `rho_ref`, `e1`, `e2`, `e1_rect`, and `e2_rect` are all negative.

C) Bend geometry for `ref_coords` set to `entrance_coords`.

D) Bend geometry for `ref_coords` set to `exit_coords`.
```

In detail:
- **angle_ref**

  The total Reference bend angle. A positive `angle_ref` represents a
bend towards negative {math}`x` as shown in {numref}`f:bend`. 
`angle_ref = length * g_ref`.
%
- **bend_field_ref**

  The `bend_field_ref` parameter is the reference magnetic bending field which is the field
that is needed for the reference particle to be bent in a circle of radius `rho_ref`.
The direction of the reference bend field along the {math}`y`-axis.
  ```{math}
  :label: bff

  \text{bend\_field\_ref} = \frac{p_0}{q} \cdot \text{g\_ref}
  ```
  Also see `g_ref`, `g_actual`, and `bend_field_actual`.
%
- **bend_field_actual (output param)**

  The actual dipole field is the sum of the reference bend field given by `bend_field_ref` 
plus any additional zeroth order multipole field component that can be specified using `Bn0`, `Bs0`, and `tilt0`.
The component of the actual bend field in the {math}`y`-dirction is given by `bend_field_actual`:
  ```{code} yaml
  bend_field_actual = bend_field_ref + Bn0 * cos(tilt0) + Bs0 * sin(tilt0)
  ```
  The {math}`(x,z)` in-bend-plane dipole component is given by `Bs0 * cos(tilt0)`. 
The orientation of this in-plane component is determined by the setting of `ref_coords`.
%
- **e1, e2**

  `e1` and `e2` give the rotation angle of the entrance and exit pole faces
respectively with respect to the radial {math}`x_1` and {math}`x_2` axes as shown in {numref}`f:bend`.
Zero `e1` and `e2` gives a wedge shaped magnet.
Also see `e1_rect` and `e2_rect`. 
With `ref_coords` set to `arc` or `chord`, the relationship, as shown in {numref}`f:bend`A is
  ```{code} yaml
  e1 = e1_rect + angle_ref/2 
  e2 = e2_rect + angle_ref/2
  ```
  With `ref_coords` set to `entrance_coords`, the relationship, as shown in {numref}`f:bend`C, is
  ```{code} yaml
  e1 = e1_rect
  e2 = e2_rect + angle_ref
  ```
  With `ref_coords` set to `exit_coords`, the relationship, as shown in {numref}`f:bend`D, is
  ```{code} yaml
  e1 = e1_rect + angle_ref
  e2 = e2_rect
  ```
%
- **e1_rect, e2_rect**

  Face angle rotations like `e1` and `e2` except angles are measured with respect to
fiducial lines that are parallel to each other.
Zero `e1_rect` and `e2_rect` gives a rectangular magnet shape.
%
- **edge1_int, edge2_int**

  The field integral for the entrance pole face `edge1_int` is given by
  ```{math}
  \text{edge1\_int} = \int_{pole} \!\! ds \frac{B_y(s) (B_{y0} - B_y(s))}{2 B_{y0}^2}
  ```
  For the exit pole face there is a similar equation for `edge2_int`

  Note: In Bmad and MAD, these integrals are represented by the product of `fint * hgap`.

  `edge1_int` and `edge2_int` can be related to the Enge function which is sometimes used to model the
  fringe field. The Enge function is of the form
  ```{math}
  B_y(s) = \frac{B_{y0}}{1 + \exp[P(s)]}
  ```
  ```{math}
  P(s) = C_0 + C_1 \cdot s + C_2 \cdot s^2 + C_3 \cdot s^3 + \ldots
  ```
  The {math}`C_0` term simply shifts where the edge of the bend is. If all the {math}`C_n` are zero except for
  {math}`C_0` and {math}`C_1` then
  ```{math}
  C_1 = \frac{1}{2 \cdot \text{field\_int}}
  ```
%
- **g_ref**

  `g_ref` = `1/rho_ref` is the reference "bend strength" which determines the curvature
of the reference arc (red lines in {numref}`f:bend`).
A positive `g_ref`, corresponds to the reference orbit bending in the {math}`-x` direction.

  `g_ref` is proportional to the reference dipole magnetic field `bend_field_ref`:
  ```{math}
  :label: gqpb


  \text{g\_ref} = \frac{q}{p_0} \cdot \mathrm{bend\_field\_ref}
  ```
  One common mistake when creating orbit bumps using a bend is to vary
`g_ref`. For this, `Kn0` should be varied.
The reason why changing `g_ref` is wrong is that variations in `g_ref` will change the 
[branch reference orbit](#s:ref.construct) and hence will move all downstream lattice elements in space.
%
- **g_actual (output param)**

  The bend strength corresponding to `bend_field_actual`.
  ```{math}
  :label: g_actual

  \text{g\_actual} = \frac{q}{p_0} \cdot \text{bend\_field\_actual}
  ```
  Also see `g_ref`.
%
- **h1, h2**

  The `h1` and `h2` parameters are the curvature of the entrance and exit pole faces. The radius of
curvature is `1/h1` and `1/h2` respectively. A value of zero implies that the face is flat.
Positive `h1` or `h2` implies the pole face is convex.
%
- **L_chord**

  `L_chord` is the chord length from entrance origin point to exit origin point 
(red dots in {numref}`f:bend`).
%
- **L_rectangle**

  "Rectangular" length of the bend. See figures {numref}`f:bend`B and {numref}`f:bend`C. 
The `L_rectangle = rho_ref / sin(angle)` independent of the setting of `ref_coords`.
%
- **L_sagitta (output param)**

  The `L_sagitta` parameter is the sagitta length (The sagitta is the distance
from the midpoint of the reference arc curve to the midpoint of the chord). 
`L_sagitta` can be negative and will have the same sign as `g_ref`. 
%
- **multipole_type**

  The `multipole_type` parameter is only relavent if `ref_coords` is set to `arc` so
that the multipole reference curve is not a straight line. 
`ref_coords` sets how multipole coefficients are to be evaluated. 
Possible values of `multipole_type` are:
  ```{code} yaml
    vertically_pure     # Vertically pure multipoles (default).
    horizontally_pure   # Horizontally pure multipoles.
  ```
See [Exact Multipole Fields in a Bend](#s:bend.multipoles) section for more details.
%
- **ref_coords**

  The `ref_coords` component switch specifies the curvelinear reference coordinates that multipoles are
calculated with respect to and sets the reference that `e1_rect` and `e2_rect` edge angles are measured
with respect to. Possible settings are:
  ```{code} yaml
  arc               # Default. Curvelinear coordinates of the circular arc of the reference curve. 
  chord             # Z-axis is the chord connecting the entrance origin point to the exit origin point.
  entrance_coords   # Entrance coordinates.
  exit_coords       # Exit coordinates.
  ```
  In all cases, the reference coordinates {math}`y`-axis are parallel to the {math}`y`-axes of the 
body coordinate system.
%
- **rho_ref**

  `rho_ref` is the reference bending radius which determines the branch coordinate system (see
[](#s:coords)). `rho_ref = 1 / g_ref`. `rho_ref` may be infinite so it is generally better
to work with `g_ref`.
%
- **tilt_ref**

  The `tilt_ref` attribute rotates a bend about the longitudinal axis at the entrance face of the
bend as explained in [](#s:ent.exi). It is important to understand that `tilt_ref`,
unlike the `tilt` attribute of other elements, bends both the reference orbit along with the
physical element.
  Important! Do not use `tilt_ref` when doing misalignment studies for a machine. Trying to misalign
a dipole by setting `tilt_ref` will affect the positions of all downstream elements! Rather, use the
`z_rot` parameter in the `BodyShiftP` group.

%---------------

