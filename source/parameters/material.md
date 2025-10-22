(s:material.params)=
## MaterialP:  Definition of materials

```{code} yaml
MaterialP:
- state:             # ["solid", "liquid", "gas"]
- material:          # [CompoundP,ElementP] definiton of the material in terms of compounds or elements.
```

The definition of materials is inspired by Geant4's material handling. One can either use the name, which is the symbol of an element (`"Cu"`, `"H"`, ...) or compound (`"G4_STAINLESS-STEEL"`).
In the future all elements and materials in the [G4 Manual](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html) will be supported, without the `G4_`-prefix for elements.

Alternatively custom elements can be defined by

```{code} yaml
ElementP:
- name:      # [string] The name of the material
- density:   # [kg/m^3] The density of the material
- Z:         # [int]    The atomic number
- A:         # [int]    The mass number (equals Z+N)
- N:         # [int]    The neutron number
- m:         # [u]      The atomic mass
```

and compounds by

```{code} yaml
CompoundP:
- name:       # [string] The name of the material
- density:    # [kg/cm^3] The density of the material
- elements:   # List of MaterialP or CompoundP of which the compound consists
- ratio:      # List of ratios of the elements
- mass_ratio: # List of mass-ratios of the elements
```

`ratio` describes the ratio in terms of atom/molecule count, while `mass_ratio` describes it int terms of mass fractions.
If density is not given it will be inferred form the densities and mass fractions of the elements.


### Examples
`MaterialP: "Cu"` or `MaterialP: "G4_STAINLESS-STEEL"` or define a new material.

Liquid deuterium can be defined with the `ElementP` parameters:
```{code} yaml
ElementP:
- name: "Deuterium(l)"
- density: 160
- Z: 1
- A: 1
- m: 2.01
```
and deuterated polyethylene (C2H4) can be defined based on the previous definition
```{code} yaml
CompoundP:
- name: "deutPE"
- density: 1050
- elements:
  - "C"
  - "Deuterium(l)"
- ratio:
  - 2
  - 4
```


