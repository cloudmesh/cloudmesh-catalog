from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.shell.command import map_parameters
from cloudmesh.catalog.server import CatalogServer

class CatalogCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_catalog(self, args, arguments):
        """
        ::

          Usage:
                catalog list
                catalog init --directory=DIR
                catalog query QUERY
                catalog table --attributes=ATTRIBUTES
                catalog print --format=FORMAT
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

            catalog query QUERY
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
        map_parameters(arguments,
                       "directory",
                       "attributes")
        # format can not be maped into a dict as reserved word use
        # arguments["--format"] instead

        VERBOSE(arguments)

        if arguments["list"]:
            raise NotImplementedError
            # BUG: not implemented

        elif arguments.init:
            # requires the catalog server and the location of a named
            # catalog in ~/.cloudmesh/catalog/{name}
            # so if we find one we could cerate some default and use that catalog
            # as default and if no name is specified we use that
            # this is to be implemented in the init function
            raise NotImplementedError
            # BUG: not implemented

        elif arguments.query:
            raise NotImplementedError
            # BUG: not implemented

        elif arguments.table:
            attributes = split(arguments.attributes,",")
            print(attributes)
            # BUG Catalog not imported
            catalog = Catalog()
            print(Printer.write(catalog.data,header=attributes))

        elif arguments["--format"]:
            kind = arguments["--format"]
            # BUG not implemented
            print (kind)
            raise NotImplementedError

        elif arguments.start:
            print("start")
            catalog = CatalogServer("catalog")
            catalog.start()

        elif arguments.stop:
            print("stop")
            raise NotImplementedError
            # BUG: not implemented

        elif arguments.status:
            print("status")
            raise NotImplementedError
            # BUG: not implemented

        return ""
