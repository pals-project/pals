(c:element.parameters)=
# Element Parameters

Lattice elements parameters are organized into **parameter groups**. 
All groups are organized as dictionaries (structures) and lists.
At the top level, there are the groups with names like 
`MagneticMultipoleP`, `ElectricMultipoleP`, `MetaP`, `AlignmentP`, etc. 
By convention, group names use upper camel case and it is highly recommended that this convention
be followed but it is not mandatory. Also, by convention, parameter groups end with a `P`.
This is to distinguish between element kinds and parameter groups which might
have similar names. For example, `Fork` is the name of an element kind and `ForkP`
is the name of a parameter group which a `Fork` element will have.

For any given element, a given parameter group can only appear once. For example,
the following is not allowed:
```{code} yaml
- q10w:
    kind: Quadrupole
    ApertureP: ...
    ApertureP: ...    # Second instance not allowed!
```

%---------------------------------------------------------------------------------------------------
(s:non.params)=
## Non-Parameter Group Parameters

There are element parameters that are so common, and do not fit into
any of the parameter groups, that they are not grouped. 
These element parameters are:
```{code} yaml
  field_master: NotSet  # [Boolean] See Below.
  is_on: true           # [Boolean] Turns on or off the fields in an element. When off, the element looks like a drift.
  kind: ""              # [enum] Kind of element (Quadrupole, etc.).
  length: 0             # [m] Length of element. For bends this is the arc length.
  name: ""              # [string] The name of element.
  s_position: 0         # [m] The longitudinal position of the element.
```

The setting of `field_master` matters when there is a change in reference energy during a simulation.
In this case, if `field_master = T`, magnetic multipoles, RF, and Bend unnormalized fields will be held constant
and normalized field strengths will be varied. And vice versa when `field_master` is `F`. 

%---------------------------------------------------------------------------------------------------
(s:inherit.params)=
## Naming and Inheriting Parameters

Any group can be given a **name** and the values can be used in another group of the same type
using **import**.
For example:
```{code} yaml
- ap1:
    kind: ApertureP
    x_min: -0.03
    x_max:  0.04
```
The above defines an aperture with the name **ap1**. 
```{code} yaml
- ap2:
    kind: ApertureP
    inherit: ap1
    y_min: -0.02
    y_max:  0.05
```
And the above defines a new aperture group which inherits from **ap1**.

Now we can use the aperture parameter group as follows:
```{code} yaml
- q0:
    kind: Quadrupole
    ApertureP:
      inherit: ap2
```

Naming a parameter group is only needed if the parameter group is defined outside of an element.
```{code} yaml
- q1:
    kind: Quadrupole
    ApertureP: 
      x_width: 0.03
      y_width: 0.02
```
And an element can inherit a parameter group from another element:
```{code} yaml
- q2:
    kind: Quadrupole
    ApertureP:
      inherit: q1.ApertureP
```

For an element to inherit all parameter groups from another element, just inherit the element itself:
```{code} yaml
- q3:
    kind: Quadrupole
    inherit: q2
```

%---------------------------------------------------------------------------------------------------
## User Settable (Input) and Dependent (Output) parameters.

Some parameters are set in the lattice file. These parameters are called "User settable" or "input". 
Some parameters will be computed by the Translator during lattice expansion. These parameters are called "dependent" or "output" parameters. There is a third class of parameters that can be an input
parameter if it is set in the lattice file or will be an output parameter if not set.

For example, the `FloorP` parameters can be set for the `BeginningEle` element which is the
first element of any branch line. For most other elements, the `FloorP` parameters can
be calculated starting at the `BeginningEle` and working forward computing the floor parameters
element-by-element.

%---------------------------------------------------------------------------------------------------

```{include} parameters/ackicker.md
```

```{include} parameters/aperture.md
```

```{include} parameters/beambeam.md
```

```{include} parameters/bend.md
```

```{include} parameters/bodyshift.md
```

```{include} parameters/electricmultipole.md
```

```{include} parameters/floor.md
```

```{include} parameters/floorshift.md
```

```{include} parameters/fork.md
```

```{include} parameters/girder.md
```

```{include} parameters/initialparticle.md
```

```{include} parameters/magneticmultipole.md
```

```{include} parameters/meta.md
```

```{include} parameters/patch.md
```

```{include} parameters/reference.md
```

```{include} parameters/referencechange.md
```

```{include} parameters/rf.md
```

```{include} parameters/solenoid.md
```

```{include} parameters/tracking.md
```


