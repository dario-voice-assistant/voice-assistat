import speech_recognition as sr
import audiomath as am
import webbrowser
import pyttsx3
import datetime
import smtplib
import requests
import os
from tkinter import *
import glob
from PIL import Image, ImageDraw

r = sr.Recognizer()

test = pyttsx3.init()


def dario_speek(audio):
    test.say(audio)
    test.runAndWait()


def search():
    search = record_audio('what do you want to search for')
    url = f'https://google.com/search?q={search}'
    webbrowser.get().open(url)
    dario_speek(f'this is what I found about {search}')


def location():
    location = record_audio('what is the location that you want e to search for ??')
    url = f'https://google.nl/maps/place/{location}/&amp;'
    webbrowser.get().open(url)


def python():
    temp = record_audio('what would you want me to search for')
    if ('for' or 'loops') in temp:
        url = 'https://www.w3schools.com/python/python_for_loops.asp'
        webbrowser.get().open(url)
    if ('function') in temp:
        url = 'https://www.w3schools.com/python/python_functions.asp'
        webbrowser.get().open(url)
    if ('variables') in temp:
        url = 'https://www.w3schools.com/python/python_variables.asp'
        webbrowser.get().open(url)
    if ('data' and 'types') in temp:
        url = 'https://www.w3schools.com/python/python_datatypes.asp'
        webbrowser.get().open(url)
    if ('operators') in temp:
        url = 'https://www.w3schools.com/python/python_operators.asp'
        webbrowser.get().open(url)
    if ('classes' or 'objects') in temp:
        url = 'https://www.w3schools.com/python/python_classes.asp'
        webbrowser.get().open(url)
    if ('list' or 'lists') in temp:
        url = 'https://www.w3schools.com/python/python_lists.asp'
        webbrowser.get().open(url)
    if ('if' or 'else' or 'conditions') in temp:
        url = 'https://www.w3schools.com/python/python_conditions.asp'
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
    s = am.Record(4)
    s.Write('some_file.wav')
    with sr.AudioFile('some_file.wav') as source:
        audio = r.listen(source)

        voice_data = ''
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
    if 'weather' in audio:
        get_weather(audio)
    if 'python' in audio:
        python()
    # if "play music" in voice_data:
    #     song_path = 'D:\\Music'
    #     songs = os.listdir(song_path)
    #     os.startfile(os.path.join(song_path, songs[0]))


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
    email_server = smtplib.SMTP('smtp.gmail.com', 587)
    email_server.ehlo()
    email_server.starttls()
    gmail_user = 'dariovapy@gmail.com'
    gmail_password = 'dariova123'
    email_server.login(gmail_user, gmail_password)
    email_server.sendmail(gmail_user, to, content)
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
    current_time = now.strftime("%I:%M %p")
    dario_speek('The current time is')
    dario_speek(current_time)


def get_weather(audio):
    temp = record_audio("what is the city name")
    city_name = temp.lower()
    api_key = "39577f16323c466893c05341fcc378c6"
    # temp_url = f"https://api.weatherbit.io/v2.0/forecast/daily?city=amman&key={api_key}"
    temp_url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={api_key}"
    responses = requests.get(temp_url)
    data = responses.json()
    temp = data["data"][0]["high_temp"]
    dario_speek(f" the temperature in {city_name} is {temp} ")


def button_talker():
    start()
    while True:
        voice_data = record_audio()
        respond(voice_data)

def features():
    feature = Toplevel()
    feature.title("Dario features")
    feature.geometry("400x400")
    Label(feature, text="Dario can do many services :", height=3, width=300,
          font="Raleway", bg='black', fg='white').pack(pady=5)
    Lb = Listbox(feature, height=50, width=250, bg='black', fg='white', font="Raleway")
    Lb.insert(1, "1. Time Feature")
    Lb.insert(2, "2. Date Feature")
    Lb.insert(3, "3. Weather Feature")
    Lb.insert(4, "4. Location Feature")
    Lb.insert(5, "5. Send Email Feature")
    Lb.insert(6, "6. Search Feature")
    Lb.insert(7, "7. Play Music Feature")
    Lb.insert(8, "8. Python Feature")
    Lb.insert(9, "9. Exit, Stop Feature")
    Lb.pack()

def application_GUI():
    root = Tk()
    root.title("Dario Voice Assistant")

    root.config(bg='yellow')
    img = PhotoImage(file="GIF.gif", format='gif')
    label = Label(
        root,
        image=img
    )
    # sdfsdfsdffsfsfdfd
    label.place(x=0, y=0, relwidth=1.1, relheight=1.1)

    root.geometry("400x250")
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.rowconfigure(3, weight=1)
    # root.configure(bg='blue')

    button1 = Button(root, text='Exit', command=root.quit, height=1, width=10, bg='#001E6C', fg='#F9F9F9')
    button2 = Button(root, text="Let's Talk", command=button_talker, height=1, width=10, bg='#001E6C', fg='#F9F9F9')
    button3 = Button(root, text='Features', command=features, height=1, width=10, bg='#001E6C', fg='#F9F9F9')
    # button3.config(bg='white')

    button1.grid(row=3, column=0)
    button2.grid(row=3, column=1)
    button3.grid(row=3, column=2)

    root.mainloop()
# # # # # # # #
# # ## ## # ## #
application_GUI()
