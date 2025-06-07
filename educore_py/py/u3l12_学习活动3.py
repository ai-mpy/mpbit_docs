#mPythonType:0
from educore import rfid, servo

import time
scan_rfid = rfid(sda=14, scl=13)
sn_list = ['36384575', '1025599731']
while True:
    rf = scan_rfid.scanning()
    sn = rf.serial_number()
    if sn in sn_list:
        servo(1).angle(180)
        time.sleep(3)
        servo(1).angle(0)
