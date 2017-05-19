#!/usr/bin/env python
#python2

import nmap
import time
import datetime
import sys

nm = nmap.PortScanner()

time.sleep(1)
print('----------------------------------------------------')
print('                                                    ')
time.sleep(1)
how_long = int(raw_input('How many minutes do you want to scan for? '))
repeat = how_long*2 # because 2 sweeps per minute
time.sleep(1)
time_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('Scan started at %s ') % time_now

def sweep():
        sys.stdout=open("/home/pi/code/logs/nmap_all.txt", "a")
        nm.scan(hosts='10.0.0.8', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
                print('{0}:{1} '.format(host, status)) + '@ ' + (  datetime.datetime.now().strftime("%H:%M:%S"))
        print('----------------------------------------------------')
        sys.stdout.close()
        
for i in range(repeat):
	sweep()
	time.sleep(60)