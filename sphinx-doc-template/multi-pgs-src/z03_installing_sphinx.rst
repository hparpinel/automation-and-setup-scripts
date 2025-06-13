Installing Sphinx and Tools
===========================

To use this template, install the following dependencies:

Python & pip
------------

Make sure Python and pip are installed:

.. code-block:: bash

    python3 --version
    pip3 --version

Install Sphinx and extensions:

.. code-block:: bash

    pip install sphinx sphinx_rtd_theme

Optional (for PDF output using LaTeX):

.. code-block:: bash

    sudo apt install texlive-latex-base texlive-latex-recommended \
                     texlive-fonts-recommended texlive-latex-extra \
                     texlive-xetex lualatex

You’ll also need:

- `lualatex`: Required for rendering custom fonts and logos
- A terminal that supports `make` (or run equivalent commands manually)

