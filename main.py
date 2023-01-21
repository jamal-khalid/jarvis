import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib

e_var={"khalid":"jamalkhalid945@gmail.com" , "abcd":"shahanwajansari5786@gmail.com"}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")

    elif hour >= 12 and hour < 18:
        speak("good afternoon")

    else:
        speak("good evening")
    speak("i am jarvis sir. how may i help you ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognition .. ")
        query=r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception  as e:
        print("say that again please : ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jamalkhalid544@gmail.com','wpydqrwpuklybezr')
    server.sendmail('jamalkhalid544@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia ....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')

        elif 'play music'  in query:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            number=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[number]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak('i am fine sir .thank you for asked')
            speak('how are you sir')

        
        elif 'what is your name'  in query:
            speak('my friends call me popatlal')

        elif  'who create you' in query:
            speak('i have been created by jamal khalid')

        elif 'send email' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                print(content,'content')
                speak('whom to send sir')
                too=takeCommand().lower()
                print(too)
                to=e_var[too]
                sendEmail(to ,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('sorry sir i am not able to send email ')

        elif 'open vs code' in query:
            codePath='C:\\Users\\jamal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codePath)
        
        elif 'exit' in query:
            break

        else:
            print('sorry sir I cant tell you because my boss forbids')
            speak('sorry sir I cant tell you because my boss forbids')

    speak('thankew for giving time to me ')

    
