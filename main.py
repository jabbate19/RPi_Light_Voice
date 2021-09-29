#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import board
import neopixel
from time import sleep

pixels = neopixel.NeoPixel(board.D18, 30)

active = False
time_to_shut_down = False

color_dict = {
    'red' : [ 255, 0, 0 ],
    'orange' : [ 255, 128, 0 ],
    'yellow' : [ 255, 255, 0 ],
    'green' : [ 0, 255, 0 ],
    'blue' : [ 0, 0, 255 ],
    'purple' : [ 127, 0 , 255 ],
    'white' : [ 255, 255, 255],
    'pink' : [ 255, 0, 255 ],
    'cyan' : [ 0, 255, 255 ]
}
def process_command(data):
    data = data.split()
    print(data)
    try:
        if data[0][:5] == 'light':
            print(1)
            if data[1] == 'off':
                print("Lights off")
            elif data[1] == 'on':
                print("Lights on")
            elif data[1] == 'set':
                print(2)
                color = []
                if data[2] == 'RGB':
                    color_data = data[3] + data[4] + data[5]
                    color = [ int(x) for x in color_data.split(',') ]
                else:
                    print(3)
                    color = color_dict[data[2]]
                    print(color)
                #print(color)
                print("Setting to:")
                print("R:", color[0])
                print("G:", color[1])
                print("B:", color[2])
                for pixel in pixels:
                    pixel = color
                sleep(1)
    except Exception as e:
        print(e)

while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        response = r.recognize_google(audio)
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Google Speech Recognition thinks you said " + response)
        if active:
            process_command( response )
        if "david" in response.lower():
            active = True
            print("THIS BITCH ACTIVE")
        if "cancel" in response.lower():
            break
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    if time_to_shut_down:
        active = False
        time_to_shut_down = False
    if active:
        time_to_shut_down = True
    