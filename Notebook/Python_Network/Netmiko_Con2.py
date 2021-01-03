#/python3
#coding:utf-8

import os

# ip = 'www.cisco.com'
# result = os.system('ping -n 1 ' + ip)
#
# if result == 0:
#     print('\n' + ip + '可达')
# else:
#     print(ip + '不可达')

for i in range(111, 117):
    ip = '192.168.27.' + str(i)
    result = os.system('ping -n 1 ' + ip)
    if result == 0:
        print(ip + ' reachable')
    else:
        print(ip + ' unreachable')


