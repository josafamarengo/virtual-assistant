#import section
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import webbrowser

#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Sorry, the service is not available")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


#function to respond to commands
def respond(text):
    if "find location" in text:
        location = get_audio()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        speak("Here is the location of " + location)
    elif "search" in text:
        search = get_audio()
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("Here is what I found for " + search)
    elif "exit" in text:
        exit()

#let's try it
#text = get_audio()
#speak(text)
while True:
    print("I am listening...")
    text = get_audio()
    respond(text)