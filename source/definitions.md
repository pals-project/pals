# Definitions

```{figure} figures/lat-tree.svg
:width: 80%
:name: f:lat.tree

An expanded lattice contains a set of branches (not necessarily in an array) and each
branch holds an ordered array of lattice elements.
```

- `Branch`: Contains an ordered list of lattice elements that can be tracked through.
A branch can describe such things as a storage ring or Linac.
- `Branch expansion`: The process, starting from the `root` `BeamLine`
of a branch, of constructing the ordered list of lattice elements contained in that branch.
- `Element`: See `Lattice element`.
- `Lattice`: The outermost structure that holds a set of branches and
can be used to define an entire accelerator complex.
- `Lattice expansion`: This includes `branch expansion` along with connecting branches
together via `Fork` elements, expression evaluations, 
and floor position and reference species and energy calculation. 
- `Root BeamLine`: A `BeamLine` that is used as the basis for creating a branch.
- `Root branch`: A branch that is specified in a `Lattice` structure. Non-root branches
are branches that are formed due to the presence of `Fork` elements.
- `Lattice element`: Basic building block of a lattice most often representing something
physical like a quadrupole magnet or an RF cavity.

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

