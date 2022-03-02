import os

from cloudmesh.common.util import banner
from cloudmesh.common.Shell import Shell
from cloudmesh.common.util import readfile
from cloudmesh.common.console import Console
from pathlib import Path


class Convert:
    """
    Implementation in support for

    catalog export bibtex [--name=NAME] [--source=SOURCE] [--destination=DESTINATION]
    catalog export md [--name=NAME]  [--source=SOURCE] [--destination=DESTINATION]
    catalog export [hugo] md [--name=NAME]  [--source=SOURCE] [--destination=DESTINATION]
    """
    def __init__(self):
        pass

    def bibtex(self, name=None, source=None, destination=None):
        raise NotImplementedError

    def md(self, name=None, source=None, destination=None):
        raise NotImplementedError

    def hugo_md(self, name=None, source=None, destination=None):
        raise NotImplementedError

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
                            content[line], "\n",
                            entry,
                        )
                        print()
                except:
                    pass
