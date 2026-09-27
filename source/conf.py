# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Particle Accelerator Language Standard (PALS)'
copyright = '2025, under CC-BY 4.0 License'
author = 'The PALS team'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_design', 'sphinxcontrib.bibtex', 'sphinxcontrib.cairosvgconverter', 'sphinx_copybutton']
myst_enable_extensions = ["colon_fence", "amsmath", "attrs_block", "attrs_inline"]
numfig = True

templates_path = ['_templates']
bibtex_bibfiles = ['bibliography.bib']

# exclude_patterns is set to get around bug in referencing figures in included files.
# See <https://github.com/sphinx-doc/sphinx/issues/9779> for some details.

exclude_patterns = ['parameters']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "show_toc_level": 3,
    "show_navbar_depth": 3,
    "collapse_navbar": False,
    "repository_url": "https://github.com/pals-project/pals",
    "use_repository_button": True,
    "logo": {
        "image_light": "_static/pals-logo-light.png",
        "image_dark": "_static/pals-logo-dark.png",
        "alt_text": "Particle Accelerator Language Standard (PALS)",
    },
}
html_static_path = ['_static']

# Show only the logo in the top-left of the sidebar (replaces the title text).
html_title = ""

# Route the theme search box to Read the Docs' server-side search.
# See _static/rtd-search-override.js for details.
html_js_files = ['rtd-search-override.js']

# Backdrops for the logo gallery on the Logos page.
# See _static/logos.css for details.
# Text size classes. See _static/text.css for details.
html_css_files = ['logos.css', 'text.css']

# LaTeX (PDF) versions of the text size classes in _static/text.css.
# Inline text `[text]{.large2}` uses \DUrolelarge2.
# Block text `:::{container} large2` uses the sphinxclasslarge2 environment.
# The \csname form is needed since LaTeX command names cannot contain digits.
text_size_classes = {
    'small4': 'tiny', 'small3': 'scriptsize', 'small2': 'footnotesize', 'small': 'small',
    'large': 'large', 'large2': 'Large', 'large3': 'LARGE', 'large4': 'huge', 'large5': 'Huge',
}
latex_elements = {
    'preamble': ''.join(
        rf'''
\expandafter\newcommand\csname DUrole{cls}\endcsname[1]{{{{\{size} #1}}}}
\newenvironment{{sphinxclass{cls}}}{{\{size}}}{{\par}}'''
        for cls, size in text_size_classes.items()),
}
