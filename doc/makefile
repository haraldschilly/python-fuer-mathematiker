# makefile options
# make (default):  build pdf
# make clean:      cleanup temporary latex files
# make latexclean: remove latex files and auxiliary directories
# make distclean:  use git's clean command to get rid of ALL files
# make show:       use xdg-open to open pdf file
# make nb:         start the IPython Notebook server
# make all:        unconditionally build all (default) targets
# make dist:       build the pdf distribution: copy pdf to a filename with date and $REVISION
#                  (if it doesn't resolve the problem, do a healthy make distclean; make)

MASTER=master
PARTS_PAT  =?-?-*
IPYTHON    ?= ipython
PARTS      := $(filter-out $(MASTER).ipynb 0-0-index.ipynb, $(wildcard *.ipynb))
PARTS_TEX  := $(patsubst %.ipynb,%.tex,$(PARTS))
REVISION   := $(shell git rev-parse --short HEAD)
TIMESTAMP  := $(shell date +"%Y%m%d")
JOB        := python4mathematiker

# $(info $(PARTS))

.PHONY = clean latexclean distclean build show cont

build: pdf

clean:
	latexmk -c

# convert all partial tex files
%.tex: %.ipynb res/partial.tplx
	$(IPYTHON) nbconvert --template res/partial.tplx --to latex $<

# convert the (empty) master file
$(JOB).pdf: master.ipynb $(PARTS_TEX) res/master.tplx
	$(IPYTHON) nbconvert --template res/master.tplx --to latex $(MASTER).ipynb
	latexmk -pdf -jobname="$(JOB)" -pdflatex="pdflatex --shell-escape %O %S" $(MASTER).tex

pdf: $(JOB).pdf

latexclean:
	latexmk -C
	find -type d -name "$(PARTS_PAT)" | xargs rm -rf
	-${RM} -f *.tex

distclean:
	-git clean -fdX .
	-${RM} -f *.tex

show: pdf
	xdg-open $(JOB).pdf

nb:
	$(IPYTHON) notebook --no-browser

all:
	make -B

dist: pdf
	cp $(JOB).pdf $(JOB)-${TIMESTAMP}-${REVISION}.pdf

