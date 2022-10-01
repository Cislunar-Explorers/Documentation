# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

os.environ["READTHEDOCS_PROJECT"] = "Cislunar Explorers Software Documentation"

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Cislunar Explorers'
copyright = '2022, Cislunar Explorers'
author = 'Cislunar Explorers'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sphinx_rtd_theme

extensions = ["sphinx_rtd_theme", "subprojecttoctree"]

# Configure these docs to be the main project of the other docs
is_subproject = False
readthedocs_url = "https://cislunar-explorers-software-documentation.readthedocs.io"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []
