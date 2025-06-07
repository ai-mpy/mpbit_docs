from educore import hid, keycode, accelerometer, oled

ble_hid = hid(name='mpy_hid')

acc = accelerometer()
while True:
    if ble_hid.isconnected():
        oled.print('蓝牙设备已连接')
    if acc.shake():
        ble_hid.keyboard_send(keycode.SPACE)
