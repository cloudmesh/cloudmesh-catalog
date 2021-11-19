from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.catalog.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters

class CatalogCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_catalog(self, args, arguments):
        """
        ::

          Usage:
                catalog list
                catalog init --directory=DIR
                catalog query --name=NAME
                catalog table --attributes=ATTRIBUTES #string with commas i.e. 'id,name'

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments, "directory", "name", "attributes")
      

        VERBOSE(arguments)

        if arguments.query:
            print(arguments.name)

        elif arguments["list"]:
            print("option b")
            
        elif arguments.table:
            attributes = split(arguments.attributes,",")
            print(attributes)
            catalog = Catalog()
            print(Printer.write(catalog.data,header=attributes))

        return ""
