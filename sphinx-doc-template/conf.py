# Configuration file for the Sphinx documentation builder.

# -- Path setup --------------------------------------------------------------
import os
import sys
import logging
import shutil
"""
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
"""
#sys.path.insert(0, os.path.abspath('..'))

CWD = os.getcwd ()

# -- Project information -----------------------------------------------------

project = ''
copyright = ''
author = ''
# this should be kept in sync with gen/catalyst.py
version = 'V2025.6.13'
numfig = True

# -- General configuration ---------------------------------------------------
"""
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
"""
extensions = [ 'sphinx_rtd_theme' ,
              'sphinx.ext.autodoc',
              'sphinx.ext.graphviz',]

# The master toctree document.
master_doc = 'index'

# The suffix(es) of source filenames.
# source_suffix = '.rst'

#sphinx.application.Sphinx
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# remove build with sphinx
html_show_sphinx = False

# -----------------------------------------------------------------------------
# HTML OPTIONS
# -----------------------------------------------------------------------------
"""
# The theme to use for HTML and HTML Help pages.  
"""
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
	
"""
# Paths that contain custom static files (such as style sheets).
# They are copied after the builtin static files,so a file named "default.css" will overwrite the builtin "default.css".
"""
html_static_path = ['_static']
	
html_logo = '_figs/logo-transparent-svg.svg'

html_icon = '_figs/logo-transparent-stacked-svg.svg'

# -----------------------------------------------------------------------------
# LATEX OPTIONS
# -----------------------------------------------------------------------------

latex_engine = 'lualatex'

latex_documents = []

# Read LaTeX preamble from external file
def load_file(file_name):
    with open(file_name, "r") as f:
	    return f.read()
	             
if os.environ.get('BUILD_MULTI_PGS', '0') == '1':
    html_css_files = ['custom.css',]
    latex_preamble = load_file("_preamble/common_preamble.tex")
    class_options = ',oneside'
    maketitle =  load_file("_preamble/custom_title.tex")
else:
    latex_preamble = load_file("_preamble/single_pg_preamble.tex")
    html_css_files = ['custom_single_pg.css',]
    html_theme_options = { 'nosidebar': True,}
    class_options = ',oneside'
    maketitle = ''
    
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '11pt',
    'figure_align': 'htbp',
    'classoptions': class_options,
    'preamble': latex_preamble,
    'maketitle': maketitle,
    'extraclassoptions': 'openany,oneside',
    'passoptionstopackages': r'\PassOptionsToPackage{svgnames}{xcolor}',
    'sphinxsetup': 'verbatimwithframe=true, VerbatimColor={named}{white}, VerbatimHighlightColor={named}{Yellow},VerbatimBorderColor={named}{Black}',   
}

# -----------------------------------------------------------------------------            
multi_pgs_name = 'multi-pgs'
single_pg_name = 'single-pg'

# Default setting (assuming both to be False)
build_multi_pgs = False

"""
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
"""
exclude_patterns = [
	'_build', 
	'Thumbs.db', 
	'.DS_Store',]

# Append the appropriate source directory based on the build target

if os.environ.get('BUILD_MULTI_PGS', '0') == '1':
    build_multi_pgs = True
    sys.path.append(os.path.abspath(os.path.join('.', multi_pgs_name)))
    logging.info(f"Building {multi_pgs_name}")
    exclude_patterns.extend(['single-pg-src/*'])  # Exclude all files in single-pg-src
    latex_documents = [
	(master_doc, f'{multi_pgs_name}.tex', 
	'Repo Documentation', '', 'manual'),
    ]
else:
    logging.warning("No specific guide set for build. Single page guide will be build!")
    sys.path.append(os.path.abspath(os.path.join('.', single_pg_name)))
    logging.info("Building single page guide")
    exclude_patterns = ['multi-pgs-src/*', 'latex_format.tex'] 
    latex_documents = [
    (master_doc, f'{single_pg_name}.tex',
   '', '', 'manual'),
    ]
	
def setup(app):
	app.add_css_file('custom.css')
