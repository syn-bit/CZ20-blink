import display, time, keypad

pattern        = [0,1,1,0, 1,2,2,1, 1,2,2,1, 0,1,1,0]
counter        = 0

color_on       = 0x808080
color_off      = 0x000000

def on_key(key_index, is_pressed):
    global pattern

    if is_pressed:
        x,y = keypad.index_to_coords(key_index)
        pattern[x + y * 4] = (pattern[x + y * 4] + 1) % 4
        if pattern[x + y * 4] == 0:
            display.drawPixel(x,y,0x400000)
        elif pattern[x + y * 4] == 1:
            display.drawPixel(x,y,0x004000)
        elif pattern[x + y * 4] == 2:
            display.drawPixel(x,y,0x004040)
        elif pattern[x + y * 4] == 3:
            display.drawPixel(x,y,0x404000)
        print(x,y,pattern)
        display.flush()

keypad.add_handler(on_key)

while True:
    for y in range(4):
        for x in range(4):
            color = color_off
            if pattern[x + y * 4] == 1:
                color = color_on

            elif pattern[x + y * 4] == 2:
                if counter % 2 == 0:
                    color = color_off
                else:
                    color = color_on

            elif pattern[x + y * 4] == 3:
                if counter % 2 == 0:
                    color = color_on
                else:
                    color = color_off

            display.drawPixel(x,y,color)
    display.flush()
    counter += 1
    time.sleep(1)
