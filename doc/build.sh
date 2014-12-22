#!/usr/bin/env bash

# TODO convert this mess to a proper makefile

# sanitation
set -e
cd `dirname "$0"`

# cleanup
find -type d -name '?-?-*' | xargs rm -rf
rm -f *.tex

# convert all partial tex files
ipython nbconvert --template res/partial.tplx --to latex ?-?-*.ipynb

# we do not need the index
rm -f 0-0-index.tex

# convert the (empty) master file
ipython nbconvert --template res/master.tplx --to latex master.ipynb

# force rebuild
latexmk -C
latexmk -pdf -jobname="python4mathematiker" -pdflatex="pdflatex --shell-escape %O %S" master.tex
