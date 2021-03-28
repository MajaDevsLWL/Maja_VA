# -*- coding: utf-8 -*-
import pyttsx3  # pip install pyttsx3
from datetime import datetime
import requests # pip install requests
from bs4 import BeautifulSoup # pip install beautifulsoup4
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
import cv2 # pip install opencv-python
from  requests import get
import pywhatkit as kit # pip install pywhatkit
import sys
import pyautogui #pip install PyAutoGUI
import time
import instaloader # pip install instaloader
import itertools
import threading
import sys
import winsound

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 145)
wikipedia.set_lang('pl')
year = int(datetime.now().year)
month = int(datetime.now().month)
day = int(datetime.now().day)

if month == 1: month = "Styczeń"
elif month == 2: month = "Luty"
elif month == 3: month = "Marzec"
elif month == 4: month = "Kwiecień"
elif month == 5: month = "Maj"
elif month == 6: month = "Czerwiec"
elif month == 7: month = "Lipiec"
elif month == 8: month = "Sierpień"
elif month == 9: month = "Wrzesień"
elif month == 10: month = "Październik"
elif month == 11: month = "Listopad"
elif month == 12: month = "Grudzień"

today = datetime.today().weekday()

if today == 0: todaydzień = "Poniedziałek"
elif today == 1: todaydzień = "Wtorek"
elif today == 2: todaydzień = "Środa"
elif today == 3: todaydzień = "Czwartek"
elif today == 4: todaydzień = "Piątek"
elif today == 5: todaydzień = "Sobota"
elif today == 6: todaydzień = "Niedziela"

strTime = datetime.now().strftime("%H:%M")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Witaj jestem Maja, twój wirtualny asystent.")

def wishme():
    speak("Witaj ponownie.")
    time = datetime.now().strftime("%H:%M")
    speak(f"Jest {todaydzień} {strTime}")
    speak(f"Aktualna data to {day}/{month}/{year}")
    hour = datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Dzień dobry.")
    elif hour >= 12 and hour <18:
        speak("Miłego popołudnia.")
    elif hour >= 18 and hour <24:
        speak("Dobry Wieczór.")
    else:
        speak("Dobrej nocy.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nasłuchuje...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Rozpoznawanie...")
        query = r.recognize_google(audio, language='pl-PL')
        print(f"Użytkownik powiedział: {query}\n")

    except Exception as e:
        print(e)
        print("Powtórz proszę.")
        return "None"
    return query

def sendEmail(to, content):
    email = input("Podaj swojego maila: ")
    password = input("Podaj swoje hasło do maila: ")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "nie dziękuję" in query or "papa" in query or "do widzenia" in query or "wyłącz się" in query:
            speak("Dziękuję za skorzystanie z mojej pomocy, do zobaczenia niebawem.")
            sys.exit()

        elif "wikipedia" in query:
            speak("Szukam w wikipedi...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Przechodzę do wikipedii.")
            print(results)
            speak(results)
            except:
                print("Nie udało mi się znależć żadnych informacji.")
                speak("Nie udało mi się znależć żadnych informacji.")

        elif "definicja słowa" in query or "kim jest" in query:
            url = f"https://www.google.com/search?q={query}"  
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            defPer = data.find("div",class_="BNeawe").text
            print(defPer)
            speak(defPer)
            except:
                print("Nie udało mi się znależć żadnych informacji.")
                speak("Nie udało mi się znależć żadnych informacji.")

        elif "otwórz stronę" in query:
            speak("Jaką stronę otworzyć?")
            domena = takeCommand().lower()
            domena = query.replace("otwórz stronę",'')
            domena = domena.replace(' .','.')
            domena = domena.replace('. ','.')
            domena = domena.replace(' ','')
            webbrowser.open(f"https://{domena}")

        elif "otwórz aplikację" in query:
            usernameWindows = input("Podaj nazwę użytkownika Windows: ")
            speak("Jaką aplikację otworzyć?")
            app = takeCommand().lower()
            app = query.replace('otwórz aplikację','')
            if "visual studio code" in app:
                os.startfile(f"C:\\Users\\{usernameWindows}\\AppData\\Local\\Programs\\Microsoft VS Code")
            elif "discord" in query:
                os.startfile(f"C:\\Users\\{usernameWindows}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk")
            else:
                speak("Nie znam tej aplikacji.")

        elif "ustaw trasę" in query or "ustal trasę" in query or "trasa" in query or "znajdź trasę" in query:
            speak("Jaki punkt początkowy?")
            start = takeCommand().lower()
            speak("Jaki punkt docelowy?")
            end = takeCommand().lower()
            webbrowser.open(f"https://www.google.com/maps/dir/{start}/{end}"

        elif "dzień tygodnia" in query or "co dzisiaj jest" in query or "co jest dzisiaj" in query or "który dzisiaj" in query or "jaki dzisiaj" in query:
            speak(f"Dzisiaj jest {todaydzień}")

        elif "gdzie jest" in query:
            where = query.replace('gdzie jest','')
            webbrowser.open(f"https://www.google.com/maps/search/{where}"

        elif "gdzie jestem" in query or "moja lokalizacja" in query:
            webbrowser.open("https://www.google.com/maps/search/Where+am+I+?/")

        elif "puść na youtube" in query or "włącz na youtube" in query or "youtube" in query:
            youtube = query.replace("puść na youtube","").lower()
            youtube = query.replace("włącz na youtube","").lower()
            youtube = query.replace("youtube","").lower()
            kit.playonyt(youtube)

        elif "wyszukaj w google" in query or "szukaj w google" in query or "znajdź w google" in query or "poszukaj w google" in query or "wygoogluj" in query or "wygooglaj" in query:
            google = query.replace("wyszukaj w google", "").lower()
            google = query.replace("szukaj w google", "").lower()
            google = query.replace("znajdź w google", "").lower()
            google = query.replace("poszukaj w google", "").lower()
            google = query.replace("wygoogluj", "").lower()
            google = query.replace("wygooglaj", "").lower()
            kit.search(google)

        elif "stack overflow" in query or "stack" in query or "overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "facebook" in query or "fejs" in query:
            webbrowser.open("www.facebook.pl")

        elif "czas" in query or "godzina" in query or "która godzina" in query or "jaka godzina" in query or "która" in query:
            speak(f"Jest{strTime}")

        elif "wyślij email" in query:
            try:
                email2 = ("Pod jaki adres email wysłać?")
                speak("Co chcesz napisać?")
                content = takeCommand()
                to = email2
                sendEmail(to, content)
                speak("Email został wysłany")
            except Exception as e:
                print(e)

        elif "otwórz notatnik" in query or "notatnik" in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif "zamknij notanik" in query:
            os.system("taskkill /f /im notepad.exe")

        elif "otwórz wiersz poleceń" in query or "otwórz cmd" in query:
            cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)

        elif "zamknij cmd" in query or "zamknij wiersz poleceń" in query:
            os.system("taskkill /f /im cmd.exe")

        elif "kamera" in query:
            print("Uruchamiam...")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k ==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "ip" in query:
            ip = get('https://api.ipify.org').text
            print(f"Twoje IP to {ip}")
            speak(ip)

        elif "zamknij system" in query or "wyłącz system" in query or "zamknij komputer" in query or "wyłącz komputer" in query or "zamknij laptopa" in query or "wyłącz laptopa" in query or "shutdown" in query:
            os.system("shutdown /s /t 5")

        elif "zmień okno" in query or "alt tab" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "screenshot" in query or "zrzut ekranu" in query or "eses" in query or "ss" in query:
            print("Wykonuję zrzut ekarnu.")
            img = pyautogui.screenshot()
            img.save("Maja.png")

        elif "profil instagram" in query or "insta profil" in query:
            print("Proszę wpisać poprawną nazwę użytkownika instagrama.")
            name = input("Wpisz nazwę użytkownika tutaj: ")
            webbrowser.open(f"www.instagram.com/{name}")
            print("Czy chcesz pobrać zdjęcie profilowe tego użytkownika?")
            condition = takeCommand().lower()
            if "tak" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                print(f"Gotowe zdjęcie profilowe użytkownika {name} zostało pobrane")
            else:
                pass

        elif "przygłoś" in query or "podgłoś" in query or "podgłośnij" in query or "głośniej" in query:
            pyautogui.press("volumeup")

        elif "przycisz" in query or "ścisz" in query or "ciszej" in query:
            pyautogui.press("volumedown")

        elif "wycisz" in query or "wyłącz dźwięk" in query or "mute" in query or "zmutuj" in query:
            pyautogui.press("volumemute")

        elif "temperatura" in query or "ile stopni" in query:
            print("W jakim mieście mam sprawdzić temperaturę?")
            miasto = takeCommand().lower()
            webbrowser.open(f"www.google.com/search?q=temperatura+{miasto}")

        elif "alarm" in query or "budzik" in query:
            print("Na którą godzinę nastawić alarm?")
            speak(f"Teraz jest{strTime}.")
            print("Wpisz godzinę alarmu.")
            alarm = float(input("Godzina alarmu: (eg. 21.37, 04.20 \n"))
            speak(f"Alarm Ustawiony na godzinę {alarm}.")
            time.sleep(alarm*3600)
            sound = "alarm_sound.wav"
            repitions = 5

            while True:
                if hour == strTime and minute == strTime:
                    for i in range(repitions):
                        winsound.PlaySound(sound, winsound.SND_ASYNC | winsound.SND_ALIAS)
                        time.sleep(5)
                        winsound.PlaySound(None, winsound.SND_ASYNC)
                    break

        speak("Coś jeszcze?")
        print("Błędy? Pisz na discordzie: https://discord.gg/EPx9CQBxyF")
