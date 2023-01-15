import openai
import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3


engine = pyttsx3.init()
engine.say("Hello, My name is Alex. How can i Help you?")
engine.runAndWait()

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        #speak(f": {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")  
        return "None"

def send_to_api(query):
    openai.api_key = "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"
    prompt = (f"User: {query}\n")
    response = openai.Completion.create(engine="text-davinci-002",prompt=prompt,max_tokens=1024)

    print(response.choices[0].text)
    speak(response.choices[0].text)
    
if __name__ == "__main__":
    query = takeCommand()
    send_to_api(query)

#Creating while loop
while True:
    query = takeCommand().lower()
    send_to_api(query)
