import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import smtplib
import webbrowser as wb 
import os


engine = pyttsx3.init()
# engine.say("Hello world")
# engine.runAndWait()
voice = engine.getProperty('voices')
engine.setProperty('voices',voice[1].id)
newVoiceRate =150
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak(time)


def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<=12:
            speak("good morning")
    elif hour>=12 and hour<18:
         speak("good afternoon")
    elif hour >=18 and hour<=24:
         speak("good evening")
    else:
         speak("good night")

#speak("at your service. how can i help you?")

# def takeCommand():
#      r = sr.Recognizer()
#      with sr.Microphone() as source:
#           print("Listining.....")
#           r.pause_threshold =1
#           audio= r.listen(source)

#      try:
#          print("Recognizing....")
#          query = r.recognize_google(audio,'en=US')
#          print(query)
#      except Exception as e:
#          print(e)
#          speak("say that again please....")

#          return "none"
#      return query
def takeCommand():

    r = sr.Recognizer()



    with sr.Microphone() as source:

        print("listening...")

        r.adjust_for_ambient_noise(source)

        r.pause_threshold = 1

        audio = r.listen(source)

        try:

            print("Recognising...")

            print (r.recognize_google(audio,language = 'en-in'))

        except Exception as e:

            print("Error :  " + str(e))

            speak("Repeat the speech again")

            return "None"

        with open("recorded.wav", "wb") as f:

            f.write(audio.get_wav_data())

def sendMail(to, content):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.ehlo()
     server.starttls()
     server.login('test@gmail.com',"123test")
     server.sendmail("text@gmail.com", to , content)
     server.close()

if __name__ == "__main__":
     wishme()
     while True:
          query= takeCommand().lower()
          print(query)

          if "time" in query:
               time()
          elif "date" in query:
               date()
          elif "offline" in query:
               quit()
          elif "wikipedia" in query:
               speak("Searching...")
               query=query.replace("wikipedia","")
               result=wikipedia.summary(query,sentences=2)
               speak(result )
          elif "send email" in query:
               try:
                    speak("what should i say?")
                    content = takeCommand()
                    to ="xyz@gmail.com"
                    # sendMail(to, content)
                    speak('email sent succesfully')
                    speak(content)
               except Exception as e:
                    speak(e)
                    speak("unable to send the message")
          elif "search in chrome" in query:
                    speak("what should i search?")
                    chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
                    search = takeCommand().lower()
                    wb.get(chromepath).open_new_tab(search + ".com")
               


     



#speak("hello this is your python assistant")


