MASTER="master"
PARTS_PAT="?-?-*"
PARTS := $(filter-out $(MASTER).ipynb 0-0-index.ipynb, $(wildcard *.ipynb))
PARTS_TEX := $(patsubst %.ipynb,%.tex,$(PARTS))
DEP_FILES := res/partial.tplx res/master.tplx

REVISION := $(shell git rev-parse --short HEAD)

# $(info $(PARTS))

.PHONY = clean latexclean distclean build

build: $(PARTS_TEX) $(DEP_FILES) pdf
#  tex_master pdf

clean:
	latexmk -c
	find -type d -name "$(PARTS_PAT)" | xargs rm -rf
	rm -f *.tex

# convert all partial tex files
%.tex: %.ipynb $(DEP_FILES)
	ipython nbconvert --template res/partial.tplx --to latex $<

# convert the (empty) master file
tex_master: master.ipynb $(DEP_FILES)
	ipython nbconvert --template res/master.tplx --to latex $(MASTER).ipynb

pdf: tex_master
	latexmk -pdf -jobname="python4mathematiker" -pdflatex="pdflatex --shell-escape %O %S" $(MASTER).tex

latexclean:
	latexmk -C

distclean:
	git clean -fdX
