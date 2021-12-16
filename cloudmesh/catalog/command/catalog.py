from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
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
                catalog table --attributes=ATTRIBUTES
                catalog start
                catalog stop
                catalog status

          This command does some useful things.

          Arguments:
              DIR   the directory path containing the entries
              NAME  the name of the entry
              ATTRIBUTES  string with commas i.e. 'id,name'

          Options:
              --f      specify the file

          Description:

            catalog list
              lists the content of the catalog

            catalog init --directory=DIR
                initializes the catalag from a directory

            catalog query --name=NAME
                queries the catalog by a named entry. This is just a preliminary
                function and needs to be improved. YAMLDB provides a much better query.

            catalog table --attributes=ATTRIBUTES
                prints the content of the catalog in table form

            catalog start --port=PORT
                starts the catalog service

            catalog stop
                stops the catalog service

            catalog status
                returns the status of the service

        """


        # arguments.FILE = arguments['--file'] or None

        map_parameters(arguments,
                       "directory",
                       "name",
                       "attributes")
      

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
