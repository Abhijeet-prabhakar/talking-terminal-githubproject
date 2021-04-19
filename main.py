import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import shutil
import pyaudio
import os

thankyou = "thanks for using me Bye"
creator1 = 'hey i am a talking terminal made by abhijeet prabhakar'
help1 = "open youtube, open github, open browser, open stackoverflow, open spotify, stop, quit, move file, copy file, delete file"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.setProperty("voice", voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning everyone")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    elif hour>=18 and hour<=20:
        speak("Good Evening")
    else:
        speak('Good Night')

# def takeCommand():
#     r = sr.Recognizer
#     with sr.Microphone() as source:
#         print("listening...")
#         r.pause_threshold = 0.8
#         audio = r.listen(source)

#     try:
#         print('recognising')
#         query = r.recognize_sphinx(audio, language='en-in')
#         print('user said:',query)

#     except Exception as e:
#         #print(e)
#         print("say that again please")
#         return "None"
#     return query

if __name__ == "__main__":
    wishMe()
    #takeCommand()
speak('please add your command')
print("type help to see all commands")
speak("type help to see all commands")
command1 = input('write a command:')

if command1 == "open browser":
  speak('opening browser')
  webbrowser.open('www.bing.com')
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "help":
  speak('showing all the commands')
  print(help1)
  speak(help1)
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "open youtube":
  speak('opening youtube')
  webbrowser.open('www.bing.com')
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "open github":
  speak('opening github')
  webbrowser.open('www.github.com')
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "open stackoverflow":
  speak('opening stackoverflow')
  webbrowser.open('www.stackoverflow.com')
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "open spotify":
  speak('opening spotify')
  webbrowser.open('www.spotify.com')
  speak(thankyou)
  speak(creator1)
  quit()

elif command1 == "move file":
  movefile1 = input('add old file path:')
  movefile2 = input("target:")
  shutil.move(movefile1,movefile2)
  speak("moved file from")
  speak(movefile1)
  speak('to')
  speak(movefile2)
  quit()

elif command1 == "copy file":
  movecopy1 = input('add old file path:')
  movecopy2 = input("target:")
  shutil.copy(movecopy1,movecopy2)
  speak("copied file from")
  speak(movecopy1)
  speak('to')
  speak(movecopy2)
  quit()

elif command1 == "delete file":
  deletefilename = input('add the file name:')
  os.remove(deletefilename)
  speak('file successfully deleted')
  quit()

elif command1 =="stop":
  speak("stopping the program")
  print("quit")
  quit()

elif command1 =="quit":
  print("quit")
  quit()

else:
    speak('command not found')
    speak(command1)
    speak('is not a valid command')
    speak(thankyou)
    speak(creator1)
    quit()





