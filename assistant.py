import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("How may I help you")

def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please")
        print("Say that again please")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP("smtp.gmail.com", 587)
#     server.ehlo()
#     server.starttls()


if __name__ == "__main__":
    welcome()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)
        elif "open youtube" in query or "youtube" in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif "open google" in query or "google" in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            speak("Opening music")
            webbrowser.open_new("https://www.youtube.com/watch?v=60ItHLz5WEA&ab_channel=AlanWalker") # just a sample
        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open vs code" in query:
            codePath = "C:\\Users\\Sufyan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code...")
            os.startfile(codePath)
        # elif "send email" in query:
        #     try:
        #         speak("What shoud I say?")
        #         content = takeCommand()
        #         to = "suffiyaanusmani@gmail.com"
        #         sendEmail(to, content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry, email not sent")
        elif "quit" in query:
            speak("Bye")
            break