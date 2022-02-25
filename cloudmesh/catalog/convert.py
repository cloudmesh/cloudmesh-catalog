import os

from cloudmesh.common.util import path_expand
from cloudmesh.common.util import banner

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
        source = path_expand(source)
        banner(f"check {source}")
        os.system(f"yamllint {source}")