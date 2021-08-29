

[User stories](user_story.md)


## Dario voice assistant

problem to solve:
It will produce a new way for communicate between the user and the machine instead of the old ways which he had to use the mouse and the keyboard to command the machine

It will provide the user the ability to command the machine to do some work for him by voice instead of ordinary ways.

minimum features for the presentation :

- Ask about the date and time
- Send emails
- Open webpages
- Ask about the weather
- Ask about locations

Stretch Goals:

- Open applications
- Set alarm
- Play music
[To use the project](requirements.txt)


# WireFrame

![wireframe](./wirefram.png)

# Domain Modeling

![domain](./dm.jpg)

# trello

[trello](https://trello.com/b/BkLfXBc2/dario-voice-assistant)





# To be able to use Dario Voice Assistant


1. Clone the repository and go to the directory.
2. Install the packages.
   - For Linux users:
   - If you are using VS Code, Run command poetry install and all packages will be installed automatically

   - Then activate the shell by running command poetry shell
   - type python -m dario.main in the command line and press enter to open the app

   - For Windows users: You might face problems on Vs Code, So we highly recommend you to download Pycharm editor instead. You can download it from this link. (<https://www.jetbrains.com/pycharm/>)
      - Run the following commands to make sure you have installed all the packages:
        - pip install speechrecognition
        - pip install audiomath
        - pip install pyttsx3
        - pip install datetime
        - pip install requests
        - pip install pyjokes
        - pip install tk
        - pip install secure-smtplib
        - pip install regex
        - pip install os-sys
        - pip install pillow
        - type python -m dario.main and in the command line and press enter to open the app

3. A Graphical user interface should appear by now with 3 buttons.
   1. "Goodbye" Button: To close it and finish talking.
   2. "Let's Talk" Button: To be able to give commands by talking.
   3. "Features" Button: That will show you a list of the features and the commands you are able to use.

