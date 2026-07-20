(s:bend.params)=
## BendP: Bend Parameters

The `BendP` group stores the parameters that characterize the shape of a [`Bend`](#s:bend) element. 
The only relevant shape parameter that is not in the `BendP` is the
length `length` parameter.

```{code} yaml
BendP:
  angle_ref: 0             # [radian] Reference bend angle
  Bn0_ref: null            # [T] Reference bend field
  e1: null                 # [radian] Entrance end pole face rotation with respect to a sector geometry
  e2: null                 # [radian] Exit end pole face rotation with respect to a sector geometry
  e1_rect: null            # [radian] Entrance end pole face rotation with respect to a rectangular geometry
  e2_rect: null            # [radian] Exit end pole face rotation with respect to a rectangular geometry
  edge1_int: 0             # [T*m] Entrance end fringe field integral
  edge2_int: 0             # [T*m] Exit end fringe field integral
  g_ref: null              # [1/m] Reference bend strength = 1/radius_ref
  h1: 0                    # [1/m] Entrance end pole face curvature
  h2: 0                    # [1/m] Exit end pole face curvature
  Kn0_from_g_ref: true     # [logical] Default `Kn0` and `Bn0` values computed from `g_ref` and `Bn0_ref`?
  L_chord: null            # [m] Chord length. 
  L_sagitta:               # [m] Output parameter. Sagitta length.
  L_rectangle: null        # [m] Rectangular length. 
  multipole_geometry: follows_ref_geometry 
                           # [enum] Sets how multipoles are calculated.
  ref_geometry: arc        # [enum] Reference bend geometry.
  radius_ref: null         # [m] Reference bend radius.
  tilt_ref: 0              # [radian] Reference tilt
```

The geometry of a bend in [body](#s:coords) coordinates is shown in {numref}`f:bend`. 
In body coordinates, the rotation axis is, by definition, always the {math}`y`-axis.

```{figure} figures/bend.svg
:width: 90%
:name: f:bend
 
Bend geometry in body coordinates.
The red curve is the reference curve.
Red dots mark the entry {math}`(z_1, x_1)` and exit {math}`(z_2, x_2)` coordinate points.
The rotation axis, by definition, is parallel to the (out of the page) {math}`y`-axis.
Note: In general the rotation axis in **branch** coordinates will not be the {math}`y`-axis.
An exception to this is if `tilt_ref` is zero for all bends so that the
machine lies in the "horizontal" plane and in this case all the bend axes will be in the {math}`y`
direction.

A) Bend geometry for `ref_geometry` set to `arc` or `chord`. For the geometry shown,
`g_ref`, `angle_ref`, `radius_ref`, `e1`, `e2`, `e1_rect`, and `e2_rect` are all positive.

B) Same as (A) but with a negative bend angle. For the geometry shown,
`g_ref`, `angle_ref`, `radius_ref`, `e1`, `e2`, `e1_rect`, and `e2_rect` are all negative.

C) Bend geometry for `ref_geometry` set to `entrance_coords`.

D) Bend geometry for `ref_geometry` set to `exit_coords`.
```

 Dependent parameters calculation:

1. Consider three parameter sets: 

   {style=upper-alpha}
   1. `g_ref`, `Bn0_ref`, and `radius_ref`
   1. `length`, `L_chord`, and `L_rectangle`
   1. `angle_ref`

   Of all the parameters listed, only two parameters may be specified in the PALS file and
   these two parameters must be from different sets. From these two parameters all others can
   be computed. If less than two parameters are set. Default values for parameters that cannot
   be determined are zero.

2. Once the above parameters are computed, `e1_rect` can be computed from `e1` or vice versa
as appropriate (see below). Similarly for `e2_rect` and `e2`.

### `BendP` parameters

**Note:** In the equations below, {math}`q` is the charge of the reference particle 
and {math}`p_0` is the reference momentum.

- **angle_ref**

  The total reference bend angle. A positive `angle_ref` represents a
bend towards negative {math}`x` as shown in {numref}`f:bend`. 
`angle_ref = length * g_ref`.
%
- **Bn0_ref**

  The `Bn0_ref` parameter is the reference magnetic bending field which is the field
that is needed for the reference particle to be bent in a circle of radius `radius_ref`.
The direction of the reference bend field is along the {math}`y`-axis.
  ```{math}
  :label: bff

  \text{Bn0\_ref} = \frac{p_0}{q} \cdot \text{g\_ref}
  ```
%
- **e1, e2**

  `e1` and `e2` give the rotation angle of the entrance and exit pole faces
respectively with respect to the radial {math}`x_1` and {math}`x_2` axes as shown in {numref}`f:bend`.
Zero `e1` and `e2` gives a wedge shaped magnet.
Associated with these angles are the angles `e1_rect` and `e2_rect`.
With `ref_geometry` set to `arc` or `chord`, the relationship, as shown in {numref}`f:bend`A is
  ```{code} yaml
  e1 = e1_rect + angle_ref/2 
  e2 = e2_rect + angle_ref/2
  ```
  With `ref_geometry` set to `entrance_coords`, the relationship, as shown in {numref}`f:bend`C, is
  ```{code} yaml
  e1 = e1_rect
  e2 = e2_rect + angle_ref
  ```
  With `ref_geometry` set to `exit_coords`, the relationship, as shown in {numref}`f:bend`D, is
  ```{code} yaml
  e1 = e1_rect + angle_ref
  e2 = e2_rect
  ```

  The default values for `e1` and `e2` are determined by the setting of `ref_geometry` and the 
settings of `e1_rect` and `e2_rect`. If `e1_rect` is set, this determines the value of `e1` via
the above equations and similarly for `e2` and `e2_rect`. If neither `e1` nor `e1_rect` are set,
the value of `e1` is zero if `ref_geometry` is set to `arc` and `e1_rect` is zero if `ref_geometry`
is set to anything else. From this the angle not set can be determined from the above equations.
%
- **e1_rect, e2_rect**

  Face angle rotations like `e1` and `e2` except angles are measured with respect to
fiducial lines that are parallel to each other.
Zero `e1_rect` and `e2_rect` gives a rectangular magnet shape.
How the default values of `e1_rect` and `e2_rect` are determined is discussed above with
the `e1` and `e2` documentation.
%
- **edge1_int, edge2_int**

  The field integral for the entrance pole face `edge1_int` is given by
  ```{math}
  \text{edge1\_int} = \int_{\text{pole}} \!\! ds \frac{B_y(s) (B_{y0} - B_y(s))}{2 B_{y0}^2}
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
  C_1 = \frac{1}{2 \cdot \text{edge\_int}}
  ```
%
- **g_ref**

  `g_ref` = `1/radius_ref` is the reference "bend strength" which determines the curvature
of the reference arc (red lines in {numref}`f:bend`).
A positive `g_ref`, corresponds to the reference orbit bending in the {math}`-x` direction.

  `g_ref` is proportional to the reference dipole magnetic field `Bn0_ref`:
  ```{math}
  :label: gqpb

  \text{g\_ref} = \frac{q}{p_0} \cdot \text{Bn0\_ref}
  ```
  One common mistake when creating orbit bumps using a bend is to vary
`g_ref`. For this, `Kn0` should be varied.
The reason why changing `g_ref` is wrong is that variations in `g_ref` will change the 
[branch reference orbit](#s:ref.construct) and hence will move all downstream lattice elements in space.
%
- **h1, h2**

  The `h1` and `h2` parameters are the curvature of the entrance and exit pole faces. The radius of
curvature is `1/h1` and `1/h2` respectively. A value of zero implies that the face is flat.
Positive `h1` or `h2` implies the pole face is convex.
%
- **Kn0_from_g_ref**

  If set `true` (the default) the actual bending field which is `Kn0` and `Bn0`, if not set, 
will be computed from the reference bend field `g_ref` or `Bn0_ref`. 
The setting of `Kn0_from_g_ref` is irrelevant if either `Kn0` or `Bn0` is set. 
%
- **L_chord**

  `L_chord` is the chord length from entrance origin point to exit origin point 
(red dots in {numref}`f:bend`).
%
- **L_rectangle**

  "Rectangular" length of the bend. `L_rectangle` is depicted in figures {numref}`f:bend`C and {numref}`f:bend`D. 
`L_rectangle = radius_ref / sin(angle_ref)` independent of the setting of `ref_geometry`.
%
- **L_sagitta (output param)**

  The `L_sagitta` parameter is the sagitta length (The sagitta is the distance
from the midpoint of the reference arc curve to the midpoint of the chord). 
`L_sagitta` can be negative and will have the same sign as `g_ref`. 
%
- **multipole_geometry**

  The `multipole_geometry` parameter sets the geometry used to calculate multipoles.
Possible values of `multipole_geometry` are:
  ```{code} yaml
  follows_ref_geometry  # Default. Use geometry equivalent to the setting of `ref_geometry`.
  vertically_pure       # Vertically pure multipoles with arc geometry
  horizontally_pure     # Horizontally pure multipoles with arc geometry
  chord                 # Z-axis is the chord connecting the entrance origin point to the exit origin point.
  entrance_coords       # Rectangular coordinates commensurate with the entrance coordinates.
  exit_coords           # Rectangular coordinates commensurate with the exit coordinates.
  ```
See the [Exact Multipole Fields in a Bend](#s:bend.multipoles) section for documentation on horizontally
and vertically pure multipoles. The `follows_ref_geometry` choice means the multipole geometry
mirrors the setting of `ref_geometry`. Since `multipole_geometry` has no `arc` setting, if 
`ref_geometry` is set to `arc`, a setting of `multipole_geometry` to `follows_ref_geometry` is
equivalent to `vertically_pure`.
%
- **ref_geometry**

  The `ref_geometry` component switch specifies the curvilinear reference coordinates that multipoles are
calculated with respect to and sets the reference that `e1_rect` and `e2_rect` edge angles are measured
with respect to. Possible settings are:
  ```{code} yaml
  arc               # Default. Reference are the curvilinear arc coordinates.
  chord             # Z-axis is the chord connecting the entrance origin point to the exit origin point.
  entrance_coords   # Rectangular coordinates commensurate with the entrance coordinates.
  exit_coords       # Rectangular coordinates commensurate with the exit coordinates.
  ```
  In all cases, the reference coordinates {math}`y`-axis is parallel to the {math}`y`-axes of the 
body coordinate system.
%
- **radius_ref**

  `radius_ref` is the reference bending radius which determines the branch coordinate system (see
[](#s:coords)). `radius_ref = 1 / g_ref`. `radius_ref` may be infinite so it is generally better
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

