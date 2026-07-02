(c:extension)=
# Extensions

An Extension is data added to a PALS file that is not part of the PALS standard.
For example, information specific to a particular machine or simulation program
that has no analogue with other machines or simulation programs can be put in as an extension. 

Maintenance of an extension schema falls outside of PALS governance. 
Extension maintainers can add documentation to this section by submitting a [pull request](#s:contribute).
Documentation here should be brief and should have a reference to full documentation maintained
elsewhere. The advantage of this setup is that since the full documentation is external to the PALS repo,
extension maintainers are not encumbered to use PALS pull requests when modifying the full documentation.

Syntax for including extension data in a PALS file is in the 
[Extension Syntax](#s:extension-syntax) section.
A list of "registered" extensions is in the [Extension Documentation](#s:extension-list) section.

%---------------------------------------------------------------------------------------------------
(s:extension-syntax)=
## Extension Syntax

An extension can be introduced at any dictionary entry within `PALS`.
The `extension` dictionary key marks the start of the extension structure, any remaining entries in that dictionary entry belong to the extension.

Explicitly naming these extension dictionary key names is helpful to enable automatically finding 
typographic errors. The syntax is:
```{code} yaml
<some_name>:
  extension: <extension-type>
  ... extension info ...
```
where `<some_name>` is any name (since a given extension type might appear in multiple places in
the PALS file), and `<extension-type>` is the type of the extension. Example:
```{code} yaml
synch_connect:                         # Extension name
  extension: Cornell_CESR_Connect      # Extension type
  alarm_system:                        # Extension stuff ...
    ...
```
In this example, the `synch_connect` dictionary key is the start of the extension. The type of extension is
`Cornell_CESR_Connect`. Any further entries in `synch_connect` will be excluded from any
PALS validation process.

Alternatively, extension metadata names may be "registered" using an `extension_labels` attribute
to be used as the start of the extension.
The `extension_labels` attribute must appear as a child of the `PALS` root node.
The `extension_labels` attribute can also be used to register list values.
`extension_labels` has three components, at least one of them is required:
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
      short_name: description of short_name usage
      blueprint: what is a blue print
      Rotator: New type of element
    prefixes:
      SciBmad_: for the SciBmad ecosystem

  facility:
    - Q1_vary_long_string:
        short_name: Q1       # Extension matching "short_name".
        SciBmad_connect:     # Extension with "SciBmad_" prefix.
          ... SciBmad connection info ...
    ...
    - R23:
        kind: Rotator   # enum value is an extension name.
```
The advantage of using `extension_labels` is that single attribute key extensions are possible
(there does not have to be an `extension` key).

%---------------------------------------------------------------------------------------------------
(s:extension-list)=
## Extension Documentation

This section is in development and will eventually contain documentation of extensions in use.
