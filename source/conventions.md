(c:conventions)=
# Conventions

%---------------------------------------------------------------------------------------------------
(s:keywords)=
## Keywords

The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

All keywords in this standard are case-sensitive.

%---------------------------------------------------------------------------------------------------
(s:syntax)=
## Syntax Used in this Document is YAML

The PALS [schema standard](#s:std.components) does not define any particular language to implement 
a lattice. Rather, there are associated
language specific standards that define grammars for YAML, JSON, Python, etc. Along with these
associated standards, there are packages that implement translation between lattice files and a 
representational internal format defined by the package.

While the standard itself is language agnostic, this document that describes the standard
needs to use some syntax and this syntax is based upon YAML.
YAML is [formally defined](https://yaml.org) and there are [tutorials to learn YAML](https://learnxinyminutes.com/yaml/).

### YAML 101

In particular, there are dictionaries, which are unordered sets of key-value pairs, e.g.:
```{code} yaml
this_dictionary:
  key1: value1
  key2: value2
  key3: value3
```

And lists, which are ordered sets of items, e.g.:
```{code} yaml
this_list:
  - entry1
  - entry2
  - more_entries
```

One can nest dictionaries into lists and other dictionaries, e.g.:
```{code} yaml
this_list:
  - key1: value1
    key2: value2
  - named_dictionary:
      key3: value3
      key4: value4
```

```{note}
   Developer note:
   PALS dictionaries should, when possible, implement a dictionary that preserves insertion order.

   While not strictly necessary, this helps with human readability:
   For example, having the [`kind`](#s:ele.syntax) key of an element as the first attribute enhances legibility.
```

### Special Values

Special values used in this document are:

1. Boolean parameters can be one of three values
- `true`
- `false`
- `null` Useful as a default value when neither `true` nor `false` is appropriate.

2. The standard defines the following symbols which can be used in place of a real or integer value:
- `null` Value has not been set.
- `Inf` Infinity
- `-Inf` Negative infinity

3. In general, `null` can be used to signify that any parameter does not have a specific default value.

%---------------------------------------------------------------------------------------------------
(s:palsroot)=
## PALS Root Object

The root of the PALS schema is given by this dictionary.
```{code} YAML
PALS:
  version:   # [string] Version of the PALS schema used in this file
  authors:   # [list] Authors associated with this file
  notes:     # [list] Notes of interest.
  reminders: # [list] Reminder messages to be printed when file is read.
  facility:  # [list] lattice elements, beamlines, lattices, parameter set commands, etc.
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
Information may appear in a lattice file outside of the `PALS` node but this information is considered
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
## Including Other Files Within Lattice Files

A PALS lattice file can rely on includes from other files using the `include` command.
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

The recommended suffixes for PALS files is discussed in the [File Formats](#c:impl.fileformats) chapter.
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
(s:units)=
## Units

The lattice standard uses SI except for energy which uses `eV`.
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
The `classical_radius_factor` is a useful number when converting a formula that involve the classical
electron or proton radius to a formula for something other than an electron or proton.

Other constants may be defined. Example:
```{code} yaml
PALS:
  facility:
    - my_const:
        kind: constant
        value: 1.45 * c_light
    ...
```
Constants must be defined directly under the `PALS` node or the `facility` node. 
Constants may not be redefined.
Exception: Since multiple include files may define the same constant, a redefinition of a constant
with the **same value** as the original is valid.

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
