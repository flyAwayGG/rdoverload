import psutil


class ProcessesLogic(object):
    def __init__(self, cpu, ram):
        self.__cpu = cpu
        self.__ram = ram

    def print_proc(self):
        print psutil.cpu_percent(interval=None)
