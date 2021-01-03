#/python3

import paramiko, time, re, socket
from datetime import datetime

now = datetime.now()
date = "%s-%s-%s" % (now.month, now.day, now.year)
time_now = "%s-%s-%s" % (now.hour, now.minute, now.second)

class Port_statistics(object):

    switch_with_tacacs_issue = []
    switch_not_reachable = []
    total_number_of_up_port = 0

    def __init__(self):
        self.ssh_login()
        self.summary()

    def ssh_login(self):
        self.iplist = open('reachable_ip.txt')
        self.number_of_switch = len(self.iplist.readlines())
        self.iplist.seek(0)

        for line in self.iplist.readlines():
            try:
                self.ip = line.strip()
                self.ssh_client = paramiko.SSHClient()
                self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh_client.connect(hostname=self.ip, username='python', password='cisco', allow_agent=False, look_for_keys=False)
                print("\nYou have successfully connect to ", self.ip)
                self.comand = self.ssh_client.invoke_shell()
                self.check_up_port()
            except paramiko.ssh_exception.AuthenticationException:
                print("TACACS is not working for " + self.ip + ".")
                self.switch_with_tacacs_issue.append(self.ip)
            except socket.error:
                print(self.ip + " is not reachable.")
                self.switch_not_reachable.append(self.ip)

    def check_up_port(self):
        self.comand.send("term len 0\n")
        self.comand.send("show ip int b | i up\n")
        time.sleep(1)
        output = self.comand.recv(65535).decode("ASCII")
        self.search_up_port = re.findall(r'GigabitEthernet', output)
        self.number_of_up_port = len(self.search_up_port)
        print(self.ip + " has " + str(self.number_of_up_port) + " ports up.")
        self.total_number_of_up_port += self.number_of_up_port

    def summary(self):
        self.total_number_of_ports = self.number_of_switch * 48
        print("\n")
        print("There are totally " + str(self.total_number_of_up_port) + " port available in the network.")
        print(str(self.total_number_of_up_port) + " ports are currently up.")
        print("Port up rate is %.2f%%" % (self.total_number_of_up_port / float(self.total_number_of_up_port) * 100))
        print('\nTACACS is not working for below switches: ')
        for i in self.switch_with_tacacs_issue:
            print(i)
        print('\nBelow switches are not reachable: ')
        for i in self.switch_not_reachable:
            print(i)
        f = open(date + ".txt", "a+")
        f.write('As of ' + date + " " + time_now)
        f.write("\n\nThere are totally " + str(self.total_number_of_ports) + " ports available in the network.")
        f.write("\n" + str(self.total_number_of_up_port) + " ports are currently up.")
        f.write("\nPort up rate is %.2f%%" % (self.total_number_of_up_port / float(self.total_number_of_ports) * 100))
        f.write("\n***************************************************************\n\n")
        f.close()

if __name__ == '__main__':
    script1_2 = Port_statistics()

