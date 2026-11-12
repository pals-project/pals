(s:material.params)=
## MaterialP: Material Parameters

The `MaterialP` parameter group describes the material that an element, or part of an element, is
made of. `MaterialP` describes only the material itself. Geometry, like the thickness of a foil, is
given by other parameters of the element.

The components of this group and their defaults are:
```{code} yaml
MaterialP:
  name: ""                       # [string] Material name. See below.
  state: null                    # [enum] SOLID, LIQUID, GAS, or PLASMA.
  density: null                  # [kg/m^3] Mass density.
  area_density: null             # [kg/m^2] Mass per unit area. See below.
  radiation_length: null         # [kg/m^2] Radiation length.
  mean_excitation_energy: null   # [eV] Mean excitation energy used for energy loss.
  components: []                 # [list] Components of a user defined material. See below.
```

A `null` value means the parameter is not set. If a parameter is not set and the material is
given by name (an element, isotope, chemical formula, or Geant4 material), a program may use
tabulated values for that material. A value that is set replaces the tabulated value. For example,
with `name: "G4_WATER"` and `density: 990`, the density is 990 kg/m^3.

### Material name

The `name` component may be one of the following:
- **Element.** The symbol of an element in the periodic table, for example `"Cu"`.
  The element has its natural isotope abundances.
- **Isotope.** A pound sign `#` followed by the mass number and the element symbol,
  for example `"#2H"` for deuterium. This is the [OpenPMD](https://github.com/openPMD/openPMD-standard/blob/upcoming-2.0.0/EXT_SpeciesType.md)
  notation used for particle species names (see [](#s:names)). Since `#` starts a YAML comment,
  the name must be quoted.
- **Chemical formula.** A compound written as element symbols each followed by an optional count,
  for example `"B4C"` or `"Al2O3"`. A group of symbols may be put in parentheses followed
  by an optional count, for example `"Ca(OH)2"`. Element symbols are case sensitive: `"CO"` is
  carbon monoxide and `"Co"` is cobalt.
- **Geant4 material.** A name from the
  [Geant4 material database](https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/Appendix/materialNames.html),
  including the `G4_` prefix. Examples: `"G4_Cu"`, `"G4_WATER"`, `"G4_AIR"`, `"G4_STAINLESS-STEEL"`,
  `"G4_lH2"` (liquid hydrogen). The composition, density, state, and mean excitation energy are those
  of the Geant4 database.
- **User defined material.** Any other name, with the composition given by `components`.
  In this case the name is a label only.

If `components` is set, `name` cannot be an element, isotope, chemical formula, or Geant4 material.

### Components

A user defined material is built from a list of components. Each component is a dict:
```{code} yaml
components:
  - material:          # [string or MaterialP] Component material.
    atoms:             # [-] Relative number of atoms (or molecules) of this component.
    mass_fraction:     # [-] Fraction of the total mass in this component.
    radiation_length:  # [kg/m^2] Radiation length of this component.
```
The component `material` is a material name (any of the forms above, including a Geant4 material)
or a `MaterialP` group. This allows a compound to be built from other compounds.
A `MaterialP` group used as a component describes only what the component is made of.
Its `name`, `state`, `radiation_length`, `mean_excitation_energy`, and `components` apply.
Its `density` and `area_density` must not be set; the density is that of the whole material.

Each component sets either `atoms` or `mass_fraction`, and all components of a material must use
the same one. `atoms` values are relative and need not sum to one. `mass_fraction` values must sum to one.

The component `radiation_length` is optional. If all components set it, the
radiation length of the material, if not set directly, is
```{code}
  1 / radiation_length = sum over components of (mass_fraction / radiation_length)
```
where the mass fractions are computed from `atoms` if `atoms` is used.

A user defined material that is not itself a component must set either `density` or `area_density`.

### Density and area density

The `density` is the mass density of the material. The `area_density` is the mass per unit area
seen by a particle going through the material at normal incidence. At most one of the two may be
set. Setting both is an error. If `area_density` is set, a tabulated density is not used.

If the element gives a thickness, the two are related by `area_density = density * thickness`, so
either one determines the other. If the element does not give a thickness, only `area_density`
can describe how much material a particle passes through.
The description of each element kind that uses `MaterialP` says which applies.

### Radiation length

The `radiation_length` is the mass radiation length, in mass per unit area. The radiation length as
a distance is `radiation_length / density`.

### Examples

Copper using tabulated values:
```{code} yaml
MaterialP:
  name: "Cu"
```

Boron carbide with a given density:
```{code} yaml
MaterialP:
  name: "B4C"
  density: 2.52e3
```

Deuterated polyethylene, built from elements by atom count:
```{code} yaml
MaterialP:
  name: "deuterated_polyethylene"
  state: SOLID
  density: 1.05e3
  components:
    - material: "C"
      atoms: 2
    - material: "#2H"
      atoms: 4
```

Liquid deuterium:
```{code} yaml
MaterialP:
  name: "#2H"
  state: LIQUID
  density: 162.4
```

A mixture of Geant4 materials by mass:
```{code} yaml
MaterialP:
  name: "steel_water_mix"
  density: 1.78e3
  components:
    - material: "G4_STAINLESS-STEEL"
      mass_fraction: 0.5
    - material: "G4_WATER"
      mass_fraction: 0.5
```
