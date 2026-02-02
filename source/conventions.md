(c:introduction)=
# Introduction

%---------------------------------------------------------------------------------------------------
(s:conventions)=
## Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

All `keywords` in this standard are case-sensitive.

%---------------------------------------------------------------------------------------------------
(s:elements.intro)=
## Lattice Elements

The basic building block used to describe an accelerator is the lattice **element**. Typically,
a lattice element is something physical like a bending magnet or an electrostatic
quadrupole, or a diffracting crystal. A lattice element may define a region in space 
distinguished by the presence of (possibly time-varying) electromagnetic fields,
materials, apertures and other possible engineered structures. However, lattice elements
are not restricted to being something physical and may, for example, just mark a particular point 
in space (EG: `Marker` elements), or may designate where beamlines intersect (`Fork` elements).
By convention, element names in PALS will be upper camel case.

%---------------------------------------------------------------------------------------------------
(s:branches.intro)=
## Lattice Branches

A lattice `branch` holds an ordered array of lattice elements
that gives the sequence of elements to be tracked through. 
A branch can represent something like a storage ring, transfer line or Linac.
In the simplest case, a program can track through the elements one element at a time.
However, lattice elements may overlap which will naturally complicate tracking.

%---------------------------------------------------------------------------------------------------
(s:lattices.intro)=
## Lattices

A `lattice` is the root structure holding the information about a
``machine``. A machine may be as simple as a line of elements (like the elements of a Linac) or
as complicated as an entire accelerator complex with multiple storage rings, Linacs, transfer
lines, etc.

Essentially a `lattice` has an array of `branches` with each branch describing part of the
machine. Branches can be interconnected to form a unified whole.
Branches can be interconnected using `Fork` elements. 
This is used to simulate forking beamlines such as a connections to a transfer line, dump line, or an
X-ray beamline.

Besides `branches`, a lattice will hold information like details of any support girders that are
present and `multipass` information in the case where elements are transversed multiple times 
as in an ERL or in opposite directions as in a colliding beam machine.

%---------------------------------------------------------------------------------------------------
(s:root.intro)=
## Root branch

The `branch` from which other `branches` fork but is not forked to by any
other branch is called a `root` branch.
A lattice may contain multiple `root` branches. For example, a pair of intersecting storage
rings will generally have two root branches, one for each ring.

%---------------------------------------------------------------------------------------------------
(s:expansion.intro)=
## Lattice Expansion

An important concept is [`lattice expansion`](#s:lattice.expand) and `branch expansion`.
Branch expansion is the process, starting from the `root` `BeamLine`
of a branch, of constructing the ordered list of lattice elements contained in that branch.
`Lattice expansion` involves branch expansion along with things like
calculating the reference energy for all elements.

%---------------------------------------------------------------------------------------------------
(s:syntax)=
## Syntax Used in this Document

The PALS [schema standard](#s:std.components) does not define any particular language to implement 
a lattice. Rather, there are associated
language specific standards that define grammars for YAML, JSON, Python, etc. Along with these
associated standards, there are packages that implement translation between lattice files and a 
representational internal format defined by the package.

While the standard itself is language agnostic, this document that describes the standard
needs to use some syntax and this syntax is based upon YAML.

%---------------------------------------------------------------------------------------------------
(s:palsroot)=
## PALS Root Object

The root of the PALS schema is given by this dictionary:
```{code} YAML
PALS:
  version: null  # version schema: defined later

  lattices:
    - ...  # a list of lattice elements and commands
```

%---------------------------------------------------------------------------------------------------
(s:matching)=
## Matching Syntax

Non-YAML syntax used here is:

1. Boolean parameters can be one of three values
- `true`
- `false`
- `null`          # Useful as a default value when neither `true` nor `false` is appropriate.

2. The standard defines the following symbols which can be used in place of a real or integer value:
- `null`   # Value has not been set.
- `Inf`    # Infinity
- `-Inf`   # Negative infinity

3. In general, `null` can be used to signify that any parameter does not have a specific default value.

Note: There is a difference between
```{code} yaml
this_group:
  key1: value1
  key2: value2
  key3: value3
```
and
```{code} yaml
this_group:
  - key1: value1
  - key2: value2
  - key3: value3
```
The first represents an unordered dictionary of key-value pairs and the second represents an ordered 
dictionary of key-value pairs. 

Note: the actual syntax in some particular language that is used to 
represent an unordered dictionary may be an ordered dictionary. That is, the standard does not
prohibit ordered dictionaries being used in place of unordered dictionaries. However, ordered
dictionaries must always be used for things that the standard defines as an ordered dictionary.
In fact, when there is a choice of using an ordered or an unordered dictionary,
an ordered dictionary may be preferred to maintain human readability. An example of this is with
lattice element attribute dictionaries where having the name of the element as the first attribute
enhances legibility. 

%---------------------------------------------------------------------------------------------------
(s:parameters)
## Parameters

All parameters are optional unless explicitly stated otherwise.
Optional real or integer parameters have a default value of zero unless otherwise stated.
Optional string parameters have a default value of blank unless otherwise stated.

%---------------------------------------------------------------------------------------------------
(s:includefiles)=
## Include Lattice Files

A lattice file can include other lattices (elements and commands) using an include statement.

Example:
```{code} YAML
PALS:
  # ...

  lattices:
    # the elements and commands of base-lattice.pals.yaml
    - include: "./base-lattice.pals.yaml"

    # the elements and commands of extra-lattice.pals.yaml
    - include: "./base-lattice.pals.yaml"

    # a list of additional lattice elements and commands
    - ...
```
where the include file names above are examples.
Includes simply insert the `lattices` block of the `include` file(s).

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
(s:name.matching)=
## Element Name Matching

Lattice element name matching is the process of finding the set of lattice elements that 
are matched to a given string. Name matching is important in a number of instances including
lattice expansion where there are [`Fork`](#s:forking) elements and for evaluating mathematical
expressions.

The simplist form of name matching is if the string matches
the `name` field of an element or elements. Regular expressions can be used. 
Regular expressions must conform to the [PCRE2](https://www.pcre.org/) standard. 

The names of an element may be "qualified" by prepending a `branch` or `BeamLine` name to the string
using the string `">>"` as a separator. For example, `"B1>>Qaf.*"` would match
to all elements in a branch or BeamLine named `"B1"` whose name begins with `"Qaf"`.

Additionally, if the match string ends with the character `"#"` followed by an integer `N`,
this will match to the `N`{sup}`th` instance matched to in any `branch` or `BeamLine`.
For example, `"Sd#3"` will match to the 3{sup}`rd` instance of all elements named
`"Sd".

Lattice elements can also be referred to by the index in which they appear in a branch
with the first element having index one, etc. Branches do not get an index since the
PALS standard does not mandate that the branches of a lattice be stored in an array (it
could, for example, be a linked list).

%---------------------------------------------------------------------------------------------------
(s:units)=
## Units

The lattice standard uses SI except for energy which uses `eV`.
```{list-table} Units used by the Standard
:width: 60%
:header-rows: 1

* - Quantity
  - Units
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
