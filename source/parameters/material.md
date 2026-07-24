(s:material.params)=
## MaterialP:  Definition of materials

```{code} yaml
MaterialP:
- state:             # ["solid", "liquid", "gas"]
- material:          # [CompoundP, string] definition of the material in terms of compounds or named elements.
```

Materials can be accessed primarily by their name. Similar to the openPMD 2.0.0 specification, pure elements names are their symbols of the periodic table, specific isotopes are denoted by a pound symbol `#` followed by the isotopic number followed by an element, e.g.: `#3He` for Helium-3. Pure elements have their natural isotope ratios.

Mixtures of multiple elements (or isotopes) in specific ratios can be accessed by their name according to Geant4's specifications [G4 Manual](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html) or defined with a custom `CompoundP` object:


```{code} yaml
CompoundP:
- name:       # [string] The name of the material
- density:    # [kg/m^3] The density of the material
- elements:   # List of ElementP or CompoundP of which the compound consists
- ratio:      # List of ratios of the elements
- mass_ratio: # List of mass-ratios of the elements
```
`ratio` describes the ratio in terms of atom/molecule count, while `mass_ratio` describes it int terms of mass fractions.
If `density` is not given it will be inferred form the densities and mass fractions of the elements.


### Examples
Materials can be the names of the material `material: "Cu"` or `material: "G4_STAINLESS-STEEL"` or defined in place:

```{code} yaml
material:
- name: "deuterated polyethylene"
- density: 1050
- elements:
  - "C"
  - "#2H"
- ratio:
  - 2
  - 4
```


