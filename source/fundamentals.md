(c:fundamentals)=
# Fundamental Structure

%---------------------------------------------------------------------------------------------------
(s:palsroot)=
## PALS Root Object

The root of the PALS schema is given by this dictionary.
```{code} YAML
PALS:
  version:          # [string] Version of the PALS schema used in this file
  authors:          # [list] Authors associated with this file
  notes:            # [list] Optional notes of interest.
  reminders:        # [list] Optional reminder messages to be printed when file is read.
  extension_labels: # [Dict] Optional extensions to PALS that the standard shall ignore.
  facility:         # [list] lattice elements, beamlines, lattices, parameter set commands, etc.
```
The difference between `notes` and `reminders` is that reminder messages are meant to be 
printed (or otherwise communicated to the user) every time the file is read.

Example:
```{code} YAML
PALS:
  version: null  # version schema: defined later

  notes:
    - "Extraction transfer line will be added to lattice in next iteration."
    - ...

  reminders:
    - "Important! West RF cavity phasing needs to be done before any simulations!!!"
    - ...

  extension_labels:
    names:
      my_extension: "See the PALS extensions chapter"

  authors:
    - author:
        name: Lastname, Firstname
        orcid: AAAA-BBBB-CCCC-DDDD
        affiliation: Affiliation Long Name
        email: lastname@laboratory.gov
    - author:
        ...

  facility:
    - ...  # lattice elements, beamlines, lattices, parameter set commands, etc.
```
Information may appear in a PALS file outside of the `PALS` node but this information is considered
to be outside of the PALS standard and will be ignored by a PALS parser.

PALS file `authors` are optional, but recommended to enable data provenance and contacts.
Per author, the `name` is required; the `orcid`, `affiliation` and `email` fields are optional.

%---------------------------------------------------------------------------------------------------
(s:parameters)=
## Parameters

All parameters (both element parameters and non-element parameters) are optional unless 
explicitly stated otherwise.
Optional real or integer parameters have a default value of zero unless otherwise stated.
Optional string parameters have a default value of blank unless otherwise stated.

%---------------------------------------------------------------------------------------------------
(s:includefiles)=
## Including Other Files Within PALS files

A PALS file can rely on includes from other files using the `include` command.
Included file data will be included verbatim at the current level of nesting.

Example:
```{code} YAML
PALS:
  include: "version-and-globals.subpals.yaml"

  facility:
    - Q01:
        kind: Quadrupole
        include: "include-Q-params.subpals.yaml"

    - ...

    - include: "parameter-set-commands.subpals.yaml"

    - ...
```
The information in an included file is inserted at the `include` point. In this example,
the included file `version-and-globals.subpals.yaml` could look like, for example:
```{code} YAML
version: null  # version schema: defined later
```
and the file `include-Q-params.subpals.yaml` could look like:
```{code} YAML
- MagneticMultipoleP:
  - Kn3L: 0.3
```
There are two types of included files. One type of file contains a subpart of a compliant PALS file
like in the example above. These "compliant format" files can be used to break up the lattice
information tree into manageable parts. Compliant format files can themselves have include
statements. 

The other type of included files, conform to some other non-PALS 
standard. For example, an included file may be an 
[OpenPMD](https://github.com/openPMD/openPMD-standard) compliant file coded in 
[HDF5](https://www.hdfgroup.org/solutions/hdf5/). 

The recommended suffixes for PALS files is discussed in the [File Formats](#c:impl.fileformats) section.
Other file endings indicate non-PALS data.

Include can appear at any level of the information tree but must be within the `PALS` root node.

%---------------------------------------------------------------------------------------------------
(s:names)=
## Names

Many constructs in the standard like lattice elements, branches, parameter groups, etc., may have
an associated name. To ensure seamless translation to particular languages, all names must conform
to the following:
- A name must start with a letter or the underscore character
- A name cannot start with a number
- A name can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _ )

%---------------------------------------------------------------------------------------------------
(s:specialvalues)=
### Special Values

Special values used in this document are:

1. Boolean parameters can be one of three values:
- `true`
- `false`
- `null`: Useful as a default value when neither `true` nor `false` is appropriate.

2. The standard defines the following symbols which can be used in place of a real or integer value:
- `null`: Value has not been set.
- `Inf`: Infinity.
- `-Inf`: Negative infinity.

3. In general, `null` can be used to signify that any parameter does not have a specific default value.

%---------------------------------------------------------------------------------------------------
(s:units)=
## Units

PALS uses SI except for energy which uses `eV`.
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
  - radians / 2 {math}`\pi`
* - magnetic field
  - Tesla
* - frequency
  - Hz
* - electric field
  - Volts/m
```

%---------------------------------------------------------------------------------------------------
(s:constants)=
## Constants and Variables

Constants defined by PALS:
```{code} yaml
pi                        # Pi
c_light                   # [ m/sec] Speed of light
h_planck                  # [eV*sec] Planck's constant
hbar                      # [eV*sec] Reduced Planck's constant
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
The difference between a constant and a variable is that a constant is not supposed to be
varied after a program reads a PALS file while a variable can vary. Since what happens
after a PALS file is read in by a program is beyond the scope of PALS, PALS treats constants
and variables the same. In particular, neither constants nor variables may not be redefined in
the PALS file. 
Exception: Since multiple include files may define the same constant, a redefinition of a constant
with the same value or same expression as the original is valid.

The parameters associated with a constant or variable are:
```{code} yaml
  absolute_error: 0       # Absolute error.       
  relative_error: 0       # Relative error.
  value                   # Constant value.
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
    - my_var
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
asinh(x), acosh(x)       # Hyperbolic arc sine and Arc cosine
atanh(x), acoth(x)       # Hyperbolic arc tangent and cotangent
abs(x)                   # Absolute Value
factorial(n)             # Factorial
random()                 # Uniform random number between 0 and 1
ran_gauss()              # Gaussian distributed random number with unit sigma and zero mean
ran_gauss(sig_cut)       # Same ran_gauss() but with a probability tail cutoff.
int(x)                   # Nearest integer with magnitude less then x
nint(x)                  # Nearest integer to x
sign(x)                  # 1 if x positive, -1 if negative, 0 if zero
floor(x)                 # Nearest integer less than x
ceiling(x)               # Nearest integer greater than x
modulo(a, p)             # a - floor(a/p) * p. Will be in range [0, p).
mass_of(A)               # Mass of particle A
charge_of(A)             # Charge, in units of the elementary charge, of particle A 
anomalous_moment_of(A)   # Anomalous magnetic moment of particle A
```
The `ran_gauss(sig_cut)` function produces a Gaussian distributed random number with unit sigma
and zero mean modified so that all random number will be in the range `[-sig_cut, sig_cut]`.
 
When `random` or `ran_gauss` functions are used in a single expression that sets multiple parameters,
a different random number is generated for each parameter. For example, 
```{code} yaml
- set:
    parameter: B1.*>BendP.e1
    value: 0.01 + 0.003 * ran_gauss()
```
In this example, the `BendP.e1` parameter of all elements whose name begins with `B1` is modified.
If there are, {math}`N` lattice elements that match the name `B1.*`, {math}`N` different random
numbers need to be generated for the calculation.

In addition, there is the `expr()` construct which is used to designate 
"delayed evaluation" expressions. See [](#s:expressions) for details.


%---------------------------------------------------------------------------------------------------
(s:expressions)=
## Mathematical Expressions

Mathematical expressions can be used in place of real values. Expressions may use the functions 
as listedin the [](#s:functions) section as well as [constants and variables](#s:constants). 
Standard math symbols `+` plus, `-` minus, `*` times, and `/` divide along with parentheses `(...)`
are valid.
Example:
```{code} yaml
- variables:
    a_var: 3.75e7 / c_light^2
    b_var: -0.34

cleo:            
  kind: Solenoid
  length: 0.1*log(abs(b_var))
  MagneticMultipoleP:
    Kn1: expr(3.74 * a_var)
```
This sets the length of the `cleo` element to `0.1*log(abs(b_var))` and the `Kn1` parameter
to `3.74 * a_var`. 

There are two types of expressions
that are commonly called "immediate evaluation" and "delayed evaluation" expressions.
Immediate evaluation expressions are expressions that, once a PALS file is read in by a program,
are meant to be immediately evaluated and never reevaluated. That is, what is stored is the
value of the expression and the expression used to compute the value can be ignored thereafter. 
Delayed evaluation on the other hand are meant to be retained by the program and, if any
variables in the expression change, the program should update the value automatically.
Delayed evaluation expressions are denoted in a PALS file using the `expr(...)` construct.
where as in the example above where the expression for `Kn1`, `3.74 * a_var` is a delayed
expression. The `expr(...)` construct must enclose the entire expression. That is, something
like `3.74 * expr(a_var)` is invalid. Note that whether an expression is delayed or immediate is
determined solely determined by if the expression is wrapped in `expr(...)` or not. The fact
that an expression may contain a variable (see the `length` expression in the above example), 
is not a consideration.
The exception is that [controller](#s:controller) expressions are always considered to be delayed. 
Also note that what a program actually does is outside of the PALS purview. The designation of
immediate or delayed is only a "hint" to the program of what the lattice designer intends.

