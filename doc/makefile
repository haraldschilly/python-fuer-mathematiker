MASTER="master"
PARTS_PAT="?-?-*"
PARTS := $(filter-out $(MASTER).ipynb 0-0-index.ipynb, $(wildcard *.ipynb))
PARTS_TEX := $(patsubst %.ipynb,%.tex,$(PARTS))

REVISION := $(shell git rev-parse --short HEAD)
JOB := python4mathematiker-$(REVISION)

# $(info $(PARTS))

.PHONY = clean latexclean distclean build show

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
	latexmk -pdf -jobname="$(JOB)" -pdflatex="pdflatex --shell-escape %O %S" $(MASTER).tex

latexclean:
	latexmk -C

distclean:
	git clean -fdX

show: pdf
	xdg-open $(JOB).pdf
