#/python3

import paramiko

hostname='192.168.27.139'
username='root'
password='2018.cn'
paramiko.util.log_to_file('syslogin.log')

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('mkdir 234')
print(stdout.read())

ssh.close()

