from daemon import Daemon

from processeslogic import ProcessesLogic
import sys
from time import sleep


class DaemonLogic(Daemon):
    def __init__(self, pidfile):
        super(DaemonLogic, self).__init__(pidfile)

    def run(self, settings):
        cpu = settings["cpu"]
        ram = settings["ram"]
        poll = settings["poll"]

        processeslogic = ProcessesLogic(cpu=cpu, ram=ram)
        while True:
            processeslogic.check()
            sleep(poll)

    def unload(self):
        if self.is_running():
            self.stop()
