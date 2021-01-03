#/python3

import paramiko, time,subprocess, os

class Ping(object):
    third_octect = range(27, 28)
    last_octect = range(111, 116)

    def __init__(self):
        self.ping()

    def ping(self):
        self.remove_last_reachable_ip_file_exist()
        for ip3 in self.third_octect:
            for ip4 in self.last_octect:
                self.ip = '192.168.' + str(ip3) + '.' + str(ip4)
                self.ping_result = subprocess.call(['ping', '-n', '2','-w', '2', self.ip])
                self.open_ip_record_file()
                self.check_ping_result()
        self.f.close()

    def open_ip_record_file(self):
        self.f = open('reachable_ip.txt', 'a')

    def check_ping_result(self):
        if self.ping_result == 0:
            self.f.write(self.ip + "\n")

    def remove_last_reachable_ip_file_exist(self):
        if os.path.exists('reachable_ip.txt'):
            os.remove('reachable_ip.txt')

if __name__ == '__main__':
    script_1 = Ping()

