import psutil


class ProcessesLogic(object):
    def __init__(self, cpu, ram):
        self._cpu = cpu
        self._ram = ram

    def check(self):
        if psutil.cpu_percent(interval=None) > self._cpu or \
                        psutil.virtual_memory().percent > self._ram:
            pinfo = self._find_bad_proc()
            self._print_proc(pinfo)

    def _find_bad_proc(self):
        for proc in psutil.process_iter():
            try:
                if proc.cpu_percent() > self._cpu or \
                                proc.memory_percent() > self._ram:
                    return proc.as_dict(attrs=['name', 'pid', 'status',
                                               'cpu_percent', 'memory_percent'])
            except psutil.NoSuchProcess:
                pass

    def _print_proc(self, process):
        print process
