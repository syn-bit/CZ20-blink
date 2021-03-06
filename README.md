# CZ20-blink

During Campzone 2020 Online, I presented on how to create your own APP for the awesome CZ20 badge.
The video of the presentation can be found at https://www.twitch.tv/videos/693116621?t=48m38s

In each step another part of the API to the badge.team firmware is added to the app. And with each step the simple blinking program is transforming into an app that could be useful too.

The easiest way to test your code during development is by starting the system shell with the command `system.shell()` in the Python terminal screen on the "Programming & Files" page of the badge.

When the shell has started, you can use `CTRL+E` to start the `paste-mode`. Now you can paste your python script and finish uploading by pressing `CTRL+D`. After this, your script will be run immediately.

There are 9 steps in this tutorial and in each of them you will learn something new about the API:

- **00-blink.py**

	This is the most elementary form of a app that blinks all the leds on the badge. It is an introduction to the `display` API.

    [Video at 1:00:20](https://www.twitch.tv/videos/693116621?t=1h00m20s)

- **01-blink-pattern.py**

	This is a preparation to create a blinking pattern. A new function in the `display` API is introduced.

    [Video at 1:02:18](https://www.twitch.tv/videos/693116621?t=1h02m18s)
	
- **02-blink-keypad.py**

	To change the blinking pattern, the `keypad` API is used to check which buttons are pressed on the keypad. Also, printing to the Python terminal is introduced as a debugging method.

    [Video at 1:06:00](https://www.twitch.tv/videos/693116621?t=1h06m00s)

- **03-blink-virtualtimers.py**

	The previous code used the `time.sleep()` function for creating the blinking. This is not optimal, as can be seen in the non-responsiveness of the keypad. In this demo the `virtualtimers` API is introduced to handle timed events.
	
	Since all code is now run by events and timers, we have the REPL console available too, which means we can print and change variables while the APP is still running. Very useful for debugging your APP.

    [Video at 1:12:40](https://www.twitch.tv/videos/693116621?t=1h12m40s)
	
- **04-blink-appconfig.py**

	In this demo, `appconfig` is introduced to create a settings tab for the APP on the Settings page of your badge. In order for this to work, you need to add the APP in the `apps` directory on the flash. Also, a `metadata.json` file needs to be present to describe your APP.
	
	Now you can change colors and beginning patterns of the APP without having to change the APP code.

    [Video at 1:21:40](https://www.twitch.tv/videos/693116621?t=1h21m40s)
	
- **05-blink-touchbuttons.py**

	It is nice to change some settings on the fly without having to restart the APP, that is where we will use the touch buttons for. This demo introduced the `touchpads` API.

    [Video at 1:33:09](https://www.twitch.tv/videos/693116621?t=1h33m09s)
	
- **06-blink-sndmixer.py**

	As the badge has two speakers, lets introduce some simple sounds with the `sndmixer` API.

    [Video at 1:37:20](https://www.twitch.tv/videos/693116621?t=1h37m20s)
	
- **07-blink-ugtts.py**

	Since simple tones are a bit dull, let's use the `audio` API to play mp3 files from the flash and use the `ugTTS` API to do text-to-speech. As this needs an Internet connection, the `wifi` API is introduced as well.

    [Video at 1:42:16](https://www.twitch.tv/videos/693116621?t=1h42m16s)
	
- **08-blink-msg.py**

	This is not so much an introduction to the badge API's, but it is an optimization that makes your code more compact, better readable and has improved manageability. It also shows you how functions are 'first class citizens'. 

    (not in the video)

- **Using the hatchery**

    After finishing your APP, you can upload your APP to the [hatchery](https://badge.team/). This will make your APP available to everyone CZ20 badge.

    [Video at 1:45:56](https://www.twitch.tv/videos/693116621?t=1h45m56s)

	
And that concludes this introduction to badge programming on the CZ20 badge.
