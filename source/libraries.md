(c:impl.libs)=
# Code Packages

There are reference implementations of PALS "parsers". Here the word "parser" is used loosely since
the parsers do much more than parse lattice files. All parsers will:

- Write and read from/to files,
- Expand & evaluate expressions on lattices ( [`lattice expansion`](#s:lattice.expand)),
- Validate existing files.
- Calculate the [floor coordinates](#s:floor) of all elements both nominal and "misaligned" positions.
- Evaluate dependent (output) parameter values.

## Parsers

- A Python based [parser](https://github.com/pals-project/pals-python) is in development.
- A C/C++ based [parser](https://github.com/pals-project/pals-cpp) to read YAML files is being developed.
Eventually, other input formats can be accommodated as the need arises.
- A Julia based [parser](https://github.com/pals-project/pals-julia) is in development. This parser
will use the C++ parser as a back end.

## Visualization

A 3D Visualization package is in development.
Xelera Research LLC is working to develop an open-source extension to the widely used graphics program Blender that will provide an intuitive graphical user-interface for accelerator modeling in 3D. The extension will support lattice editing in both a 2D graphical node-based layout as well as in the 3D view, and it will include support for importing and exporting the PALS lattice standard format. The goal is for this software to enable viewing, editing, or constructing beamline models with a 3D layout that can include realistic physical constraints and infrastructure. Xelera also plans to explore incorporating external signals into the software to permit integration with control systems at accelerator facilities. This would enable such signals to be coupled with a model to permit continuously updated output in the 3D view. This work is supported by the U.S. Department of Energy SBIR program.

## Language converters.

Language converters between PALS and other accelerator simulation languages is contemplated (and is in need
of volunteers). It is envisaged that converting to PALS format will be handled by the individual programs
that implement non-PALS languages since these programs already have the ability to read in
a non-PALS format.

- Conversion between PALS and [Bmad/SciBmad](https://github.com/bmad-sim) is in the planning stages.
