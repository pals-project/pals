%---------------------------------------------------------------------------------------------------
(s:meta.params)=
## MetaP: Metadata Parameters

`MetaP` has six standard components:
```{code} yaml
MetaP:
  alias: ""         # [string] An alternate name for the element.
  ID: ""            # [string] An identification string.
  label: ""         # [string] A label string
  description: ""   # [string] A descriptive string
  location: ""      # [string] Element's location.
  history: ""       # [string] Element's history. 
```
In addition to an element's `name`, these six strings can be used for pattern matching
when trying to locate all elements of a given type.

Besides the six standard strings, the `MetaP` parameter group can be used to store metadata 
that describes the lattice element but is not part of the PALS standard. 
Example metadata could be blueprint information, information on power supply connections, etc.

Components of `MetaP` are not limited to being simple strings or numbers but can be complex 
structures. The information contained in `MetaP` should be restricted to information that 
does not affect simulations. Also, program specific (as opposed to machine specific) information
should be stored elsewhere.
```{code} yaml
quad1:                  # user-defined name
  kind: Quadrupole      # element switch
  MetaP:
    ID: 0137-85
    location: East transfer line
    history:
      - 2022-04-01: Fixed water leak to vacuum.
      - 2023-06-24: Fixed short in main bus bar.
    manufacture:        # Custom information
      - date: 2017-03-07
      - installed: 2018-01-23
      - ...
```


