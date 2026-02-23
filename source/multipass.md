(c:multipass)=
# Multipass

By default, elements in a lattice are considered to be physically distinct from each other
even if they have the same name.
For example:
```{code} YAML
- this_line
    kind: BeamLine
    line:
      - EleA
      - EleA
```
In this example, the two `EleA` elements are considered to be physically distinct. 

However, there are cases where sets of elements in lattice represent the same physical element.
Consider the Energy Recovery Linac (ERL) example shown in {numref}`f:erl`.
```{figure} figures/erl.svg
:width: 70%
:name: f:erl

Example Energy Recovery Linac (ERL): Particle beams are injected
into the linac line from the injection line, after acceleration from the linac, the beams
are transferred through the arc back to the linac where they are decelerated to recover
their energy and then transfered to the dump line.
```

In this example, beams of particles:
```{code} YAML
  a) travel through the injection line, 
  b) accelerate while traveling through the linac line,
  c) travel through the arc line back to the linac line,
  d) decellerate (energy recover) through the linac line,
  e) get dumped into the dump line.
```
Beams on their journey travel through the linac twice and thus elements in the linac will show
up in the [expanded lattice](#s:expansion.intro) twice. 
To mark these pairs of elements in the lattice as the same physical element, 
PALS has the [`multipass`](#s:beamline.components) flag which can be applied to beam lines. 
The ERL may then be constructed like:
```{code} YAML
- inj_line:
    kind: BeamLine
    line: 
       ...

- dump_line:
    kind: BeamLine
    line:
      ...

- arc_line:
    kind: BeamLine
    line:
      ...

- linac_line:
    kind: BeamLine
    multipass: True
    line:
      - cavityA
      - cavityA

- erl_line:
    kind: BeamLine
    line:
      - inj_line
      - linac_line
      - arc_line
      - linac_line
      - dump_line

- erl:
    kind: Lattice
    branches:
      - erl_line
```
Here, for purposes of illustration, the `linac_line` has two elements both named `cavityA`.
Each of these elements is considered distinct from each other however,
when the `erl` lattice is expanded, `cavityA` will appear four times:
```{code} YAML
inj_line elements..., cavityA, cavityA, arc_line elements..., cavityA, cavityA, dump_line elements
                        (1)      (2)                            (1)      (2)
```
Each physical `cavityA` element appears twice in the expanded line. Explicitly, the two `cavityA`
elements that are marked with a `(1)` underneath them represent the first of the `cavityA`
elements in `linac_line` and the two that are marked with a `(2)` underneath them represent second
`cavityA` element in `linac_line`. 
In a more complicated situation where the `linac_line` is traversed {math}`N` times,
the two physical `cavityA` elements will each appear {math}`N` times in the expanded line.
Sets of lattice elements that represent the same physical element are called ``physical element'' sets.

The procedure for how to group lattice elements into physical element sets is as follows. 
For any given element in the lattice, this element has some line it
came from. Call this line {math}`L_0`. The {math}`L_0` line in turn may have been contained 
in some other line {math}`L_1`, etc. 
The chain of lines {math}`L_0`, {math}`L_1`, ..., {math}`L_n` ends at some point and the last (top) line
{math}`L_n` will be one of the root lines used for a lattice branch. 
For any given element in the lattice, starting with {math}`L_0` and proceeding upwards through the
chain, let {math}`L_m` be the *first* line in the chain that is marked as `multipass`. If no such
line exists for a given element, that element has no associated physical elements. 
For elements that have an associated {math}`L_m` multipass line, 
all elements that have a common {math}`L_m` line and have the same
element index[^foot-ix] when {math}`L_m` is expanded are taken to represent the same physical element.
In the example above, the chain for both `cavityA` physical elements is 
```{code} YAML
linac_line, erl_line
```
and `linac_line` is the {math}`L_m` line (*first* line in the chain that is marked as `multipass`) for both.

The elements of a physical element set do not have to all be in the same lattice branch.
For example, in a colliding beam machine with two intersecting rings, the machine can be
represented with two branches, one for each ring. The interaction region where
both beams are passing through common elements can be a beam line that
is marked multipass. In this case, physical element sets will all have two elements, one from each branch.

It is important to note that the [floor](#s:floor) coordinates of the elements in a physical 
element set are not constrained by the `multipass` construction to be the same. 
It is up to the lattice designer to make
sure that the floor positions of the elements in the set make sense (that is, are all the same).

[^foot-ix]: for a given line the
element index with respect to that line is 1 for the first element in the expanded line, the second
element has index 2, etc.

