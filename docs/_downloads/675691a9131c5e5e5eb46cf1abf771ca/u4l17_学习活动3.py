#mPythonType:0
from educore import wifi, mqttclient, dht, pin, light

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='5b47f74242', user='5b47fxteR6', psd='5b47fd2MW1')

import time
while True:
    temp = dht(13).read()[0]
    hum = pin(1).read_analog()
    lgt = light().read()
    mqttclient.publish(topic='5b47fEAPYI', content=(str(temp)))
    mqttclient.publish(topic='5b47faQc2j', content=(str(lgt)))
    mqttclient.publish(topic='5b47fabuh0', content=(str(hum)))
    time.sleep(30)
