import pyttsx3
import speech_recognition as sr
import datetime
from googlesearch import search 
import webbrowser
import smtplib
pairs = [
    [
        'how are you',"I'm great...What can I do for you"
    ],
    [
        'hi',"Kon'nichiwa,that's hello in japanese !  How may I help"
    ],

]

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    speak("I am Alpha.Can i be of any help to you?")
    print("I am Alpha.Can i be of any help to you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=6)

    try:
        print('Recognizing...')
        #speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        #speak(f"you said {query}")

    except Exception as e:
        print("Say that again please...")
        #speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('one.alpha1jarvis@gmail.com', 'Alpha12345')
    server.sendmail('one.alpha1jarvis@gmail.com', 'one.alpha1jarvis@gmail.com', content)
    server.close()

def googlesearch() :
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    speak("What do you want to search")
    query=takeCommand()
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open("https://google.com/search?q=%s" % query)

def openwebsite():
    speak("What is the name of the website")
    website=takeCommand()
    for site in search(website, tld="co.in", num=10, stop=1, pause=2): 
        print(site)
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % site)        

def main():
   print("If you are new here try asking what can you do")
    while True:
        input = takeCommand().lower()
        for i in range(len(pairs)):
            if pairs[i][0] in query:
                speak(pairs[i][1])
                break
        tokens=word_tokenize(input)
        stop_words = set(stopwords.words('english'))
        clean_tokens = [w for w in tokens if not w in stop_words]
        query=' '
        query=query.join(clean_tokens)

        if 'send email' in query:
            try:
                #speak("Please type the Email address of the receiver.")
                #to = input('Email : ')
                to=''
                speak("What should I say?")
                print("What should I say?")
                content = takeCommand()
                sendEmail(to, content)
                print("I have sent your Email.")
            except Exception as e:
                print(e)
                speak("Sorry, Could not send this email.")
                print("Sorry, Could not send this email.")

        elif 'what can you do' in query:
            speak('''I can do the following tasks
1 send an Email
2 open a website
3 search on google ........
say command to view all the existing commands''')
        elif 'stop' in query:
            speak("call me if you need")
            break
        elif 'search' in query:
            googlesearch()
        elif 'open website' in query:
            openwebsite()
        elif 'command' in query:
            print(''' 1.search (To search on google)
2. open website (To open a particular website) )
3.send email (To send an email)
4.stop (Ends the code)''')
        else:
            print("If you are new here try asking what can you do")
     
        
if __name__ == "__main__": 
    wishMe()
    main()
