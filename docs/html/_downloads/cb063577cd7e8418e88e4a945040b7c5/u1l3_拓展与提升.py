from educore import oled, light

while True:
    light_value = light().read()
    oled.print(light_value)
