import system, display, time, keypad, touchpads, virtualtimers, appconfig, sndmixer, wifi, ugTTS

settings = appconfig.get('blink', {'pattern': [2,0,0,2, 0,2,2,0, 0,2,2,0, 2,0,0,2], 'interval': 1000, 'color_on': 0xFF0000, 'color_off': 0x004000, 'speech': True})
pattern  = settings['pattern']
interval = settings['interval']
counter  = 0
blinking = True
connected = False

def msg(text):
    func = ugTTS.speak if connected else print
    func(text)
    
def interval_down(is_pressed):
    global interval

    if is_pressed:
        interval = interval // 2 if interval >= 100 else 50
        msg("Interval is now {}".format(interval))
        

def interval_up(is_pressed):
    global interval

    if is_pressed:
        interval = interval * 2 if interval <= 5000 else 10000
        msg("Interval is now {}".format(interval))
        

def stop_blinking(is_pressed):
    global blinking

    if is_pressed:
        blinking = False
        msg("Blinking is now {}".format(blinking))


def continue_blinking(is_pressed):
    global blinking

    if is_pressed:
        blinking = True
        msg("Blinking is now {}".format(blinking))


def goodbye(is_pressed):
    if is_pressed:
        msg("Well kids, that concludes our demo for today!")
        time.sleep(5)
        system.launcher()


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
if settings['speech']:
    if not wifi.status():
        print("Connecting to WiFi, please wait.")
        audio.play('/cache/system/wifi_connecting.mp3')
        wifi.connect()
        if not wifi.wait():
            audio.play('/cache/system/wifi_failed.mp3')
            print("Unable to connect to the WiFi network.")
        else:
            connected = True
            audio.play('/cache/system/wifi_connected.mp3')
            print("Connected to the WiFi network.")

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
touchpads.on(touchpads.HOME, goodbye)
