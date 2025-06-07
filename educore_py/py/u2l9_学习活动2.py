from educore import oled, wifi

wifi.connect(ssid='mywifi', psd='123456789', timeout=10000)

import urequests
import ujson

url = 'https://quan.suning.com/getSysTime.do'
_response = urequests.get(url)
res = _response.text
data = ujson.loads(res)
nowtime = data['sysTime2']
oled.print(nowtime)
