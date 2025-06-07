#mPythonType:0
from educore import wifi, mqttclient, servo

import time

def open():
    global s, msg
    servo(1).angle(180)
    time.sleep(1.5)
    servo(1).angle(0)

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f88377', user='5b47fLPnCo', psd='5b47fPkugf')

def receive_5b47fDXrEq():
    global msg
    msg = mqttclient.message("5b47fDXrEq")
    if msg == 'open':
        open()
mqttclient.received(topic="5b47fDXrEq", callback=receive_5b47fDXrEq)
