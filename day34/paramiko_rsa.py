#/python3

import paramiko, os, sys

hostname = '192.168.27.139'
username = 'root'
paramiko.util.log_to_file('syslogin.log')

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
privatekey = os.path.expanduser('D:\\B_configure')
key = paramiko.RSAKey.from_private_key_file(privatekey)

ssh.connect(hostname=hostname, username=username,pkey=key)
stdin,stdout,stderr=ssh.exec_command('free -m')
print(stdout.read())

ssh.close()



