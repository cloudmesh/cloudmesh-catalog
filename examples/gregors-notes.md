         s = Server(
                    name=arguments.NAME,
                    spec=path_expand(arguments.YAML),
                    directory=path_expand(
                        arguments.directory) or arguments.directory,
                    port=arguments.port,
                    server=arguments.wsgi,
                    debug=arguments.debug
                )

                pid = s.run_os()

                VERBOSE(arguments, label="Server parameters")

                print(f"Run PID: {pid}")

leverage 
https://github.com/cloudmesh/cloudmesh-openapi/blob/main/cloudmesh/openapi/function/server.py
we want tnot to use flask but fastapi

https://stackoverflow.com/questions/57412825/how-to-start-a-uvicorn-fastapi-in-background-when-testing-with-pytest