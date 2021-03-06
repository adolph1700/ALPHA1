import wx
import pyttsx3
import speech_recognition as sr
import datetime
from googlesearch import search 
import webbrowser
import smtplib
from ALPHA1 import wishMe,main

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


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

    
    def OnEnter(self, event):
        input =self.txt.GetValue()
        input=input.lower()
        wishMe()
        main()


#run the app with the below code
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
