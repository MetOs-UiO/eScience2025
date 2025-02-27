# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from urllib.request import urlopen
from pathlib import Path

# HTML context:
from os.path import basename, dirname, realpath

sys.path.insert(0, os.path.abspath("."))


# -- Project information -----------------------------------------------------

project = "eScience-2025"
copyright = "2025, MetOs, UiO"
author = "MetOs-UiO"
github_user = "MetOs-UiO"
github_repo_name = "eScience2025"  # auto-detected from dirname if blank
github_version = "master"
conf_py_path = "/docs/"  # with leading and trailing slash

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    # "sphinx_lesson",
    # remove once sphinx_rtd_theme updated for contrast and accessibility:
    # "sphinx_rtd_theme_ext_color_contrast",
    "sphinx.ext.graphviz",
    "myst_nb",
    "sphinx_copybutton",
    "sphinx_book_theme",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxemoji.sphinxemoji",
    "sphinx_toolbox.collapse",
    "sphinx_togglebutton",
    "sphinx_toolbox.installation",
]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
# jupyter_execute_notebooks = "off"
# jupyter_execute_notebooks = "auto"   # *only* execute if at least one output is missing.
# jupyter_execute_notebooks = "force"
# jupyter_execute_notebooks = "cache"
nb_execution_mode = "off"
nitpicky = True
# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
    "**.ipynb_checkpoints",
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["css"]

#theme things
html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}
html_theme_options = {
    "repository_url": "https://github.com/MetOs-UiO/eScience2025",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
    "repository_branch":"master",
    "show_navbar_depth":2,
    "home_page_in_toc":True
}
# Intersphinx mapping.  For example, with this you can use
# :py:mod:`multiprocessing` to link straight to the Python docs of that module.
# List all available references:
#   python -msphinx.ext.intersphinx https://docs.python.org/3/objects.inv
# extensions.append('sphinx.ext.intersphinx')
# intersphinx_mapping = {
#    #'python': ('https://docs.python.org/3', None),
#    #'sphinx': ('https://www.sphinx-doc.org/', None),
#    #'numpy': ('https://numpy.org/doc/stable/', None),
#    #'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
#    #'pandas': ('https://pandas.pydata.org/docs/', None),
#    #'matplotlib': ('https://matplotlib.org/', None),
#    'seaborn': ('https://seaborn.pydata.org/', None),
# }

html_logo = "img/es-logo.png"

html_favicon = "img/es-logo.ico"

suppress_warnings = ["myst.header","image.not_readable"]

#def setup(app):
#    app.add_css_file("style.css")
