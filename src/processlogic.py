from daemon import Daemon


class ProcessLogic(Daemon):
    def __init__(self, settings, pidfile):
        super(ProcessLogic, self).__init__(pidfile)
        self.cpu = settings["cpu"]
        self.ram = settings["ram"]
        self.poll = settings["poll"]

    def run(self):
        print "Test"

    def enable(self):
        print self.cpu
        print self.ram
        print self.poll
        self.start()
        pass

    @staticmethod
    def disable():
        pass
