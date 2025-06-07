#mPythonType:0
from educore import mqttclient, pin, speaker, dht, oled, wifi

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

mqttclient.connect(server='iot.mpython.cn', port=1883, client_id='a73ac31a4c', user='a73acPABoi', psd='a73ackRR4c')

import time
p1 = pin(13)
p2 = pin(15)
s1 = speaker()
t = 0
h = 0
while True:
    temp = dht(0).read()[0]
    hum = dht(0).read()[1]
    oled.print('温度：' + str(temp) + '\n湿度：' + str(hum))
    mqttclient.publish(topic='a73acaCSvY', content='温度：' + str(temp) + '\\n湿度：' + str(hum))
    if temp > 28 or temp < 26:
        p1.write_digital(value=1)
        t = t + 1
    else:
        p1.write_digital(value=0)
        t = 0
    if hum > 70 or hum < 60:
        p2.write_digital(value=1)
        h = h + 1
    else:
        p2.write_digital(value=1)
        h = 0
    if t >= 30 or h >= 30:
        s1.tone(freq=1000, dur=1000)
    time.sleep(1)
