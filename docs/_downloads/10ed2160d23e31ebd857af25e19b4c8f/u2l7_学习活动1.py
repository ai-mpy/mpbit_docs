from educore import oled,rfid

scan_rfid = rfid(scl=19,sda=20)
oled.clear()

while True:
    if scan_rfid.find_card():
        sn = scan_rfid.serial_number()
        oled.print(sn)
