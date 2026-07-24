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
In the `value` expression, `parameter` can be used for the current value of the parameter being changed
and `self` can be used for the lattice element whose parameter is being changed. 
Example:
```{code} yaml
- B1a:
    kind: Bend
    BendP:
      e1: 0.1 / c_light
      g_ref: 0.02

- set:
    parameter: B1.*>BendP.e1
    value: 2*parameter + atan(self.BendP.g_ref)
```
In this example, the `BendP.e1` parameter of all elements whose name begins with `B1` is modified.
This includes element `B1a`. 

Note: Pattern matching is not supported in the `value` expression.

For sets that only have a value, an alternative compact form has the syntax:
```{code} yaml
- sets:
    - param1: value1
    - param2: value2
    ...
```
