#This converter requires an internet connection and uses google translate API
#for conversion of text to speech
#Install the API in the terminal
#pip install gTTS

#Import the required module
from gtts import gTTS
#Ths module is needed to play the sound in the system
import os
user_text=input("enter the text you want to hear")
#select the preeferred language by looking up the correct code 
#for the language supported by google translate
language="en"
#pass the above parameters to the gTTS function
audio=gTTS(text=user_text,lang=language,slow=False)
#save to an mp3 file
audio.save("your_text.mp3")
#this command lets you listen to the saved mp3 file
os.system("your_text.mp3")
