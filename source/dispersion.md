(s:dispersion)=
# Dispersion

The dispersion {math}`\eta` is defined in the standard way
```{math}
:label: eedxdpz
  \text{eta_x} = \eta_x(s) \equiv \left. \frac{dx}{dp_z} \right|_s, \qquad
  \text{eta_y} = \eta_y(s) \equiv \left. \frac{dy}{dp_z} \right|_s
```

The associated momentum dispersion is:
```{math}
  \text{etap_x} = \eta_{px} \equiv \left. \frac{dp_x}{dp_z} \right|_s, \qquad 
  \text{etap_y} = \eta_{py} \equiv \left. \frac{dp_y}{dp_z} \right|_s \qquad 
```
The momentum dispersion is useful when constructing particle bunch distributions and for
various calculations like for calculating radiation integrals.

The one drawback with the momentum dispersion is that it is not always simply related to the
derivative of the dispersion {math}`d\eta/ds`. This becomes a factor when designing lattices where, if
some section of the lattice needs to be dispersion free, it is convienient to be able to optimize
{math}`d\eta/ds` to zero. The dispersion derivative is related to the momentum dispersion by
\begin{align}
\text{deta_x_ds} &\equiv \frac{d\eta_x}{ds}
= \frac{d}{dp_z} \left( \frac{dx}{ds} \right)
= \frac{d}{dp_z} \left( \frac{p_x}{1 + p_z} \right)
= \frac{1}{1 + p_z} \, \eta_{px} - \frac{p_x}{(1 + p_z)^2}  \nonumber \\
\text{deta_y_ds} &\equiv \frac{d\eta_y}{ds}
= \frac{d}{dp_z} \left( \frac{dy}{ds} \right)
= \frac{d}{dp_z} \left( \frac{p_y}{1 + p_z} \right)
= \frac{1}{1 + p_z} \, \eta_{py} - \frac{p_y}{(1 + p_z)^2}
\label{dexds}
\end{align}

For a lattice branch which is [non-periodic](#s:lattice.construct), the dispersion of the {math}`z` phase space
coordinate, {math}`\eta_z` can be defined similar to the dispersion of the other coordinates. In this
case, the dispersion vector {math}`{\bf\eta}` is defined by
```{math}
  {\bf\eta} = (\eta_x, \eta_{px}, \eta_{y}, \eta_{py}, \eta_z, 1)
```
and this vector is propagated via
```{math}
  {\bf\eta}(s_2) = {\bf M}_{21} \, {\bf\eta}(s_1)
```
where {math}`{\bf M}_{21}` is the transfer matrix between points {math}`s_1` and {math}`s_2`.

For a non-periodic lattice branch, there are two ways one can imagine
defining the dispersion: Either with respect to changes in energy at the beginning of the machine or
with respect to the local change in energy at the point of measurement. The former definition will
be called "non-local dispersion" and the latter definition will be called "local dispersion"
which what Bmad calculates. The non-local dispersion {math}`\widetilde{\bf\eta}(s_1)` at some point {math}`s_1` is
related to the local dispersion {math}`{\bf\eta}(s_1)` via
```{math}
  \widetilde{\bf\eta}(s_1) = \frac{dp_{z1}}{dp_{z0}} \, {\bf\eta}(s_1)
```
where {math}`s_0` is the {math}`s`-position at the beginning of the machine. The non-local dispersion has the
merit of reflecting what one would measure if the starting energy of the beam is varied. The local
dispersion, on the other hand, reflects the correlations between the particle energy and particle
position within a beam.

For a periodic lattice branch, defining the dependence of {math}`z` on {math}`p_z` is problematical.
With the RF off, {math}`z` is not periodic so a closed orbit {math}`z` cannot be defined.  With the RF on, the
dispersion of any of the phase space components is not well defined.  This being the case, {math}`\eta_z`
is just treated as zero for a closed branch.

Note: For a periodic branch with RF on, it is possible to define dispersions. If {math}`{\bf v}` is
the eigenvector of the eigenmode associated with longitudinal oscillations, the dispersion {math}`\eta_x`
can be defined by {math}`{\bf v}(1) / {\bf v}(6)` with similar definitions for the other dispersion components.
With this definition, the dispersion become complex. In the low RF limit, the dispersions {math}`\eta_x`,
{math}`\eta_{px}`, {math}`\eta_y`, {math}`\eta_{py}` converge to the standard (real) values and {math}`\eta_z` diverges
to infinity.\footnote
{
This is assuming a linear system. In practice, the motion will become unstable due to
the finite size of the RF bucket.

