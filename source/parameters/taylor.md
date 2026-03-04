(s:taylor.params)=
## TaylorP: Taylor Map Parameters

The `TaylorP` group stores a Taylor transport map. This includes both orbital phase space 
and spin components of the particle.
The components of `TaylorP` are:
```{code} yaml
TaylorP:
  x_out:      # [Struct] Taylor series for output x orbital component.
  px_out:     # [Struct] Taylor series for output px orbital component.
  y_out:      # [Struct] Taylor series for output y orbital component.
  py_out:     # [Struct] Taylor series for output py orbital component.
  z_out:      # [Struct] Taylor series for output z orbital component.
  pz_out:     # [Struct] Taylor series for output pz orbital component.
  S1_out:     # [Struct] Taylor series for output S1 quaternion component.
  Sx_out:     # [Struct] Taylor series for output Sx quaternion component.
  Sy_out:     # [Struct] Taylor series for output Sy quaternion component.
  Sz_out:     # [Struct] Taylor series for output Sz quaternion component.
  ref_in:     # [Struct] Input orbital reference point for the map. 
```
Here "input" refers to the starting coordinates at the beginning of the element,
and "output" referes to the ending coordinates at the end of the element.
The particular definition of the orbital components is given by the 
[`phase_space_coordinates`](#s:phase.space) node. The spin rotation map is represented
using [quaternions](#s:spin).

Each Taylor series structure has a set of monomial `term` nodes with the syntax:
```{code} yaml
term <coef> <e1> <e2> <e3> <e4> <e5> <e6>
```
Each `term` specifies a real valued coefficient `<coef>` and six integer exponents 
`<e1>` through `<e6>`.
Example:
```{code} yaml
T9:               # Taylor element
  kind Taylor
  TaylorP:
    x_out:
      term 3.4 1 0 0 2 0 1
      term ...
    y_out:
      ...
```
The term `term 3.4 1 0 0 2 0 1` represents the monomial {math}`3.4 \cdot x \cdot p_y^2 \cdot p_z`
for the Taylor series for the output value of the orbital {math}`x` component. 
Note that the spin transport is independent of the input spin coordinates. 
In other words, Stern-Gerlach effects are ignored.

The `ref_in` component of `TaylorP` gives the orbital reference point about which the
taylor map is constructed. The components of ref_in are:
```{code} yaml
x:      # x orbital component
px:     # px orbital component
y:      # y orbital component
py:     # py orbital component
z:      # z orbital component
pz:     # pz orbital component
```
Example:
```{code} yaml
TaylorP:
  ref_in:
    x: 0.034
    px: 0.02
    ...
```

