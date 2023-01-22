import time
import pyttsx3
import speech_recognition as sr
import datetime
import os
import os.path
import cv2
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
from twilio.rest import Client
import pyjokes
import pyautogui
from pynput.keyboard import Key, Controller
import face_recognition
import numpy as np
import instaloader
import operator
import PyPDF2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi

MY_EMAIL = "yahoo email"
MY_PASSWORD = "password"
MY_TELEGRAM_PASSWORD = "password"

alphabet = {
    "a": "a",
    "apple": "a",
    "hey": "a",
    "be": "b",
    "big": "b",
    "see": "c",
    "clever": "c",
    "dee": "d",
    "d": "d",
    "dog": "d",
    "e": "e",
    "ey": "e",
    "eagle": "e",
    "f": "f",
    "ef": "f",
    "eff": "f",
    "flight": "f",
    "g": "g",
    "gee": "g",
    "girl": "g",
    "h": "h",
    "aitch": "h",
    "haitch": "h",
    "heart": "h",
    "ay": "i",
    "i": "i",
    "ice": "i",
    "j": "j",
    "jay": "j",
    "jy": "j",
    "judge": "j",
    "k": "k",
    "kay": "k",
    "key": "k",
    "l": "l",
    "el": "l",
    "ell": "l",
    "life": "l",
    "m": "m",
    "em": "m",
    "my": "m",
    "n": "n",
    "en": "n",
    "nose": "n",
    "o": "o",
    "oh": "o",
    "orange": "o",
    "p": "p",
    "pee": "p",
    "person": "p",
    "q": "q",
    "cue": "q",
    "kew": "q",
    "kue": "q",
    "que": "q",
    "question": "q",
    "r": "r",
    "ar": "r",
    "or": "r",
    "rose": "r",
    "s": "s",
    "ess": "s",
    "es": "s",
    "sun": "s",
    "t": "t",
    "tee": "t",
    "tea": "t",
    "u": "u",
    "you": "u",
    "use": "u",
    "v": "v",
    "vee": "v",
    "vite": "v",
    "w": "w",
    "double-u": "w",
    "wolf": "w",
    "x": "x",
    "ex": "x",
    "xerox": "x",
    "y": "y",
    "why": "y",
    "wy": "y",
    "wye": "y",
    "yes": "y",
    "z": "z",
    "zed": "z",
    "zee": "z",
    "zebra": "z"
}

Omadbek = {
    "Omadbek_account_sid": "SID",
    "Omadbek_auth_token": "TOKEN",
    "Omadbek_twilio_number": "NUMBER",
    "Omadbek_number": "NUMBER"
}
Mother = {
    "Mother_account_sid": "SID",
    "Mother_auth_token": "TOKEN",
    "Mother_twilio_number": "NUMBER",
    "Mother_number": "NUMBER"
}
Father = {
    "Father_account_sid": "SID",
    "Father_auth_token": "TOKEN",
    "Father_twilio_number": "NUMBER",
    "Father_number": "NUMBER"
}
Abdulla_aka = {
    "Abdulla_aka_account_sid": "SID",
    "Abdulla_aka_auth_token": "TOKEN",
    "Abdulla_aka_twilio_number": "NUMBER",
    "Abdulla_aka_number": "NUMBER"
}
Doniyorbek_ukaxon = {
    "Doniyorbek_ukaxon_account_sid": "SID",
    "Doniyorbek_ukaxon_auth_token": "TOKEN",
    "Doniyorbek_ukaxon_twilio_number": "NUMBER",
    "Doniyorbek_ukaxon_number": "NUMBER"
}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)
keyboard = Controller()


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source, timeout=0, phrase_time_limit=5)
#     try:
#         print("Recognizing...")
#         query1 = r.recognize_google(audio, language='en-in')
#         print(f"User said: {query1}")
#     except Exception as e:
#         speak("Say that again please...")
#         return "none"
#     return query1


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    time = datetime.datetime.now().strftime('%I:%M %p')
    if 0 <= hour <= 12:
        speak(f"Good morning. Its {time}")
    elif 12 < hour < 18:
        speak(f"Good afternoon. Its {time}")
    else:
        speak(f"Good evening. Its {time}")
    speak("I am Jarvis sir, please tell me how can I help you")


def sendEmail(to, content):
    connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=to, msg=content)
    connection.close()


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4c2ea77820ef49b7995bceb18f18253c'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    speak("You should input path for this book")
    path = input("Enter path with name of pdf here: ")
    book = open(f'{path}', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book are {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)


def findEncodings(pictures):
    encodeList = []
    for picture in pictures:
        picture = cv2.cvtColor(picture, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(picture)[0]
        encodeList.append(encode)
    return encodeList


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
        self.condition = None
        self.msg = None
        self.to = None
        self.content = None
        self.message = None
        self.song = None
        self.data = None
        self.cm = None
        self.name = None
        self.to_exit = None
        self.deletion = None
        self.letter = None
        self.word = None
        self.write = None
        self.work = None
        self.choice = None
        self.query = None
        self.quit_camera = None

    def run(self):
        self.TaskExecution()

    def take_command(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            # audio = r.listen(source, timeout=0, phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
        except Exception as e:
            # speak("Say that again please...")
            return "none"
        query = query.lower()
        return query

    def security_checker(self):
        global faceDis
        speak("show your face to camera in case of security")
        path = "Images"
        images = []
        classNames = []
        myList = os.listdir(path)
        # print(myList)
        for cl in myList:
            curImg = cv2.imread(f"{path}/{cl}")
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        # print(classNames)
        encodeListKnown = findEncodings(images)
        print("Encoding Complete")
        cap = cv2.VideoCapture(0)
        is_it_you = False
        while not is_it_you:
            success, img = cap.read()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
            faceDis = 0

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    if faceDis > 0.3:
                        cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (255, 255, 255), 2)
                    else:
                        cv2.putText(img, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1,
                                    (255, 255, 255), 2)
                cv2.imshow("Webcam", img)
                speak("You can say 'q' to quit")
                self.quit_camera = self.take_command()
                if self.quit_camera in alphabet:
                    keyboard.press(alphabet[self.quit_camera])
                else:
                    is_it_you = True
                    cv2.destroyAllWindows()
                if cv2.waitKey(0) & 0xFF == ord("q"):
                    is_it_you = True
            cv2.destroyAllWindows()
            if faceDis > 0.3:
                return True
            else:
                return False

    # def send_sms_message(client, message):
    #     pass

    # if __name__ == "__main__":
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.take_command()
            # if 1:
            # keyboard = Controller()

            # logic building for tasks
            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")
            elif "open chrome" in self.query:
                chpath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chpath)
            elif "close chrome" in self.query:
                speak("okay sir, closing chrome")
                os.system("taskkill /f /im chrome.exe")
            elif "open pycharm" in self.query:
                pypath = "C:\\Program Files\\JetBrains\\PyCharm 2022.1.1\\bin\\pycharm64.exe"
                os.startfile(pypath)
            elif "close pycharm" in self.query:
                speak("okay sir, closing pycharm")
                os.system("taskkill /f /im pycharm64.exe")
            elif "open visual studio" in self.query:
                vpath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
                os.startfile(vpath)
            elif "close visual studio" in self.query:
                speak("okay sir, closing visual studio")
                os.system("taskkill /f /im devenv.exe")
            elif "open visual studio code" in self.query:
                vcpath = "C:\\Users\\01\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(vcpath)
            elif "close visual studio code" in self.query:
                speak("okay sir, closing visual studio code")
                os.system("taskkill /f /im Code.exe")
            elif "open telegram" in self.query:
                tpath = "D:\\Telegram Desktop\\Telegram.exe"
                os.startfile(tpath)
                working_in_telegram = True
                while working_in_telegram:
                    speak("Do you want to use telegram with voice")
                    self.choice = self.take_command()
                    if self.choice == "yes":
                        checked = self.security_checker()
                        if not checked:
                            speak("You are not Mr Omadbek")
                            speak("Sorry, I will close telegram")
                            os.system("taskkill /f /im Telegram.exe")
                        else:
                            speak("Welcome Omadbek")
                            keyboard.type(MY_TELEGRAM_PASSWORD)
                            keyboard.press(Key.enter)
                            is_in_telegram = True
                            while is_in_telegram:
                                speak("What can I do for you in telegram")
                                self.work = self.take_command()
                                if self.work == "type" or self.work == "message":
                                    is_in_write = True
                                    while is_in_write:
                                        speak("Do you want to write with speaking or spelling")
                                        self.write = self.take_command()
                                        if self.write == "speaking":
                                            is_in_saying = True
                                            while is_in_saying:
                                                speak("say you want to write")
                                                self.word = self.take_command()
                                                keyboard.type(self.word)
                                                if self.word == "jarvis quit" or self.word == "quit":
                                                    is_in_write = False
                                                    is_in_saying = False
                                        elif self.write == "spelling":
                                            is_in_letter = True
                                            while is_in_letter:
                                                speak("spell a word that you want to write")
                                                self.letter = self.take_command()
                                                if self.letter == "jarvis quit" or self.letter == "quit":
                                                    is_in_write = False
                                                    is_in_spelling = False
                                                is_in_alphabet = True
                                                while is_in_alphabet:
                                                    if self.letter in alphabet:
                                                        keyboard.press(alphabet[self.letter])
                                                        is_in_alphabet = False
                                                    elif self.letter == "jarvis quit" or self.letter == "quit":
                                                        is_in_alphabet = False
                                                    else:
                                                        speak(f"There is no letter like {self.letter}")
                                                        speak("Please spell correctly")
                                                        is_in_alphabet = False
                                        else:
                                            speak(f"There is no function like {self.write}")
                                            speak("Please try again")
                                    is_in_write = False
                                elif self.work == "delete":
                                    is_in_deletion = True
                                    while is_in_deletion:
                                        speak("Do you want to delete  one character or all ")
                                        self.deletion = self.take_command()
                                        if self.deletion == "letter":
                                            in_one_deletion = True
                                            while in_one_deletion:
                                                self.to_exit = self.take_command()
                                                keyboard.press(Key.backspace)
                                                if self.to_exit == "jarvis quit" or self.to_exit == "quit":
                                                    in_one_deletion = False
                                                    is_in_deletion = False
                                        elif self.deletion == "all":
                                            in_all_deletion = True
                                            while in_all_deletion:
                                                self.to_exit = self.take_command()
                                                with keyboard.pressed(Key.ctrl):
                                                    keyboard.type("a")
                                                keyboard.press(Key.delete)
                                                if self.to_exit == "jarvis quit" or self.to_exit == "quit":
                                                    in_all_deletion = False
                                                    is_in_deletion = False
                                        else:
                                            speak(f"There is no function like {self.deletion}")
                                            speak("Please try again")
                                    is_in_deletion = False
                                elif self.work == "select":
                                    with keyboard.pressed(Key.ctrl):
                                        keyboard.type("a")
                                elif self.work == "enter":
                                    keyboard.press(Key.enter)
                                elif self.work == "nothing":
                                    is_in_telegram = False
                                else:
                                    speak(f"There is no function like {self.work}")
                                    speak("Please try again")
                        working_in_telegram = False
                    elif self.choice == "no":
                        working_in_telegram = False
                    else:
                        speak("You can say only yes or no ")
                        speak("Try again")
            elif "close telegram" in self.query:
                speak("okay sir, closing telegram")
                os.system("taskkill /f /im Telegram.exe")
            elif "open command prompt" in self.query:
                os.system('start cmd')
            elif "close command prompt" in self.query:
                speak("okay sir, closing command prompt")
                os.system("taskkill /f /im cmd.exe")
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow("Webcam", img)
                    k = cv2.waitKey(50)
                    if k == 27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            elif "play music" in self.query:
                music_dir = "D:\Новая папка (2)\Python\Music Player with Python\Musics"
                songs = os.listdir(music_dir)
                song = random.choice(songs)
                os.startfile(os.path.join(music_dir, song))
                # for song in songs:
                #     if song.endswith('.mp3'):
                #         os.startfile(os.path.join(music_dir, song))
            elif "set alarm" in self.query:
                that_hour = int(datetime.datetime.now().hour)
                that_minute = int(datetime.datetime.now().minute)
                if that_hour == 19 and that_minute == 1:
                    music_dir = "D:\Новая папка (2)\Python\Music Player with Python\Musics"
                    songs = os.listdir(music_dir)
                    song = random.choice(songs)
                    os.startfile(os.path.join(music_dir, song))
            elif "change window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
            elif "ip address" in self.query:
                ip = get("https://api.ipify.org").text
                speak(f"your IP address is {ip}")
            elif "calculate" in self.query or "can you calculate" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("Listening....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)

                def get_operator_fn(op):
                    return {
                        "+": operator.add,
                        "-": operator.sub,
                        "x": operator.mul,
                        "divided": operator.__truediv__,
                        "Mod": operator.mod,
                        "mod": operator.mod,
                        "^": operator.xor,
                    }[op]

                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)

                speak(eval_binary_expr(*(my_string.split())))
            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    # print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    # state = geo_data['state']
                    country = geo_data['country']
                    speak(f"sir I am not sure, but I think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, due to network issue I am not able to find where we are.")
                    pass
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                self.name = self.take_command()
                speak("please sir hold the screen for few seconds, I am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{self.name}.jpg")
                speak("I am done sir, the screenshot is saved in our main folder. Now I am ready for next command")
            elif "read book" in self.query:
                pdf_reader()
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif "tell me news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()
            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                speak("what should I search in wikipedia")
                self.data = self.take_command()
                data = self.data.replace("wikipedia", "")
                results = wikipedia.summary(data, sentences=2)
                speak("according to wikipedia")
                speak(results)
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the username correctly")
                name = input("Enter username here: ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account")
                self.condition = self.take_command()
                if "yes" in self.condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("I am done sir, profile picture is saved in our main folder. Now I am ready for next command")
                else:
                    pass
            elif "open youtube in web" in self.query:
                webbrowser.open("www.youtube.com")
            elif "open facebook in web" in self.query:
                webbrowser.open("www.facebook.com")
            elif "open telegram in web" in self.query:
                webbrowser.open("www.telegram.com")
            elif "open stackoverflow in web" in self.query:
                webbrowser.open("www.stackoverflow.com")
            elif "open google" in self.query:
                speak("sir what should I search on google")
                self.cm = self.take_command()
                webbrowser.open(f"{self.cm}")
            elif "play song on youtube" in self.query:
                speak("what song do you want to listen")
                self.song = self.take_command()
                kit.playonyt(f"{self.song}")
            elif "send whatsapp message" in self.query:
                speak("who do you want to send")
                receiver = input("Input number of receiver: ")
                speak("what is message")
                self.message = self.take_command()
                kit.sendwhatmsg(f"+{receiver}", f"{self.message}", 2, 25)
            elif "send email" in self.query:
                try:
                    speak("what should I say")
                    self.content = self.take_command()
                    to = "omadbekinhastudent32@yahoo.com"
                    sendEmail(to, self.content)
                    speak("Email has been sent to omadbek")
                except Exception as e:
                    print(e)
                    speak("sorry sir, i am not able to sent this mail to omadbek")
            elif "send message" in self.query:
                try:
                    is_receiver = False
                    while not is_receiver:
                        speak("who do you want to send")
                        self.to = self.take_command()
                        if self.to == "myself":
                            client = Client(Omadbek["Omadbek_account_sid"], Omadbek["Omadbek_auth_token"])
                            speak("say message you want to send")
                            self.msg = self.take_command()
                            message = client.messages.create(body=self.msg, from_=Omadbek["Omadbek_twilio_number"],
                                                             to=Omadbek["Omadbek_number"])
                            speak(f"Message has been successfully sent to {self.to} with {message.status} status code.")
                            is_receiver = True
                        elif self.to == "mother":
                            client = Client(Mother["Mother_account_sid"], Mother["Mother_auth_token"])
                            speak("say message you want to send")
                            self.msg = self.take_command()
                            message = client.messages.create(body=self.msg, from_=Mother["Mother_twilio_number"],
                                                             to=Mother["Mother_number"])
                            speak(f"Message has been successfully sent to {self.to} with {message.status} status code.")
                            is_receiver = True
                        elif self.to == "father":
                            client = Client(Father["Father_account_sid"], Father["Father_auth_token"])
                            speak("say message you want to send")
                            self.msg = self.take_command()
                            message = client.messages.create(body=self.msg, from_=Father["Father_twilio_number"],
                                                             to=Father["Father_number"])
                            speak(f"Message has been successfully sent to {self.to} with {message.status} status code.")
                            is_receiver = True
                        elif self.to == "My bro":
                            client = Client(Abdulla_aka["Abdulla_aka_account_sid"],
                                            Abdulla_aka["Abdulla_aka_auth_token"])
                            speak("say message you want to send")
                            self.msg = self.take_command()
                            message = client.messages.create(body=self.msg,
                                                             from_=Abdulla_aka["Abdulla_aka_twilio_number"],
                                                             to=Abdulla_aka["Abdulla_aka_number"])
                            speak(f"Message has been successfully sent to {self.to} with {message.status} status code.")
                            is_receiver = True
                        elif self.to == "doniyor":
                            client = Client(Doniyorbek_ukaxon["Doniyorbek_ukaxon_account_sid"],
                                            Doniyorbek_ukaxon["Doniyorbek_auth_token"])
                            speak("say message you want to send")
                            self.msg = self.take_command()
                            message = client.messages.create(body=self.msg,
                                                             from_=Doniyorbek_ukaxon["Doniyorbek_ukaxon_twilio_number"],
                                                             to=Doniyorbek_ukaxon["Doniyorbek_number"])
                            speak(f"Message has been successfully sent to {self.to} with {message.status} status code.")
                            is_receiver = True
                        elif self.to == "quit":
                            speak("thanks for using messanger")
                            is_receiver = True
                        else:
                            speak(f"there is no contact like {self.to}")
                            speak("please repeat name of receiver")
                    # send_sms_messanger(client, message)
                except Exception as e:
                    print(e)
                    speak(f"sorry sir, i am not able to sent message")
            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir please tell me you want to hide this folder or make it visible for everyone")
                self.condition = self.take_command()
                if "hide" in self.condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all the files in this folder are now hidden")
                elif "visible" in self.condition:
                    os.system("attrib -h /s /d")
                    speak(
                        "sir, all the files in this folder are now visible to everyone, i wish you are taking this decision in your own peace")
                elif "leave it" in self.condition or "leave for now" in self.condition:
                    speak("Ok sir")
            elif "hello" in self.query or "hey" in self.query:
                speak("hello sir, may i help you with something.")
            elif "how are you" in self.query:
                speak("i am fine sir, what about you.")
            elif "thank you" in self.query:
                speak("It's my pleasure sir")
            elif "no thanks" in self.query:
                speak("thanks for using me sir, have a good day.")
                sys.exit()

            speak("sir, do you have any other work ")


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("ironman.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("initialize.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
