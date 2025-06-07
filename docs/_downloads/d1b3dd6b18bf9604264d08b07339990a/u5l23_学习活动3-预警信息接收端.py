#mPythonType:0
from educore import oled, speaker, wifi, mqttclient

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47ff3847', user='5b47fFKTLn', psd='5b47fvJEqe')

def receive_5b47f4HK2Z():
    global msg
    msg = mqttclient.message("5b47f4HK2Z")
    oled.print(msg)
    s.tone(freq=1000, dur=1000)
s = speaker()
mqttclient.received(topic="5b47f4HK2Z", callback=receive_5b47f4HK2Z)
