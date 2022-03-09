import os
from pathlib import Path
import yaml

from cloudmesh.catalog.converter import Converter
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import banner
from cloudmesh.common.util import readfile
from cloudmesh.common.util import writefile
from cloudmesh.common.console import Console

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
        result = Path(source).rglob('*.yaml')
        return result

    def convert(self, source=None, conversion=None, template=None):
        if type(source) is str and os.path.isdir(source):
            sources = self._find_sources_from_dir(source=source)
        elif type(source) is str:
            sources = [source]
        else:
            sources = source
        for source in sources:
            print(f"Convert {source} to {conversion.__name__[1:]}")
            if template is None:
                conversion(source)
            else:
                conversion(source, template)

    def _bibtex(self, source):
        destination = str(source).replace(".yaml", ".bib")
        converter = Converter(filename=source)
        entry = converter.bibtex()
        writefile(destination, entry)

    def _markdown(self, source):
        destination = str(source).replace(".yaml", ".md")
        converter = Converter(filename=source)
        entry = converter.markdown()
        writefile(destination, entry)

    def _hugo_markdown(self, source):
        destination = str(source).replace(".yaml", "-h.md")
        converter = Converter(filename=source)
        entry = converter.hugo_markdown()
        writefile(destination, entry)

    def _template(self, source, template):
        raise NotImplementedError
        ending = str(source).rsplit(".")[1]
        destination = str(source).replace(".yaml", ending)
        converter = Converter(filename=source)
        entry = converter.template(template)
        writefile(destination, entry)

    def template(self, sources=None, template=None):
        self.convert(sources, self._template, template=template)

    def bibtex(self, sources=None):
        self.convert(sources, self._bibtex)

    def markdown(self, sources=None):
        self.convert(sources, self._markdown)

    def hugo_markdown(self, sources=None):
        self.convert(sources, self._hugo_markdown)

    def yaml_check(self, source="."):
        source = Path(source).resolve()
        banner(f"check {source}")
        for filename in Path(source).rglob('*.yaml'):
            content = readfile(filename).splitlines()
            report = Shell.run(f"yamllint {filename}").strip().splitlines()[1:]
            for entry in report:
                entry = entry.replace("\t", " ").strip()
                # line, column\
                parts = entry.split()
                line, column = parts[0].split(":")
                line = int(line)
                try:
                    if "line too long" in entry and not "http" in entry:
                        pass
                    else:
                        print(
                            filename, "\n",
                            content[line - 1], "\n",
                            entry,
                        )
                        print()
                except:
                    pass

            content = readfile(filename)
            entry = yaml.safe_load(content)

            value = entry["id"]
            if value.lower() in ["missing", "unkown"]:
                Console.error(f"id is not specified {filename} id={value} wrong")

            for _date in ["modified", "created"]:
                value = entry[_date]
                # verify if value is corredt. datetime
                try:
                    year, month, day = value.split("-")
                    if len (year) != 4:
                        Console.error(f"year format in {filename} at {_date} wrong: it should be YYYY-MM-DD")
                    if not (1 <= month <= 12):
                        Console.error(f"month format in {filename} at {_date} wrong: it should be YYYY-MM-DD")
                    if not (1 <= day <= 31):
                        Console.error(f"day format in {filename} at {_date} wrong: it should be YYYY-MM-DD")
                except:
                    Console.error(f"time format in {filename} at {_date} wrong: it should be YYYY-MM-DD")


