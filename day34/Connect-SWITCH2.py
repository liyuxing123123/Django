#/python3

from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_nxos', ip='192.168.27.101',
                        username='admin', password='cisco')

def task1():
    output = device.send_command("show version")
    print(output)
    output = device.send_command('show ip int brief')
    print(output)
    output = device.send_command('show clock')
    print(output)
    output = device.send_command('show running-config | in username')
    output = output.splitlines()
    for item in output:
        if ("username" in item):
            item = item.split(" ")
            print("username configured:", item[1])


task1()