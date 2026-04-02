(c:impl.fileformats)=
# File Formats

The Particle Accelerator Lattice Standard (PALS) documents objects and their properties.
For readability, [this standard uses YAML-style](c:conventions) examples, 
but the PALS schema can be implemented in a variety of file formats.

## File Endings

It is highly recommended that the following self-describing file suffixes be used for 
top-level PALS files (files that contain the root `PALS` node):

* [YAML](https://yaml.org): `.pals.yaml`
* [JSON](https://www.json.org/json-en.html): `.pals.json`
* [TOML](https://toml.io): `.pals.toml`

For sub-level [included](#s:includefiles) PALS format files, replace `.pals` with `.subpals`.

Note: Not following the recommendation may lead to, for example, reader/visualization tools 
not auto discovering the file as PALS, which can create friction for users.

## Schema Files

Schema files for validation have not yet been developed.
A validation tool based on pydantic is in development.
See the [Libraries](#c:impl.libs) section.
