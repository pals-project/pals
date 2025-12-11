(c:impl.fileformats)=
# File Formats

The Particle Accelerator Lattice Standard (PALS) documents objects and their properties.
For readability, [this standard uses YAML-style](c:conventions) examples, but the PALS schema can be implemented in a variety of file formats.


## File Endings

When storing a PALS lattice in a file, please use the following self-describing file endings.

* [YAML](https://yaml.org/faq.html): `.pals.yaml`
* [JSON](https://www.json.org/json-en.html): `.pals.json`
* [TOML](https://toml.io): `.pals.toml`
* [XML](https://en.wikipedia.org/wiki/XML): `.pals.xml`


## Schema Files

Schema files for validation have not yet been developed.
A validation tool based on pydantic is in development.
See the [Libraries](#c:impl.libs) section.
