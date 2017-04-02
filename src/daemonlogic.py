from daemon import Daemon

from processeslogic import ProcessesLogic
import sys
from time import sleep


class DaemonLogic(Daemon):
    def __init__(self, settings, pidfile):
        super(DaemonLogic, self).__init__(pidfile)
        self.__cpu = settings["cpu"]
        self.__ram = settings["ram"]
        self.__poll = settings["poll"]

    def run(self):
        processeslogic = ProcessesLogic(cpu=self.__cpu, ram=self.__ram)
        while True:
            processeslogic.print_proc()
            sleep(self.__poll)
