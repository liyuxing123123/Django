#/python3

from fabric.api import run



def host_type():
    run('uname -s')

host_type()