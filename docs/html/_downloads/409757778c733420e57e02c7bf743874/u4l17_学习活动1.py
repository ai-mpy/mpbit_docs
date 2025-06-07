#mPythonType:0
from educore import oled, wifi

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

import urequests

import ujson
city_code = 'CH010100'
key = '5g8koi0s83vk0ihn'
_response = urequests.get('http://api.yytianqi.com/forecast7d?city=' + city_code + '&key=' + key)
if _response.status_code == 200:
    data = ujson.loads(_response.text)
    tq1 = data['data']['list'][0]['tq1']
    tq2 = data['data']['list'][0]['tq2']
    tq = tq1 + '-' + tq2
    oled.print(tq)
