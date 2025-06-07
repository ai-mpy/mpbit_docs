#mPythonType:0
from educore import button, wifi, mqttclient

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='04edc14052', user='04edcZGUpB', psd='04edcaQ7w6')

import time
k1 = button(button.a)
k2 = button(button.b)
while True:
    if k1.status() == 1:
        mqttclient.publish(topic='04edcwHK1N', content='use1,psd1,open')
        time.sleep(1)
    if k2.status() == 1:
        mqttclient.publish(topic='04edcwHK1N', content='use2,psd2,open')
        time.sleep(1)
