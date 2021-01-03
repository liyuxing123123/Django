

import socket

host = ''
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("Server is running on port %d; press Ctrl-C to terminate." % port)

while True:
    clientsock, clientaddr = s.accept()
    clientfile = clientsock.makefile('rwb', 0)
    clientfile.write(("Welcome, " + str(clientaddr) + "\n").encode())
    clientfile.write(("Please enter a string: ").encode())
    line = clientfile.readline().strip()
    clientfile.write(("You entered %d characters.\n" % len(line)).encode())
    clientfile.close()
    clientsock.close()