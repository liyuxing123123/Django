#/python3

from netmiko import ConnectHandler
import time

def pushbgpconfig(routerip, remoteip, localas, remoteas, newconfig= 'false'):
    uname = 'admin'
    passwd = 'cisco'
    device = ConnectHandler(device_type='cisco_nxos', ip = routerip,
                            username = uname, password = passwd)
    device.send_command("feature bgp")
    cmds = ""
    cmds = "router bgp " + localas
    cmds1 = " neighbor " + remoteip + " remote-as " + remoteas
    cmds3 = 'remote-as ' + remoteas
    cmds2 = [cmds,cmds1,cmds3,'address-family ipv4 unicast']
    xcheck = device.send_config_set(cmds2)
    print(xcheck)
    outputx = device.send_command("copy run star")
    print(outputx)
    device.disconnect()

def validatebgp(routerip, remoteip):
    uname = "admin"
    passwd = "cisco"
    device = ConnectHandler(device_type='cisco_nxos', ip = routerip,
                            username = uname, password = passwd)
    cmds = 'show ip bgp nei ' + remoteip + " | include BGP"
    outputx = device.send_command(cmds)
    outputx = outputx.split()
    print(outputx)
    if ("Established," in outputx):
        print("Remote IP " + remoteip + " on local router " + routerip + "is in "
                                                                         "ESTABLISHED state")
    else:
        print("Remote IP " + remoteip + " on local router " + routerip + " is NOT IN "
                                                                         "ESTABLISHED state")
    device.disconnect()

pushbgpconfig("192.168.27.101", "192.168.27.102", "200", "200")
###we give some time for bgp to establish
print("Now sleeping for 5 seconds...")
time.sleep(5)
validatebgp("192.168.27.101", "192.168.27.102")

