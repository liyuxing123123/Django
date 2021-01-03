#/python3

import paramiko, time, getpass

username = input("Username: ")
password = getpass.getpass("Password: ")

f = open("ip_list.txt", "r")
for line in f.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("Successfully connect to ", ip)
    remote_connection = ssh_client.invoke_shell()
    remote_connection.send("configure terminal\n")
    remote_connection.send("router eigrp 1\n")
    remote_connection.send("end\n")
    remote_connection.send("wr mem\n")
    time.sleep(1)
    output = remote_connection.recv(65535).decode("ASCII")
    print(output)

f.close()
ssh_client.close()

