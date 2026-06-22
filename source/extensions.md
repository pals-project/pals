(c:extension)=
# Extensions

An Extension is data added to a PALS file that is not part of the PALS standard.
For example, information specific to a particular machine or simulation program
that has no analogue with other machines or simulation programs can be put in as an extension. 

Maintenance of an extension schema falls outside of PALS governance. 
Extension maintainers can add extension documentation submitting a [pull request](#s:contribute).
If the amount of documentation is "large", it is encouraged that the documentation put in the PALS
repository should be relatively brief and there should be a reference to full documentation maintained
elsewhere. The advantage of this setup is that since the full documentation is external to the PALS repo,
extension maintainers are not encumbered to use PALS pull requests when modifying the full documentation.

Syntax for including extension data in a PALS file is in the 
[Extension Syntax](#s:extension-syntax) section.
A list of documented extensions is in the [Extension Documentation](#s:extension-list) section
and this is where extension maintainers should put their extension documentation.

%---------------------------------------------------------------------------------------------------
(s:extension-syntax)=
## Extension Syntax

An extension block can be introduced at any level in a PALS file.
The syntax is:
```{code} yaml
<some_name>:
  extension: <extension-type>
  ... extension info ...
```
where `<some_name>` is any name and `<extension-type>` is the type of the extension. Example:
```{code} yaml
synch_connect:                         # Extension name
  extension: Cornell_CESR_Connect      # Extension type
  alarm_system:                        # Extension stuff ...
    ...
```
In this example, the `synch_connect` dictionary key is the start of the extension. The type of extension is
`Cornell_CESR_Connect`. Any further entries in `synch_connect` will be excluded from any
PALS validation process. Either a dict or a list can be used for the children of `<some_name>`.

Alternatively, extension metadata names may be "registered" using an `extension_labels` attribute.
Registration means that a PALS parser can validate the extension name.
Extension metadata names appear at the start (top level) of an extension block.
The `extension_labels` attribute must appear as a child of the `PALS` root node.
The `extension_labels` block can also be used to define enum values.
The `extension_labels` block has three components, at least one of them is required:
```{code} yaml
PALS:
  extension_labels:
    names:            # Dict of names + description
    prefixes:         # Dict of prefixes + description
    suffixes:         # Dict of suffixes + description
```
The `names` section contains a dictionary of extension names. 
The key of each entry of the dictionary is an extension name and the value of each
entry being a short description.
Any key name or enum value in the PALS file that match one of these names is considered an extension.
Similarly, the `prefixes` and `suffixes` sections contain dictionaries of extension prefixes and suffixes as keys, and their descriptions as values.
Any key name or enum value in the PALS file that has a prefix or suffix that matches one of these 
is considered an extension.
Example:
```{code} yaml
PALS:
  extension_labels:
    names:
      data_base:   Name used in the machine database.
      blueprint:   Blueprint ID number. 
      Rotator:     Enum value. A new type of element.
    prefixes:
      SciBmad_:    Prefix for the SciBmad ecosystem.

  facility:
    - Q1w:                   # Lattice element name
        data_base: Q1_czt    # Extension matching "data_base".
        SciBmad_connect:     # Extension with "SciBmad_" prefix.
          ... SciBmad connection info ...
    ...
    - R23:              # Another lattice element
        kind: Rotator   # enum value is a registered extension.
```
The advantage of using `extension_labels` is that enums can be defined and 
single attribute key extensions are possible (there does not have to be an `extension` key).

%---------------------------------------------------------------------------------------------------
(s:extension-list)=
## Extension Documentation

This section is in development and will eventually contain documentation of extensions in use.
