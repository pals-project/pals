(c:impl.libs)=
# Code Packages

There are reference implementations of PALS "parsers". Here the word "parser" is used loosely since
the parsers do much more than parse PALS files. All parsers will:

- Write and read from/to files.
- Expand and evaluate expressions on lattices ( [`lattice expansion`](#s:lattice.expand)).
- Validate existing files.
- Calculate the [floor coordinates](#s:floor) of all elements, both nominal and "misaligned" positions.
- Evaluate dependent (output) parameter values.

%---------------------------------------------------------------------------------------------------
## Parsers

- A Python [parser](https://github.com/pals-project/pals-python) is in development.
- A C/C++ [parser](https://github.com/pals-project/pals-cpp) is in development.
Currently supporting only YAML files, other formats will be added as needed.
- A Julia [parser](https://github.com/pals-project/pals-julia) is in development. This parser
uses the C++ parser as a back end.

%---------------------------------------------------------------------------------------------------
## Visualization

A 3D Visualization package is in development.
Xelera Research LLC is working to develop an open-source extension to the widely used graphics program Blender that will provide an intuitive graphical user-interface for accelerator modeling in 3D. The extension will support lattice editing in both a 2D graphical node-based layout as well as in the 3D view, and it will include support for importing and exporting the PALS standard format. The goal is for this software to enable viewing, editing, or constructing beamline models with a 3D layout that can include realistic physical constraints and infrastructure. Xelera also plans to explore incorporating external signals into the software to permit integration with control systems at accelerator facilities. This would enable such signals to be coupled with a model to permit continuously updated output in the 3D view. This work is supported by the U.S. Department of Energy SBIR program.

%---------------------------------------------------------------------------------------------------
## Language converters.

Language converters between PALS and other accelerator simulation languages is contemplated (and is in need
of volunteers). It is envisaged that converting to PALS format will be handled by the individual programs
that implement non-PALS languages since these programs already have the ability to read in
a non-PALS format.

In construction... pals-cpp and related packages to be documented here ...

%---------------------------------------------------------------------------------------------------
### Bmad Conversion

Converting between PALS and [Bmad](https://github.com/bmad-sim/bmad-ecosystem):

- Conversion from Bmad to PALS can be done with using the `Tao` program. Run `Tao` with a
  Bmad lattice and then a PALS YAML file can be created using the command:
  ```{code} yaml
    write pals <file-name>
  ```
  where `<file-name>` is the name of the yaml file. The default file name, if `<file-name>` 
  is not present, is `lat_1.pals.yaml`. 

  The Bmad to PALS conversion uses the following conventions:
  - Bmad extension information uses `Bmad` for an extension name and `Bmad_` for an extension prefix.
  - If the PALS lattice element kind does not correspond to the Bmad kind, the Bmad kind is
    recorded in a `Bmad.Bmad_key` node.
  - Bmad `overlay` elements are translated to PALS ABSOLUTE `Controllers` and Bmad `group` elements
    are translated to PALS RELATIVE `Controllers`.
  - Bmad `alias`, `type` and `descrip` attributes are translated to PALS `MetaP.alias`, 
    `MetaP.label`, and `MetaP.description` nodes respectively.

- Conversion from PALS to Bmad is performed by the `pals_to_bmad` function in `PALSJulia`.

%---------------------------------------------------------------------------------------------------
### SciBmad Conversion

Conversion between PALS and [SciBmad](https://github.com/bmad-sim/SciBmad.jl):

- Conversion from SciBmad to PALS is experimental. Code is at: [https://github.com/bmad-sim/Beamlines.jl/pull/114](https://github.com/bmad-sim/Beamlines.jl/pull/114).

- Conversion from PALS to SciBmad is performed by the `pals_to_scibmad` function in `PALSJulia`.

