#/python3

import telnetlib

host = '192.168.27.111'
username = 'python'
password = 'cisco'

tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(username.encode('ASCII') + b'\n')
tn.read_until(b'Password: ')
tn.write(password.encode('ASCII') + b'\n')

print('Succes login in ' + host)

tn.write(b'config t\n')
tn.write(b'int loop 2\n')
tn.write(b'ip add 3.3.3.3 255.255.255.255\n')
tn.write(b'end\n')
tn.write(b'wr mem\n')
tn.write(b'exit\n')

output = tn.read_all().decode('ASCII')
print(output)

