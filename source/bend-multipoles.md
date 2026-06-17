(s:bend.multipoles)=
# Exact Multipole Fields in a Bend

For static magnetic and electric multipole fields in a bend with `ref_coords` set
to `arc`, the spatial dependence of the
field is different from multipole fields in an element with a straight geometry as given
by Eqs. {eq}`bbmult` and {eq}`exiey`. The analysis of the multipole fields in a bend here follows
McMillan {footcite:p}`McMillan:Multipoles`. Note: Whether the multipole coefficients represent
vertically pure or horizontally pure multipoles (see below) is by the `multipole_type` switch
of the [`BendP`](#s:bend.params) parameter group. See the `BendP` documentation for more details.


In the rest of this section, normalized coordinates {math}`\widetilde r = r / \rho`,
{math}`\widetilde x / = x / \rho`, and {math}`\widetilde y = y / \rho` will be used where 
{math}`\rho` is the bending radius of the reference coordinate system,
{math}`r` is the distance, in the plane of the bend, from the bend center to the observation point, 
{math}`x` is the distance, in the plane of the bend, from the referene coordinates to the observation point, 
and {math}`y` is the distance out-of-plane to the observation point. 
With this convention {math}`\widetilde r = 1 + \widetilde x`.

As McMillian shows, it is possible to calculate the magnetic field by constructing the
appropriate vector potential. However, from a practical point of view, it is simpler to use a
scalar potential {math}`\phi` for both the magnetic and electric fields with
the field given by {math}`-\nabla \phi`.  The potential is a solution to Laplace's equation
```{math}
  \frac{1}{\widetilde r} \, \frac{\partial}{\partial \, \widetilde r} 
  \left( \widetilde r \, \frac{\partial \, \phi}{\partial \, \widetilde r} \right) +
  \frac{\partial^2 \phi}{\partial \, \widetilde y^2} = 0
```

Solutions to Laplace's equation can be written in form
```{math}
:label: pspn1
  \phi_{n}^r = \frac{-1}{1+n} \sum_{p = 0}^{2p \le n+1} 
             \begin{pmatrix} n + 1 \cr 2 \, p \end{pmatrix} \,
             (-1)^{p} \, F_{n+1-2p}(\widetilde r) \, \widetilde y^{2p}
```
and in the form
```{math}
:label: pspn2
  \phi_{n}^i = \frac{-1}{1+n} \sum_{p = 0}^{2p \le n}
             \begin{pmatrix} n + 1 \cr 2p +1 \end{pmatrix} \,
             (-1)^{p} \, F_{n-2p}(\widetilde r) \, \widetilde y^{2p+1}
```
where {math}`\binom{a}{b}` ("a choose b") denotes a binomial coefficient, and {math}`n` is the order
number which can range from 0 to infinity.[^foot1] The functions {math}`\phi_{n}^r` and 
{math}`\phi_{n}^i` together form a complete set of solutions.
That is, any given field that satisfies
Maxwell's equations and is independent of {math}`z` can be expressed as a linear combination of
{math}`\phi_n^r` and {math}`\phi_n^i`. 

In {eq}`pspn1` and {eq}`pspn2` the {math}`F_p(\widetilde r)` are related by
```{math}
:label: fpp

  F_{p+2} = (p + 1) \, (p + 2) \, \int_1^{\widetilde r} \frac{d\widetilde r}{\widetilde r} 
  \left[ \int_1^{\widetilde r} d\widetilde r \, \widetilde r \, F_{p} \right]
```
with the "boundary condition":
```{math}
:label: f1fln

F_0(\widetilde r) &= 1 \nonumber \\
F_1(\widetilde r) &= \ln \, \widetilde r
```
This condition ensures that the number of terms in the sums in Eqs. {eq}`pspn1` and {eq}`pspn2`
are finite. With this condition, all the {math}`F_p` can be constructed:
```{math}
:label: ffff

F_1 &= \ln \, \widetilde r = \widetilde x - \frac{1}{2}\widetilde x^2 + \frac{1}{3}\widetilde x^3 - \ldots \\
F_2 &= \frac{1}{2} (\widetilde r^2 - 1) - \ln \widetilde r = \widetilde x^2 - \frac{1}{3}\widetilde x^3 + \frac{1}{4} \widetilde x^4 - \ldots \\
F_3 &= \frac{3}{2} [-(\widetilde r^2 - 1) + (\widetilde r^2 + 1) \ln \widetilde r] = \widetilde x^3 - \frac{1}{2} \widetilde x^4 + \frac{7}{20} \widetilde x^5 - \ldots
 \\
F_4 &= 3 [ \frac{1}{8} (\widetilde r^4 - 1) + \frac{1}{2} (\widetilde r^2 - 1) - (\widetilde r^2 + \frac{1}{2}) \ln \widetilde r] =
\widetilde x^4 - \frac{2}{5} \widetilde x^5 + \frac{3}{10} \widetilde x^6 - \ldots \\
&\text{Etc...}
```
Note: Care must be take when evaluating these functions near {math}`\widetilde x = 0` using the exact
{math}`\widetilde r`-dependent functions can be problematical due to round off error. 
For example, Evaluating {math}`F_4(\widetilde r)` at {math}`\widetilde x = 10^{-4}` results
in a complete loss of accuracy (no significant digits!) when using double precision numbers.

For magnetic fields, the "real" {math}`\phi_n^r` solutions will correspond to skew fields and the
"imaginary" {math}`\phi_n^i` solutions will correspond to normal fields
```{math}
:label: bpql

  {\bf B} = -\frac{P_0}{q \, L} \, 
    \sum_{n = 0}^\infty \rho^n \, \left[ a_n \, \widetilde \nabla \phi_n^r + b_n \, \widetilde \nabla \phi_n^i \right]
```
where the gradient derivatives of {math}`\widetilde \nabla` are with respect to the normalized
coordinates. In the limit of infinite bending radius {math}`\rho`, the above equations converge
to the straight line solution given in Eq. {eq}`bbmult`.

For electric fields, the "real" solutions will correspond to normal fields and the
"imaginary" solutions are used for skew fields
```{math}
:label: enrn

  {\bf E} = -\sum_{n = 0}^\infty \rho^n \, \left[ a_{en} \, \widetilde \nabla \phi_n^i + 
  b_{en} \, \widetilde \nabla \phi_n^r \right]
```
And this will converge to Eq. {eq}`exiey` in the straight line limit.

In the vertical plane, with {math}`\widetilde x = 0`, the solutions {math}`\phi_n^r` and {math}`\phi_n^i` have the same
variation in {math}`\widetilde y` as the multipole fields with a straight geometry. For example, the field
strength of an {math}`n = 1` (quadrupole) multipole will be linear in {math}`\widetilde y` 
for {math}`\widetilde x = 0`. However, in the
horizontal direction, with {math}`\widetilde y = 0`, the multipole field will vary 
like {math}`dF_2/d\widetilde x` which has
terms of all orders in {math}`\widetilde x`. In light of this, the solutions {math}`\phi_n^r` and 
{math}`\phi_n^i` are called "vertically pure" solutions.

The functions {math}`\phi_n^r` and {math}`\phi_n^i` form the a complete set of solutions but other
complete sets may be formed by defining basis functions which are linear combinations of 
{math}`\phi_n^r` and {math}`\phi_n^i`. In particular, 
it is possible to construct a complete set of "horizontally pure" solutions. 
That is, it is possible to
construct solutions {math}`\psi_n^r` and {math}`\psi_n^i` that in the horizontal plane, 
with {math}`\widetilde y = 0`, behave the same as the corresponding
multipole fields with a straight geometry. The relationship between the vertically pure solutions
and the horizontally pure solutions can be written in the form
```{math}
:label: p1rc

  \psi_n^r = \sum_{k = n}^\infty C_{nk} \, \phi_k^r, \qquad
  \psi_n^i = \sum_{k = n}^\infty D_{nk} \, \phi_k^i
```
For any given order {math}`n`, the {math}`C_{nk}` and {math}`D_{nk}` are determined up to an 
overall scaling factor. PALS sets this scaling factor by demanding
{math}`C_{nn} = D_{nn} = 1`.

The {math}`C_{nk}` and {math}`D_{nk}` are chosen, order
by order, so that {math}`\psi_n^r` and {math}`\psi_n^i` are horizontally pure. For the real
potentials, the {math}`C_{nk}`, are obtained from a matrix {math}`{\bf M}` where {math}`M_{ij}` is the
coefficient of the {math}`\widetilde x^j` term of {math}`(dF_i/d\widetilde x)`
when {math}`F_i` is expressed as an expansion in
{math}`\widetilde x` (Eq. {eq}`ffff`). {math}`C_{nk}`, {math}`k = 0, \ldots, \infty` 
are the row vectors of the inverse matrix {math}`{\bf M}^{-1}`. 
For the imaginary potentials, the {math}`D_{nk}` are constructed similarly
but in this case the rows of {math}`{\bf M}` are the coefficients in {math}`\widetilde x` for the functions {math}`F_i`.
To convert between field strength coefficients, Eqs. {eq}`bpql` and {eq}`enrn` and Eqs. {eq}`p1rc`
are combined
\begin{alignat}{3}
a_n &= \sum_{k = n}^\infty \frac{1}{\rho^{k-n}} \, C_{nk} \, \alpha_k, \quad
&a_{en} &= \sum_{k = n}^\infty \frac{1}{\rho^{k-n}} \, D_{nk} \, \alpha_{ek}, \nonumber \\
b_n &= \sum_{k = n}^\infty \frac{1}{\rho^{k-n}} \, D_{nk} \, \beta_k, \quad
&b_{en} &= \sum_{k = n}^\infty \frac{1}{\rho^{k-n}} \, D_{nk} \, \beta_{ek}
\end{alignat}
where {math}`\alpha_k`, {math}`\beta_k`, {math}`\alpha_{ek}`, and {math}`\beta_{ek}` are the corresponding coefficients
for the horizontally pure solutions.

When expressed as a function of {math}`\widetilde r` and {math}`\widetilde y`, 
the vertically pure solutions {math}`\phi_n` have a
finite number of terms (Eqs. {eq}`pspn1` and {eq}`pspn2`). On the other hand, the horizontally
pure solutions {math}`\psi_n` have an infinite number of terms.

An important point: To properly simulate a machine, one must first of all
understand whether the multipole values that have been handed to you are for horizontally
pure multipoles, vertically, pure multipoles, or perhaps the values do not correspond to
either horizontally pure nor vertically pure solutions! Failure to understand this point
can lead to differing results. For example, the chromaticity induced by a horizontally
pure quadrupole field will be different from the chromaticity of a vertically pure
quadrupole field of the same strength.

[^foot1]: Notice that here {math}`n` is related to {math}`m` in
McMillian's paper by {math}`m = n + 1`. Also note that the {math}`\phi^r` and {math}`\phi^i` 
here have a normalization factor that is different from McMillian.


```{footbibliography}
```
