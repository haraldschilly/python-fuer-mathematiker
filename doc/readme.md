# Python für Mathematiker/innen

## Setup

Tell the `%matplotlib inline` magic to always use SVG for plotting.
This gives much nicer graphics in the PDF.

For that, in your local `~/.ipython/profile_default/ipython_config.py` include this:

    c = get_config()
    c.InlineBackend.figure_format = 'svg'

## Compile

just run `make`

## Dependencies

python, numpy, scipy, matplotlib, pandas, sympy, ...

