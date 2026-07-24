(c:lattice-construct)=
# Lattice Construction

%---------------------------------------------------------------------------------------------------
(s:lattice.construct)=
## Constructing a Lattice

A `Lattice` contains a set of branches. The component of `Lattice` is:
```{code} yaml
branches        # [List] List of branches.
```
Each branch is instantiated from a `BeamLine` that is called the `root BeamLine`.
Example:
```{code} yaml
- my_lattice:
    kind: Lattice
    branches:
      - this_line    # this_line is the root beamline for the branch.
      - that_line:
          inherit: that_ring    # Inherit from that_ring BeamLine
          periodic: true
```
In this example, `this_line` and `that_line` are the names of the root beamlines
for the two `Branches` that will be created when the lattice is [expanded](#s:expansion.intro).
Branches created due to `Fork` elements also have root `BeamLines`. `Branches` specified
in the `Lattice` structure are called `root branches` of the `lattice`. Non-root branches
are those branches created due to `Fork` elements.

A branch has the optional components
```{code} yaml
inherit   # [String] Optional. Name of the root BeamLine for the branch. Default is the name of the Branch.
periodic  # [logical] Optional. Are orbit and Twiss parameters periodic? 
          #   Default is the setting of the root BeamLine.
```
The setting of `periodic` for a `Branch` overrides the setting of `periodic`
set in the root `BeamLine`. See [](#s:beamline.components) for documentation of `periodic`.

%---------------------------------------------------------------------------------------------------
(s:branch.expand)=
## Branch Expansion

`Branch expansion` is the process, starting from the `root BeamLine`
of a branch, of constructing the ordered list of lattice elements contained in that branch.
That is, the definitions
of any sublines are substituted into the branch and if the sublines have sublines, this process
is repeated until there are no sublines left.

The first lattice element of any root `BeamLine` line must be a `BeginningEle` element and the expanded
branch line may only contain this one `BeginningEle` element. If a subline contains a `BeginningEle`
element, this element must be dropped from the branch line.

Notes:
- In any region of an expanded `Branch` where the elements are not directionally reversed, the elements
must be ordered such that the longitudinal positions at the upstream end of the elements is ordered
in increasing {math}`s`-position value. For a region where the elements are directionally
reversed, the downstream end of the elements must be ordered in increasing {math}`s`-position.
This mandate on element ordering ensures that the order of elements in a directionally reversed
`BeamLine` is always the reverse of the order of elements in the non-reversed `BeamLine`.
- The order of `BeamLine` definitions within a `facility` list does not affect the expansion.
In particular, the definition of a subline can come after it's use.

%---------------------------------------------------------------------------------------------------
(s:lattice.expand)=
## Lattice Expansion

"Lattice expansion" is the process of creating 
a "finished" lattice structure with all branches expanded and all computable parameters computed.
Note that it may well be that not all computations can be done. For example, if the beginning reference
energy is not set, the reference energy throughout the lattice cannot be computed and any
calculations depending upon the reference energy cannot be done. A PALS compliant parser will flag
such problems.

The steps used for lattice expansion are:

* Start with the root PALS file and construct a tree that contains all `include` and `load` trees.
This is the base tree for the lattice expansion.

* Divide the `facility` list into two lists: The first list, called the "pre-expansion list"
is everything that comes before an `expand_lattice` node. The second list, 
called the "post-expansion" list is everything that comes after the `expand_lattice` node. 
Both lists preserve the order from the initial list.
The post-expansion list will be empty if there is no `expand_lattice` node. 
The post-expansion list is ignored until after the branches have been expanded.

* Go through the pre-expansion list in order and node-by-node evaluate any expressions and execute any `set` commands.
There is no distinction here between delayed evaluation and immediate evaluation [expressions](#s:expressions). 
Both are evaluated. Controllers are ignored here.

  Set commands can only act on the parameters that have been defined up to that point in the 
  pre-expansion list. For example:
  ```{code} yaml
  PALS:
    facility:
      - Q1:                       # Defined before the set
          kind: Quadrupole

      - set:
          parameter: Q.*>MagneticMultipoleP.Kn0
          value: PARAMETER + 0.02

      - Q2:                       # Defined after the set
          kind: Quadrupole
  ```
  In this case since `Q2` is defined after the set, its `MagneticMultipoleP.Kn0` value is not affected
  by the set.

  Note: Some parameter values may not be calculable when an expression is evaluated. 
  If the expression value uses such a parameter, this is an error. For example:
  ```{code} yaml
  PALS:
    facility:
      - Q1:                       # Defined before the set
          kind: Quadrupole
          MagneticMultipoleP:
            Ks1: 0.34

      - set:
          parameter: Q2>MagneticMultipoleP.Bs1
          value: Q1>MagneticMultipoleP.Bs1        # Error! Bs1 not well defined!
  ```
  Here the value of `Ks1` of element `Q1` is set in the element definition
  and eventually the value of `Bs1` will be calculated based on the value of `Ks1`. 
  But this calculation depends upon the reference momentum which is not
  yet known. Therefore `Bs1` is unknown when the `set` command is processed and this is an error. 
  Notice that if `Ks1` had not been set, `Bs1` would default to zero and there would be no error.

* The root `BeamLines` of the root lattice branches are [expanded](#s:branch.expand). 

* If `Fork` elements are present that fork to new beamlines, new branches are created for these
new beamlines and branch expansion is performed on these new lines. 
The new branches may themselves have `Fork` elements that fork to new beamlines
and this process is repeated until there are no new branches to be created.

* Apply the `ABSOLUTE` `Controllers` from the pre-expansion list.
`RELATIVE` `Controllers` are not involved in lattice expansion.

* For each branch, element-by-element, starting at the beginning, the reference parameters (energy, 
species, time, etc.) are calculated along with dependent parameters (EG multipole `Ks1` if `Bs1`
has been set), floor positions, and s-positions.

* Using the post-expansion list, node-by-node from the list beginning, 
evaluate any expressions and execute any `set` commands. Controllers are ignored here.

* Apply `ABSOLUTE` `Controllers` from both lists. 
`RELATIVE` `Controllers` are not involved in lattice expansion.

* Recalculate floor and reference parameters as needed.

Notes:
- All branches must have unique names. However, different branches may use the same root `BeamLine`.
- As detailed in [](#s:forking), some `Fork` elements may connect to an existing branch.
These `Fork` elements will not trigger new branch creation. 
- The PALS standard does not mandate how branches should be stored in memory after expansion.
For example, branches could be stored using an array or a tree. 
In any case, the root branches must be marked as such.


%---------------------------------------------------------------------------------------------------
(s:forking)=
## Forking

A [`Fork`](#s:fork) element marks a point in a lattice branch where another branch branches off from. 
A common example is using a `Fork` element to connect from a storage ring to 
an extraction line or an X-ray beam line. Similarly, a `Fork` can be used to connect 
from the end of an injection line to some place in a ring.
Beam travel is always from the `Fork` element to another point in the machine.
Using `Fork` elements, complex machine layouts may be constructed.
An example is shown in figure {numref}`f:fork`. See the [ForkP](#s:fork.params) documentation
for more details.

```{figure} figures/fork.svg
:width: 80%
:name: f:fork

Example of how `Fork` and `Patch` elements can be used to describe even complicated machine geometries.
In the upper right hand corner is shown the Cornell/Brookhaven CBETA machine.
This machine includes an Energy Recovery Linac (ERL) with
8-pass (4 passes with increasing energy and 4 passes with decreasing energy) along with
an injection line, a diagnostic line, and a beam stop line.
The ERL part of the machine includes the Linac, a Fixed Focusing Alternating 
Gradient (FFAG) arc, and splitter sections.

Shown in the main body of the figure is a blowup of the region where the injection line connects 
to the Linac along with the diagnostic line and the end of the FFAG arc.
The injection line and the ERL was modeled as a single lattice branch which contained all 8 passes.
`Fork` elements were used to connect the injection line to the diagnostic line and ERL to the 
beam stop line.
The geometry of the splitter sections, used to correct the timings of the beams with 
differing energies, is done using `Patch` elements.
```

The `branch` containing a forking element is called the
"source" branch. The `branch` that the forking element points to is called the
"destination" branch. It is possible for these two branches to be one and the same.
The element in the destination branch that the `Fork` connects to is called the "destination" element.

`Fork` elements are uni-directional. That is, particles can travel from a `Fork` element
to the destination element but travel cannot happen in
the reverse direction. To get a bi-directional link, use two `Fork` elements with
the destination element of both Forks being the other `Fork`.

To avoid ambiguities, a `Fork` element has zero length and unit transfer map and
the kinds of destination element are restricted to be one of:
- `Marker`
- `BeginningEle`
- `FloorShift`
- `Fork`

Notice that these kinds of elements have zero length and unit transfer maps.

Example `Fork` element:
```{code} yaml
- to_dump:
    kind: Fork
    ForkP:
      to_line: dump_beamline
      destination_element: dump_beginning
      new_branch: proton_dump
      propagate_reference: true
```
In this example, a `Fork` element connects to a new branch that will be instantiated using
a `BeamLine` called `dump_beamline`. In the expanded lattice, the destination branch will be called
`proton_dump`. The reference properties at the `dump_beginning` element that is forked to,
assuming this is the `BeginningEle` element at the beginning of the branch, will be
the reference properties at the `Fork` element.

%---------------------------------------------------------------------------------------------------
(s:use)=
## use Statement

Multiple `Lattice`s can be defined in a PALS file. By default, the one that gets instantiated 
is the last lattice. This default can be overridden by a `use` statement. Example:
```{code} yaml
- lat1:
    kind: Lattice
    branches:
      ...

- lat2:
    kind: Lattice
    branches:
      ...

- use: lat1
```

%---------------------------------------------------------------------------------------------------
(s:expand.lat)=
## expand_lattice Statement

By default, [lattice expansion](#s:expansion.intro) happens at the end when a PALS file has been read.
Lattice expansion can be triggered before this if there is an `expand_lattice` statement.
This statement must be a child of the `facility` node. Triggering lattice expansion is necessary
when reference to the expanded lattice is needed. For example:
```{code} yaml
facility:
  - q1:
      kind: Quadrupole
      MagneticMultipoleP:
        Kn1L: 0.375

  - bline:
      kind: Beamline
      line:
        - q1:
            repeat: 3

  - lat:
      kind: Lattice
      branches: bline

  - expand_lattice

  - set:
      parameter: lat>>q1>MagneticMultipoleP.Kn1L
      value: parameter * (1 + 1e-4*random_gauss())
```
In this example, the expanded lattice has three elements named `q1`. 
To add a random error to each of these, the lattice has to be expanded before a `set` command is used.

If the `expand_lattice` command is removed from the above example, the three `q1` elements of `lat` have
not yet been instantiated and the set command as written cannot be done. When there is no
`expand_lattice` statement, trying to set the `Kn1L` parameter in the `q1` element definition as in:
```{code} yaml
  - set 
      parameter: q1>MagneticMultipoleP.Kn1L
      value: parameter * (1 + 1e-4*random_gauss())
```
will be successful but without `expand_lattice`, the set targets the single `q1` definition, 
so `random_gauss()` is evaluated only once and all three expanded copies inherit that one value.


