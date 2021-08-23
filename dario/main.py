import speech_recognition as sr
import audiomath as am
import webbrowser
import pyttsx3 
import datetime
import smtplib
import requests
import os
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
root = tk.Tk()
canvas = tk.Canvas(root,width = 600 , height = 400)
canvas.grid(columnspan = 3)

#logo
root.iconbitmap('../logo.ico')

logo = Image.open('../mic.gif')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)
root.title('Dario Voice Assistant ')

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

def python():
    temp=record_audio('what would you want me to search for')
    if ('for'or 'loops')in temp:
        url='https://www.w3schools.com/python/python_for_loops.asp'
        webbrowser.get().open(url)
    if ('function')in temp:
        url='https://www.w3schools.com/python/python_functions.asp'
        webbrowser.get().open(url)
    if ('variables')in temp:
        url='https://www.w3schools.com/python/python_variables.asp'
        webbrowser.get().open(url)
    if ('data'and'types')in temp:
        url='https://www.w3schools.com/python/python_datatypes.asp'
        webbrowser.get().open(url)
    if ('operators')in temp:
        url='https://www.w3schools.com/python/python_operators.asp'
        webbrowser.get().open(url)
    if ('classes'or'objects')in temp:
        url='https://www.w3schools.com/python/python_classes.asp'
        webbrowser.get().open(url)
    if ('list'or'lists')in temp:
        url='https://www.w3schools.com/python/python_lists.asp'
        webbrowser.get().open(url)
    if ('if'or'else' or 'conditions')in temp:
        url='https://www.w3schools.com/python/python_conditions.asp'
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
    root.after(1000, respond)



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

def respond():
    audio = record_audio()

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
    if "play music" in voice_data:
        song_path = 'D:\\Music'
        songs = os.listdir(song_path)
        os.startfile(os.path.join(song_path, songs[0]))

 
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

def on_start():
   global running
   running = True

def on_stop():
    dario_speek("Good Bye sir! nice to meet you")
    global running
    running = False
    root.destroy()


def open_window():
    feature_window = Toplevel(root)
    feature_window.title("Dario features")
    feature_window.geometry("550x300")
    Label(feature_window,text="Dario is here to help you, he can do many services:", height = 3,  width = 500, font = "Raleway" , bg = '#724bf2').pack(pady = 10)
    Lb = Listbox(feature_window ,height = 200,width = 500,  bg = '#724bf2', font = "Raleway" )
    Lb.insert(1, "1.")
    Lb.insert(2, "2.")
    Lb.insert(3, "3.")
    Lb.insert(4, "4.")
    Lb.insert(5, "5.")
    Lb.insert(6, "6.")
    Lb.insert(7, "7.")
    Lb.pack()
    feature_window.mainloop()



start_talk = tk.Button(height=1, width=10, text="Let's Talk ", command=start, bg='#724bf2', fg='white')
start_talk.config(font=("Raleway", 12))
start_talk.place(x=350, y=520)


my_features = tk.Button(height=1, width=11, text="My Features ", command=open_window, bg='#724bf2', fg='white')
my_features.config(font=("Raleway", 12))
my_features.place(x=550, y=520)

good_bye = tk.Button(height=1, width=10, text="Good Bye", command=on_stop, bg='#724bf2', fg='white')
good_bye.config(font=("Raleway", 12))
good_bye.place(x=150, y=520)




root.mainloop()


# start()
# while True:
#     voice_data=record_audio()
#     respond(voice_data)

