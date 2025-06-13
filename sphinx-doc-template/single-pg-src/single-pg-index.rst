:orphan:

===========================================
Sphinx Documentation Template: Quick Guide
===========================================

.. toctree::
    :maxdepth: 2
    :caption: Contents:

.. raw:: latex

    \headerlogo
    \thetitle

Introduction
------------

This **single-pg guide** provides a concise overview of how to build documentation using this Sphinx template.

Unlike the full **multi-pgs**, this version is optimized for quick reference and generates a **single-page HTML or PDF**. It's ideal for handouts, simple walkthroughs, or embedded documentation in other platforms.

Repository Highlights
---------------------

This documentation system is built with:

- `Sphinx` + `sphinx_rtd_theme`
- Custom LaTeX preamble and title page
- Support for both multi-page and single-page formats
- Configurable output: HTML and PDF
- Easy-to-use Makefile automation

Quick Start
-----------

1. **Install Sphinx and dependencies:**

.. code-block:: bash

    pip install sphinx sphinx_rtd_theme
    sudo apt install lualatex  # For PDF (Linux only)

2. **Generate HTML:**

.. code-block:: bash

    make single-page-html

3. **Generate PDF:**

.. code-block:: bash

    make single-page-pdf

Directory Layout
----------------

- `single-page/`: Contains this quick guide (`quick-index.rst`)
- `_preamble/`: LaTeX settings for PDF rendering
- `_figs/`, `_fonts/`: Assets and fonts
- `output-dir/single-page/`: Output folder for generated HTML and PDF

For full instructions and advanced configuration, refer to the file **multi-pgs.pdf**.
