# donna desktop assistant
from time import sleep
import pywhatkit
import wikipedia
import datetime
import pyttsx3
import webbrowser
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def remover(st):
    removing_items = ['what', 'why', username, 'please', 'search', 'play']
    new = st.split()
    final = ''
    for i in new:
        if i not in removing_items:
            final += (i + ' ')
    return final

# wishing user
def wish_me():
    hr = int(datetime.datetime.now().hour)
    if 12 > hr >=0:
        print('good morning boss!!')
    elif 16 > hr >= 12:
        print('Good afternoon boss!!')
    else:
        print('Good evening boss')

def takeCommand():
    #It takes microphone input from the user and returns string output

    rr = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        rr.pause_threshold = 1
        audio = rr.listen(source)

    try:
        print("Recognizing...")
        query = rr.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        speak("Connection error")
        return "None"
    return query

username = 'donna'

if __name__ == '__main__':
    while True:
        text = takeCommand().lower()
        if username in text:
            wish_me()
            speak('how may i help you ?')
            while True:
                inp = input()
                if 'search' in inp:
                    inp = remover(inp)
                    pywhatkit.search(inp)
                    sleep(5)
                elif "who are you" in inp or "about you" in inp or "your details" in inp:
                    iam = "I am Donna an A I based computer program developed by Ballav, but i can help you lot like a your assistant ! try me to give simple command !"
                    speak(iam)
                elif 'who make you' in inp or 'who made you' in inp or 'who created you' in inp or 'who develop you' in inp:
                    speak(" For your information Ballav Created me !    I can show you his Linked In profile if you want to see.    Yes or no .....")
                    ansMadefromUser = takeCommand().lower()
                    if 'yes' in ansMadefromUser or 'ok' in ansMadefromUser or 'yeah' in ansMadefromUser:
                        webbrowser.open("https://www.linkedin.com/in/ballav-kumar-behera-3820b7213/")
                        speak('opening his profile...... please wait')

                    elif 'no' in ansMadefromUser or 'no thanks' in ansMadefromUser or 'not' in ansMadefromUser:
                        speak("All right ! OK...")
                    else :
                        speak("I can't understand. Please say that again !")
                elif 'open youtube' in inp:
                    webbrowser.open("www.youtube.com")
                    speak("opening youtube")

                elif 'open github' in inp:
                    webbrowser.open("https://www.github.com")
                    speak("opening github")

                elif 'open facebook' in inp:
                    webbrowser.open("https://www.facebook.com")
                    speak("opening facebook")

                elif 'open instagram' in inp:
                    webbrowser.open("https://www.instagram.com")
                    speak("opening instagram")   

                elif 'open google' in inp:
                    webbrowser.open("google.com")
                    speak("opening google")
                elif 'open gmail' in inp:
                    webbrowser.open("https://mail.google.com")
                    speak("opening google mail")
                elif 'what is' in inp:
                    inp = remover(inp)
                    txt = wikipedia.summary(inp, sentences=3)
                    print('according to wikipedia:')
                    print(txt)
                elif 'play' in inp:
                    pywhatkit.playonyt(remover(inp))
                elif 'what is the time' in inp.lower():
                    strTime=datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"the time is :{strTime}")
                elif inp == 'none':
                    continue
                elif 'sleep' or 'good night' in inp:
                    print('see you later boss!!')
                    break