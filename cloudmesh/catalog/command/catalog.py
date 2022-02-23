from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.Printer import Printer
from cloudmesh.shell.command import map_parameters
from cloudmesh.catalog.manager import ServiceManager

class CatalogCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_catalog(self, args, arguments):
        """
        ::

          Usage:
                catalog info
                catalog start [--docker] [--name=NAME]
                catalog stop [--docker] [--name=NAME]
                catalog status [--docker] [--name=NAME]
                catalog list
                catalog default [--name=NAME]
                catalog init  DIR [--name=NAME] [--port=PORT] [--docker]
                catalog query QUERY [--name=NAME]
                catalog table --attributes=ATTRIBUTES [--name=NAME]
                catalog print [--format=FORMAT] [--name=NAME]
                catalog copy [--docker] [--name=NAME] [--source=URL]
                catalog federate [--docker] [--name=NAME] [--source=URL]
                catalog load [--docker] [--name=NAME] [--source=URL]

          This command manages the catalog service.

          Arguments:
              DIR   the directory path containing the entries

          Options:
              --docker      docker
              --name=NAME  the name of the entry
              --port=PORT  the port

          Description:

            catalog list
              lists all available catalog services. There could be multiple
              catalog services

            catalog default [--name=NAME]
              sets the default catalog server to the given name.
              The names of all services is stored in a yaml file at
              ~/.cloudmesh/catalog.services.yaml

              > cloudmesh:
              >  catalog:
              >    - name: my-service-a
              >      mode: native
              >      port: 10000
              >    - name: my-service-a
              >      mode: docker
              >      port: 10001

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
              issues a querry to the given catalog services. If the name is ommitted the default service is used
              The query is formulated using https://jmespath.org/tutorial.html

            catalog print [--format=FORMAT] [--name=NAME]
                prints all entries of the given catalogs. With attributs you can select a number of attribtes.
                If the attributes ae nested a . notation can be used
                The format is by default table, but can also set to json, yaml, csv

            catalog start [--docker] [--name=NAME]
                This command starts the services. If docker is used the service is started
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog stop [--docker] [--name=NAME]
                This command stops the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog status [--docker] [--name=NAME]
                This command gets that status of the services. If docker is used the service is stopped
                as container. The name specifies the service so multiple services can be started
                If the name is omited the default container is used. If only one service is specified
                this is the default

            catalog copy [--docker] [--name=NAME] [--source=URL]
                This command copies the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port
                However it can also load data from a file or directory when specified as
                file://path. Relative path can be specified as file::../data

            catalog federate [--docker] [--name=NAME] [--source=URL]
                This command federates the contents from all catalogs specified by the
                source urls. Please note that the URLs are of teh form host:port.
                When the federation service is queried, parallel queries will be issued to
                all sources and the query result will be reduced to a single result.
                whne the cache option is specified the result will be cached and the next
                time the query is asked it will use also the cached result. A time to live
                is specified to asure the cached result will be deleted after the ttl is expired.

            catalog load [--docker] [--name=NAME] [--source=URL]

        """
        a = "dummy"

        """




            catalog status [--docker] [--name=NAME]

            catalog copy [--docker] [--name=NAME] [--source=URL...]


            catalog federate [--cache] [--ttl=TTL] [--docker] [--name=NAME] [--source=URL...]

            catalog load [--docker] [--name=NAME] [--source=DIR...]
                In contrast to the copy command, the LOAD command reads the data from
                directories or files and not from URLs
                However, copy can also do file://path

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
            #attributes = split(arguments.attributes,",")
            #print(attributes)
            # TODO Catalog not imported
            #catalog = Catalog()
            #print(Printer.write(catalog.data,header=attributes))
            raise NotImplementedError

        elif arguments["--format"]:
            kind = arguments["--format"]
            # TODO not implemented
            print (kind)
            raise NotImplementedError

        elif arguments.start:
            service = ServiceManager()
            service.start()

        elif arguments.stop:
            service = ServiceManager()
            service.stop()

        elif arguments.status:
            service = ServiceManager()
            print(service.status())

        elif arguments.info:
            service = ServiceManager()
            print(service.info())


        return ""
