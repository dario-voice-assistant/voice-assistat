## Dario voice assistant

Problem to solve:
It will produce a new way for communicate between the user and the machine instead of the old ways which he had to use the mouse and the keyboard to command the machine


It will provide the user the ability to command the machine to do some work for him by voice instead of ordinary ways.

Minimum features for the presentation :

- Ask about the date and time 
- Send emails. 
- Open webpages. 
- Ask about the weather. 
- Ask about locations. 
- Ask about the current time.
- Play music.
- Hear jokes.

Stretch Goals:

- Open applications.
- Set alarms.
- Make it an application.


## To be able to use Dario Voice Assistant
1. Clone the repository.
2. Install the packages.
   1. For Linux users: If you are using VS Code, Run command **$ poetry install** and all packages will be installed automatically, Then activate the shell by running command  **$ poetry shell**   
   2. For Windows users: You might face problems on Vs Code, So we highly recommend you to download Pycharm editor instead. You can download it from this link. (https://www.jetbrains.com/pycharm/)
      - Run the following commands to make sure you have installed all the packages:
        - **$ pip install speechrecognition**
        - **$ pip install audiomath**
        - **$ pip install pyttsx3**
        - **$ pip install datetime**
        - **$ pip install requests**
        - **$ pip install pyjokes**
        - **$ pip install tk**
        - **$ pip install secure-smtplib**
        - **$ pip install regex**
        - **$ pip install os-sys**
        - **$ pip install pillow**
3. Run main.py file
4. A Graphical user interface should appear by now with 3 buttons.
   1. "Goodbye" Button: To close it and finish talking.
   2. "Let's Talk" Button: To be able to give commands by talking.
   3. "Features" Button: That will show you a list of the features and the commands you are able to use.

## User Stories:

### User story #1

#### Title
- Search about somthing in the browser.
#### User Story sentence
- As a user I want to be able to search using my voice so that I dont need to write every thing I want to search for.

#### Feature Tasks
- The user can command the machine to search for him
#### Acceptance Tests

- GIVEN: The user has pressed the "Let's talk" Button.
- WHEN:  The user asks to search and then says what he want to search for.
- THEN:  The application open a google page have the topic that the user want to search for.


### User story #2

#### Title
- Ask about time 
#### User Story sentence
- As a user I want to be able to know the current time by asking the assistant about it.
#### Feature Tasks
- The user can command the assistant to tell him the time.
#### Acceptance Tests
- GIVEN: The user has pressed the "Let's talk" button.

- WHEN: The user asks the assistant for the time.

- THEN: the assistant will say the exact current time.


### User story #3
#### Title
- Search about location.
#### User Story sentence
- As a user I want to search about location of any city so I can know exactlly the correct location whithout opening any app or typing anything
#### Feature Tasks
- The user can command the assistant to display the location on the map.
#### Acceptance Tests
- GIVEN: The user has pressed the "Let's talk" button.

- WHEN: The user asks for the location first then provide the name of the location after that. 

- THEN: The application displays the city location using the browser.



### User story #4
#### Title
- Send email
#### User Story sentence
- As a user I want to be able to send emails faster without having to touch the keyboard and write it by my own.
#### Feature Tasks
- The user can command the assistant to send him an email.
#### Acceptance Tests
- GIVEN: You need to press on the "Let's talk" button.

- WHEN: The user asks to send an email then provide the massage, and then give the name of the person. 

- THEN: The application send the email and says tells the user that the email has been sent successfully.

### User story #5
#### Title
- Ask about Python 
#### User Story sentence
As a user, I want to search for instructions in the Python programming language so that I can get results through voice commands without resorting to traditional methods.
#### Feature Tasks
the user can command the machine to give him nstuctions about some python topics
#### Acceptance Tests
- Give: press the microphone icon

- When: the user asks for instructions in the Python programming language.

- Then: the application will open a website where the instructions that he asked about are presented to him.


### User story #6
#### Title
- Ask about weather
#### User Story sentence
- As a user I would like to know the temperature of the day for a specific city after asking the assistant to search for it.
#### Feature Tasks
- The user can command the assistant to give weather feedback.
#### Acceptance Tests
- Given: The user pressed on the "Let's talk" button.

- When: The user asks for weather and provides the city name after that.

- Then: Dario assistant will be able to say the exact weather temperature of the day.



# WireFrame :

![wireframe](./wirefram.png)



# Domain Modeling


![domain](./dm.jpg)




# trello

[trello](https://trello.com/b/BkLfXBc2/dario-voice-assistant)