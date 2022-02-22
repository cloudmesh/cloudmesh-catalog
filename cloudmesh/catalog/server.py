from cloudmesh.common.util import readfile, writefile
from cloudmesh.common.Shell import Shell
import os

class CatalogServer:

    # r = cloudmesh.common.SHell.run("uvicrn .... ")
    
    def __init__(self, name):
        print("init")
        #if dir does not exists
        Shell.mkdir("~/.cloudmesh/catalog")
        # start fastapi  with unicorn and get pid, see if SHell
        # command has feature to do this
        # pid can be retrieved also from commandline,
        # if file is missing. If so we may not need a file
        # at all which his better
        pid = "1" # TBD
        writefile(f"~/.cloudmesh/catalog/{name}.pid", str(pid))

    def start(self):
        # TODO: see manual where to get port and name. This is not completed
        # we want to initialize with 127.0.0.1 so that only localhost can connect for now
        print("start")
        os.system("uvicorn server-fastapi:app --reload")

    def stop(self):
        # TODO: not implemented, get the pid and use that by name
        raise NotImplementedError

    def status(self):
        # TODO: not implemented
        raise NotImplementedError

    def print(self, kind="yaml", data=None):
        print ("print", kind)
        # which has kind for json, yaml, table
        # TODO: not implemented
        # table_str = Printer.write(data, output=kind) # or similar
        # print (table_str)
        # Q: maybe we should jus use "json" and yaml as outout format
        raise NotImplementedError

