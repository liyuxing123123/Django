#/python3

import paramiko, time, getpass

username = input('Username: ')
password = getpass.getpass('Password: ')
# password = input('Password: ')
for i in range(111, 116):
    ip = '192.168.27.' + str(i)
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("Sucessfully connect to ", ip)
    command = ssh_client.invoke_shell()
    command.send("configure terminal\n")
    for n in range (10, 21):
        print("Creating VLAN " + str(n))
        command.send("Vlan " + str(n) + "\n")
        command.send("name Python_VLAN " + str(n) + "\n")
        time.sleep(0.5)

    command.send("end\n")
    command.send("wr mem\n")
    time.sleep(2)
    output = command.recv(65535).decode("ASCII")
    print(output)

ssh_client.close()


