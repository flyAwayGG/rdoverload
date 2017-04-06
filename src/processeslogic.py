import psutil


class ProcessesLogic(object):
    def __init__(self, cpu, ram):
        self.__cpu = cpu
        self.__ram = ram

    def print_proc(self):
        if psutil.cpu_percent(interval=None) > self.__cpu:
            # find bad proccess by CPU
            pass

        if psutil.virtual_memory().percent > self.__ram:

            for proc in psutil.process_iter():
                try:
                    pinfo = proc.as_dict()  # cpu_percent() #as_dict(attrs=['pid', 'name'])
                except psutil.NoSuchProcess:
                    pass
                else:
                    print(pinfo)
            # find bad process by ram
            pass
