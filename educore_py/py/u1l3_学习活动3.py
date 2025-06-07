from educore import sound, oled

while True:
    sound_value = sound().read()
    oled.print(('声音响度：' + str(sound_value)))
