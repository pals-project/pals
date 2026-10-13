(c:top.level)=
# Top Level Structure

%---------------------------------------------------------------------------------------------------
(s:palsroot)=
## PALS Root Object

The root of the PALS schema is given by a `PALS` node. Possible subnodes are:
```{code} yaml
PALS:
  adjustments:              # [list] Lattice parameter adjustments after lattice expansion.
  authors:                  # [list] Authors associated with this file.
  extension_labels:         # [Dict] Optional extensions to PALS that the standard shall ignore.
  facility:                 # [list] lattice elements, beamlines, lattices, parameter set commands, etc.
  girders:                  # [Dict] Girder elements.
  include:                  # [string] Optional literal insert of a file
  load:                     # [list] Files to load. See the "Load Files" section.
  notes:                    # [list] Optional notes of interest.
  phase_space_coordinates:  # [enum] Type of phase space coordinates.
  post_expansion:           # [list] Optional post-expansion setup. 
  reminders:                # [list] Optional reminder messages to be printed when file is read.
  version:                  # [string] Version of the PALS schema used in this file.
```
The `girders` node is documented with the [`Girders` element](#s:girder) documentation.

The difference between `notes` and `reminders` is that reminder messages are meant to be 
printed (or otherwise communicated to the user) every time the file is read.

Example:
```{code} yaml
PALS:
  version: null  # version schema: defined later

  notes:
    - "Extraction transfer line will be added to lattice in next iteration."
    - ...

  reminders:
    - "Important! West RF cavity phasing needs to be done before any simulations!!!"
    - ...

  extension_labels:
    names:
      my_extension: "See the PALS extensions chapter"

  authors:
    - name: Lastname, Firstname
      orcid: AAAA-BBBB-CCCC-DDDD
      affiliation: Affiliation Long Name
      email: lastname@laboratory.gov
    - name: Lastname2, Firstname2
      orcid: EEEE-FFFF-GGGG-HHHH
      affiliation: Affiliation2 Long Name
      email: lastname2@university.edu

  facility:
    - ...  # lattice elements, beamlines, lattices, parameter set commands, etc.
```
Information may appear in a PALS file outside of the `PALS` node but this information is considered
to be outside of the PALS standard and will be ignored by a PALS parser.

PALS file `authors` are optional, but recommended to enable data provenance and contacts.
Per author, the `name` is required; the `orcid`, `affiliation` and `email` fields are optional.

%---------------------------------------------------------------------------------------------------
(s:facility)=
## facility and post_expansion

Constructing the lattice can be divided into two phases. 
The first, "pre-expansion", phase basically involves defining lattice elements, controllers, 
beam lines, etc., and ends with [lattice expansion](#s:lattice.expand).
The second, "post-expansion", phase basically involves making modifications to the expanded lattice. 
Essentially, the information needed for the pre-expansion phase is put in the `facility` sub-node
of `PALS` and the information for the post-expansion phase is put in the `post_expansion` sub-node.
Example:
```{code} yaml
PALS:
  facility:
    - q1:
        kind: Quadrupole
        MagneticMultipoleP:
          Kn1L: 0.375

    - bline:
        kind: Beamline
        line:
          - q1:
              repeat: 3

    - lat:
        kind: Lattice
        branches: bline

  post_expansion:
    - set:
        parameter: q1>MagneticMultipoleP.Kn1L
        value: PARAMETER * (1 + 1e-4*random_gauss())
```
In this example, the expanded lattice has three elements named `q1`. 
To add a random error to each of these, the lattice has to be expanded before a `set` command is used,
and this is accomplished by placing a `set` command under the `post_expansion` node.
If the `set` command had appeared in the `facility` node, and not in the `post_expansion` node, then
when the set command is executed, the set would be applied to the value of `Kn1L` in the definition
of `q1`. In this case, the result would be that all three of the `q1` elements in the expanded lattice would
have the same value of `Kn1L`.

The set of node types that can be used under the `post_expansion` node is the same as the
`facility` node except for `lattice` and `use` nodes.


%---------------------------------------------------------------------------------------------------
(s:includefiles)=
## Including Other Files Within a PALS File

A PALS file can rely on includes from other files using the `include` command.
Included file data will be included verbatim at the current level of nesting.

Example:
```{code} yaml
PALS:
  include: "version-and-globals.subpals.yaml"

  facility:
    - Q01:
        kind: Quadrupole
        include: "include-Q-params.subpals.yaml"

    - ...

    - include: "parameter-set-commands.subpals.yaml"

    - ...
```
The information in an included file is inserted at the `include` point. In this example,
the included file `version-and-globals.subpals.yaml` could look like, for example:
```{code} yaml
version: null  # version schema: defined later
```
and the file `include-Q-params.subpals.yaml` could look like:
```{code} yaml
MagneticMultipoleP:
  Kn3L: 0.3
```
There are two types of included files. One type of file contains a subpart of a compliant PALS file
like in the example above. These "compliant format" files can be used to break up the lattice
information tree into manageable parts. Compliant format files can themselves have include
statements. 

The other type of included files, conform to some other non-PALS 
standard. For example, an included file may be an 
[OpenPMD](https://github.com/openPMD/openPMD-standard) compliant file coded in 
[HDF5](https://www.hdfgroup.org/solutions/hdf5/). 

The recommended suffixes for PALS files is discussed in the [File Formats](#c:impl.fileformats) section.
Other file endings indicate non-PALS data.

An include statement can appear at any level of the information tree but must be within the `PALS` root node.
Note: with YAML files, the overall indentation of the included file is ignored.

A file path in an `include` is interpreted relative to the location of the file that contains the
`include` node.

%---------------------------------------------------------------------------------------------------
(s:load)=
## Load Files

"Loading" files is similar to [including files](#s:includefiles) in that the contents of several
files can be combined. A common use case is where one file defines the layout of a machine and another
file defines the magnet and other settings for a given machine configuration. The final lattice
is the union of these two files. This gives the flexibility where multiple settings files
need only reference one layout file.

While `load` and `include` both combine the contents of separate files, they differ in how the
combination is done. An `include` inserts the contents of a file verbatim at the point where the
`include` appears, and so can be used at any level of the information tree. A `load`, by contrast,
merges whole files `PALS` subnode by `PALS` subnode at the `PALS` root level, following the rules given
below. When both are present, `include` statements are resolved first so that each file is complete
before the files are combined by `load`.

For example, a layout can look like:
```{code} yaml
# Layout file: layout.pals.yaml
PALS:
  notes:
    - "Layout as of 03/12/2027"

  extension_labels:
    names:
      a_ext: A-type extension
      b_ext: B-type extension

  facility:
    - injector:
        kind: Lattice
        branches:
          - ...
```
and a settings file could look like:
```{code} yaml
# Settings file: settings.pals.yaml
PALS:
  notes:
    - "Settings for 12 mrad crossing angle, 0.23 m beta_y at IP."
    - "This is a second node."

  extension_labels:
    names:
      a_ext: A-type extension
      c_ext: C-type extension

  facility:
    - sets:
        - Q1a>MagneticMultipoleP.Kn1: 0.34
        - ...
```
A "joiner" file that combined these files could look like:
```{code} yaml
# Joiner file
PALS:
  notes:
    - "Lattice with orbit correction for blown chopper at B34W."

  load:
    - layout.pals.yaml
    - settings.pals.yaml
    - SELF

  facility:
    - sets:
        - B35W>MagneticMultipoleP.Kn0L: 0.07
        - ...
```

The rules for using `load` are as follows:
- The `load` node must be a component of the `PALS` node. 
- The joiner and loaded files must have a `PALS` node and only that node is merged so
loading ignores custom data outside of the `PALS` tree. 
- A `SELF` designation in the `load` list indicates where the contents of
the joiner file, if there is anything else other than a `load` node,
are to be combined with the contents of the loaded files. If not present, contents of the joiner
file are to be combined at the end. In the above example, the `SELF` line is not needed since it
is last on the `load` list.
- Contents from the joiner and loaded files are combined `PALS` subnode by `PALS` subnode. 
- For the `version` subnode of `PALS`, if the version strings are not the same, the combined version
will be a comma delimited list of the different versions with duplicates discarded. It is an
error for the versions to be incompatible. That is, if the major version is different.
For example, version `1.4.2` is incompatible with `2.0.1`.
- For other scalar `PALS` nodes (EG [`phase_space_coordinates`](#s:phase.space)) the values
must be the same.
- For list type subnodes, the combined list retains the order set by the `load` list and the order
  set within the files themselves. In the above example, the combined `notes` subnode will be:
  ```{code} yaml
  notes:
    - "Layout as of 03/12/2027"
    - "Settings for 12 mrad crossing angle, 0.23 m beta_y at IP."
    - "This is a second note."
    - "Lattice with orbit correction for blown chopper at B34W."
  ```
- For Dict type subnodes of `PALS`, the combined dict will be the union of all the dict entries
for all of the files. If the dict entries are themselves a dict, this combining rule is applied
to the subdicts. If the dict entries are lists, the lists are combined as discussed above.
If the dict entries are scalars, the scalars are combined as discussed above.
In the above example, the combinded `extension_labels` subnode will be
  ```{code} yaml
  # Settings file: settings.pals.yaml
  PALS:

    extension_labels:
      names:
        a_ext: A-type extension
        b_ext: B-type extension
        c_ext: C-type extension
  ```
- A loaded file may itself contain a `load` node, so loading can be nested to any depth. 
There is no ambiguity as to what `SELF` refers to; a `SELF` designation always refers to the 
joiner file in which it appears and there can be at most one SELF entry.
Any combination of cirular and included loads (EG A loads B which includes A) are prohibited.
Files are to be only loaded once and must be loaded at the first opertunity. 
For example, if A loads B and then C, and if B and C both load D, then when B is loaded into A,
D will be included, and when C is loaded into A, D will not be loaded. 
- As with `include`, a file path in a `load` list is interpreted relative to the location of the
file that contains the `load` node (and not the location of the file including or loading the file
that contains the `load` node).
- Load nodes will not appear in the combinded tree.

Loading can also be useful in constructing "composite" accelerator complexes from individual machines.
For example, a joiner file may look like:
```{code} yaml
PALS:
  load:
    - Booster_to_AGS_line.pals.yaml
    - AGS_ring.pals.yaml


  facility:
    - AGS_fork:
        kind: Fork
        ForkP:
          to_line: AGS_ring           # Defined in AGS_ring.pals.yaml
          destination_element: d24w   # AGS element at injection point

    - AGS_inj_patch:
        kind: Patch
        ...

    - AGS_inject:
        kind: BeamLine
        line:
          - Booster_to_AGS_line   # Defined in Booster_to_AGS_line.pals.yaml
          - AGS_inj_patch         # Needed to adjust the branch reference geometry.
          - AGS_fork              # And add a fork to the AGS at the end.

    - Combined_Inject_and_AGS:
        kind: Lattice
        branches:
          - AGS_inject
```
In this example, the file `Booster_to_AGS_line.pals.yaml` (not shown) contains the specification for the transfer
line from the Booster ring to the AGS ring. The file `AGS_ring.pals.yaml` (also not shown) contains the specification
for the AGS ring. The joiner file reads in these specifications and then creates a new transfer
line called `AGS_inject` with a `Patch` element to shift the branch coordinate system from the transfer
line coordinate system to the AGS coordinate system. The `Patch` element is followed by a `Fork` 
element at the end to connect to the AGS. 
The `Combined_Inject_and_AGS` lattice will have this extended transfer line and when the full 
lattice is constructed, the `AGS_ring` will be pulled in due to the `Fork` element. 
