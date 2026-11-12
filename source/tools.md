(c:software)=
# Software Tools

There are reference implementations of PALS "parsers". Here the word "parser" is used loosely since
the parsers do much more than parse PALS files. All parsers will:

- Write and read from/to files.
- Expand and evaluate expressions on lattices ([`lattice expansion`](#s:lattice.expand)).
- Validate existing files.
- Calculate the [floor coordinates](#s:floor) of all elements, both nominal and "misaligned" positions.
- Evaluate dependent (output) parameter values.

## Parsers

- A C/C++ based package [PALSParserCpp](https://github.com/pals-project/PALSParserCpp) 
  which includes a parser has been developed.
  Currently supporting only YAML files, other formats will be added as needed.
- A Python based package [PALSParserPy](https://github.com/pals-project/PALSParserPy),
  which includes the PALSParserCpp parser, has been developed.
- A Julia based package [PALSParserJ](https://github.com/pals-project/PALSParserJ.jl),
  which includes the PALSParserCpp parser, has been developed.
- A Python parser [pals-python](https://github.com/pals-project/pals-python) is in development.

All the parsers mentioned above can be used standalone or integrated into a program.

## Visualization

Both the PALSParserPy and PALSParserJ packages mentioned above have 2D and 3D visualization
components. 

Xelera Research LLC is working to develop an open-source 3D Visualization package
based upon the Blender graphics program. 
This package will provide an intuitive graphical user-interface for accelerator modeling in 3D. 
This work is supported by the U.S. Department of Energy SBIR program.

## Language Converters

Conversion between PALS and other lattice formats, including Bmad, SciBmad, and MAD-X, is
documented in the [Language Converters](#s:language.covert) section.

## Schema Files

Schema files for validation have not yet been developed.
A validation tool based on pydantic is in development.

## List of Simulation Codes Interfaced to PALS

- [BLAST ImpactX](https://impactx.readthedocs.io)
