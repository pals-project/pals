(c:impl.fileformats)=
# File Formats

The Particle Accelerator Lattice Standard (PALS) documents objects and their properties.
For readability, [this standard uses YAML-style](c:conventions) examples, but the PALS schema can be implemented in a variety of file formats.


## File Endings

The following self-describing file suffixes shall be used for top-level PALS files (files that 
contain the root `PALS` node):

* [YAML](https://yaml.org): `.pals.yaml`
* [JSON](https://www.json.org/json-en.html): `.pals.json`
* [TOML](https://toml.io): `.pals.toml`
* [XML](https://en.wikipedia.org/wiki/XML): `.pals.xml`

For sub-level [included](#s:includefiles) PALS format files, replace `.pals` with `.subpals` .

## Schema Files

Schema files for validation have not yet been developed.
A validation tool based on pydantic is in development.
See the [Libraries](#c:impl.libs) section.
