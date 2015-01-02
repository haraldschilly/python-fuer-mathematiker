# Python für Mathematiker/innen

This is a German "book" outlining some Python basics from the perspective
of a mathematican or a scienctific researcher doing mathematics.

There are three main tracks:

* *Introduction and basic concepts*
* *Mathemtics*, which does cover concrete mathematics up to statistics
* *Programming techniques* goes in depth of various ways how to program

## Setup

Tell the `%matplotlib inline` magic to always use SVG for plotting.
This gives much nicer graphics in the PDF.

For that, in your local `~/.ipython/profile_default/ipython_config.py` include this:

    c = get_config()
    c.InlineBackend.figure_format = 'svg'

(If that file isn't there, do not hesitate to create it)

## Compile

Just run `make` or read the [makefile] header to learn more about the targets.

## Dependencies

python, numpy, scipy, matplotlib, pandas, sympy, networkx, ...

