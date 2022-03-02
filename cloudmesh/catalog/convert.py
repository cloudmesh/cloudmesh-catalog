import os

from cloudmesh.common.util import banner
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import readfile
from cloudmesh.common.console import Console
from pathlib import Path
from cloudmesh.catalog.converter import Converter
from cloudmesh.common.util import writefile

class Convert:
    """
    Implementation in support for

    catalog export bibtex [--name=NAME] [--source=SOURCE] [--destination=DESTINATION]
    catalog export md [--name=NAME]  [--source=SOURCE] [--destination=DESTINATION]
    catalog export [hugo] md [--name=NAME]  [--source=SOURCE] [--destination=DESTINATION]
    """
    def __init__(self):
        pass

    def _find_sources_from_dir(self, source=None):
        source = Path(source).resolve()
        return Path(source).rglob('*.yaml')

    def convert(self, sources=None, conversion=None):
        if os.path.isdir(sources):
            sources = self._find_sources_from_dir(self, source=None)
        else:
            sources = [sources]
        for source in sources:
            conversion(source)

    def _bibtex(self, source):
        destination =  source.replace(".yaml", ".bib")
        converter = Converter(filename=source)
        entry = converter.bibtex()
        writefile(destination, entry)

    def _markdown(self, source):
        destination =  source.replace(".yaml", ".md")
        converter = Converter(filename=source)
        entry = converter.markdown()
        writefile(destination, entry)

    def _hugo_markdown(self, source):
        destination =  source.replace(".yaml", "-h.md")
        converter = Converter(filename=source)
        entry = converter.hugo_markdown()
        writefile(destination, entry)

    def bibtex(self, sources=None):
        self.convert(sources, self._bibtex)

    def markdown(self, sources=None):
        self.convert(sources, self._md)

    def hugo_markdown(self, sources=None):
        self.convert(sources, self._hugo_md)

    def yaml_check(self, source="."):
        source = Path(source).resolve()
        banner(f"check {source}")
        for filename in Path(source).rglob('*.yaml'):
            content = readfile(filename).splitlines()
            report = Shell.run(f"yamllint {filename}").strip().splitlines()[1:]
            for entry in report:
                enty = entry.replace("\t", " ").strip()
                #line, column\
                parts    = entry.split()
                line,column = parts[0].split(":")
                line = int(line)
                try:
                    if "line too long" in entry and not "http" in entry:
                        pass
                    else:
                        print (
                            filename, "\n",
                            content[line-1], "\n",
                            entry,
                        )
                        print()
                except:
                    pass
