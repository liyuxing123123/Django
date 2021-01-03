#/python3


import paramiko
import time
import getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

f1 = open("ip_list.txt", "r")

num = 0
for i in f1.readlines():
    ip = i.strip()
    num += 1
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password, allow_agent=False, look_for_keys=False)

    print("Successfully login in " + ip)
    command = ssh_client.invoke_shell()

    command.send("configure terminal\n")
    command.send("hostname Switch" + str(num) + '\n')
    command.send("router eigrp 1\n")
    command.send("end\n")
    command.send("wr mem\n")

    time.sleep(1)

    output = command.recv(65535).decode("ASCII")
    print(output)

f1.close()
ssh_client.close()

