#/python3
# coding:utf-8

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    addrs = socket.getaddrinfo(host_name,None)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)
    # print("ALL IP address: %s" % addrs)
    for item in addrs:
        # print(item)
        if ':' not in item[4][0]:
            print('当前主机IPv4地址为: ' + item[4][0])

if __name__ == '__main__':
    print_machine_info()



