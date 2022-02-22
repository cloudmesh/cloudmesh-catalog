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
                catalog default --name=NAME
                catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                catalog query QUERY [--name=NAME]
                catalog table --attributes=ATTRIBUTES [--name=NAME]
                catalog print --format=FORMAT [--name=NAME]
                catalog start [--docker] [--name=NAME]
                catalog stop [--docker] [--name=NAME]
                catalog status [--docker] [--name=NAME]

          This command manages the catalog service.

          Arguments:
              DIR   the directory path containing the entries
              NAME  the name of the entry
              ATTRIBUTES  string with commas i.e. 'id,name'

          Options:
              --f      specify the file

          Description:

            catalog list
              lists all available catalog services. There could be multiple
              catalog services

            catalog default --name=NAME
              sets the default catalog server to the given name.
              The names of all services is stored in a yaml file at
              ~/.cloudmesh/catalog.services.yaml

              cloudmesh:
                catalog:
                  - name: my-service-a
                    mode: native
                    port: 10000
                  - name: my-service-a
                    mode: docker
                    port: 10001

            catalog init  DIR [--name=NAME] [--port=PORT] [--docker]

                This command initializes a given catalog service, while using the
                directory DIR as a content dir for the entries.
                The dir can have multiple subdirectories for better organization.
                Each subdirectory name is automatically a "tag" in the entry.
                Note that it will be added to any tag that is in the entry. If
                the tag is already in the entry it will be ignored.

                The name is the name of the catalog to identify it in case
                multiple catalogs exist

                The port is the port number. The number is identified from the catalog list and is the next
                available port if it is not already used. If no prior catalog service with a port exists
                the port 40000 will be used

                If the docker flag is specified the catalog willl not be started natively, but in a
                docker container. uid and gid will be automatically vorwarded to the container, so data cahnges are
                conducted with the host user.

                If the image is not existand, a docker container will be started. The Dockerfile is located in the code
                base and dynamically retrieved from the pip installed package in
                cloudmesh/catalog/Dockerfile


            catalog query QUERY [--name=NAME]
              TBD

            catalog print [--catalog=CATALOGS] [--attributes=ATTRIBUTES] [--format=FORMAT] [--name=NAME]
                prints all entries of the given catalogs.

            catalog start [--docker] [--name=NAME]
            catalog stop [--docker] [--name=NAME]
            catalog status [--docker] [--name=NAME]


            catalog init DIR
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
                       "attributes",
                       "docker")
        # format can not be maped into a dict as reserved word use
        # arguments["--format"] instead

        VERBOSE(arguments)

        if arguments["list"]:
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.init:
            # requires the catalog server and the location of a named
            # catalog in ~/.cloudmesh/catalog/{name}
            # so if we find one we could cerate some default and use that catalog
            # as default and if no name is specified we use that
            # this is to be implemented in the init function
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.query:
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.table:
            attributes = split(arguments.attributes,",")
            print(attributes)
            # TODO Catalog not imported
            catalog = Catalog()
            print(Printer.write(catalog.data,header=attributes))

        elif arguments["--format"]:
            kind = arguments["--format"]
            # TODO not implemented
            print (kind)
            raise NotImplementedError

        elif arguments.start:
            print("start")
            catalog = CatalogServer("catalog")
            catalog.start()

        elif arguments.stop:
            print("stop")
            raise NotImplementedError
            # TODO: not implemented

        elif arguments.status:
            print("status")
            raise NotImplementedError
            # TODO: not implemented

        return ""
