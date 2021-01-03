#/python3

from netmiko import ConnectHandler

device = ConnectHandler(device_type= 'cisco_nxos', ip = '192.168.27.101',
                        username = 'admin', password = 'cisco')

def task1():
    output1 = device.send_command('show version')
    print(output1)
    output2 = device.send_command('show ip int brief')
    print(output2)
    output3 = device.send_command('show clock')
    print(output3)
    output4 = device.send_command('show run | in username')
    output4 = output4.splitlines()
    for item in output4:
        if ('username' in item):
            item = item.split()
            print(item)
            print('username configured: ', item[1])

task1()

