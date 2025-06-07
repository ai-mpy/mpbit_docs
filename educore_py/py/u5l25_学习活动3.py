#mPythonType:0
from educore import ds18b20, wifi, mqttclient, oled

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='04edc14052', user='04edcZGUpB', psd='04edcaQ7w6')

import time
while ds18b20(0).read() > 80:
    oled.print((str(ds18b20(0).read())))
    time.sleep(1)
t = 0
while True:
    v = ds18b20(0).read()
    if v < 40:
        break
    oled.print(str(t) + ':' + str(v))
    mqttclient.publish(topic='04edcwHK1N', content=str(t) + ':' + str(v))
    t = t + 1
    time.sleep(10)
oled.print('测量结束')
