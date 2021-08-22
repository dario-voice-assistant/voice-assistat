import speech_recognition as sr
import audiomath as am
import webbrowser
import pyttsx3 
import datetime
import smtplib
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

def location():
    location = record_audio('what is the location that you want e to search for ??')
    url = f'https://google.nl/maps/place/{location}/&amp;'
    webbrowser.get().open(url)


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
    if ('send email' or 'email') in audio:
        sender()
    if ('stop' or 'exit' or 'sleep' or 'exit' or 'goodbye') in audio:
        dario_speek('nice to meet you')
        exit()
    if ('date' or 'what is the date') in audio:
        get_date()
    if ('time' or 'what is the time') in audio:
        get_time()
    if 'location' in audio:
        location()

 
def sender():
    try:
        dario_speek("yes sir, what should I say?")
        content = record_audio()
        to = {'awonkhrais@gmail.com'}
        send_email(to, content)
        dario_speek("Email has been sent sir!")

    except Exception as e:
        print(e)
        dario_speek("Unable to send the email")

def send_email(to, content):
    email_server = smtplib.SMTP('smtp.gmail.com',587)
    email_server.ehlo()
    email_server.starttls()
    gmail_user = 'dariovapy@gmail.com'
    gmail_password = 'dariova123'
    email_server.login(gmail_user,gmail_password)
    email_server.sendmail(gmail_user,to,content)
    email_server.quit()

def get_date():
    year = int(datetime.datetime.now().year)
    month_num = str(datetime.datetime.now().month)
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")
    day = int(datetime.datetime.now().day)
    dario_speek("The current date is")
    dario_speek(day)
    dario_speek(full_month_name)
    dario_speek(year)

def get_time():
    now = datetime.datetime.now()
    current_time= now.strftime("%I:%M %p")
    dario_speek('The current time is')
    dario_speek(current_time)

start()
while True:
    voice_data=record_audio()
    respond(voice_data)

