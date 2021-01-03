#/python3

import paramiko, time, getpass, sys

username = input("Username: ")
password = getpass.getpass("Password: ")
ip_file = sys.argv[1]
cmd_file = sys.argv[2]

iplist = open(ip_file, 'r')

for line in iplist.readlines():
    ip = line.strip()
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    print("You have successfully connect to ", ip)
    command = ssh_client.invoke_shell()
    cmdlist = open(cmd_file, 'r')
    cmdlist.seek(0)
    for line in cmdlist.readlines():
        command.send(line + "\n")
        time.sleep(2)
    cmdlist.close()
    output = command.recv(65535).decode("ASCII")
    print(output)

iplist.close()
ssh_client.close()


