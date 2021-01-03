#/python3

import socket

def convert_integer():
    data = 1234
    # 32-bit
    print(data, socket.ntohl(data), socket.htonl(data))
    print(data, socket.ntohs(data), socket.htons(data))

if __name__ == '__main__':
    convert_integer()