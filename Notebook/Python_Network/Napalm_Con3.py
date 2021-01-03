#/python3

from napalm import get_network_driver
from getpass import getpass

ip = '192.168.27.111'
username = input('Username: ')
password = input('Password: ')

driver = get_network_driver('ios')
SW = driver(ip, username, password)
SW.open()

SW.load_merge_candidate(filename='Napalm_config.cfg')
diff = SW.compare_config()
print(diff)

