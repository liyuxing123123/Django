#/python3

from netmiko import ConnectHandler

device = ConnectHandler(device_type = 'cisco_nxos', ip = '192.168.27.101',
                        username = 'admin', password = 'cisco')

def task2():
    global device
    configcmds = ['username test1 password test1']
    device.send_config_set(configcmds)
    output1 = device.send_command('show run | in username')
    output1 = output1.splitlines()
    for item in output1:
        if ('username' in item):
            item = item.split()
            print('username configured: ', item[1])
            device.disconnect()
    try:
        device=ConnectHandler(device_type='cisco_nxos', ip = '192.168.27.101',
                              username = 'test', password = 'test')
        print('Authenticated successfully with username test')
        device.disconnect()
    except:
        print('Unable to authenticate with username test')

task2()

