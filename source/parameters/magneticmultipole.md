(s:mag.mult.params)=
## MagneticMultipoleP: Magnetic Multipole Parameters

The `MagneticMultipoleP` parameter group describes magnetic multipoles associated with the lattice
element. For a multipole of order `N`, the magnetic field {math}`(B_x, B_y)`
at a point {math}`\bf r` in terms of the points polar coordinates {math}`(r, \theta)` is
```{math}
:label: bbmult

B_y({\bf r}) + i \, B_x({\bf r}) = 
\frac{1}{N!}(B_n + i \, B_s) \, e^{-i(N+1)T} \, e^{iN\theta} \, r^N
```
where {math}`T` is the "tilt" of the `N`{sup}`th` multipole and {Math}`B_n` and {math}`B_s` are
the normal and skew components of the field. `N` is defined such that 
{math}`N = 0` describes a dipolar multipole, {math}`N = 1` describes a quadrupolar multipole, etc.

The three parameters, {math}`T`, {Math}`B_n` and {math}`B_s` are not independent and only two
are needed to specify a multipole. 
However, it is sometimes convenient to use all three. 
For example, {Math}`B_n` and {math}`B_s` with {math}`N=0` can be used to describe 
an element with independent horizontal and vertical steerings while {math}`T` can be used
to represent rotational errors.

The components of `MagneticMultipoleP` for specifying a multipolar field of order `N` is:
```{code} yaml
tiltN     # Tilt
BnN       # Normal component 
BsN       # Skew component
```

Alternatively, the field components can be specified using normalized values
```{code} yaml
KnN       # Normalized normal component 
KsN       # Normalized skew component
```
where the conversion between field and normalized components is:
```{math}
  (K_n, K_s) = \frac{q}{P_0} \, (B_n, B_s)
```
with {math}`q` being the charge of the reference particle and {math}`P_0` being the 
reference momentum.

Furthermore, the field and normalized values can be given in terms of the integrated strength.
Integrated values are specified with the letter 
`L` appended at the end of the name. Example:
```{code} yaml
MagneticMultipoleP:
  tilt7: 0.7        # Tilt of 7th order multipole
  Bn3: 27.3         # Normal multipole component of order 3.
  Bn2L: 3.47e1      # length integrated normal multipole component of order 2.
```
The length integrated values are related to the non-integrated values via
```{code} yaml
  (BnL, BsL, KnL, KsL) = length * (Bn, Bs, Kn, Ks)
```
where `length` is the length of the element.

For a given element, when specifying a multipole of a given order, 
the two strength components must be of the same type.
That is, it is not permitted for one component to be length integrated and the other not,
as well as it is not permitted for one component to be a field and the other component to be normalized.
However, the multipole components of different order do not have to be of the same type.

With a `bend` element, the reference line about which the multipoles are referenced to
may be curved. This is set by the `ref_geometry` parameter of the [`BendP`](#s:bend.params)
parameter group. If `ref_geometry` is set to `arc`, the `multipole_type` parameter of
`BendP` will set how the multipoles are evaluated. See the `BendP` documentation for more details.

"Tapering parameters" account for the fact that, due to synchrotron radiation, the energy of a
beam at a particular point can be different from the reference value. There is an
associated tapering parameter for all of the field parameters:
```{code} yaml
Parameter       Associated Tapering Parameter
  BnN             BnN_taper
  BsN             BsN_taper
  KnN             KnN_taper
  KsN             KsN_taper
```
Additionally, there are four length integrated tapering parameters corresponding to the four
length integrated field parameters. The actual (total) field is the sum of the field plus
the tapering field. For example:
```{code} yaml
Bs2 (actual) = Bs2 + Bs2_taper
```
