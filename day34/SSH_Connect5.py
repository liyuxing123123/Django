#/python3

from netmiko import ConnectHandler

def task3():
    device = ConnectHandler(device_type='cisco_nxos', ip = '192.168.27.101',
                            username = 'admin', password = 'cisco')
    output1 = device.send_command('show run | in username')
    # print(output1)
    output1 = output1.splitlines()
    print(output1)
    for item in output1:
        if ('username' in item):
            if ('test' in item):
                item = item.split(" ")
                print(item[1])
                cmd = 'no username ' + item[1]
                output2 = device.send_config_set(cmd)
    output3 = device.send_command('show run | in username')
    output3 = output3.splitlines()
    for item in output3:
        if ('username' in item):
            item = item.split()
            print('username configured: ', item[1])
    device.disconnect()

task3()


