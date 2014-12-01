
.PHONY = style

style:
	find -name "*.py" -print0 | xargs --null autopep8 --aggressive -i --max-line-length=120
