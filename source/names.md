(c:names)=
# Names

%---------------------------------------------------------------------------------------------------
(s:names)=
## Name Syntax

Many constructs in the standard like lattice elements, branches, parameter groups, etc., may have
an associated name. To ensure seamless translation to particular languages, all names must conform
to the following:
- A name must start with a letter or the underscore character
- A name cannot start with a digit
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
(s:name.matching)=
(s:element.matching)=
## Name Matching

Name matching is the process of finding the set of named constructs — lattice
elements, element parameter groups, element parameters, constants, variables,
etc. — that a given string is matched to. Name matching is important in a number of
instances and PALS defines a standard syntax for this.

The full form of a name match string for a single construct is
```{code} text
{lattice-name}>>>{branch-or-beamline-name}>>{kind}::{name}#{N}>{parameter-group}.{sub-group1}. ... .{parameter}
```
where only `{name}` is required. The components are:
- `{lattice-name}>>>` — Lattice qualifier. See [](#s:qualified.names).
- `{branch-or-beamline-name}>>` — Branch or BeamLine qualifier. See [](#s:qualified.names).
- `{kind}::` — Kind restriction. See [](#s:kind.matching).
- `{name}` — Base name. See [](#s:basic.matching).
- `#{N}` — `N`{sup}`th` instance selection. See [](#s:instance.matching).
- `>{parameter-group}. ... .{parameter}` — Parameter path. See [](#s:parameter.matching).

The base name can be one of:
- A lattice element name
- A lattice element index. See [](#s:qualified.names).
- A controller name
- A constant or variable name
- A value associated with a [MetaP](#s:meta.params) string component. See [](#s:kind.matching).

Lattice elements may also be combined into sets using ranges, unions, and intersections
as explained in [](#s:element.sets). In this case the full form of a name match string is
```{code} text
{element-set}>{parameter-group}.{sub-group1}. ... .{parameter}
```
where each member of `{element-set}` may carry its own lattice, branch, kind, and instance
qualifiers, and the parameter path, if present, applies to every element in the set.

%---------------------------------------------------------------------------------------------------
(s:basic.matching)=
### Basic Name Matching

At its simplest, a string is matched against the base name of a construct.
For example, the string `Q1` will match to all elements (or constants, variables, ...) named `Q1`.

Names may be [PCRE2](https://www.pcre.org/) regular expressions. Regex matching is a
whole-name (fully anchored) match — the pattern must match the entire name — so `qa.*` matches
any name beginning with `qa`, while `qa` on its own matches only the exact name `qa`.

Regex matching is applied to the lattice name, branch name, and element name separately and
a match to the string requires all the individual names to match.
When applying regex to an element name, any prefix (anything before and including a `::`) and
any suffix (anything after and including a `#` character) is not included in the regex match.
For example, with:
```{code} yaml
B.4>>Quadrupole::Qaf.*
B.4>>Quadrupole::Qaf.*#2
```
For both lines, regex would be applied to the strings `B.4` and `Qaf.*`.
For the first line, this would match to all Quadrupole elements in branches
which have three characters beginning in `B` and ending in `4` with the element name
beginning with `Qaf`.
For the second line, this would match to the second element matched to in the first line.

Character tokens inside of any `(...)`, `[...]` or `{...}` bracket group are ignored
in terms of isolating a base name or for matching to ranges, unions, and intersections.
For example:
```{code} text
Qa,Qb
Q\d{2,3}
```
In the first example, the comma appears outside of any bracket group and is considered
to be a union character. That is, this will match to all elements named `Qa` or `Qb`.
In the second example, the comma appears within the `{...}` group and is thus considered
to be part of the PCRE2 string. In this case the string will match to the letter `Q` followed
by either 2 or 3 digits. For example, `Q12` or `Q123`.

%---------------------------------------------------------------------------------------------------
(s:kind.matching)=
### Kind and MetaP Matching

Name matches may be restricted to a given kind using the notation
```{code} yaml
{kind}::{name}
```
where `{name}` is the base name and
`{kind}` is one of:
- An element kind
- The name `Controller`
- The name of a [MetaP](#s:meta.params) string component.

Examples:
```{code} yaml
Marker::bpm.        # Marker elements with four-character names starting with bpm.
Controller::cdt     # The controller named cdt.
alias::black        # All lattice elements with MetaP.alias equal to "black".
```
The first line will match to all `Marker` elements whose name is four characters starting with `bpm`
(since a dot matches to any single character). The second line will match to the `Controller`
named `cdt`. The third example matches to all lattice elements with `MetaP.alias` equal to `"black"`.

%---------------------------------------------------------------------------------------------------
(s:instance.matching)=
### Instance Selection

The `N`{sup}`th` element with a given name can be matched to by appending the character `#`
followed by an integer `N`. For example, `Quadrupole::Q1#3` will match to the third element
that matches `Quadrupole::Q1`. The `N`{sup}`th` instance selection is always applied last.
Thus with this example, the element kind selector `::` is applied first to get a list of all
quadrupole elements named `Q1` and then the `#3` selection is used to get the third instance.

In the discussion below, all of the element name constructs above — a name with optional kind
or `MetaP` prefix and optional instance suffix — will be called an "element name".

%---------------------------------------------------------------------------------------------------
(s:qualified.names)=
### Branch and Lattice Qualifiers

The names of an element may be "qualified" by prepending a `branch` or `BeamLine` name
(henceforth just referred to as a branch name) to the string,
using the string `>>` as a separator. For example, `B1>>Sextupole::Saf` would match
to all `Sextupole` elements in a branch or `BeamLine` named `B1` whose name was `Saf`.
This includes sublines of BeamLines. Thus if `B1` is a BeamLine that contains a subline `B2`
that in turn contains a Sextupole element named `Saf`, the string `B1>>Sextupole::Saf`
will match to this element. An element name without a branch or lattice qualifier is
called "unqualified".

Lattice elements can also be referred to by the index in which they appear in a branch
with the first element having index one, etc. For example, `B1>>7` matches the seventh
element in branch `B1`.

Branches do not get an index since the
PALS standard does not mandate that the branches of a lattice be stored in an array (it
could, for example, be a linked list).

If there are multiple [`Lattice`](#s:lattice.construct) constructs, the element name may be qualified
using the lattice name with `>>>` as a separator. There are several permutations where `>>` and `>>>` are used:
```{code} text
{lattice-name}>>>{branch-or-beamline-name}>>{element-name}
{lattice-name}>>>{element-name}
{branch-or-beamline-name}>>{element-name}
```

%---------------------------------------------------------------------------------------------------
(s:element.sets)=
### Ranges, Unions, and Intersections

Elements can be matched using a range construct which has the form
```{code} yaml
{ele1}:{ele2}
```
where `{ele1}` marks the beginning of the range and `{ele2}` marks the end of the range.
Example:
```{code} yaml
Q1:Q2
```
In this example, the range matches all elements from `Q1` to `Q2` inclusive of `Q1` and `Q2`.
If `{ele2}` comes before `{ele1}` the range "wraps around" the branch or beamline.
For example, if `Q2` comes before `Q1` in the above example, the range matches all elements from
`Q1` to the end of the line plus all elements from the beginning of the line to `Q2`.

Commas `,` can be used to form the union of element sets. The syntax is
```{code} text
{element-set1}, {element-set2}, ... , {element-setN}
```
where `{element-set1}`, ... `{element-setN}` are element sets.
Example:
```{code} yaml
A, B, Q.*
```
This will match to all elements named `A`, `B`, and all elements whose name begins with `Q`.

Ampersands `&` can be used to form the intersection of element sets. The syntax is
```{code} text
{element-set1} & {element-set2} & ... & {element-setN}
```
where `{element-set1}`, ... `{element-setN}` are element sets.
Example:
```{code} yaml
Marker::.* & Q1:Q2
```
This will match to all `Marker` elements that are in the range from `Q1` to `Q2` inclusive.

Qualifiers apply only to the element name they are attached to (see [](#s:matching.precedence)).
For example, in `L1>>>A, B` only `A` is restricted to lattice `L1`. A range always lies
within a single branch or beamline, so in a range like `B1>>Q1:Q2` the end element `Q2` is
searched for in the same branch or beamline as the start element `Q1`.

%---------------------------------------------------------------------------------------------------
(s:parameter.matching)=
### Parameter Matching

Element parameters are matched by appending the parameter path to an element name
or element set match, using a single `>` as the separator. A parameter that belongs to a
[parameter group](#s:param.groups) is matched using the group path:
```{code} text
{element-set}>{parameter-group}.{sub-group1}. ... .{sub-groupN}.{parameter}
```
while a parameter that is not in any group — for example `length`, `is_on`, or
the element kind (see [Non-Group Parameters](#s:non.params)) — is matched
directly:
```{code} text
{element-set}>{parameter}
```
where
```{code} yaml
{element-set}                   # Element name or element set match.
{parameter-group}               # Parameter group name (for grouped parameters).
{sub-group1}. ... .{sub-groupN} # Subgroups if they exist.
{parameter}                     # Parameter name.
```
The `{element-set}` component is any element name match as described above — including its
kind (`::`), instance (`#`), branch (`>>`), and lattice (`>>>`) qualifiers — or any
[range, union, or intersection](#s:element.sets) of element names. The parameter path
following the `>` is, unlike element names, matched exactly rather than with
PCRE2; the dots within it are therefore unambiguous, and the single `>`
separator is distinct from the `>>` and `>>>` qualifiers that may appear inside
`{element-set}`.

Example:
```{code} yaml
qa.*>MagneticMultipoleP.Ks2L
Quadrupole::qa.*>MagneticMultipoleP.Ks2L
Q1>length
Q1:Q2>length
```
The first line matches the `Ks2L` component of `MagneticMultipoleP` for all
elements whose name begins with `qa`. The second is the same but restricted to
elements of kind `Quadrupole`. The third matches the ungrouped `length`
parameter of the element `Q1`. The fourth matches the `length` parameter of all
elements from `Q1` to `Q2` inclusive.

A trailing part of the path may be dropped to match the enclosing construct
instead of a parameter: omit `{parameter}` to match a parameter group, or omit
the `>{parameter-group}...` entirely to match the element itself. Example:
```{code} yaml
qa.*>MagneticMultipoleP    # Match the MagneticMultipoleP parameter group.
qa.*                       # Match the element.
```

%---------------------------------------------------------------------------------------------------
(s:constant.matching)=
### Constant and Variable Matching

Constructs that are not element parameters are matched by name in the same way.
Top-level [constants and variables](#s:constants) are matched directly, with no
`>`-qualified path. A variable that is owned by a controller, however, is matched
through its controller using the same single `>` separator —
`{controller-name}>{variable-name}` — just as an element parameter is reached
through its element.

%---------------------------------------------------------------------------------------------------
(s:matching.precedence)=
### Order of Precedence

The order of precedence of the name matching operators is:
```{code} text
>>>     # Highest
>>
::
#
:
&
,
>       # Lowest
```
Thus, for example, in `Q1:Q2>length` the parameter path `length` applies to the whole range
`Q1:Q2`, and in `B1>>A, B` the branch qualifier `B1` applies only to `A`.
Note that parentheses cannot be used to override this order since characters inside a
bracket group are treated as part of a regular expression (see [](#s:basic.matching)).
