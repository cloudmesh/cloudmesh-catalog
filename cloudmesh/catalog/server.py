from cloudmesh.common.util import readfile, writefile
from cloudmesh.common.Shell import Shell

class Catalog:

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
        writefile(f"~/.cloudmesh/catalog/{name.pid}", str(pid))

    def start(self):
        print("start")

    def stop(self):
        print("stop")

    def status(self):
        print("status")

    def print(self, kind="table", data=None):
        print ("print", kind)
        # use cloud mesh Printer.write(data, ....)
        # which has kind for json, yaml, table

    def table(self):
        print ("table")
        data = [] # get from fastapi service
        self.print(kind="table", data=data)