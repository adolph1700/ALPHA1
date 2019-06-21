import speech_recognition as sr  
from gtts import gTTS
import os
from playsound import playsound
from googlesearch import search 
import webbrowser

# get audio from the microphone

def talk(audio):
    #for lines in audio.splitlines:
    #os.system("say"+ audio)
    file="file.mp3"
    tts=gTTS(audio,lang='en')
    tts.save(file)
    playsound(file)
        
def mycommand():

    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listning....")                                                                                   
        audio = r.listen(source)   

    try:
        
        command=r.recognize_google(audio).lower()
        print("You said " + command )
        file="file.mp3"
        tts=gTTS(command,lang='en')
        #tts.save(file)
        #playsound(file)
        #os.system("say"+file)
        talk("you said"+command)
        #query=message
        #for j in search(query, tld="co.in", num=10, stop=1, pause=2): 
        #    print(j)
        #    webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % j)
    except sr.UnknownValueError:
        print("Could not understand audio")
        talk("Could not understand audio please speak again")
        command=mycommand()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e)) 
    return command


def tasks(command):
    if command=="open website":
        talk("What is the name of the website")
        website=mycommand()
        for j in search(website, tld="co.in", num=10, stop=1, pause=2): 
            print(j)
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % j)        
            #webbrowser.open_new_tab('http://www.google.com/%s' % j)
    #elif command==


tasks(mycommand())


