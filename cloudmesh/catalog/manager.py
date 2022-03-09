import os
import socket

import psutil

from cloudmesh.common.Shell import Shell
from cloudmesh.common.console import Console
from cloudmesh.common.dotdict import dotdict
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import readfile


class ServiceManager:

    # r = cloudmesh.common.SHell.run("uvicorn .... ")

    def __init__(self, name=None):
        """

        :param name:
        :type name:
        """
        self.name = name or "cloudmesh-catalog-service"
        self.path = path_expand("~/.cloudmesh/catalog")
        self.pid_file = f"{self.path}/{self.name}.pid"
        self.port = 8001
        self.reload = "--reload"

        Shell.mkdir(self.path)

    def is_port_in_use(self) -> bool:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', self.port)) == 0

    def start(self):
        """

        :return:
        :rtype:
        """

        if self.is_port_in_use():
            Console.error(f"Port {self.port} already in use")
            return

        name = f"{self.path}/{self.name}"
        os.system(f"rm -f {name}.pid")
        command = f"nohup uvicorn cloudmesh.catalog.service:app --port={self.port} {self.reload} " \
                  f"> {name}.log 2>&1 & echo $! > {name}.pid"
        print(command)
        result = os.system(command)
        print(result)
        if result != 0:
            Console.error("The catalog server could not be started due to an error")
        try:
            content = readfile(f"{self.pid_file}")
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
        try:
            pid = readfile(f"{self.pid_file}").strip()
            # if not psutil.pid_exists(pid):
            #    pid = None
        except:
            pid = None
        return pid

    def stop(self, pid=None):
        """

        :return:
        :rtype:
        """

        if pid is None:
            info = self.info()
            pid = info["pid"]

        for child in psutil.Process(pid).children():
            try:
                print(f"Deleting {child.pid} ", end="")
                p = psutil.Process(child.pid)
                p.kill()
                Console.green("deleted.")

            except psutil.Error:
                Console.red(". failed")
        print(f"Deleting {child.pid} ", end="")
        p = psutil.Process(pid)
        p.kill()
        Console.green("deleted.")
        os.remove(self.pid_file)

    def status(self):
        """

        :return:
        :rtype:
        """
        # for debug only
        probe = Shell.run(f"curl localhost:{self.port}")
        return '{"Cloudmesh Catalog":"running"}' in probe

    def info(self):
        """

        :return:
        :rtype:
        """

        data = dotdict({
            "pid": None,
            "children": None,
            "status": False
        })
        try:
            data.pid = int(self.get_pid())
        except:
            pass
        try:
            data.status = self.status()
        except:
            pass
        try:
            data.children = [child.pid for child in psutil.Process(data.pid).children()]
        except Exception as e:
            pass

        return data
