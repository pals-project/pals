(s:fork.from.params)=
## ForkFromP: List of names of Fork elements forking to this element.

The `ForkFromP` parameter group gives a list of Fork elements forking to the element containing
the `ForkFromP` group. This list is constructed by a PALS compliant parser and included in the
expanded lattice tree.

The components of `ForkFromP` are the names of the fork elements using 
`{branch-name}>>{element-name}` with a value equal to the index in the line of the fork element.
Example: 
```{code} yaml
  ForkFromP:
    - inject_line>>inj_fork: 134       
    - alt_line>>end_fork: 37
```
In this case there are two `Fork` elements forking to this element. One `Fork` element is called
`inj_fork` and is in the `inject_line` branch. This element is the 137{sup}`th` element in the branch.
The other `Fork` element is named `end_fork` and is the 37{sup}`th` element in the `alt_line` branch.
