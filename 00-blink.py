import display, time

while True:
    display.drawFill(0xFFFFFF)
    display.flush()
    time.sleep(1)
    display.drawFill(0x000000)
    display.flush()
    time.sleep(1)
