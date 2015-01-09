
.PHONY = style

all: style
	$(MAKE) -C doc/

style:
	find -name "*.py" -print0 | xargs --null autopep8 --aggressive -i --max-line-length=120


