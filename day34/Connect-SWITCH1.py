#/python3



from netmiko import ConnectHandler

f = open("D:\\B_configure\\mytest.txt",'a+')
print("Before config push")
device = ConnectHandler(device_type='cisco_nxos', ip='192.168.27.101', username='admin', password='cisco')

output = device.send_command("show running-config interface e1/4")
print(output)
f.write(output)
configcmds = ["interface e1/4", "description my test", "no switchport","ip address 192.168.100.100/24"]


device.send_config_set(configcmds)

print("After config push")

output = device.send_command("show running-config interface e1/4")
print(output)

f.write(output)
f.close()

device.send_command("copy run star")
device.disconnect()