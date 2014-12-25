# makefile options
# make (plain):    build pdf
# make clean:      cleanup temporary latex files and remove auxiliary directories
# make distclean:  use git's clean command to get rid of ALL files
# make show:       use xdg-open to open pdf file
# make nb:         start the IPython Notebook server

MASTER="master"
PARTS_PAT="?-?-*"
PARTS := $(filter-out $(MASTER).ipynb 0-0-index.ipynb, $(wildcard *.ipynb))
PARTS_TEX := $(patsubst %.ipynb,%.tex,$(PARTS))
REVISION := $(shell git rev-parse --short HEAD)
JOB := python4mathematiker-$(REVISION)
LATEXCMD := -pdf -jobname="$(JOB)" -pdflatex="pdflatex --shell-escape %O %S" $(MASTER).tex

# $(info $(PARTS))

.PHONY = clean latexclean distclean build show cont

build: pdf

clean:
	latexmk -c
	find -type d -name "$(PARTS_PAT)" | xargs rm -rf
	rm -f *.tex

# convert all partial tex files
%.tex: %.ipynb res/partial.tplx
	ipython nbconvert --template res/partial.tplx --to latex $<

# convert the (empty) master file
tex_master: master.ipynb $(PARTS_TEX) res/master.tplx
	ipython nbconvert --template res/master.tplx --to latex $(MASTER).ipynb

pdf: tex_master
	latexmk $(LATEXCMD)

latexclean:
	latexmk -C

distclean:
	git clean -fdX

show: pdf
	xdg-open $(JOB).pdf

nb:
	ipython notebook --no-browser
