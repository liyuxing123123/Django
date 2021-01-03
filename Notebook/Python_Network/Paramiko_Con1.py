#/python3

# import paramiko, time
#
# ip = "192.168.27.111"
# username = "python"
# password = "cisco"
#
# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh_client.connect(hostname=ip, username=username, password=password)
#
# print("Sucessfully login to ", ip)
#
# command = ssh_client.invoke_shell()
#
# command.send("configure terminal\n")
# command.send("int lo0\n")
# command.send("ip add 1.1.1.1 255.255.255.255\n")
# command.send("end\n")
# command.send("wr mem")
# time.sleep(1)
# output = command.recv(65535).decode('ascii')
# print(output)
#
# ssh_client.close()

import paramiko, time

ip = '192.168.27.111'
username = 'python'
password = 'cisco'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh_client.connect(hostname=ip, username=username, password=password)

print("Sucessfully login to ", ip)

command = ssh_client.invoke_shell()

command.send("enable\n")
command.send("cisco\n")
command.send("configure terminal\n")
command.send("hostname Switch1\n")
command.send("int lo2\n")
command.send("ip add 2.2.2.2 255.255.255.255\n")
command.send("end\n")
command.send("wr mem\n")
time.sleep(1)
output = command.recv(65535).decode('ASCII')
print(output)

ssh_client.close()