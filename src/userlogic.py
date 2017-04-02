import os
from sys import exit
import time
import sched
from daemonlogic import DaemonLogic
''' 
Program working as Linux daemon. When any of the processes exceeds 
the allowable value of RAM or CPU, report it in stdout and Radidx logs.
'''


class UserLogic(object):
    __help = ('Specify valid arguments: \n'
              '# rdoverload enable [cpu=[1-100]] [ram=[1-100]] [poll=[5-1000]] \n'
              ' Start daemon and add it to autostart. \n'
              ' Set listener on all processes with established CPU and RAM threshold in percents. \n'
              ' Params:\n'
              '     cpu [percent] - minimum threshold for process CPU usage. Default is 20. Boundaries from 1 to 100. \n'
              '     ram [percent] - minimum threshold for process RAM usage. Default is 20. Boundaries from 1 to 100. \n'
              '     poll [seconds] - polling time of processes usage. Default is 5 seconds. Boundaries from 5 to 1000 seconds. \n'
              ' \n'
              '# rdoverload disable \n'
              ' Unload and delete daemon from autostart. '
              )

    __default_enable_settings = {"cpu": 20, "ram": 20, "poll": 5}
    __pid_file = '/tmp/overload.pid'

    def execute(self, args):
        args_len = len(args)

        if args_len == 0 or args_len > 4:
            self.__help_and_exit()

        if args_len == 1 and args[0] == "disable":
            self.__disable()
        elif args[0] == "enable":
            settings = self.__parse_enable_args(args[1:])
            self.__enable(settings)
        else:
            self.__help_and_exit()

    def __parse_enable_args(self, enable_args):
        enable_settings = self.__default_enable_settings
        for arg in enable_args:
            k, v = arg.split("=")
            if not v.isdigit():
                self.__help_and_exit("Value of key %s - %s is not number" % (k, v))
            v = int(v)

            if k in self.__default_enable_settings.keys() and self.__is_setting_valid(k, v):
                enable_settings[k] = v
            else:
                self.__help_and_exit()

        return enable_settings

    def __help_and_exit(self, optional_str=""):
        print optional_str, self.__help
        exit(1)

    def __is_setting_valid(self, key, value):
        if (key == "cpu" or key == "ram") and (1 <= value <= 100):
            return True
        if key == "poll" and (5 <= value <= 1000):
            return True

        self.__help_and_exit("Wrong boundaries for [" + key + "=" + str(value) + "]\n")

    def __disable(self):
        pass

    def __enable(self, settings):
        daemon = DaemonLogic(settings=settings, pidfile=self.__pid_file)
        daemon.start()
