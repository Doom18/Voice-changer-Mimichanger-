import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
v = input("Enter 0 for male voice and 1 for female voice")
v = int(v)
engine.setProperty('voice',voices[v].id)
with sr.Microphone() as source:
    print("Speak")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        query = r.recognize_google(audio)
        print("You said: ")
        print(query)
        engine.say(query)
        engine.runAndWait()

    except Exception as e:
        print("Couldn't make out the words.... please speak again")