#mPythonType:0
from educore import wifi, mqttclient, button

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f73789', user='5b47fI57Vd', psd='5b47fEkOJI')

import time
bt = button(button.a)
while True:
    if bt.status() == 1:
        mqttclient.publish(topic='5b47fD2cGl', content='有人按门铃')
        time.sleep(5)
