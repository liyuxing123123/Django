#/python3

from netmiko import ConnectHandler

def task3():
    device = ConnectHandler(device_type='cisco_nxos', ip='192.168.27.101',
                            username='admin', password='cisco')
    print("auth sucess")
    output = device.send_command('show run | in username')
    output = output.splitlines()
    print(output)
    for item in output:
        if ('username' in item):
            if ('test' in item):
                item = item.split()
                print(item[1])
                cmd = 'no username ' + item[1]
                print(cmd)
                outputnew = device.send_config_set(cmd)
    output = device.send_command('show run | in username')
    output = output.splitlines()

    for item in output:
        if ('username' in item):
            item = item.split(' ')
            print('username configured:', item[1])
    device.disconnect()

task3()
    # output4 = device.send_command('show run | in username')
    # output4 = output4.splitlines()
    # for item in output4:
    #     if ('username' in item):
    #         item = item.split()
    #         print(item)
    #         print('username configured: ', item[1])

