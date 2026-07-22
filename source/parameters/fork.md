(s:fork.params)=
## ForkP: Fork Parameters

The `ForkP` parameter group holds parameters for a [`Fork`](#s:fork) element to describe what element
the `Fork` element is connected to.

The components of the `ForkP` group are:
```{code} yaml
ForkP:
  to_line                    # [string] Required. Name of branch or beam line to fork to.
  destination_element        # [string] Destination element to fork to. Default is the beginning element.
  direction: FORWARDS        # [enum] Longitudinal Direction of travel of injected beam.
  new_branch: SELF           # [string] Name to give newly created destination branch.
  propagate_reference: true  # [logical] Propagate reference species and energy.
```

The `branch` containing a forking element is called the
"source" branch. The `branch` that the forking element points to is called the
"destination" branch. It is possible for these two branches to be one and the same.
The element in the destination branch that the `Fork` connects to is called the "destination" element.

The `to_line` parameter is required and names the branch or beam line to fork to.
- If the value of `new_branch` is `SELF` (the default), `to_line` must point to a `BeamLine` 
  and a new branch is created with the same name as the beam line.
- If the value of `new_branch` is `null`, `to_line` must point to an existing branch and no new branch is created.
- If the value of `new_branch` is anything else, the action is the same as if the setting is `SELF`
  except that the new branch is named using the value of `new_branch`. 

If and only if the destination element is the beginning element of a new branch, 
the floor coordinates will be propagated from the `Fork` element to the beginning of the new branch.

The optional `destination_element` component of `ForkP` gives the name of the destination element. 
If not present, the default is the first element of the line.
The name given by `destination_element` must be unique.
The destination element may inherit the reference species and energy of the `Fork` element 
if and only if the destination element is the beginning element of a new branch and
the `propagate_reference` component is set to `true`. If the destination element is not
the beginning element, `propagate_reference` is ignored and no reference parameters are
propagated.

The possible values of the optional `direction` switch are:
```{code} yaml
FORWARDS            # Injected particle propagates in the forward (+s) direction. Default.
BACKWARDS           # Injected particle propagates in the backward (-s) direction.
```

The `direction` component of `ForkP` indicates the direction that a particle moving into
the forked-to branch will travel. If `direction` is set to `FORWARDS` (the default)
the direction of travel is downstream (`+s`-direction) and vice versa if `direction` is set to
`BACKWARDS`. Note: It does not make sense to have `direction` set to `BACKWARDS` if the
destination element is the `Beginning` element. Similarly, it does not make sense to have `direction`
set to `FORWARDS` if the destination element is the end element in the branch.

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
`proton_dump`. The reference properties at the `dump_beginning` element that is forked to
will be the reference properties at the `Fork` element.

