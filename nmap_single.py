#!/usr/bin/env python
#! python3

import nmap
import time
import datetime

nm = nmap.PortScanner()

print(' ')
time.sleep(1)
print('----------------------------------------------------')
print(' ')
time.sleep(1)
how_long = int(input('How many minutes do you want to scan for? '))
repeat = how_long/5 #because 2 sweeps per minute

time.sleep(1)
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(('Scan started at %s ') % time_now)
print(' ')

def sweep():
	nm.scan(hosts='10.0.0.16', arguments='-sn')
	hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
	for host, status in hosts_list:
		print(('{0}:{1} '.format(host, status)) + ('@ ') + ( datetime.datetime.now().strftime("%H:%M:%S")))
for i in range (int(repeat)):
    sweep()
    time.sleep(300)
    print('----------------------------------------------------')
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(('Scan finished at %s ') % time_now)


