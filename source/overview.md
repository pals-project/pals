# Overview

The Particle Accelerator Lattice Standard (PALS) defines a standard for the sharing of
machine information in general and lattice information in particular for
particle accelerators and storage rings. PALS aims to promote:

 - Portability between various applications and differing algorithms
 - A unified open access description for scientific data (publishing and archiving)
 - A unified description for post-processing, visualization and analysis.

Additionally, associated PALS code will be usable from within simulation programs to read and write
lattice files thus relieving programmers from reinventing the wheel.

PALS is able to describe the connections between various things
from the connection of injection and extraction lines connected to a storage ring to the interaction region
of colliding beam storage rings where particles are moving through magnets in opposite directions. A PALS
based lattice is able to
hold all the information about an entire machine complex from beam creation to dump lines enabling a 
single lattice to be used as the basis of start-to-end simulations.

PALS is built to be easily customizable so that custom information may be inserted by a program into a lattice.
This custom information is generally not usable by other programs but can be useful when a program accesses
lattice files that it generated. 


%---------------------------------------------------------------------------------------------------
## What PALS Is

PALS is a schema that defines things like the names of various lattice element kinds, 
how to organize lattice elements into lines which beams of particles or photons can move through, etc. 
PALS is also being developed to describe non-lattice things like the machine control system, power supply
connections, shielding wall geometries, etc.

%---------------------------------------------------------------------------------------------------
## What PALS Is Not

PALS does not do simulations and, in particular, does not do tracking. That said, PALS lattice files
can store parameters that can be used to configure simulations. 

%---------------------------------------------------------------------------------------------------
(s:std.components)=
## PALS components

The general idea as to how a simulation program could use PALS to read and write lattice
files is shown schematically below.
```{figure} figures/translator.svg
:width: 70%
:name: f:trans

Schematic showing how a simulation program can interact with a PALS compliant lattice file.
```
The components here are:
- **Simulation program:** A simulation program.
- **Interface layer:** Code to interface between the structures defined by the program and the 
lattice structure defined by the Translator. This code will be program specific and outside the
scope of the standard. However, structure translation should (hopefully) be 
relatively straightforward.
- **Translator:** Package supplied with the lattice standard. The Translator has code to put 
lattice information into an "expanded form". 
This includes expanding beam lines, evaluating expressions, etc.
- **Reader / Writer:** Package to read/write files of a standard format (JSON, YAML, etc). 
Packages to do this are widely available.
- **Lattice File:** A PALS lattice file in a standard format such as JSON, YAML, etc.

The PALS standard can be divided into several pieces:
- **Schema standard:** The schema defines, in a language neutral manner, the information that 
can appear in a lattice file. This includes standardized names of lattice elements and 
lattice parameters, definitions of lattice parameters, how lattice elements can be organized
into branches to describe the entire accelerator complex, etc.
- **File format standards:** For various formats like YAML and Python there is a file format
standard to ensure that different translators are able to read a PALS compliant lattice file.
- **Translator standard:** After reading in a lattice file, a translator can present to
a simulation program a data object that represents the lattice file. 
There are two basic representations that a PALS compliant translator must be able construct.
The **exact** representation is a direct translation of the contents of the lattice file
without any lattice expansions or expression evaluations.
The **expanded** representation has, among other things, all lines expanded into branches 
and all expressions evaluated. 

Note: Since the schema and translator parts are logically intertwined, there has been no attempt
to separate these in the PALS documentation here.
The file formats for the various languages like YAML, etc. are separately documented.

