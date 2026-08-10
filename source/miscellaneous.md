(c:misc)=
# Miscellaneous

%---------------------------------------------------------------------------------------------------
(s:set)=
## Setting Parameters

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter               # [String] Parameter(s) to vary.
value                   # [Expression] Value to set.
absolute_error: 0       # Absolute error.       
relative_error: 0       # [-] Relative error.
```
If both `absolute_error` and `relative_error` are specified, 
the true error is `absolute_error + relative_error * |value|`.
In the `value` expression, `PARAMETER` can be used for the current value of the parameter being changed
and `SELF` can be used for the lattice element whose parameter is being changed.
Example:
```{code} yaml
- B1a:
    kind: Bend
    BendP:
      e1: 0.1
      g_ref: 0.02

- set:
    parameter: B1.*>BendP.e1
    value: 2*PARAMETER + atan(SELF.BendP.g_ref)
```
In this example, the `BendP.e1` parameter of all elements whose name begins with `B1` is modified.
This includes element `B1a`. Notice that when a set of parameters is being changed, as in this example,
the value of `PARAMETER` used can be different for different parameters in the set. 

For any group of interdependent parameters, the setting of one member of the group nullifies previous
settings of all other members of the group. For example,
```{code} yaml
- s1:
    kind: Sextupole
    length: 0.27
    MagneticMultipoleP:
      Ks2: 0.34

- set:
    parameter: s1>MagneticMultipoleP.Ks2L
    value: ...
```
Here the `Ks2` value of `s1` has been set in the definition of `s1`. When the
`set` of `Ks2L` is done, this nullifies the setting of `Ks2` so that there
is no inconsistency. Note that for the sextupole skew multipole, 
there are four interdependent parameters: `Ks2`, `Ks2L`, `Bs2`, `Bs2L`.


Note: Pattern matching is not supported in the `value` expression.

For sets that only have a value, an alternative compact form has the syntax:
```{code} yaml
- sets:
    - param1: value1
    - param2: value2
    ...
```
