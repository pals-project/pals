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
(s:name.matching)=
(s:parameter.matching)=
## Name Matching

Name matching is the process of finding the set of named constructs — lattice
elements, element parameter groups, element parameters, constants, variables,
etc. — that a given string is matched to. PALS defines a standard syntax for this.

At its simplest, a string is matched against the `name` of a construct. For
example, `qa.*` matches every element (or constant, variable, ...) whose name
begins with `qa`. Names may be [PCRE2](https://www.pcre.org/) regular
expressions. Regex matching is a whole-name (fully anchored) match — the pattern
must match the entire name — so `qa.*` matches any name beginning with `qa`,
while `qa` on its own matches only the exact name `qa`.

Name matches may be restricted to a given construct kind using the notation
```{code} yaml
{kind}::{name}
```
where `{kind}` is the construct kind — for example a lattice element kind such as
`Marker`, or a non-element kind such as `Controller` — and `{name}` is the name
match. Example:
```{code} yaml
Marker::bpm.
```
This will match to all `Marker` elements whose name is four characters starting with `bpm`
(since a dot matches to any single character).

Element parameters are matched by appending the parameter path to an element name
match, using a single `>` as the separator. A parameter that belongs to a
[parameter group](#s:param.groups) is matched using the group path:
```{code} text
{element-name}>{parameter-group}.{sub-group1}. ... .{sub-groupN}.{parameter}
```
while a parameter that is not in any group — for example `length`, `is_on`, or
the element kind (see [Non-Group Parameters](#s:non.params)) — is matched
directly:
```{code} text
{element-name}>{parameter}
```
where
```{code} yaml
{element-name}                  # Element name match, see below.
{parameter-group}               # Parameter group name (for grouped parameters).
{sub-group1}. ... .{sub-groupN} # Subgroups if they exist.
{parameter}                     # Parameter name.
```
The `{element-name}` component is any element name match from
[Element Name Matching](#s:element.matching) — including its kind (`::`),
BeamLine/Branch (`>>`), and Lattice (`>>>`) qualifiers. The parameter path
following the `>` is, unlike element names, matched exactly rather than with
PCRE2; the dots within it are therefore unambiguous, and the single `>`
separator is distinct from the `>>` and `>>>` qualifiers that may appear inside
`{element-name}`.

Example:
```{code} yaml
qa.*>MagneticMultipoleP.Ks2L
Quadrupole::qa.*>MagneticMultipoleP.Ks2L
Q1>length
```
The first line matches the `Ks2L` component of `MagneticMultipoleP` for all
elements whose name begins with `qa`. The second is the same but restricted to
elements of kind `Quadrupole`. The third matches the ungrouped `length`
parameter of the element `Q1`.

A trailing part of the path may be dropped to match the enclosing construct
instead of a parameter: omit `{parameter}` to match a parameter group, or omit
the `>{parameter-group}...` entirely to match the element itself. Example:
```{code} yaml
qa.*>MagneticMultipoleP    # Match the MagneticMultipoleP parameter group.
qa.*                       # Match the element.
Controller::cd.t           # Match all Controllers whose four-character name starts with `cd` and ends with `t`.
```

Constructs that are not element parameters are matched by name in the same way.
Top-level [constants and variables](#s:constants) are matched directly, with no
`>`-qualified path. A variable that is owned by a controller, however, is matched
through its controller using the same single `>` separator —
`{controller-name}>{variable-name}` — just as an element parameter is reached
through its element.

%---------------------------------------------------------------------------------------------------
(s:element.matching)=
## Element Name Matching

Lattice element name matching is the process of finding the set of lattice elements that 
are matched to a given string. Name matching is important in a number of instances including
lattice expansion where there are [`Fork`](#s:forking) elements and for evaluating mathematical
expressions.

The simplest form of name matching is if the string matches
the `name` field of an element or elements. 
For example, the string `"Q1"` will match to all elements named `Q1`.

The `N`{sup}`th` element with a given name can be matched to by appending the character `"#"` 
followed by an integer `N`. For example, `"Quadrupole::Q1#3"` will match to the third element
that matches `"Quadrupole::Q1"`. The `N`{sup}`th` instance selection is always applied last.
Thus with this example, the element kind selector `::` is applied first to get a list of all
quadrupole elements named `Q1` and then the `#3` selection is used to get the third instance.

Besides the element name, any parameter that is a string in the [`MetaP`](#s:meta.params) parameter group can
be matched to using the syntax `"{param-name}::{name-to-match}"`. For example, `"alias::black"`
would match to any element whose `alias` parameter is set to `black`.

In the discussion below, all of the above constructs will be called an "element name".

The names of an element may be "qualified" by prepending a `branch` or `BeamLine` name 
(henceforth just referred to as a branch name) to the string,
using the string `">>"` as a separator. For example, `"B1>>Sextupole::Saf"` would match
to all `Sextupole` elements in a branch or `BeamLine` named `"B1"` whose name was `"Saf"`.
This includes sublines of BeamLines. Thus if `B1` is a BeamLine that contains a subline `B2` 
that in turn contains a Sextupole element named `Saf`, the string `"B1>>Sextupole::Saf"`
will match to this element.

Lattice elements can also be referred to by the index in which they appear in a branch
with the first element having index one, etc. For example, `"B1>>7"` matches the seventh
element in branch `B1`.

Branches do not get an index since the
PALS standard does not mandate that the branches of a lattice be stored in an array (it
could, for example, be a linked list).

If there are multiple [`Lattice`](#s:lattice.construct) constructs, the element name may be qualified using the lattice
name with `">>>"` as a separator. There are several permutations where `>>` and `>>>` are used:
```{code} text
{lattice-name}>>>{branch-name}>>{element-name}
{lattice-name}>>>{element-name}
{branch-name}>>{element-name}
```

Regular expressions can be used. 
Regular expressions must conform to the [PCRE2](https://www.pcre.org/) standard. 
Regex matching is applied to the lattice name, branch name, and element name separately and
a match to the string requires all the individual names to match.
When applying regex to a lattice name, any prefix (anything before and including a `"::"`) and
any suffix (anything after and including a `"#"` character) is not included in the regex match.
For example, with:
```
B.4>>Quadrupole::Qaf.*
B.4>>Quadrupole::Qaf.*#2
``` 
For both lines, regex would be applied to the strings `B.4` and `Qaf.*`. 
For the first line, this would match to all Quadrupole elements in branches 
which have three characters beginning in "B" and ending in "4" with the element name 
beginning with "Qaf".
For the second line, this would match to the second element matched to in the first line.

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
where `{element-set1}`, ... `{element-setN} are element sets. 
Example:
```{code} yaml
Marker::.* & Q1:Q2
```
This will match to all `Marker` elements that are in the range from `Q1` to `Q2`.

Order of precedence:
```{code}
>>>     # Highest
>>
>
::      
#
:
,
&      # Lowest
```
