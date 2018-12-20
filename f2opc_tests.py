#!/usr/bin/env python3.5

import os
from datetime import datetime
import csv
import epics
import time

os.environ["EPICS_CA_ADDR_LIST"] = "172.17.2.36 172.16.2.255 172.17.102.130 172.17.102.139"

def onValueChange(pvname=None, value=None, char_value=None, host=None, **kws):
    global counter
    global prevVal
    if (value != prevVal):
        print('Value Changed: {0} {1} {2}'.format(pvname, value, char_value))
        counter = 0
    prevVal = value

def onObservation(pvname=None, value=None, char_value=None, host=None, **kws):
    global obsFlag
    global tgx
    global tgy
    print(char_value)

    if (value == 2):
        obsFlag = True
        print('BUSY')
    if (obsFlag and (value == 0)):
        obsFlag = False
        print(tgx.value, ' ', tgy.value, ' ')

# with open('names.csv') as csvfile:
    # reader = csv.reader(csvfile)
    # for row in reader:

tgx = epics.PV('f2:wfs:probeAssembly.A')
tgy = epics.PV('f2:wfs:probeAssembly.B')

posx = epics.PV('f2:wfs:probeCalcPosition.VALA')
posy = epics.PV('f2:wfs:probeCalcPosition.VALB')

bpos = epics.PV('f2:wfs:probeBasDevice.MPOS')
braw = epics.PV('f2:wfs:probeBasDevice.RRBV')
benc = epics.PV('f2:wfs:probeBasDevice.RENC')

ppos = epics.PV('f2:wfs:probePkoDevice.MPOS')
praw = epics.PV('f2:wfs:probePkoDevice.RRBV')
penc = epics.PV('f2:wfs:probePkoDevice.RENC')

# prevVal = False
# tcsConfigOiwfs = epics.PV('tc1:configOiwfs.DIR', callback=onValueChange)
# tcsConfigOiwfs = epics.PV('tc1:configOiwfs.DIR')
# f2Observe = epics.PV('f2:observeC.VAL')
f2Observe = epics.PV('tcs:applyC.VAL')
print(f2Observe.get())
print('value: {0}'.format(f2Observe.value))
print('char value: {0}'.format(f2Observe.char_value))
f2Observe.add_callback(callback=onObservation)


obsFlag = False
counter = 0
# prevVal = tcsConfigOiwfs.value
# tcsConfigOiwfs.add_callback(callback=onValueChange)
# print('tc1:configOiwfs.DIR: ', tcsConfigOiwfs.char_value)

# tcsConfigOiwfs.get()

while (counter < 100):
    counter += 1
    # print ('counter: ', counter)
    time.sleep(2)

# tcsConfigOiwfs.disconnect()
f2Observe.disconnect()

# dir1 = epics.caget('tc1:configOiwfs.DIR')
# dir2 = epics.caget('tc1:iocStats:TOD')
# print('tc1:configOiwfs.DIR: ', dir1)
# print('tc1:iocStats:TOD: ', dir2)
# dir1 = epics.caput('tc1:configOiwfs.DIR', 0)
# print('tc1:configOiwfs.DIR: ', dir1)
# time.sleep(5)
# dir1 = epics.caput('tc1:configOiwfs.DIR', 3)
# print('tc1:configOiwfs.DIR: ', dir1)
# time.sleep(5)
# dir1 = epics.caput('tc1:configOiwfs.DIR', 1)
# print('tc1:configOiwfs.DIR: ', dir1)
