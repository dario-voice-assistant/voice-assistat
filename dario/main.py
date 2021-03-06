from audiomath.Base import DecodeTimecodeString
import speech_recognition as sr
import audiomath as am
import webbrowser
import pyttsx3 
import datetime
import smtplib
import requests
import urllib.request
import re
import os
import pyjokes

import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk

root = tk.Tk()

r = sr.Recognizer()

test=pyttsx3.init()
def dario_speek(audio,tests=False):

    """
    Dario speak is the function make the assistant talk to the user and convert the text to audio.
    """

    if tests:
        return True
        
    test.say(audio)
    test.runAndWait()

    


def search(test=False):

    """
    it is the function to search on google, when user ask for serach about something.
    """

    search=record_audio('what do you want to search for',test)
    url = f'https://google.com/search?q={search}'
    webbrowser.get().open(url)
    dario_speek(f'this is what I found about {search}',test)
    check=True
    return url

def search_youtube(test=False):

    """
    it is the function to search on youtube, when user ask for play music.
    """

    search=record_audio('what do you want me to play',test)
    search_new = search.replace(' ', '+')
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={search_new}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    webbrowser.get().open("https://www.youtube.com/watch?v=" + video_ids[0])
    return (f"https://www.youtube.com/results?search_query={search_new}")


def location(test=False):

    """
    it is the function to apper the locations on maps, when user ask for location.
    """

    location = record_audio('what is the location that you want e to search for ??',test)
    url = f'https://google.nl/maps/place/{location}/&amp;'
    webbrowser.get().open(url)
    return url

def python():

    """
    it is the function to search about python topics, when user ask for python topics.
    """

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


counter = 0

def start():

    """
    it is the function to start the whole app.
    """

    global counter
    if counter == 0 :
        hour = datetime.datetime.now().hour
        if hour >= 6 and hour < 12:
            dario_speek("Good morning ")
        elif hour >= 12 and hour < 18:
            dario_speek("Good afternoon ")
        elif hour >= 18 and hour < 24:
            dario_speek("Good evening ")
        else:
            dario_speek("Good night ")

        dario_speek("Dario at your service please tell me how can I help you?")
  
    counter +=1
    respond()
    # root.after(1000, respond)


recording=False
def start_record():

    """
    it is the function to start record when user talk to the assistant.
    """

    global recording 
    recording=True
    s=am.Record(4)
    recording=False
    return s


def record_audio(ask=False,test=False):

    """
    It is the function convert the audio to text.
    """

    if test:
        return 'test'
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
            dario_speek('sorry, I did not get that, please repeat')
            voice_data=record_audio()
        except sr.RequestError:
            dario_speek('sorry, my speech service is down')
        return voice_data

trying=0

def respond():

    """
    It is the function take users command and act upon it.
    """

    global trying
    if trying>0:
        dario_speek('anything else')
    trying+=1
    audio = record_audio()
    
    if ('what is your name' or 'name') in audio:
        dario_speek('my name is dario')
        root.after(1000, respond)

    if 'search' in audio:
        search()
        # root.after(1000, respond)
        trying=0

    if ('send' or 'email') in audio:
        sender()
        # root.after(1000, respond)
        trying=0

    if ('stop' or 'exit' or 'sleep' or 'goodbye'or 'no') in audio:
        dario_speek('see you next time')
        exit()
    if ('date' or 'what is the date') in audio:
        get_date()
        root.after(1000, respond)

    if ('time' or 'what is the time') in audio:
        get_time()
        root.after(1000, respond)

    if 'location' in audio:
        location()
        # root.after(1000, respond)
        trying=0

    if ('weather'or 'condition' or 'hi') in audio:
        get_weather(audio)
        root.after(1000, respond)

    if ('python'or'advise'or 'advice') in audio:
        python()
        # root.after(1000, respond)
        trying=0

    if "play music" in audio:
        search_youtube()
        # root.after(1000, respond)
        trying=0

    if 'joke' in audio:
        joke()
        root.after(1000, respond)


def joke(test=False):

    """
    It is the function tell the user a jokes when user ask for a joke.
    """

    joke1=pyjokes.get_joke(language='en', category= 'all')
    dario_speek(joke1,test)
    dario_speek('ha ha ha ha ha ha ha ha ha ',test)
    return True

def sender():

    """
    It is the function that save the contet email message and the reciver.
    """

    try:
        
        content = record_audio("yes sir, what should I say?")
        reciver=record_audio("for who ??")
        to = {'Sam':'awonkhrais@gmail.com',
        "Feras":'ferasezaldeen@gmail.com',
        "Jack":'ferasezaldeen@gmail.com'}
        print(to[reciver])
        send_email(to[reciver], content)
        dario_speek("Email has been sent sir!")

    except Exception as e:
        
        dario_speek("Unable to send the email")

def send_email(to, content):

    """
    It is the function that send the emails for the user.
    """

    email_server = smtplib.SMTP('smtp.gmail.com',587)
    email_server.ehlo()
    email_server.starttls()
    gmail_user = 'dariovapy@gmail.com'
    gmail_password = 'dariova123'
    email_server.login(gmail_user,gmail_password)
    email_server.sendmail(gmail_user,to,content)
    email_server.quit()

def get_date(test=False):

    """
    It is the function tell the user the date when user ask about the date.
    """

    year = int(datetime.datetime.now().year)
    month_num = str(datetime.datetime.now().month)
    datetime_object = datetime.datetime.strptime(month_num, "%m")
    full_month_name = datetime_object.strftime("%B")
    day = int(datetime.datetime.now().day)
    dario_speek("The current date is",test)
    dario_speek(day,test)
    dario_speek(full_month_name,test)
    dario_speek(year,test)
    return True

def get_time(test=False):

    """
    It is the function tell the user the time when user ask about the time.
    """

    now = datetime.datetime.now()
    current_time= now.strftime("%I:%M %p")
    dario_speek('The current time is',test)
    dario_speek(current_time,test)
    return True

def get_weather(test = False):

    """
    It is the function tell the user the weather when user ask about the weather.
    """

    temp = record_audio("what is the city name", test)
    city_name = temp.lower()
    api_key = "39577f16323c466893c05341fcc378c6"
    temp_url = f"https://api.weatherbit.io/v2.0/forecast/daily?city={city_name}&key={api_key}"
    responses = requests.get(temp_url)
    data = responses.json()
    temp = data["data"][0]["high_temp"]
    dario_speek(f" the temperature in {city_name} is {temp} ", test)
    return temp_url
    

def on_start():

   global running
   running = True
#
def on_stop():

    """
    It is the function that cloce the app.
    """

    dario_speek("Good Bye sir! nice to meet you")
    global running
    running = False
    exit()
    # root.destroy()



def open_window():

    """
    It is the function that open the features window.
    """

    global root
    feature_window = Toplevel(root)
    # feature_window.iconbitmap('../icon.ico')

    feature_window.title("Dario features")
    feature_window.geometry("550x300")
    Label(feature_window,text="Dario is here to help you with the following services:", height = 3,  width = 500, font = "Raleway" , bg = '#282828',fg= '#429fca').pack(pady = 10)
    Lb = Listbox(feature_window ,height = 200,width = 500,  bg = '#282828', font = "Raleway",fg='#429fca')
    Lb.insert(1, "1. Time Feature")
    Lb.insert(2, "2. Date Feature")
    Lb.insert(3, "3. Weather Feature")
    Lb.insert(4, "4. Location Feature")
    Lb.insert(5, "5. Send Email Feature")
    Lb.insert(6, "6. Search Feature")
    Lb.insert(7, "7. Play Music Feature")
    Lb.insert(8, "8. Python Feature")
    Lb.insert(9, "9. Joke Feature")
    Lb.insert(10, "10. Exit, Stop Feature")
    Lb.pack()
    feature_window.mainloop()



def gui():

    """
    It is the function that appear the Interface for the users we have inside it 3 buttons :

    1- Features button : It is the button show the app features in exterior window when user click on it.

    2- Let's talk button : It is the button that starts the most of app functionality when the user click on it can talk with the assistant
    and ask for the features he's want to ask about it and the assistant will give the user what he was asking about.

    3- Goodbye button : It is the button close the app when user finish.
    """

    canvas = tk.Canvas(root, width=600, height=400)
    canvas.grid(columnspan=3)


    logo = Image.open('./voice_ui_logo.jpg')
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image = logo)
    logo_label.image = logo
    logo_label.grid(column=1,row=0)
    root.title('Dario Voice Assistant ')


    start_talk = tk.Button(height=1, width=10, text="Let's Talk ", command=start, bg='#429fca', fg='white')
    start_talk.config(font=("Raleway", 12))
    start_talk.place(x=350, y=520)


    my_features = tk.Button(height=1, width=11, text="My Features ", command=open_window, bg='#429fca', fg='white')
    my_features.config(font=("Raleway", 12))
    my_features.place(x=500, y=520)
    #c61a80

    good_bye = tk.Button(height=1, width=10, text="Good Bye", command=on_stop, bg='#429fca', fg='white')
    good_bye.config(font=("Raleway", 12))
    good_bye.place(x=200, y=520)


    root.mainloop()


if __name__ == '__main__':
    gui()


# start()
# while True:
#     voice_data=record_audio()
#     respond(voice_data)

