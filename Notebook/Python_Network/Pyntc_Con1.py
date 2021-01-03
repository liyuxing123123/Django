#/python3

import scapy

import json
from pyntc import ntc_device as NTC

SW = NTC(host = '192.168.27.111', username = 'python', password = 'cisco', device_type='cisco_ios_ssh')
SW.open()

# print(json.dumps(SW.facts, indent=4))

SW.config('hostname SWITCH1')
SW.config_list(['int lo3', 'ip add 4.4.4.4 255.255.255.255'])
SW.close()


