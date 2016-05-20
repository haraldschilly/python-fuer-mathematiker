
.PHONY = style

all: style
	$(MAKE) -C doc/

style:
	find -name "*.py" -print0 | xargs --null autopep8 -i --ignore=E501 # long lines

clean:
	$(MAKE) -C doc/
