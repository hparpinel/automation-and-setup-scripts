# ====================================================================
# Makefile for Building Multi-page and Single-page Sphinx Guides
# --------------------------------------------------------------------
# Targets:
#   - multi-pgs-html, multi-pgs-pdf
#   - single-pg-html, single-pg-pdf
# Cleaning:
#   - clean, clean-all, clean-multi-pgs, clean-single-pg, etc.
# Usage:
#   $ export BUILD_MULTI_PGS=1
#   $ make multi-pgs-html
# ====================================================================

SPHINXOPTS       =
SPHINXBUILD      = sphinx-build

# -----------------------------
# Source directories
ROOTDIR           = .
MULTI_PGS_SRCDIR  = $(ROOTDIR)/multi-pgs-src
SINGLE_PG_SRCDIR  = $(ROOTDIR)/single-pg-src
FIGSDIR           = $(ROOTDIR)/_figs
FONTSDIR          = $(ROOTDIR)/_fonts


# -----------------------------
# Intermiediate build directories
BUILDDIR_MULTI_PGS = _build/multi-pgs-src
BUILDDIR_SINGLE_PG = _build/single-pg-src

# -----------------------------
# Final output directories
OUTPUTDIR  = ./output-dir
MULTI_PGS  = $(OUTPUTDIR)/multi-pgs
SINGLE_PG  = $(OUTPUTDIR)/single-pg

# -----------------------------
# Final output files name
MULTI_PGS_OUT_FNAME = multi-pgs
SINGLE_PG_OUT_FNAME = single-pg

# -----------------------------
.PHONY: help
help:
	@echo ''
	@echo '====================== MAKEFILE HELP ======================'
	@echo ''
	@echo 'Environment Variables:'
	@echo '  export BUILD_MULTI_PGS=1       # Enable building the multi-page guide'
	@echo ''
	@echo 'Build Targets:'
	@echo '  make multi-pgs-html            # Generate HTML output for the multi-page guide'
	@echo '  make multi-pgs-pdf             # Generate PDF output for the multi-page guide'
	@echo '  make single-pg-html            # Generate HTML output for the single-page guide'
	@echo '  make single-pg-pdf             # Generate PDF output for the single-page guide'
	@echo ''
	@echo 'Output Directory:'
	@echo '  All generated output will be placed in:'
	@echo '    $(OUTPUTDIR)'
	@echo ''
	@echo 'Cleaning Targets:'
	@echo '  make clean                     # Remove intermediate build files'
	@echo '  make clean-all                 # Remove all builds (HTML & PDF for both guides)'
	@echo '  make clean-multi-pgs           # Remove all multi-page guide builds'
	@echo '  make clean-multi-pgs-html      # Remove multi-page HTML build'
	@echo '  make clean-multi-pgs-pdf       # Remove multi-page PDF build'
	@echo '  make clean-single-pg-html      # Remove single-page HTML build'
	@echo '  make clean-single-pg-pdf       # Remove single-page PDF build'
	@echo ''
	@echo '==========================================================='

# ------------------------------------------------------	
# Targets for multiple pages guide
# ------------------------------------------------------
multi-pgs-html: 
	@cp $(MULTI_PGS_SRCDIR)/*.rst $(ROOTDIR)
	@mv $(ROOTDIR)/multi-pgs-index.rst $(ROOTDIR)/index.rst
	$(SPHINXBUILD) -b html "$(ROOTDIR)" "$(BUILDDIR_MULTI_PGS)/html" $(SPHINXOPTS)
	@$(MAKE) multi-pgs-cleanup
	$(call SUCCESS_MESSAGE,Multiple pages,HTML,$(MULTI_PGS)/html)
	
multi-pgs-pdf: 
	@cp $(MULTI_PGS_SRCDIR)/*.rst $(ROOTDIR)
	@mv $(ROOTDIR)/multi-pgs-index.rst $(ROOTDIR)/index.rst
	@$(SPHINXBUILD) -b latex "$(ROOTDIR)" "$(BUILDDIR_MULTI_PGS)/pdf" $(SPHINXOPTS)
	@cp -r $(FONTSDIR) "$(BUILDDIR_MULTI_PGS)/pdf/"
	@cp $(FIGSDIR)/logo-transparent-stacked-png.png "$(BUILDDIR_MULTI_PGS)/pdf/"
	@cp $(FIGSDIR)/logo-transparent-png.png "$(BUILDDIR_MULTI_PGS)/pdf/"
	@cd "$(BUILDDIR_MULTI_PGS)/pdf" && lualatex multi-pgs.tex
	@$(MAKE) multi-pgs-cleanup
	cp "$(MULTI_PGS)/pdf/$(MULTI_PGS_OUT_FNAME).pdf" "$(OUTPUTDIR)/$(MULTI_PGS_OUT_FNAME).pdf"
	$(call SUCCESS_MESSAGE,Multiple pages,PDF,$(MULTI_PGS)/pdf)
	
# ------------------------------------------------------	
# Targets for single page guide
# ------------------------------------------------------
single-pg-html: 
	@cp $(SINGLE_PG_SRCDIR)/single-pg-index.rst $(ROOTDIR)/index.rst
	@$(SPHINXBUILD) -b singlehtml "$(ROOTDIR)" "$(BUILDDIR_SINGLE_PG)/html" $(SPHINXOPTS)
	@$(MAKE) single-pg-cleanup
	$(call SUCCESS_MESSAGE,Single page Guide,HTML,$(SINGLE_PG)/html)
		
single-pg-pdf: 
	@cp $(SINGLE_PG_SRCDIR)/single-pg-index.rst $(ROOTDIR)/index.rst
	@$(SPHINXBUILD) -b latex "$(ROOTDIR)" "$(BUILDDIR_SINGLE_PG)/pdf" $(SPHINXOPTS) 
	@cp -r $(FONTSDIR) "$(BUILDDIR_SINGLE_PG)/pdf/"
	@cp $(FIGSDIR)/logo-transparent-stacked-png.png "$(BUILDDIR_SINGLE_PG)/pdf/"
	@cp $(FIGSDIR)/logo-transparent-png.png "$(BUILDDIR_SINGLE_PG)/pdf/"
	@cd "$(BUILDDIR_SINGLE_PG)/pdf" && lualatex single-pg.tex  && $(MAKE) 
	@$(MAKE) single-pg-cleanup
	cp "$(SINGLE_PG)/pdf/$(SINGLE_PG_OUT_FNAME).pdf" "$(OUTPUTDIR)/$(SINGLE_PG_OUT_FNAME).pdf"
	$(call SUCCESS_MESSAGESingle page Guide,PDF,$(SINGLE_PG)/pdf)
		
# ------------------------------------------------------
# Pattern rule for common cleanup
multi-pgs-cleanup:
	mkdir -p $(MULTI_PGS)
	rsync -a --remove-source-files $(BUILDDIR_MULTI_PGS)/ $(MULTI_PGS)/
	rm -rf $(ROOTDIR)/*.rst $(ROOTDIR)/*.rsti _build
		
single-pg-cleanup:
	mkdir -p $(SINGLE_PG)
	rsync -a --remove-source-files $(BUILDDIR_SINGLE_PG)/ $(SINGLE_PG)
	rm -rf $(ROOTDIR)/*.rst $(ROOTDIR)/*.rsti _build
	
SUCCESS_MESSAGE = @echo "The $(1) guide $(2) version has been successfully built and can be found at $(3)!"	

# ------------------------------------------------------
define CLEAN_TARGET
	-rm -rf $1
endef

# ------------------------------------------------------
# Multiple pages guide cleaning rules
clean-multi-pgs: clean-multi-pgs-html  clean-multi-pgs-pdf

clean-multi-pgs-html:
	$(call CLEAN_TARGET,$(MULTI_PGS)/html $(MULTI_PGS_OUT_FNAME).html)

clean-multi-pgs-pdf:
	$(call CLEAN_TARGET,$(MULTI_PGS)/pdf $(MULTI_PGS_OUT_FNAME).pdf)

# ------------------------------------------------------
# Quick guide cleaning rules
clean-single-pg: clean-single-pg-html clean-single-pg-pdf

clean-single-pg-html:
	$(call CLEAN_TARGET,$(SINGLE_PG)/html $(SINGLE_PG_OUT_FNAME).html)
	
clean-single-pg-pdf:
	$(call CLEAN_TARGET,$(SINGLE_PG)/pdf $(SINGLE_PG_OUT_FNAME).pdf)	

# ------------------------------------------------------	
# General cleaning rule
clean-all:
	$(call CLEAN_TARGET,$(MULTI_PGS)/* $(SINGLE_PG)/* $(OUTPUTDIR)/*.pdf $(OUTPUTDIR)/*html)	

# ------------------------------------------------------	
# Revome .rst files and
clean:
	$(call CLEAN_TARGET,$(ROOTDIR)/*.rst $(ROOTDIR)/*.rsti _build)
		
