#mPythonType:0
import urequests

import ujson

from educore import oled, parrot, SoilHumiditySensor, light, wifi

import time

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)
city_code = 'CH010100'
key = 'cws921gkkqpqsjcg'
_response = urequests.get('http://api.yytianqi.com/forecast7d?city=' + str(city_code) + '&key=' + key)
if _response.status_code == 200:
    data = ujson.loads(_response.text)
    tq1 = data['data']['list'][0]['tq1']
    tq2 = data['data']['list'][0]['tq2']
    tq = [tq1, tq2]
M1 = parrot(parrot.M1)
hum_max = 3000
hum_min = 2000
while True:
    hum = SoilHumiditySensor(0).read()
    lgt = light().read()
    oled.print('土壤湿度：' + str(hum))
    if hum > hum_max:
        M1.speed(0)
    elif hum > hum_min:
        if '雨' in tq[0] or '雨' in tq[1]:
            M1.speed(0)
        else:
            M1.speed(100)
            time.sleep(5)
        if lgt > 1200:
            hum_min = 2500
        else:
            hum_min = 2000
    else:
        M1.speed(100)
        time.sleep(5)
