''' Using wxPython'''
import wx
import pyttsx3
import speech_recognition as sr
import datetime
#from googlesearch import search 
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    print(audio)
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

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('one.alpha1jarvis@gmail.com', 'Alpha12345')
    server.sendmail('one.alpha1jarvis@gmail.com', to, content)
    server.close()
def googlesearch() :
    chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
    for url in search(query, tld="co.in", num=1, stop=1, pause=2):
        webbrowser.open("https://google.com/search?q=%s" % query)

def openwebsite():
    speak("What is the name of the website")
    website=takeCommand()
    for site in search(website, tld="co.in", num=10, stop=1, pause=2): 
        print(site)
        webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % site)   
#set a main class for the app frame
class MyFrame(wx.Frame):
    def __init__(self):        
        #set some basic gui info about the app
        wx.Frame.__init__(self, None,
                        pos=wx.DefaultPosition, size=wx.Size(450,100),
                        style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                        wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                        title="ALPHA1")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, 
        label="Hello I am ALPHA1 the Python  Virtual Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        #set up a simple text box with the following properties
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()
        #self.close()
    
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
            query = self.text.SetValue(r.recognize_google(audio, language='en-in'))
            print(f"User said: {query}\n")
            #speak(f"you said {query}")

        except Exception as e:
            print("Say that again please...")
            #speak("Say that again please...")
            return "None"
        return query




    def OnEnter(self, event):
        input =self.txt.GetValue()
        input=input.lower()
#         if input=='':
#             query=self.takeCommand
        wishMe()
        #while True:
        print("If you are new here try asking what can you do")
        query =self.txt.GetValue()
        
        query = query.lower()
        if 'send email' in query:
            try:
                speak("Please type the Email address of the receiver.")
                print("Email")
                #to = self.txt.GetValue(takecommand()).lower()
                self.txt.Bind(wx.EVT_TEXT_ENTER,self.OnEnter)
                to=self.txt.GetValue()
                speak("What should I say?")
                content = self.txt.GetValue().lower()
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
            #break
        elif 'search' in query:
            googlesearch()
        elif 'open website' in query:
            openwebsite()
        elif 'command' in query:
            print(''' 1.search (To search on google)
2. open website (To open a particular website) )
3.send email (To send an email)
4.stop (Ends the code)''')


#run the app with the below code
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
