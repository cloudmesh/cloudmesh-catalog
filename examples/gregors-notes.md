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

this seems easy:
https://levelup.gitconnected.com/how-to-restart-fastapi-server-with-bash-script-f05a5bfcec5c

nohup uvicorn myapp:app &

#!/bin/bash
source /home/project/myenv/bin/activate
cd /home/project/server
PID=$(ps aux | grep 'uvicorn myapp:app' | grep -v grep | awk {'print $2'} | xargs)
if [ "$PID" != "" ]
then
kill -9 $PID
sleep 2
echo "" > nohup.out
echo "Restarting FastAPI server"
else
echo "No such process. Starting new FastAPI server"
fi
nohup uvicorn myapp:app &