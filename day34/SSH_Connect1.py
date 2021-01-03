#/python3

from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_nxos', ip = '192.168.27.101',
                        username = 'admin', password = 'cisco')
output = device.send_command('show version')
print(output)

device.disconnect()


