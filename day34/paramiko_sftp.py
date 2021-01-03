#/python3

import paramiko

username = 'root'
password = '2018.cn'
hostname = '192.168.27.139'
port = 22

# try:
t = paramiko.Transport(hostname, port)
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)

# sftp.put("D:\\B_configure\\3RJ-1.txt", "/home/3RJ-1.txt")
# sftp.get("/home/test1.txt", "D:\\B_configure\\test1.txt")
# sftp.mkdir("/home/userdir", 755)
# sftp.rmdir("/home/userdir")
sftp.rename("/home/test1.txt", "/home/test2.txt")
# print(sftp.stat("/home/testfile.sh"))
print(sftp.listdir("/home"))
t.close()
# except Exception as e:
#     print(str(e))
