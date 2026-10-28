%---------------------------------------------------------------------------------------------------
(s:girder.params)=
## GirderP: Girder Parameters

The `GirderP` parameter group holds parameters that describe `Girder` elements.

The components of this group are:
```{code} yaml
  elements: ""        # [string] list of lattice elements the girder supports.
```
The list of lattice elements is not restricted. The list does not have to be in any order and
elements from different branches may be present.