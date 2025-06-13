Usage
=====

Directory Structure
-------------------

The main components of this repo are:

- `multi-pgs-src/`: Contains reStructuredText files for the multi-page guide.
- `single-pg-src/`: Contains content for the one-page quick guide.
- `_preamble/`: Custom LaTeX preambles and title pages.
- `_figs/`: Logo assets used in the documentation.
- `_fonts/`: Custom fonts (e.g., Montserrat) used for PDF output.
- `_static/` and `_templates/`: CSS and HTML template overrides.
- `output-dir/`: Stores final output files.
- `Makefile`: Automates building guides.

Build Commands
--------------

Set the appropriate environment variable and run the following commands:

**Multiple Pages Guide:**

.. code-block:: bash

    export BUILD_MULTI_PGS=1 
    make multi-pgs-html         # Generates multi-page HTML
    make make multi-pgs-pdf     # Generates multi-page PDF

**Single Page Guide:**

.. code-block:: bash

    make single-pg-html    # Generates single-page HTML
    make single-pg-pdf    # Generates single-page PDF

Cleanup Commands:

.. code-block:: bash

    make clean             # Removes intermediate files
    make clean-all         # Removes all builds and outputs
