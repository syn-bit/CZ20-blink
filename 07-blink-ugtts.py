import display, time, keypad, virtualtimers, appconfig, sndmixer, wifi, ugTTS

settings = appconfig.get('blink', {'pattern': [0,1,1,0, 1,2,2,1, 1,2,2,1, 0,1,1,0], 'interval': 1000, 'color_on': 0x808080, 'color_off': 0x000000})
pattern  = settings['pattern']
interval = settings['interval']
counter  = 0
blinking = True
cnnected = False

def interval_down(is_pressed):
    global interval

    if is_pressed:
        interval = interval // 2 if interval >= 100 else 50
        if connected:
            ugTTS.speak("Interval is now {}".format(interval))
        else:
            print("Interval is now {}".format(interval))
        

def interval_up(is_pressed):
    global interval

    if is_pressed:
        interval = interval * 2 if interval <= 5000 else 10000
        if connected:
            ugTTS.speak("Interval is now {}".format(interval))
        else:
            print("Interval is now {}".format(interval))
        

def stop_blinking(is_pressed):
    global blinking

    if is_pressed:
        blinking = False
        if connected:
            ugTTS.speak("Blinking is now {}".format(blinking))
        else:
            print("Blinking is now {}".format(blinking))


def continue_blinking(is_pressed):
    global blinking

    if is_pressed:
        blinking = True
        if connected:
            ugTTS.speak("Blinking is now {}".format(blinking))
        else:
            print("Blinking is now {}".format(blinking))


def sound_off():
    sndmixer.volume(synth,0)
    return 0


def on_key(key_index, is_pressed):
    global pattern

    if is_pressed:
        x,y = keypad.index_to_coords(key_index)
        pattern[x + y * 4] = (pattern[x + y * 4] + 1) % 4
        if pattern[x + y * 4] == 0:
            display.drawPixel(x,y,0x400000)
            tone = 396
        elif pattern[x + y * 4] == 1:
            display.drawPixel(x,y,0x004000)
            tone = 440
        elif pattern[x + y * 4] == 2:
            display.drawPixel(x,y,0x004040)
            tone = 495
        elif pattern[x + y * 4] == 3:
            display.drawPixel(x,y,0x404000)
            tone = 528
        display.flush()
        sndmixer.freq(synth, tone)
        sndmixer.play(synth)
        sndmixer.volume(synth, 64)
        virtualtimers.new(100, sound_off, False)


def draw():
    global counter

    if blinking:
        counter += 1

    for y in range(4):
        for x in range(4):
            color = settings['color_off']
            if pattern[x + y * 4] == 1:
                color = settings['color_on']

            elif pattern[x + y * 4] == 2:
                if counter % 2 == 0:
                    color = settings['color_off']
                else:
                    color = settings['color_on']

            elif pattern[x + y * 4] == 3:
                if counter % 2 == 0:
                    color = settings['color_on']
                else:
                    color = settings['color_off']

            display.drawPixel(x,y,color)
    display.flush()

    return interval

# initiate WiFi connection for the Text-to-Speach interface
wifi.connect() # Connect to the WiFi network using the stored credentials
if not wifi.wait():
    print("Unable to connect to the WiFi network.")
else:
    connected = True
    ugTTS.speak("You are now connected to WiFi!")

sndmixer.begin(1)
synth = sndmixer.synth()
sndmixer.waveform(synth, 0)
sndmixer.volume(synth, 0)

# Adding callbacks
virtualtimers.begin(50)
virtualtimers.new(0, draw, False)
keypad.add_handler(on_key)
touchpads.on(touchpads.RIGHT, interval_up)
touchpads.on(touchpads.LEFT, interval_down)
touchpads.on(touchpads.CANCEL, stop_blinking)
touchpads.on(touchpads.OK, continue_blinking)
