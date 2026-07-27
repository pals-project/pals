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

  The PALS to Bmad conversion uses the following conventions:
  - PALS multipole coefficients are plain field derivatives while Bmad's `An` and `Bn` carry a
    factor of `1/n!` and are integrated over the element length, so the two differ by `L/n!`.
    Where a multipole is the element's own strength it becomes `K1`, `K2` or `K3` instead, which
    are normalized but not length integrated and so need neither factor.
  - A bend's `MagneticMultipoleP.Kn0` is the field the bend actually has, while its
    `BendP` parameters give the reference geometry. Bmad states the difference between the two as
    `DG`, so the reference is subtracted off.
  - A PALS aperture limit is a signed transverse position, whereas a Bmad limit is a distance
    from the axis, so the low-side limits change sign: PALS `x_min: -0.03` becomes
    `x1_limit = 0.03`.
  - A branch's `periodic` setting becomes Bmad's `geometry`, `closed` or `open`.
  - PALS `constant` and `variable` definitions become Bmad definitions written above the
    elements that use them, Bmad resolving a name against what the file has defined *above* the
    point of use rather than anywhere in the file.
  - ABSOLUTE `Controllers` become Bmad `overlay` elements and RELATIVE `Controllers` become
    Bmad `group` elements, the reverse of the Bmad to PALS direction above.

%---------------------------------------------------------------------------------------------------
### MAD-X Conversion

Conversion between PALS and [MAD-X](https://mad.web.cern.ch/mad/):

- Conversion from MAD-X to PALS is not yet available.

- Conversion from PALS to MAD-X is performed by the `pals_to_madx` function in `PALSJulia`.

  MAD-X is a narrower language than PALS, so the converter reports what it cannot carry rather
  than approximating it. The conversion uses the following conventions:
  - MAD-X has no field-valued attribute, so a stated field is normalized by the reference
    rigidity. `beam->brho` is unsigned where the rigidity that normalizes a field is signed, so
    the converter defines its own `pals_brho` constant and divides by that.
  - MAD-X states the reference energy in GeV, RF voltage in MV, RF frequency in MHz and RF phase
    in turns, where PALS states them in eV, V, Hz and radians.
  - MAD-X builds a bend out of its bend angle and arc length. PALS states the same geometry with
    any two of a curvature, a length and the angle, so the missing pair is derived. Face angles
    are measured from the sector face, so a rectangular face angle picks up the part of the bend
    angle that the element's `ref_geometry` assigns to that face.
  - `BodyShiftP` becomes a `SELECT, FLAG=ERROR` and `EALIGN` pair, MAD-X carrying misalignments
    as errors applied to a used sequence rather than as element attributes.
  - `Controllers` become MAD-X variables and deferred (`:=`) assignments. A PALS controller owns
    its variables, so two controllers may each have a variable of the same name; a MAD-X variable
    is a name in the one namespace the whole file shares, so a name more than one controller
    claims is prefixed with the controller that owns it. A RELATIVE controller moves its slave by
    how far the controller has turned from its initial setting, which MAD-X has no notion of, so
    the assignment carries the value of the expression at those initial settings as a subtracted
    term.
  - MAD-X has no geometry attribute -- whether a branch closes on itself follows from how it is
    used -- so a branch's `periodic` setting is carried across as a comment.

%---------------------------------------------------------------------------------------------------
### SciBmad Conversion

Conversion between PALS and [SciBmad](https://github.com/bmad-sim/SciBmad.jl):

- Conversion from SciBmad to PALS is experimental. Code is at: [https://github.com/bmad-sim/Beamlines.jl/pull/114](https://github.com/bmad-sim/Beamlines.jl/pull/114).

- Conversion from PALS to SciBmad is performed by the `pals_to_scibmad` function in `PALSJulia`.

  SciBmad keeps the PALS parameter names and groups, so the conversion is largely a change of
  syntax rather than of convention. `length` is the one element parameter that is not in a
  parameter group and the one whose name differs, becoming `L`.

