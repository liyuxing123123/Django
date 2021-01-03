#/python3

#coding:utf-8

# import Notebook.Python_Network_20201231.script1 as script1
#
# script1.script1()
# print("This is script 2.")

import os
hostname = 'www.cisco.com'
respone = os.system('ping -n 2 ' + hostname)
if respone == 0:
    print(hostname + ' is reachable.')
else:
    print(hostname + ' is not reachable!')