(c:misc)=
# Miscellaneous

%---------------------------------------------------------------------------------------------------
(s:set)=
## Setting Parameters

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter               # [String] Parmeter(s) to vary.
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
      e1: 0.1
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

%---------------------------------------------------------------------------------------------------
(s:controller)=
## Controllers

A `Controller` is a construct that essentially bundles expressions used to set lattice
parameter values into one "package". 
While expressions can be used in place of controllers, 
controllers add a level of organization and modularity that make them useful constructs. 
Controllers typically represent a physical object like a power supply controlling magnet elements
in a machine. Example:
```{code} yaml
facility:
  - ps27:                             # Controller name
      kind: Controller
      control_type: ABSOLUTE           # Or RELATIVE.
      variables:
        cur1: 0.023
        cur2: cur1 / c_light
        ...
      controls:
        - parameter: Qa.*>MagneticMultipoleP.Ks2L  # Parameter control specification.
          expression: 0.075*sin(cur1) + 0.3*cur2
        - parameter: ...                           # Another specification
          expression: ...   
        ...
```
In this example, a controller called `ps27` has two variables used to control parameters called
`cur1` and `cur2`. Initial values can be set for variables. The default value of a variable is zero.
The parameters controlled are set by the `controls` component. Each entry has a 
`parameter` component giving the [regular expression](#s:parameter.matching) to 
match parameters to and an `expression` component that gives the arithmetic expression
used in setting the parameters matched to. 
In the above example, the first `controls` entry will match to the `Ks2L` 
component of all elements whose name begins with `Qa`, and the associated expression
is `0.075*sin(cur1) + 0.3*cur2`.

Controllers can control the variables of other controllers. The syntax for a controller 
variable is:
```{code} yaml
{controller-name}>{variable-name}
```
So, for example, with the above example, outside of the `ps27` controller the `cur1` variable
has the name `ps27>cur1`. While controllers can control the variables of other controllers,
circular definitions are not allowed.

There are two types of controllers that are differentiated by the setting of the controller's
`control_type` parameter. The possible settings of `control_type`:
```{code} yaml
ABSOLUTE          # Default. Absolute control.
RELATIVE          # Relative control.
```

`RELATIVE` type controllers are meant for simulating something like a control system orbit bump knob
where a change in the knob value results in changes to a set of steerings that are used to
locally change the orbit in a section of a machine. Example:
```{code} yaml
facility:
  - chrom_a:
      kind: Controller
      control_type: RELATIVE
      variables:
        command: 0.4
      controls:
        - parameter: S1>MagneticMultipoleP.Kn2L
          expression: 5.62 * command + 0.02 * command^2
        - parameter: S2>MagneticMultipoleP.Kn2L
          expression: -4.72 * command + 0.13 * command^2
        ...

  - S1:
      kind: Sextupole
      MagneticMultipoleP:
        Kn2L: 0.33
```
Here `chrom_a` is a knob for controlling the chromaticity in a ring. `chrom_a` has a
variable `command` and varies a set of sextupoles. When the PALS file is read in, the
sextupole `Kn2L` strengths are set by the values in the elements themselves. In the above
example, the initial setting of `Kn2L` for element `S1` will be 0.33. After the lattice has
been read in by a simulation program, variation of the `command` setting of `chrom_a` will
result in variation of the controlled `Kn2L` parameter values. In the example, if the `command`
value is changed from `v1` (which is 0.4 at the beginning) to some other value `v2` the change
in `Kn2L` of `S1` will be:
```{code} yaml
change in MagneticMultipoleP.Kn2L = (5.62*v2 + 0.02*v2^2) - (5.62*v1 + 0.02*v1^2)
```

`ABSOLUTE` type controllers are meant for simulating something like power supplies controlling 
magnet strengths where the setting of the power supplies completely determine the magnet strengths.
Example:
```{code} yaml
facility:
  - ps1: 
      kind: Controller
      control_type: ABSOLUTE
      variables:
        cur: 0.023
      controls:
        - parameter: a_kicker>MagneticMultipoleP.Kn0
          expression: 0.075*sin(cur)
        ...

  - ps2:
      kind: Controller
      control_type: ABSOLUTE
      variables:
        cur: 0.044
      controls:
        - parameter: a_kicker>MagneticMultipoleP.Kn0
          expression: 0.123*cur
        ...
```
Here two controllers control the `Kn0` parameter of the `a_kicker` element.
In a case where there are multiple `ABSOLUTE` controllers controlling the same parameter,
the value of the parameter is the sum of the values set by the individual controllers.
In the present example, the value of `Kn0` for `a_kicker` would be:
```{code} yaml
a_kicker>MagneticMultipoleP.Kn0 = 0.075*sin(ps1>cur) + 0.123*ps2>cur
```

A given lattice parameter may be controlled by multiple `ABSOLUTE` controllers or multiple `RELATIVE` 
controllers but may not (because it does not make sense) be controlled by both `ABSOLUTE` and
`RELATIVE` controllers.
