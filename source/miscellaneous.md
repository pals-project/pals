(c:misc)=
# Miscellaneous

%---------------------------------------------------------------------------------------------------
(s:set)=
## Set command

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter     # [String] Parmeter(s) to vary.
value         # [Expression] Value to set.
delta         # [Boolean] Default false. If false, parameter is set to value.
              #   If true, value is added to existing value of parameter.
```
In the `value` expression, the symbol `@` can be used for the value of the parameter being changed.
Example:
```{code} yaml
- Q1:
    kind: Quadrupole
    ...

- set:
    parameter: Q1.*>MagneticMultipoleP.Kn3
    value: 2 * @ 

- Lattice:
  - branches:
      - line1         # First branch
      ...             # More branches
```
In this example, the `Kn3` parameter of all elements whose name begins with `Q1` is doubled.
