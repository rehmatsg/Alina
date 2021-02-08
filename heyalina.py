import settings
import speech_recognition as sr
import pyttsx3
import backend
import time
from win10toast import ToastNotifier
import functions as fn

t = time.localtime()

toaster = ToastNotifier()

engine = pyttsx3.init()

r = sr.Recognizer()
mic = sr.Microphone()

#Shows a notification
toaster.show_toast("Alina has started","Alina service is active. Say 'Alina' to trigger me.")

print(fn.greet() + ", Rehmat")
engine.say(fn.greet() + ", Rahamat. Say 'Alina' to trigger me.")
engine.runAndWait()

mode = "chat"
name = "Rehmat"

while True:
    with mic as source:
        audio = r.listen(source)

        try:
            rec = r.recognize_google(audio)

            print("[" + rec + "]")

            if 'Elena' in rec:
                rec = rec.replace('Elena', 'Alina')

            if 'Alina' in rec or 'alina' in rec:
                q = rec.replace("Alina", "")
                toaster.show_toast("Hearing...","You probably said: [" + q + "]")
                print("You --> " + q)
                response = backend.Alina(q, name, mode)
                alina_resp = response[0]
                mode = response[1]
                long_text = response[2]
                url = response[3]
                print("Alina --> " + alina_resp + "\n" + long_text + "\n" + url)
                engine.say(alina_resp + " " + long_text)
                engine.runAndWait()
            else:
                print("Say 'Alina' to trigger me. (ERR1)")

        except:
            print("Sorry, I could not understand that. (ERR2)")

print("Goodbye")
engine.say("Goodbye, see you later")
engine.runAndWait()
engine.stop()