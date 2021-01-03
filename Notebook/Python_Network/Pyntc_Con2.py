#/python3

from pyntc import ntc_device as NTC
import time

SW = NTC(host='192.168.27.111', username ='python', password ='cisco', device_type='cisco_ios_ssh')
SW.open()
# time.sleep(5)
SW.running_config
print(SW.running_config)

# SW.backup_running_config('SW1_config.cfg')
# SW.close()

