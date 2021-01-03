#/python3


import socket, sys

port = 70                   # Gopher uses port 70
host = sys.argv[1]
filename = sys.argv[2]
filename = filename.encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except socket.gaierror:
    print("Error connecting to server: %s" % socket.gaierror)
    sys.exit(1)
s.sendall(filename + "\r\n".encode())

while 1:
    buf = s.recv(2048)
    if not len(buf):
        break
    sys.stdout.write(buf.decode())



