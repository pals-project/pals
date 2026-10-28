(c:params)=
# Parameter Values and Controllers

%---------------------------------------------------------------------------------------------------
(s:units)=
## Units

PALS uses the following units:
```{list-table} Units used by the Standard
:width: 60%
:header-rows: 1

* - Quantity
  - Units
* - charge
  - fundamental charge
* - length
  - meters
* - time
  - seconds
* - energy
  - eV
* - momentum
  - eV/c
* - mass
  - eV/c^2
* - voltage
  - Volts
* - angles and phases
  - radians
* - magnetic field
  - Tesla
* - frequency
  - Hz
* - electric field
  - Volts/m
```

Exceptions where the units are radians/2pi and not radians are:
```{code} yaml
tune
spin_tune
chromaticity
```

%---------------------------------------------------------------------------------------------------
(s:constants)=
## Constants and Variables

Constants defined by PALS:
```{code} yaml
pi                        # [-] Pi
twopi                     # [-] 2*pi
c_light                   # [m/sec] Speed of light
h_planck                  # [eV*sec] Planck's constant
hbar                      # [eV*sec] Reduced Planck's constant
k_boltzmann               # [eV/K] Boltzmann's constant
r_electron                # [m] Classical electron radius
r_proton                  # [m] Classical proton radius
e_charge                  # [Coul] Elementary charge
mu_0                      # [eV*sec^2/m] Vacuum permeability
epsilon_0                 # [1/eV*m] Permittivity of free space
classical_radius_factor   # [m*eV] Classical Radius Factor: 1/(4 pi epsilon_0 c^2)
fine_structure            # [-] Fine structure constant
n_avogadro                # [-] Avogadro's constant
```
The `classical_radius_factor` is a useful number when converting a formula that involves the classical
electron or proton radius to a formula for something other than an electron or proton.

Other constants and variables may be defined using `constant` or `variable` as the `kind`.
The parameters associated with a constant or variable are:
```{code} yaml
  absolute_error: 0       # Absolute error.       
  relative_error: 0       # Relative error.
  value:                  # Constant or variable value.
```
If both `absolute_error` and `relative_error` are specified, 
the true error is `absolute_error + relative_error * |value|`.

Constants and variables must be defined directly under the `PALS` node or the `facility` node. 
Example:
```{code} yaml
PALS:
  facility:
    - my_const:
        kind: constant
        value: 1.45 * c_light
        relative_error: 0.02
    - my_var:
        kind: variable
        value: 37
    ...
```

For constants or variables that only have a value, an alternative compact form has the syntax:
```{code} yaml
  - constants:
      - const_a: value_a        # Define const_a
      - const_b: value_b        # Define const_b
      - const_c: pi * const_a   # Can use expressions.
      ...
  - variables:
      - var_a: var_val_a        # Define var_a
      ...
```
The difference between a constant and a variable is one of intent of the PALS file creator.
That is, a constant is not supposed to be
varied after a program reads a PALS file, while a variable can vary. For example, a constant could
be the length of a magnet which will not change, while a variable could be a magnet strength which
does vary.
When a PALS file is read in, neither constants nor variables may be redefined to have a different value. 
That is, the following is not valid:
```{code} yaml
- variables:
    - my_var: 37.5

...

- variables:
    - my_var: 0.13     # VALUE CHANGE NOT VALID!
```
It is sometimes convenient when there are included PALS files, to define the same constant or variable
in multiple files. Multiple definitions of the same constant or variable are allowed with the 
restriction that the value is always the same.

Circular definitions are not allowed. For example, if constant `a` is defined in terms of constant
`b`, and constant `b` is defined in terms of constant `c`, then the expression for `c` cannot
involve `a` nor `b`.

%---------------------------------------------------------------------------------------------------
(s:functions)=
## Functions

Functions that can be used in [](#s:expressions):
```{code} yaml
sqrt(x)                  # Square Root
log(x)                   # Logarithm
exp(x)                   # Exponential
sin(x), cos(x)           # Sine and cosine
tan(x), cot(x)           # Tangent and cotangent
sinc(x)                  # Sin(x)/x Function
asin(x), acos(x)         # Arc sine and Arc cosine
atan(x)                  # Arc tangent
atan2(y, x)              # Arc tangent of y/x
sinh(x), cosh(x)         # Hyperbolic sine and cosine
tanh(x), coth(x)         # Hyperbolic tangent and cotangent
asinh(x), acosh(x)       # Hyperbolic arc sine and arc cosine
atanh(x), acoth(x)       # Hyperbolic arc tangent and cotangent
abs(x)                   # Absolute Value
factorial(n)             # Factorial
random()                 # Uniform random number between 0 and 1
random_gauss()           # Gaussian distributed random number with unit sigma and zero mean
random_gauss(sig_cut)    # Same as random_gauss() but with a probability tail cutoff.
int(x)                   # Nearest integer with magnitude less than or equal to |x| (truncation toward zero)
nint(x)                  # Nearest integer to x
sign(x)                  # 1 if x positive, -1 if negative, 0 if zero
floor(x)                 # Nearest integer less than or equal to x
ceiling(x)               # Nearest integer greater than or equal to x
modulo(a, p)             # a - floor(a/p) * p. Will be in range [0, p).
mass_of(A)               # Mass of particle A
charge_of(A)             # Charge, in units of the elementary charge, of particle A 
anomalous_moment_of(A)   # Anomalous magnetic moment of particle A
```

%---------------------------------------------------------------------------------------------------
(s:expressions)=
## Mathematical Expressions

Mathematical expressions can be used in place of any real value.
The expressions can involve the functions listed in the [Functions](#s:functions) section,
and the PALS defined constants and the user defined constants and variables documented in the
[Constants and Variables](#s:constants) section.
[Lattice element parameter](#s:parameter.matching) values can also be incorporated.

%---------------------------------------------------------------------------------------------------
(s:io.params)=
## User Settable (Input) and Dependent (Output) Parameters

All parameters (both element parameters and non-element parameters) are optional unless 
explicitly stated otherwise.
Optional real or integer parameters have a default value of zero unless otherwise stated.
Optional string parameters have a default value of blank unless otherwise stated.

Some parameters are set in the PALS file. These parameters are called "User settable" or "input". 
Some parameters will be computed by the Translator during lattice expansion. 
These parameters are called "dependent" or "output" parameters. There is a third class of parameters that can be an input
parameter if it is set in the PALS file or will be an output parameter if not set.

For example, the `FloorP` parameters can be set for the `BeginningEle` element which is the
first element of any branch line. For most other elements, the `FloorP` parameters can
be calculated starting at the `BeginningEle` and working forward computing the floor parameters
element-by-element.

%---------------------------------------------------------------------------------------------------
(s:set)=
## Setting Parameters

The `set` command is used for setting parameters. The components of `set` are:
```{code} yaml
parameter               # [string] Parameter(s) to vary.
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
      e1: 0.1 / c_light
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
      MetaP:
        description: Model Mitsubishi 800KL
      variables:
        cur1: 0.023
        cur2: 1e8 / c_light
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

Initial values for controller variables may be equations. These equations and the equations
used for `expression`s are not allowed
to contain lattice parameters nor variables as this could greatly complicate the problem of 
evaluation order.

Note: All controller `expression`s are considered to be ["delayed evaluation"](#s:expressions)
as it does not make sense for these expressions to be considered immediate.

Besides control information, a controller can contain a [`MetaP`](#s:meta.params) parameter group
which aids in documentation and searching.

Controllers can control the variables of other controllers. The syntax for a controller 
variable is:
```{code} text
{controller-name}>{variable-name}
```
So, for example, with the above example, outside of the `ps27` controller the `cur1` variable
has the name `ps27>cur1`. While controllers can control the variables of other controllers,
circular definitions are not allowed. The set of all controllers thus forms a hierarchy and
controller evaluation works by starting at the top of the hierarchy and working downwards.
The order in which controllers are defined in the PALS file is irrelevant to controller evaluation.

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

A given lattice parameter may not be assigned a delayed evaluation expression and be controlled 
by a controller.

%---------------------------------------------------------------------------------------------------
(s:adjust)=
## Adjustments

The calculated value of a given quantity can vary from simulation program to simulation program
due to differing physics models. An example is the tune of a machine. For some calculations, this
variation may be problematical. To alleviate this, the `adjustments` construct can be used as
a hint to a program as to how to correct a lattice before any simulations are done.
An `adjustments` block is put as a sub-node of the `PALS` node. The syntax of this is:
```{code} yaml
PALS:
  adjustments:
    - optimize:
        ...
    - optimize:
        ...
```
The `adjustments` block has a number of `optimize` subblocks. Each `optimize` subblock represents
an optimization where a set of parameters are varied in order to get a set of target parameters
to be specific values.

Each `optimize` block has the syntax:
```{code} yaml
  - optimize:
      - vary: 
          parameter: <parameters-to-vary>   # [name] Parameter(s) to vary
          weight: <weight>                  # [-] Optional variable weight. Default is 0.
      - vary: 
          ...
      - target:
          parameter: <target-parameter>     # Data Parameter(s) to optimize
          value: <value>                    # Optimum value
          weight: <weight>                  # [-] Optional datum weight. Default is 1.
      - target:
          ...
```   
The `vary` nodes specify the parameters to be varied and the `target` nodes specify the data target
parameters and data target values to optimize. The merit function {math}`M` to minimize is:
```{math}
M = \sum_i w_i \left[ \delta D_i \right]^2 + \sum_j w_j \left[ \delta V_j \right]^2
```
where {math}`\delta D_i` is the difference between datum value and the target value, {math}`\delta V_j`
is the difference between the variable's value and its initial value before any optimization, and
the {math}`w_i` and {math}`w_j` are the data and variable weights respectively which default to one
and zero respectively.

Example:
```{code} yaml
PALS:
  adjustments:
    - optimize:
        - vary:
            parameter: Qa,Qb>MagneticMultipoleP.Kn1
        - target:
            parameter: fractional_tune_a
            value: 0.37*twopi
        - target:
            parameter: fractional_tune_b
            value: 0.53*twopi
```
