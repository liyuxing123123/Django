#/python3
#coding:utf-8


from pythonping import ping

for i in range(111, 117):
    ip = '192.168.27.' + str(i)
    result = ping(ip)
    # print(type(result))
    if 'Reply' in str(result):
        print(ip + ' reachable')
    else:
        print(ip + ' unreachable')
