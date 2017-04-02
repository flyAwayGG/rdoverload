#!/usr/bin/python

from sys import argv
from userlogic import UserLogic

if __name__ == '__main__':
    UserLogic().execute(argv[1:])
