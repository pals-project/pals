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
  load:             # [list] Files to load. See the "Load Files" section.
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
## Including Other Files Within a PALS File

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

A file path in an `include` is interpreted relative to the location of the file that contains the
`include` node.

%---------------------------------------------------------------------------------------------------
(s:load)=
## Load Files

"Loading" files is similar to [including files](#s:includefiles) in that the contents of several
files can be combined. A common use case is where one file defines the layout of a machine and another
file defines the magnet and other settings for a given machine configuration. The final lattice
is the union of these two files. This gives the flexibility where multiple settings files
need only reference one layout file.

While `load` and `include` both combine the contents of separate files, they differ in how the
combination is done. An `include` inserts the contents of a file verbatim at the point where the
`include` appears, and so can be used at any level of the information tree. A `load`, by contrast,
merges whole files `PALS` subnode by `PALS` subnode at the `PALS` root level, following the rules given
below. When both are present, `include` statements are resolved first so that each file is complete
before the files are combined by `load`.

For example, a layout can look like:
```{code} yaml
# Layout file: layout.pals.yaml
PALS:
  notes:
    - "Layout as of 03/12/2027"

  facility:
    - injector:
        kind: Lattice
        branches:
          - ...
```
and a settings file could look like:
```{code} yaml
# Settings file: settings.pals.yaml
PALS:
  notes:
    - "Settings for 12 mrad crossing angle, 0.23 m beta_y at IP."
    - "This is a second note."

  facility:
    - sets:
        - Q1a>MagneticMultipoleP.Kn1: 0.34
        - ...
```
A "joiner" file that combined these files could look like:
```{code} yaml
# Joiner file
PALS:
  notes:
    - "Lattice with orbit correction for blown chopper at B34W."
  load:
    - layout.pals.yaml
    - settings.pals.yaml
    - SELF
  facility:
    - sets:
        - B35W>MagneticMultipole.Kn0L: 0.07
        - ...
```

The rules for using `load` are as follows:
- The `load` node must be a component of the `PALS` node. 
- The top level of the joiner and loaded files must be `PALS`. 
- A `SELF` designation in the `load` list indicates where the contents of
the joiner file, if there is anything else other than a `load` node,
are to be combined with the contents of the loaded files. If not present, contents of the joiner
file are to be combined at the end. In the above example, the `SELF` line is not needed since it
is last on the `load` list.
- Contents from the joiner and loaded files are combined `PALS` subnode by `PALS` subnode. For list
type subnodes, the combined list retains the order set by the `load` list and the order set within the files
themselves. In the above example, the combined `notes` subnode will be:
  ```{code} yaml
  notes:
    - "Layout as of 03/12/2027"
    - "Settings for 12 mrad crossing angle, 0.23 m beta_y at IP."
    - "This is a second note."
    - "Lattice with orbit correction for blown chopper at B34W."
  ```
- For Dict type subnodes of `PALS`, the combined dict will be the union of all the dict entries
for all of the files. For any duplicate entries, the entry values must be the same and the combined Dict
will discard the duplicates.
- For the `version` subnode of `PALS`, if the version strings are not the same, the combined version
will be a comma delimited list of the different versions with duplicates discarded.
- A loaded file may itself contain a `load` node, so loading can be nested to any depth. It is
easiest to think of the process from the bottom up: each loaded file is fully combined into a single
`PALS` file before it, in turn, is loaded into the joiner file that references it. There is no
ambiguity as to what `SELF` refers to; a `SELF` designation always refers to the joiner file in
which it appears.
- As with `include`, a file path in a `load` list is interpreted relative to the location of the
file that contains the `load` node.

Loading can also be useful in constructing "composite" accelerator complexes from individual machines.
For example, a joiner file may look like:
```{code} yaml
PALS:
  load:
    - Booster_to_AGS_line.pals.yaml
    - AGS_ring.pals.yaml


  facility:
    - AGS_fork:
        kind: Fork
        to_line: AGS_ring           # Defined in AGS_ring.pals.yaml
        destination_element: d24w   # AGS element at injection point

    - AGS_inj_patch:
        kind: Patch
        ...

    - AGS_inject:
        kind: Beamline
        line:
          - Booster_to_AGS_line   # Defined in Booster_to_AGS_line.pals.yaml
          - AGS_inj_patch         # Needed to adjust the branch reference geometry.
          - AGS_fork              # And add a fork to the AGS at the end.

    - Combined_Inject_and_AGS:
        kind: Lattice
        branches:
          - AGS_inject
```
In this example, the file `Booster_to_AGS_line.pals.yaml` (not shown) contains the specification for the transfer
line from the Booster ring to the AGS ring. The file `AGS_ring.pals.yaml` (also not shown) contains the specification
for the AGS ring. The joiner file reads in these specifications and then creates a new transfer
line called `AGS_inject` with a `Patch` element to shift the branch coordinate system from the transfer
line coordinate system to the AGS coordinate system. The `Patch` element is followed by a `Fork` 
element at the end to connect to the AGS. 
The `Combined_Inject_and_AGS` lattice will have this extended transfer line and when the full 
lattice is constructed, the `AGS_ring` will be pulled in due to the `Fork` element. 

%---------------------------------------------------------------------------------------------------
(s:names)=
## Names

Many constructs in the standard like lattice elements, branches, parameter groups, etc., may have
an associated name. To ensure seamless translation to particular languages, all names must conform
to the following:
- A name must start with a letter or the underscore character
- A name cannot start with a number
- A name can only contain alpha-numeric characters and underscores (A-Z, a-z, 0-9, and _ )

The exception is that particle species names, which are considered to be strings and not proper
computer language variable names, follow the
[OpenPMD](https://github.com/openPMD/openPMD-standard/blob/upcoming-2.0.0/EXT_SpeciesType.md) convention.
Examples:
```{code} yaml
charge_of("#3He+2")          # Helium with atomic number three.
mass_of("anti-proton")       # Notice the dash.
my_particle: "Au+79"         # Assign a species to a variable or constant.
charge_of(my_particle)       # The variable or constant can be used in an equation.
```
Notice that particle names must be quoted.

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
## Constants

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

Other constants may be defined using `constant` as the `kind`.
The parameters associated with a constant are:
```{code} yaml
  absolute_error: 0       # Absolute error.       
  relative_error: 0       # Relative error.
  value                   # Constant value.
```
If both `absolute_error` and `relative_error` are specified, 
the true error is `absolute_error + relative_error * |value|`.
Example:
```{code} yaml
PALS:
  facility:
    - my_const:
        kind: constant
        value: 1.45 * c_light
        relative_error: 0.02
    ...
```
Constants must be defined directly under the `PALS` node or the `facility` node. 
Constants may not be redefined.
Exception: Since multiple include files may define the same constant, a redefinition of a constant
with the **same value** as the original is valid.

For constants that only have a value, an alternative compact form has the syntax:
```{code} yaml
  - constants:
      - const_a: value_a        # Define const_a
      - const_b: value_b        # Define const_b
      - const_c:: pi * const_a  # Can use expressions.
      ...
```

%---------------------------------------------------------------------------------------------------
(s:functions)=
## Functions

Functions defined by PALS:
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
ran_gauss()              # Gaussian distributed random number
ran_gauss(sig_cut)       # Gaussian distributed random number
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
