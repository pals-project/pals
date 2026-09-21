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

Lattice element definitions may only be placed as a child node of the [`facility`](#s:palsroot)
or [`post_expansion`](#s:palsroot) nodes, 
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
