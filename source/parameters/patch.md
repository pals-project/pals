%---------------------------------------------------------------------------------------------------
(s:patch.params)=
## PatchP:  Patch Parameters

```{figure} figures/patch.svg
:name: f:patch

A) A `Patch` element can align its exit face arbitrarily with respect to its entrance face. The
red arrow illustrates a possible particle trajectory form entrance face to exit face. B) The
reference length of a `Patch` element, if `ref_coords` is set to the default value of
`EXIT_END`, is the longitudinal distance from the entrance origin to the exit origin using the
reference coordinates at the exit end as shown. If `ref_coords` is set to `ENTRANCE_END`, the
length of the patch will be equal to the `z_offset`.
```

The `PatchP` parameter group describes the shift the reference curve of a `Patch` or element.
Also see [`ReferenceChangeP`](#s:ref.change.params) for the parameter group that can be used
to change reference time and/or energy. 
The components of `PatchP` are:
```{code} yaml
PatchP:
  x_offset          # [m] Offset in x-direction.
  y_offset          # [m] Offset in y-direction.
  z_offset          # [m] Offset in z-direction.
  x_rot             # [rad] Rotation around x-axis.
  y_rot             # [rad] Rotation around y-axis.
  z_rot             # [rad] Rotation around z-axis.
  flexible          # [logical] Default is False.
                    #    true -> User sets offsets and rot. 
                    #    False -> Offsets and rot from branch layout.
  ref_coords        # [enum] Coordinate system defining the length
  user_sets_length  # [logic] Default is False. Is the element length User set? 
```

The transformation from `Patch` entrance coordinates to exit coordinates is given by [](#wws)
with
```{math}
:label: lxyz

\begin{align}
  {\bf L} &= 
    \begin{pmatrix} 
      \text{x_offset} \\ \text{y_offset} \\ \text{z_offset} 
    \end{pmatrix}
    \\
  {\bf S} &= {\bf R}_{y} (\text{y_rot}) \; {\bf R}_{x} (\text{x_rot}) \; {\bf R}_{z} (\text{z_rot}) 
\end{align}
```

A straight line element like a `Drift` or a `Quadrupole` has the exit face parallel to the
entrance face. With a `Patch` element, the entrance and exit faces can be arbitrarily oriented
with respect to one another as shown in {numref}`f:patch`A.

There are two different ways the orientation of the exit face is determined. Which way is used is
determined by the setting of the `flexible` attribute. With the `flexible` attribute set to
`False`, the default, the exit face of the `Patch` will be determined from the offset, and rot
parameters. This type of `Patch` is called
"rigid" or "inflexible" since the geometry of the `Patch` is solely determined by the
`Patch`'s attributes as set in the lattice file and is independent of everything else. Example:
```{code} yaml
- pt
    kind: Patch
    PatchP:
      z_offset: 3.2 
```
Note: A `Patch` element with only a `z_offset`, like in the example, is equivalent to a drift
with the same length as the `z_offset` value.

With `flexible` set to `true`, the exit face is taken to be the reference frame of the
entrance face of the next element in the lattice. In this case, it must be possible to compute the
reference coordinates of the next element before the reference coordinates of the `Patch` are
computed. A `flexible` `Patch` will have its offsets, pitches, and tilt as dependent
parameters and these parameters will be computed appropriately. Here the
`Patch` is called "flexible" since the geometry of the patch will depend upon the geometry of
the rest of the lattice and, therefore, if the geometry of the rest of the lattice is modified (is
"flexed"), the geometry of the `Patch` will vary as well.

The coordinates of the lattice element downstream of a `flexible` `Patch` can be computed
if there is a [`Fiducial`](#s:fiducial) element somewhere downstream or if there is a
[`multipass_slave`](#c:multipass) element which is just downstream of the `Patch` or at
most separated by zero length elements from the `Patch`. In this latter case, the
`multipass_slave` must represent an {math}`N^{th}` pass slave with {math}`N` greater than 1. This works since
the first pass slave will be upstream of the `Patch` and so the first pass slave will have its
coordinates already computed and the position of the downstream slave will be taken to be the same
as the first pass slave. Notice that, without the `Patch`, the position of multipass slave
elements are independent of each other.

By default, there are no fields in the region of a `Patch` so A particle, starting at the upstream face of the
`Patch`, is propagated in a straight line to the downstream face. At the downstream end, a suitable coordinate
transformation must be made to translate the particle's coordinates from the upstream coordinate frame to
the downstream coordinate frame. In this case, the `Patch` element can be
thought of as a generalized `drift` element.

A `Patch` element can have an associated electric or magnetic field. 
A typical case, for example, is if a patch is used at the end of an injection line to match the reference
coordinates of the injection line to the line being injected into and the patch
element is within the field generated by an element in the line being injected into. In such a case,
it can be convenient to set what the reference coordinates are since the orientation of any fields
that are defined for a patch element will be oriented with respect to the patch element's reference
coordinates. For this, the `ref_coords`
parameter of a patch can be used. Possible settings are:
`ref_coords` are:
```{code} yaml
ENTRANCE_END  #
EXIT_END      # Default
```
The default setting of `ref_coords` is `EXIT_END` and with this the reference coordinates are
set by the exit end coordinate system (see {numref}`f:patch`). If `ref_coords` is set to
`ENTRANCE_END`, the reference coordinates are set by the entrance end coordinate system.

Unfortunately, there is no intuitive way to define the "`length`" of a patch. This is
important since the reference transit time is the element length divided by the
reference velocity. If the parameter `user_sets_length` is set to true, the
value of `length` set in the lattice file will be used (default is zero). `user_sets_length` is set
to False (the default), the length of a patch is calculated depending upon the setting of
`ref_coords`.  If `ref_coords` is set to `EXIT_END`, the length of the patch is calculated
as the perpendicular distance between the origin of the patch's entrance coordinate system and the
exit face of the patch as shown in {numref}`f:patch`B. If `ref_coords` is set to `ENTRANCE_END`,
the length is calculated as the perpendicular distance between the entrance face and the origin of
the exit coordinate system. In this case, the length will be equal to `z_offset`.

Note: To shift the reference energy, time, or species, use the 
[ReferenceChangeP](#s:ref.change.params) parameter group.
The `extra_dtime_ref` of the `ReferenceChageP` group can be used to set
the change in reference time through a patch. The difference between using `extra_dtime_ref` and
`length` is that the reference time change using `extra_dtime_ref` is independent of the reference 
velocity while with `length` there is a dependence upon the reference velocity. 
