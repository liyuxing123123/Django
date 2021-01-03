#/python3

import paramiko, time, getpass, sys, socket

username = input("Username: ")
password = getpass.getpass("Password: ")

ip_file = sys.argv[1]
cmd_file = sys.argv[2]

switch_with_authentication_issue = []
switch_not_reachable = []

iplist = open(ip_file, 'r')
for line in iplist.readlines():
    try:
        ip = line.strip()
        ssh_cilent = paramiko.SSHClient()
        ssh_cilent.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_cilent.connect(hostname=ip, username=username, password=password)
        print("You have successfully connect to ", ip)
        command = ssh_cilent.invoke_shell()
        cmdlist = open(cmd_file, 'r')
        cmdlist.seek(0)
        for line in cmdlist.readlines():
            command.send(line + "\n")
        time.sleep(2)
        cmdlist.close()
        output = command.recv(65535).decode("ASCII")
        print(output)
    except paramiko.ssh_exception.AuthenticationException:
        print("User authentication failed for " + ip + ".")
        switch_with_authentication_issue.append(ip)
    except socket.error:
        print(ip + " is not reachable.")
        switch_not_reachable.append(ip)

iplist.close()
ssh_cilent.close()

print('\nBelow switches are not reachable:' )
for i in switch_not_reachable:
    print(i)

print('\nUser authentication failed for below switches: ')
for i in switch_with_authentication_issue:
    print(i)
