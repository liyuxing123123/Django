#/python3

from netmiko import ConnectHandler

print("Before config push")
device = ConnectHandler(device_type= 'cisco_nxos', ip = '192.168.27.101',
                        username = 'admin', password = 'cisco')
output = device.send_command("show run interface e1/5")
print(output)

configcmds = ['int e1/5', 'des my test2', 'no switchport', 'ip add 1.1.1.1/24', 'no sh']

print("After config push")
output2 = device.send_config_set(configcmds)
print(output2)

output3 = device.send_command('show run int e1/5')
print(output3)

output4 = device.send_command('copy run star')
print(output4)

device.disconnect()



