import speech_recognition as sr
import audiomath as am
import webbrowser
import pyttsx3 
import datetime
r = sr.Recognizer()

test=pyttsx3.init()
def dario_speek(audio):
    test.say(audio)
    test.runAndWait()


def search():
    search=record_audio('what do you want to search for')
    url = f'https://google.com/search?q={search}'
    webbrowser.get().open(url)
    dario_speek(f'this is what I found about {search}')

def start():
   
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        dario_speek("Good morning sir")
    elif hour >= 12 and hour < 18:
        dario_speek("Good afternoon sir")
    elif hour >= 18 and hour < 24:
        dario_speek("Good evening sir")
    else:
        dario_speek("Good night sir")

    dario_speek("Dario at your service please tell me how can I help you?")

def record_audio(ask=False):
    if ask:
        dario_speek(ask)  
    s=am.Record(4)
    s.Write('some_file.wav')  
    with sr.AudioFile('some_file.wav') as source:
        audio = r.listen(source)
        
       
        voice_data=''
        try:
            voice_data = r.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
            print('sorry: I did not get that ')
        except sr.RequestError:
            print('sorry: my speech service is down')
        return voice_data

def respond(audio):
    if ('what is your name' or 'name') in audio:
        dario_speek('my name is dario')
    if 'search' in audio:
        search()
    if ('stop'or 'exit' or'sleep')in audio:
        dario_speek('nice to meet you' )
        exit()
 




start()
while True:
    voice_data=record_audio()
    respond(voice_data)