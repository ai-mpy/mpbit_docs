#mPythonType:0
from educore import wifi, mqttclient, button

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f88377', user='5b47fLPnCo', psd='5b47fPkugf')

import time
btn_a = button(button.a)
while True:
    if btn_a.status() == 1:
        mqttclient.publish(topic='5b47fDXrEq', content='open')
        time.sleep(5)
