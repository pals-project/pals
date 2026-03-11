(c:lat.ele)=
# Lattice Elements

The following discusses lattice elements in general.
For details on the different element kinds see [here](#c:ele.kinds).

%---------------------------------------------------------------------------------------------------
(s:lat.elements)=
## Lattice Elements 

The basic building block used to describe an accelerator is the lattice **element**. Typically,
a lattice element is something physical like a bending magnet or an electrostatic
quadrupole, or a diffracting crystal. A lattice element may define a region in space 
distinguished by the presence of (possibly time-varying) electromagnetic fields,
materials, apertures and other possible engineered structures. However, lattice elements
are not restricted to being something physical and may, for example, just mark a particular point 
in space (EG: `Marker` elements), or may designate where beamlines intersect (`Fork` elements).
By convention, element names in PALS will be upper camel case.
The different kinds of elements are discussed in the [Element Kinds](#c:ele.kinds) section.

%---------------------------------------------------------------------------------------------------
(s:ele.syntax)=
## Lattice Element Definition

Lattice element definition syntax is:
```{code} yaml
<element-name>:
  kind: <kind-of-element>
  ... other parameters ...
```
where `<element-name>` is the name of the element, and `<kind-of-element>` is the element 
[kind](#c:ele.kinds). Example:
```{code} yaml
crab1:
  kind: CrabCavity
  RFP:
    frequency: 394.0e6 
    phase: 0.0
    voltage: 1.0e6
```

Lattice element definitions may only be placed as a child node of the [`facility`](#s:palsroot) node
or "in place" in a `line` within a [`BeamLine`](#s:beamline.components). Example:
```{code} yaml
PALS:
  facility:
    - Q1:                 # An element defined under the facility node.
        kind: Quadrupole
        ...

    - myline:
        kind: BeamLine
        line:
          - thingT:     # An element defined within a line.
             kind: Marker
          ...
```

Element parameters from one element may be inherited by another using an `inherit` node. Example:
```{code} yaml
S2: 
  kind: Sextupole
  length: 0.45
  MagneticMultipoleP:
    Kn2L: 0.56
    tilt2: 0.12

S3:
  inherit: S2        # Inherits parameters from S2
  length: 0.55       # And any inherited parameter may be modified.
```
Inheritance may also be done on the parameter group level. See [here](#s:inherit.params).

To avoid confusion, lattice elements may not be redefined. That is, two lattice element definitions
that use the same element name is not allowed.

%---------------------------------------------------------------------------------------------------
(s:element.matching)=
## Element Name Matching

Lattice element name matching is the process of finding the set of lattice elements that 
are matched to a given string. Name matching is important in a number of instances including
lattice expansion where there are [`Fork`](#s:forking) elements and for evaluating mathematical
expressions.

The simplist form of name matching is if the string matches
the `name` field of an element or elements. 
For example, the string `"Q1"` will match to all elements named `Q1`.

Element matches may be restricted to a given element kind using the notation
```{code} yaml
{kind}::{name}
```
where `{kind}` is the element kind and `{name}` is the element name.
Example:
```{code} yaml
Marker::bpm.
```
This will match to all `Marker` elements whose name is four characters starting with `bpm`
(since a dot matches to any single character, see below).

The `N`{sup}`th` element with a given name can be matched to by appending the character `"#"` 
followed by an integer `N`. For example, `"Quadrupole::Q1#3"` will match to the third element
that matches `"Quadrupole::Q1"`. The `N`{sup}`th` instance selection is always applied last.
Thus with this example, the element kind selector `::` is applied first to get a list of all
quadrupole elements named `Q1` and then the `#3` selection is used to get the third instance.

<!--
Besides the element name, any parameter in the [`MetaP`](#s:meta.params) parameter group can
be matched to using the syntax `"{param-name}::{name-to-match}"`. For example, `"alias::black"`
would match to any element whose `alias` parameter is set to `black`.
-->

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
For example, `"B.4>>Quadrupole::Qaf.*"` would match to all Quadrupole elements in branches 
which have three characters
beginning in "B" and ending in "4" with the element name beginning with "Qaf". And 
`"B.4>>Quadrupole::Qaf.*#2"` would match to the second element matched to.

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
::      
#
:
,
&      # Lowest
```
