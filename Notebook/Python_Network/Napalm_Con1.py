#/python3
#coding:utf-8

from napalm import get_network_driver
from getpass import getpass
import json

ip  = '192.168.27.111'
username = input("Username: ")
password = input("Password: ")

driver = get_network_driver('ios')
SW = driver(ip, username, password)
SW.open()

output = SW.get_interfaces()
# print(output)
# print(json.dumps(output, indent=2))

print('\n交换机%s的下列端口的状态为up/up: \n' % ip)

# f1 = open('Napalm.txt', 'a+')

for key, value in output.items():
    if value['is_up'] == True:
        print(key, " MAC地址为: " + value['mac_address'])
        # f1.write(key + " MAC地址为: " + value['mac_address'] + '\n')


