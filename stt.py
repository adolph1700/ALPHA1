import speech_recognition as sr  
from gtts import gTTS
import os
from playsound import playsound
from googlesearch import search 
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

try:
    message=r.recognize_google(audio)
    print("You said " + message)
    file="file.mp3"
    tts=gTTS(message,lang='en')
    tts.save(file)
    playsound(file)
    query=message
    for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        print(j)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e)) 


