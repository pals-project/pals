(s:elec.mult.params)=
## ElectricMultipoleP:  Electric Multipole Parameters

The `ElectricMultipoleP` parameter group describes electric multipoles associated with the lattice
element. For a multipole of order `N`, the electric field {math}`(E_x, E_y)`
at a point {math}`\bf r` in terms of the points polar coordinates {math}`(r, \theta)` is
```{math}
:label: exiey
  E_x({\bf r}) - i \, E_y({\bf r}) = 
  \frac{1}{N!}(E_n - i \, E_s) \, e^{-i(N+1)T} \, e^{iN\theta} \, r^N
```
where {math}`T` is the "tilt" of the `N`{sup}`th` multipole and {Math}`E_n` and {math}`E_s` are
the normal and skew components of the field. `N` is defined such that 
{math}`N = 0` describes a dipolar multipole, {math}`N = 1` describes a quadrupolar multipole, etc.

The three parameters, {math}`T`, {Math}`E_n` and {math}`E_s` are not independent and only two
are needed to specify a multipole. 
However, it is sometimes convenient to use all three. 
For example, {Math}`E_n` and {math}`E_s` with {math}`N=0` can be used to describe 
an element with independent horizontal and vertical steerings while {math}`T` can be used
to represent rotational errors.

The components of `ElectricMultipoleP` for specifying a multipolar field of order `N` is:
```{code} yaml
  tiltN: 0                  # [Radians] Tilt
  EnN: 0                    # [V/m^(N+1)] Normal component
  EsN: 0                    # [V/m^(N+1)] Skew component
  EnNL: 0                   # [V/m^N] Length integrated normal component 
  EsNL: 0                   # [V/m^N] Length integrated skew component
```

The field and normalized values can be given in terms of the integrated strength.
Integrated values are specified with the letter 
`L` appended at the end of the name. Example:
```{code} yaml
emp1:
  kind: Bend
  length = 0.86
  ElectricMultipoleP:
    tilt7: 0.7        # Tilt in raidians of 7th order multiple
    En3: 27.3         # Normal multipole component of order 3 in V/m^4
    En2L: 3.47e1      # Length integrated normal multipole component of order 2 in V/m^2
    geometry: vertically_pure   # See below
```
The length integrated values are related to the non-integrated values via
```{code} yaml
  (EnL, EsL) = length * (En, Es)
```
where `length` is the length of the element.

For a given element, when specifying a multipole of a given order, 
the two strength components must be of the same type.
That is, it is not permitted for one component to be length integrated and the other not,
However, the multipole components of different order do not have to be of the same type.

With a `bend` element, the reference line about which the multipoles are referenced to
may be curved. This is set by the `ref_geometry` parameter of the [`BendP`](#s:bend.params)
parameter group. If `ref_geometry` is set to `arc`, the `multipole_type` parameter of
`BendP` will set how the multipoles are evaluated. See the `BendP` documentation for more details.
