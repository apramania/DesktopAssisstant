import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Hey I am Eve!Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please..")
        return("None")

    return query




if __name__ == "__main__":
    wishMe()
    while (True):
        
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia")
            speak(results)
        
        elif 'open youtube' in query:
            speak("Opening youtube for you")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google for you")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("Opening stackoverflow for you")
            webbrowser.open("stackoverflow.com")

        elif 'play hindi music' in query:
            speak("Playing hindi music for you")
            music_dir = "C:\\Users\\User\\ApraMusic\\Hindi Songs"
            songs = os.listdir(music_dir)
            play = random.randint(0,8)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[play]))

        elif 'play english music' in query:
            speak("Playing english music for you")
            music_dir = "C:\\Users\\User\\ApraMusic\\English songs"
            songs = os.listdir(music_dir)
            play = random.randint(0,4)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[play]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'The time is {strTime}')

        elif 'open visual code' in query:
            speak("Opening Visual Studio Code for you")
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            

