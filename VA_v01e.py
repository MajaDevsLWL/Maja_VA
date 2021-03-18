import pyttsx3  # pip install pyttsx3
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia
import webbrowser
import os
import smtplib
import cv2
from  requests import get
import pywhatkit as kit # pip install pywhatkit
import sys


engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[3].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 145)

wikipedia.set_lang('pl')

year = int(datetime.now().year)
month = int(datetime.now().month)
day = int(datetime.now().day)

if month == 1: month = "styczeń"
elif month == 2: month = "luty"
elif month == 3: month = "marzec"
elif month == 3: month = "kwiecień"
elif month == 3: month = "maj"
elif month == 3: month = "czerwiec"
elif month == 3: month = "lipiec"
elif month == 3: month = "sierpień"
elif month == 3: month = "wrzesień"
elif month == 3: month = "październik"
elif month == 3: month = "listopad"
elif month == 3: month = "grudzień"

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
#speak("Witaj jestm Maja, Twój wirtualny asystent")

def wishme():
    speak("Witaj ponownie")
    time = datetime.now().strftime("%H:%M")
    speak(f"Jest {todaydzień} {strTime}")
    speak(f"Aktualna data to {year} rok, {day} {month}")
    #date()
    hour = datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Dzień dobry")
    elif hour >= 12 and hour <18:
        speak("Miłego popołudnia")
    elif hour >= 18 and hour <24:
        speak("Dobry Wieczór")
    else:
        speak("Dobrej nocy")
    
    speak("Maja jest do Twojej dyspozycji, proszę powiedz w czym mogę pomóc")
#wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Nasłuchuje....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Rozpoznawanie...")
        query = r.recognize_google(audio, language='pl-PL')
        print(f"Użytkownik powiedział: {query}\n")
    

    except Exception as e:
        print(e)
        #speak("Powtórz proszę")
        print("Powtórz proszę")
        return "None"
    return query 
#takeCommand()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "your-password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:        
        query = takeCommand().lower()

        if 'nie dziękuję' in query or "papa" in query or "do widzenia" in query or "wyłącz się" in query:
            speak("Dziękuję za skorzystanie z mojej pomocy, do zobaczenia niebawem")
            sys.exit()
        
        elif 'wikipedia' in query:
            speak("Szukam w wikipedi...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Przechodzę do wikipedii")
            print(results)
            speak(results)

        elif 'definicja słowa' in query:
            url = f"https://www.google.com/search?q={query}"    
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            definicja = data.find("div",class_="BNeawe").text
            print(definicja)
            speak(definicja)

        elif 'kim jest' in query:
            try:
                url = f"https://www.google.com/search?q={query}"    
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                osoba = data.find("div",class_="BNeawe").text
                print(osoba)
                speak(osoba)
            except:
                speak("Nie udało mi się nzlaeźć żadnych informacji o tej osobie")

        elif 'otwórz stronę' in query: # np otwórz stronę allegro.pl
            domena = query.replace("otwórz stronę",'')
            domena = domena.replace(' .','.')
            domena = domena.replace('. ','.')
            domena = domena.replace(' ','')
            webbrowser.open("http://"+domena)
            speak(f"otwieram stronę {domena}")

        elif 'otwórz aplikację' in query:
            app = query.replace('otwórz aplikację','')
            if ' visual studio code' in app:
                os.startfile(r'C:\Users\Nazwa twojego użytkownika\AppData\Local\Programs\Microsoft VS Code')
                speak("otwieram visual studio code. miłego kodowania")
            elif 'discord' in query:
                os.startfile(r'C:\Users\Nazwa twojego użytkownika\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk')
                speak("otwieram discorda")
            else:
                speak("nie znam tej aplikacji")

        elif "ustaw trasę" in query or "ustal trasę" in query or "trasa" in query or "znajdź trasę" in query:
            speak("Jaki punkt początkowy?")
            poczatek = takecom()
            speak("Jaki punkt docelowy?")
            koniec = takecom()
            webbrowser.open("https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec))
            speak("Oto najszybsza trasa do miasta {}. Czy chcesz zmienić trasę?".format(koniec))

            odp = takecom()
            if odp == 'zmień punkt początkowy':
                speak("okej, jaki będzie punkt początkowy?")
                poczatek = takecom()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)

            elif odp == 'zmień punkt docelowy':
                speak("okej, jaki będzie punkt docelowy?")
                koniec = takecom()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)
            elif odp == 'zmień oba punkty':
                speak("okej, jaki będzie punkt początkowy?")
                poczatek = takecom()
                speak("a jaki punkt docelowy?")
                koniec = takecom()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)
            elif odp == 'nie zmieniaj':
                speak("oki")

        elif 'dzień tygodnia' in query or 'co dzisiaj jest' in query or 'co jest dzisiaj' in query:
            speak("dzisiaj jest "+todaydzień)

        elif "gdzie jest" in query:
            where = query.replace('gdzie jest','')
            url = "https://www.google.com/maps/search/{}".format(where)
            speak("Znalazłam {} na mapach google".format(where))
            webbrowser.open(url)
            speak("zobacz")

        elif 'gdzie jestem' in query or 'moja lokalizacja' in query:
            webbrowser.open("https://www.google.com/maps/search/Where+am+I+?/")
            speak("Zapewne jesteś w tym mieście na podstawie map google")
            
        elif 'puść na youtube' in query or "włącz na youtube" in query:
            yt = query.replace("puść na youtube","").lower()
            yt = query.replace("włącz na youtube","").lower()
            kit.playonyt(f"{yt}")
            #webbrowser.open("youtube.com")
            #speak("Otwieram Youtube")

        elif 'wyszukaj w google' in query or "szukaj w google" in query or 'znajdź w google' in query or 'poszukaj w google' in query:
            cm = query.replace("wyszukaj w google", "").lower()
            cm = query.replace("szukaj w google", "").lower()
            cm = query.replace("znajdź w google", "").lower()
            cm = query.replace("poszukaj w google", "").lower()
            kit.search(f"{cm}")
            speak(f"Oto co znalazłam w google dla frazy {cm}")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Otwieram stackoverflow")
        
        elif 'facebook' in query:
            webbrowser.open("facebook.pl")
            speak("Twarzoksiążka została otwara")

        elif 'czas' in query or "godzina" in query:
            speak(f"jest{strTime}")
        
        elif 'otwórz Visual Studio Code' in query:
            codepath = "C:\\Users\\Dawid\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Otwieram Visual Studio Code miłego kodowania")
        
        elif 'wyślij email' in query:
            try:
                speak("Co chcesz napisać")
                content = takeCommand()
                to = "twójEmail@gmail.com"
                sendEmail(to, content)
                speak("email został wysłąny")
            except Exception as e:
                print(e)
                speak("Przepraszam ale nie mogę wysłać maila")

        elif 'otwórz notatnik' in query:
            speak("Otwieram notatnik")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        
        elif 'otwórz wiersz poleceń' in query:
            speak("Otwieram wiersz poleceń")
            cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)
        
        elif 'kamera' in query:
            speak("uruchamiam")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k ==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'ip' in query:
            ip = get('https://api.ipify.org').text
            print(f"Twoje IP to {ip}")
            speak(f"Twoje IP to {ip}")
        
        speak("coś jeszcze?")
