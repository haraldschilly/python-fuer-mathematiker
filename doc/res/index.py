#!/usr/bin/env python
# coding: utf8
from glob import glob
from IPython.display import HTML
from IPython.nbformat import current

index_style = """
<style>
div.index > div {
display: block;
font-size: 135%;
line-height: 140%;
}
div.index > div.minor {
font-size: 125%;
padding-left: 2em;
}
</style>
"""


def extract_title(cell):
    """
    Extracts from a given cell in a notebook the <h1> title in a markdown content, if available,
    or the explicitly set heading of level 1 - otherwise None.
    """
    if cell["cell_type"] == "markdown":
        for line in cell["source"].splitlines():
            if line.startswith("# "):
                return line[2:]
    elif cell["cell_type"] == "heading" and cell["level"] == 1:
        return cell["source"]
    return None


def mk_index():
    out = index_style + u"<div class='index'>"
    for fn in sorted(glob("?-?-*.ipynb")):
        with open(fn) as f:
            nb = current.read(f, "ipynb")
            for cell in nb["worksheets"][0]["cells"]:
                title = extract_title(cell)
                if title:
                    break

            title = title or fn.split("-")[2][:-6].title()
            major, minor = fn.split("-")[:2]
            if int(minor) == 0:
                minor = ""
                cls = "major"
            else:
                minor = "." + minor
                cls = "minor"
            fn = fn.decode("utf8")
            out += u"""
                    <div class='{cls}'>
                        §{major}{minor} <a href='{fn}'>{title}</a>
                    </div>""".format(**locals())
    return HTML(out + u"</div>")
