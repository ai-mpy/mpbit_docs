#mPythonType:0
from educore import servo, wifi, mqttclient

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f573ff', user='5b47fviXMJ', psd='5b47fNb18u')

import time

def open():
    global msg, servo, status, s, blink, mouth
    servo(0).angle(100)
    time.sleep(1.5)
    servo(0).angle(0)

import ujson

def receive_3a2ddfHhTw():
    global mouth, blink, s, status, servo, msg
    msg = mqttclient.message("3a2ddfHhTw")
    status = ujson.loads(msg)['status']
    blink = ujson.loads(msg)['blink']
    mouth = ujson.loads(msg)['mouth_open']
    if status == 1 and blink > 1 and mouth > 1:
        open()
mqttclient.received(topic="3a2ddfHhTw", callback=receive_3a2ddfHhTw)
