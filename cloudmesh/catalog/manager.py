import os

from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import readfile


class ServiceManager:

    # r = cloudmesh.common.SHell.run("uvicrn .... ")

    def __init__(self, name=None):
        """

        :param name:
        :type name:
        """
        self.name = name or "cloudmesh-catalog-service"
        self.path = path_expand("~/.cloudmesh/catalog")
        self.port = 8001
        self.reload = "--reload"

        Shell.mkdir(self.path)

    def start(self):
        """

        :return:
        :rtype:
        """

        name = f"{self.path}/{self.name}"
        os.system(f"rm -f {name}.pid")
        command = f"nohup uvicorn cloudmesh.catalog.service:app --port={self.port} {self.reload} "\
                  f"> {name}.log 2>&1 & echo $! > {name}.pid"
        print(command)
        result = os.system(command)
        print(result)
        if result != 0:
            Console.error("The catalog server could not be started due to an error")
        try:
            content = readfile(f"{self.path}/{self.name}.pid")
            if "Address already in use" in content:
                Console.error("Address already in use")
            else:
                print(content)
        except:
            Console.error("pid file could not be found")

    def get_pid(self):
        """

        :return:
        :rtype:
        """
        pid = None
        # command = f"$(ps aux | grep 'uvicorn {self.name}' | grep -v grep | awk {'print $2'} | xargs)"
        # pid = Shell.run(command).strip()
        name = f"{self.path}/{self.name}"
        pid = readfile(f"{name}.pid").strip()
        return pid

    def stop(self):
        """

        :return:
        :rtype:
        """
        info = self.info()
        pids = [info["pid"]] + info["children"]
        try:
            for pid in pids:
                print(f"Killing: {pid}", end="")
                result = Shell.run(f"kill -9 {pid}")
                if "No such process" in result:
                    Console.red(". not found.")
                else:
                    Console.green(". deleted.")
        except:
            print("Process not found")

    def status(self):
        """

        :return:
        :rtype:
        """
        # for debug only
        os.system("ps")
        pid = self.get_pid()
        os.system(f"pstree -p {pid}")

    def info(self):
        """

        :return:
        :rtype:
        """
        pid = self.get_pid()
        children = Shell.run(f"pstree -p {pid}").replace(f"({pid})", "").splitlines()
        pids = []
        for line in children:
            pids.append("".join(filter(str.isdigit, line)))
        data = {
            "pid": pid,
            "children": pids,
        }
        return data
