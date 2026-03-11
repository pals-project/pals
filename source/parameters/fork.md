(s:fork.params)=
## ForkP: Fork Parameters

The `ForkP` parameter group holds parameters for a [`Fork`](#s:fork) element to describe what element
the `Fork` element is connected to.

The components of the `ForkP` group are:
```{code} yaml
  to_line                    # [name] Required. Name of branch or beam line to fork to.
  to_element                 # [name] Element to fork to. Default is the beginning element.
  direction: FORWARDS        # [enum] Longitudinal Direction of travel of injected beam.
  new_branch: null           # [name] Name to give newly created Branch.
  propagate_reference: true  # [logical] Propagate reference species and energy.
```

The `branch` containing a forking element is called the
"`from-branch`". The `branch` that the forking element points to is called the
"`to-branch`". It is possible for these two branches to be one and the same.
The element in the to-branch that the `Fork` connects to is called the "`to-element`".

The `to_line` parameter is required and names the branch or beam line to fork to.
If `new_branch` is present and not `null`, a new branch is created in the lattice 
set of branches with
the name given by `new_branch` and the `Fork` element will point to this new branch. 
If `new_branch` is not present or is `null`, the to-element will be in an existing branch.

The optional `to_element` component of `ForkP` gives the name of the `to-element`. 
If not present, the default is the `Beginning` element.
The names given by `to_element` must be unique.
The `to-element` may inherit the reference species and energy of the `Fork` element 
if and only if the `to-element` is the `Beginning` element and
the `propagate_reference` component is set to `true`. If the `to-element` is not
the beginning element, `propagate_reference` is ignored and no reference parameters are
propagated.

The possible values of the optional `direction` switch are:
```{code} yaml
FORWARDS            # Injected particle propagates in forward (+s) direction. Default.
BACKWARDS           # Injected particle propagates in reverse (-s) direction.
```

The `direction` component of `ForkP` indicates the direction that a particle moving into
the forked-to branch will travel. If `direction` is set to `FORWARDS` (the default)
the direction of travel is downstream (`+s`-direction) and vice versa if `direction` is set to
`BACKWARDS`. Note: It does not make sense to have `direction` set to `BACKWARDS` if the
to-element is the `Beginning` element. Similarly, it does not make sense to have `direction`
set to `FORWARDS` if the to-element is the end element in the branch.

Example `Fork` element:
```{code} yaml
- to_dump:
    kind: Fork
    ForkP:
      to_line: generic_dump
      to_element: dump_beginning
      to_branch: this_dump
      propagate_reference: true
```
In this example, a `Fork` element connects to a new branch that will be instantiated using
a beam line called `generic_dump`. In the expanded lattice the to-branch will be called
`this_dump`. The reference properties at the `dump_beginning` element that is forked to,
assuming this is the `BeginningEle` element at the beginning of the branch, will be
the reference properties at the `Fork` element.

