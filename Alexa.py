import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass    
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is' + time)

    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 5)
        print(info)
        talk(info) 

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'how are you' in command:
        print('i am alright how are you my boss')
        talk('i am alright how are you my boss')

    elif 'i am fine' in command:
        print('ok how can i help you')
        talk('ok how can i help you')

    elif 'google' in command:
        result = command.replace('google', '')
        talk('searching ' + result + 'on google')
        pywhatkit.search(result)

    else:
         talk('Please say that command again')

while True:
    run_alexa()