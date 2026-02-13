(c:misc)=
# Miscellaneous

%---------------------------------------------------------------------------------------------------
(s:set)=
## Set command

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter     # [String] Parmeter(s) to vary.
value         # [Expression] Value to set.
```
In the `value` expression, the symbol `@Param` can be used for the current value of the parameter being changed
and `@Ele` can be used for the lattice element whose parameter is being changed. 
Example:
```{code} yaml
- B1a:
    kind: Bend
    BendP:
      e1: 0.1
      g_ref: 0.02

- set:
    parameter: B1.*>BendP.e1
    value: 2*@Param + atan(@Ele.BendP.g_ref)
```
In this example, the `BendP.e1` parameter of all elements whose name begins with `B1` is modified.
This includes element `B1a`. 

Note: Grep (pattern matching) is not used in `value` expressions.
