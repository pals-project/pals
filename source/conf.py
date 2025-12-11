# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Particle Accelerator Lattice Standard (PALS)'
copyright = '2025, under CC-BY 4.0 License'
author = 'Jean-Luc Vay, David Sagan, Chad Mitchell, Axel Huebl, David Bruhwihler, Christopher Mayes, Eric Stern, Daniel Winklehner, Michael Ehrlichman, Martin Berz, Giovanni Iadarola, Ji Qiang, Edoardo Zoni, Laurent Deniau, et al.'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design', 'sphinxcontrib.bibtex', 'sphinxcontrib.cairosvgconverter', 'sphinx_copybutton']
myst_enable_extensions = ["colon_fence", "amsmath"]
numfig = True

templates_path = ['_templates']
bibtex_bibfiles = ['bibliography.bib']

# exclude_patterns is set to get around bug in referencing figures in included files.
# See <https://github.com/sphinx-doc/sphinx/issues/9779> for some details.

exclude_patterns = ['parameters']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
## html_static_path = ['_static']
