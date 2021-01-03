#/python3



from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_nxos', ip='192.168.27.101',
                        username='admin', password='cisco')

def task2():
    configcmds = ['username test password test']
    device.send_config_set(configcmds)
    output = device.send_command("show run | in username")
    output = output.splitlines()
    for item in output:
        if ('username' in item):
            item = item.split(" ")
            print('username configured:', item[1])
    device.disconnect()

task2()

try:
    device = ConnectHandler(device_type='cisco_nxos', ip='192.168.27.101',
                            username='test', password='test')
    print("Authenticated sucessfully with username test")
    output = device.send_command('show ip int b')
    print(output)
    device.disconnect()
except:
    print("Unable to authenticate with username test")


