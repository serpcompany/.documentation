# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SERP Handbook'
copyright = 'SERP'
author = 'SERP'
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "nbsphinx",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "myst_nb",
    "sphinx_design"
]

myst_enable_extensions = [
    "colon_fence",
    "html_image",
    "deflist",
]

myst_heading_anchors = 3


source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
    '.html': 'html',
    '.css': 'css',
}

# use language set by highlight directive if no language is set by role
inline_highlight_respect_highlight = False
inline_highlight_literals = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['_static', '_static/images','_static/images/css']


# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
# html_theme = 'furo'

html_theme_options = {

    "repository_url": "https://github.com/serpcompany/handbook",
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "toc_title": "Page TOC",
    "use_repository_button": True,
    "launch_buttons": {
        "colab_url": "https://colab.research.google.com",
        "deepnote_url": "https://deepnote.com",
    },
    "logo": {
      "image_light": "_static/images/logo-light.png",
      "image_dark": "_static/images/logo-dark.png",
   }

}

# -- Options for Sphinx Jupyter Notebooks -------------------------------------------------
nbsphinx_allow_errors = True

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".