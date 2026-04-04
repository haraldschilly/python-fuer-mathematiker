# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

"Python für Mathematiker" (Python for Mathematicians) is a German-language educational curriculum delivered as a collection of Jupyter notebooks, designed to be read online or compiled into a single PDF book.

## Common Commands

```bash
# Format all Python files with autopep8 (ignores long line warnings E501)
make style

# Build full PDF documentation (runs style + builds doc/)
make all

# Start Jupyter notebook server
make -C doc nb

# Build PDF from notebooks (uses 4 parallel jobs)
make -C doc pdf

# Clean temporary LaTeX build artifacts
make -C doc clean

# Clean everything including generated files
make -C doc latexclean

# Open generated PDF
make -C doc show
```

## Architecture

### Directory Structure

- `doc/` — All content notebooks and build system
  - `master.ipynb` — Assembles all section notebooks into one book
  - `0-0-index.ipynb` — Table of contents
  - `1-*.ipynb` — Introduction & basic concepts
  - `2-*.ipynb` — Core programming constructs
  - `3-*.ipynb` — Mathematics applications (SymPy, NumPy, plotting, crypto, etc.)
  - `4-*.ipynb` — Advanced topics (testing, concurrency, networking, HPC, etc.)
  - `5-0-links.ipynb`, `6-0-glossar.ipynb`, `7-0-outro.ipynb` — Back matter
  - `res/` — Python source files, images, CSV data, and LaTeX templates (`.tplx`)
- `bsp/` — Standalone example notebooks and test notebooks

### Build Pipeline

Notebooks → `nbconvert` (with `doc/res/master.tplx` / `doc/res/partial.tplx`) → LaTeX → `latexmk`/`pdflatex` → PDF

The `doc/makefile` handles the full conversion chain. Custom `.tplx` templates control LaTeX output formatting.

### Key Dependencies

Python: NumPy, SciPy, Matplotlib, Pandas, SymPy, NetworkX, Jupyter/IPython

Build tools: `nbconvert`, `latexmk`, `pdflatex`, `autopep8`

### Licenses

- Notebooks (text/images/code examples): CC BY-SA 4.0
- Standalone Python files in `doc/res/`: Apache 2.0
