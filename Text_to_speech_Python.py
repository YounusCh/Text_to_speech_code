#pyttsx3 is used for text to speech conversion if your system is offline
#A more preferable option which need the internet is gTTS but this code will use pyttsx3
-----
#Enter this in the terminall to install pyttsx3 library
#pip install pyttsx3
-----
#Import the library
import pyttsx3
#initialize the text-to-speech engine
engine = pyttsx3.init()
#prompt the user to enter the text of their choice
text = input("enter the text you would like to hear")
#set the rate of speech if needed
engine.setProperty('rate', 110)
#pass the text as an argument 
engine.say(text)
#play the speech
engine.runAndWait() 
