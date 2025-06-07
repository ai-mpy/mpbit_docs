#mPythonType:0
from educore import oled, wifi, mqttclient

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f10241', user='5b47fGR9Dy', psd='5b47fdIdrz')

import time

def receive_5b47fD2cGl():
    global msg
    msg = mqttclient.message("5b47fD2cGl")
    if msg == '有人按门铃':
        oled.print(msg)
        time.sleep(5)
        oled.clear()
mqttclient.received(topic="5b47fD2cGl", callback=receive_5b47fD2cGl)
