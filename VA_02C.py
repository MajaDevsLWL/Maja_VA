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

done = False

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
speak("Witaj jestem Maja, twój wirtualny asystent")

def wishme():
    speak("Witaj ponownie")
    time = datetime.now().strftime("%H:%M")
    speak(f"Jest {todaydzień} {strTime}")
    speak(f"Aktualna data to {day}/{month}/{year}")
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

'''def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rSłucham ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

t = threading.Thread(target=animate)
t.start()'''

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
        print("Powtórz proszę")
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
            speak("Dziękuję za skorzystanie z mojej pomocy, do zobaczenia niebawem!")            
            sys.exit()
        
        elif "wikipedia" in query:
            speak("Szukam w wikipedi...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Przechodzę do wikipedii")
            print(results)
            speak(results)

        elif "definicja słowa" in query:
            try:
                url = f"https://www.google.com/search?q={query}"    
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                definicja = data.find("div",class_="BNeawe").text
                print(definicja)
                speak(definicja)
            except Exception as e:
                print("Nie udało mi się znależć żadnych informacji.")
                speak("Nie udało mi się znależć żadnych informacji.")

        elif "kim jest" in query:
            try:
                url = f"https://www.google.com/search?q={query}"    
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                osoba = data.find("div",class_="BNeawe").text
                print(osoba)
                speak(osoba)
            except:
                speak("Nie udało mi się znależć żadnych informacji o tej osobie *Smutna żaba*")

        elif 'otwórz stronę' in query:
            speak("Jaką stronę otworzyć?")
            domena = takeCommand().lower()
            domena = query.replace("otwórz stronę",'')
            domena = domena.replace(' .','.')
            domena = domena.replace('. ','.')
            domena = domena.replace(' ','')
            webbrowser.open("https://"+domena)
            speak(f"Otwieram stronę {domena}")

        elif 'otwórz aplikację' in query:
            usernameWindows = input("Podaj nazwę użytkownika Windows: ")
            print("Jeśli używasz Linux to znam twój bół, pozdrawiam L1KE5358 :D")
            speak("Jaką aplikację otworzyć?")
            app = takeCommand().lower()
            app = query.replace('otwórz aplikację','')
            if ' visual studio code' in app:
                os.startfile(f'C:\\Users\\{usernameWindows}\\AppData\\Local\\Programs\\Microsoft VS Code')
                speak("Otwieram visual studio code. Miłego kodowania :D")
            elif 'discord' in query:
                os.startfile(f'C:\\Users\\{usernameWindows}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk')
                speak("Otwieram discorda")
            else:
                speak("Nie znam tej aplikacji. Może dlatego że jestem tylko głupim botem i moja egzystencja nie ma znaczenia innego niż robienie tego co mi rozkażesz...")

        elif "ustaw trasę" in query or "ustal trasę" in query or "trasa" in query or "znajdź trasę" in query:
            speak("Jaki punkt początkowy?")
            poczatek = takeCommand().lower()
            speak("Jaki punkt docelowy?")
            koniec = takeCommand().lower()
            webbrowser.open("https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec))
            speak("Oto najszybsza trasa do miasta {}. Czy chcesz zmienić trasę?".format(koniec))

            odp = takeCommand().lower()
            if odp == 'zmień punkt początkowy':
                speak("Okej, jaki będzie punkt początkowy?")
                print("Nie ułatwiasz mi roboty!")
                poczatek = takeCommand().lower()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)

            elif odp == 'zmień punkt docelowy':
                speak("Okej, jaki będzie punkt docelowy?")
                print("Nie ułatwiasz mi roboty!")
                koniec = takeCommand().lower()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)

            elif odp == 'zmień oba punkty':
                speak("Okej, jaki będzie punkt początkowy?")
                print("Nie ułatwiasz mi roboty!")
                poczatek = takeCommand().lower()
                speak("A jaki punkt docelowy?")
                koniec = takeCommand().lower()
                url = "https://www.google.com/maps/dir/{}/{}".format(poczatek,koniec)
                webbrowser.open(url)

            elif odp == 'nie zmieniaj':
                speak("Oki")

        elif 'dzień tygodnia' in query or 'co dzisiaj jest' in query or 'co jest dzisiaj' in query or 'który dzisiaj' in query or 'jaki dzisiaj' in query:
            speak("Dzisiaj jest "+todaydzień)

        elif "gdzie jest" in query:
            where = query.replace('gdzie jest','')
            url = "https://www.google.com/maps/search/{}".format(where)
            speak("Znalazłam {} na mapach google".format(where))
            webbrowser.open(url)
            speak("Zobacz")

        elif 'gdzie jestem' in query or 'moja lokalizacja' in query:
            webbrowser.open("https://www.google.com/maps/search/Where+am+I+?/")
            speak("Zapewne jesteś w tym mieście")
            
        elif 'puść na youtube' in query or "włącz na youtube" in query or 'youtube' in query:
            yt = query.replace("Puść na youtube","").lower()
            yt = query.replace("Włącz na youtube","").lower()
            kit.playonyt(f"{yt}")

        elif 'wyszukaj w google' in query or "szukaj w google" in query or 'znajdź w google' in query or 'poszukaj w google' in query or 'wygoogluj' in query or 'wygooglaj' in query:
            cm = query.replace("wyszukaj w google", "").lower()
            cm = query.replace("szukaj w google", "").lower()
            cm = query.replace("znajdź w google", "").lower()
            cm = query.replace("poszukaj w google", "").lower()
            kit.search(f"{cm}")
            speak(f"Oto co znalazłam w google dla frazy {cm}")

        elif 'stack overflow' in query or 'stack' in query or 'overflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak("Otwieram stackoverflow")
        
        elif 'facebook' in query or 'fejs' in query:
            webbrowser.open("www.facebook.pl")
            speak("Twarzoksiążka została otworzona")

        elif 'czas' in query or "godzina" in query or "która godzina" in query or "jaka godzina" in query or "która" in query:
            speak(f"Jest{strTime}")
        
        elif 'otwórz visual studio code' in query:
            usernameWindows = input("Podaj nazwę użytkownika Windows: ")
            print("Jeśli używasz Linux to znam twój bół, pozdrawiam L1KE5358 :D")
            codepath = f"C:\\Users\\{usernameWindows}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Otwieram Visual Studio Code. Miłego kodowania :D")
        
        elif 'wyślij email' in query:
            try:
                email2 = ("Pod jaki adres email wysłać?")
                speak("Co chcesz napisać?")
                content = takeCommand()
                to = email2
                sendEmail(to, content)
                speak("Email został wysłany")
            except Exception as e:
                print(e)
                speak("Przepraszam ale nie mogę wysłać maila D:")

        elif 'otwórz notatnik' in query:
            speak("Otwieram notatnik")
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'zamknij notanik' in query:
            speak("Zamykam notanik")
            os.system("taskkill /f /im notepad.exe")
        
        elif 'otwórz wiersz poleceń' in query:
            speak("Otwieram wiersz poleceń")
            cmdpath = "C:\\WINDOWS\\system32\\cmd.exe"
            os.startfile(cmdpath)
        
        elif 'kamera' in query:
            speak("Uruchamiam")
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

        elif "zamknij system" in query:
            os.system("shutdown /s /t 5")
        
        elif "zmień okno" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "screenshot" in query or "zrzut ekranu" in query:
            speak("Jak ma się nazywać plik?")
            name = takeCommand().lower()
            speak("Poczekaj chwilę wykonuję zrzut ekranu")
            print("Wykonuję zrzut ekarnu")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("zrzut ekranu wykonany")
        
        elif "profil instagram" in query or "insta profil" in query:
            speak("Proszę wpisać poprawną nazwę użytkownika instagrama")
            name = input("Wpisz nazwę użytkownika tutaj: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Oto profil użytkownika {name} na instagramie")
            time.sleep(3)
            speak("Czy chcesz pobrać zdjęcie profilowe tego użytkownika?")
            condition = takeCommand().lower()
            if "tak" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak(f"Gotowe zdjęcie profilowe użytkownika {name} zostało pobrane")
            else:
                pass
                
                
        elif "przygłoś" in query or "podgłoś" in query or "podgłośnij" in query or "głośniej" in query:
            pyautogui.press("volumeup")
            
        elif "przycisz" in query or "ścisz" in query or "ciszej" in query:
            pyautogui.press("volumedown")
            
        elif "wycisz" in query or "wyłącz dźwięk" in query:
            pyautogui.press("volumemute")
            
        elif "temperatura" in query:
            speak("W jakim mieście mam sprawdzić temperaturę?")
            miasto = takeCommand().lower()
            search = f"temperatura+{miasto}"
            webbrowser.open(f"www.google.com/search?q={search}")             
            #speak(f"{search} wynosi {temp}")  
        # TODO 

        '''elif "alarm" in query or "budzik" in query: # TODO w fazie testów
            speak("Na którą godzinę nastawić alarm?")
            speak(f"teraz jest{strTime}")
            speak("Wpisz godzinę alarmu")
            hour = int(input("Godzina alarmu: "))
            speak("wpisz minuty alarmu")
            minute = int(input("Minuty alarmu: "))
            speak(f"Alarm Ustawiony na godzinę {hour}:{minute}")
            sound = "alarm_sound.wav" 
            repitions = 5


            
            while True:
                if hour == strTime and minute == strTime:
                    for i in range(repitions):
                        winsound.PlaySound(sound, winsound.SND_ASYNC | winsound.SND_ALIAS)
                        time.sleep(5)
                        winsound.PlaySound(None, winsound.SND_ASYNC)
                    break

        elif "alarm" in query or "budzik" in query:
            print("Na którą godzinę nastawić alarm?")
            speak(f"Teraz jest{strTime}.")
            print("Wpisz godzinę alarmu.")
            alarm = float(input("Godzina alarmu: (eg. 21.37, 04.20 \n"))
            speak(f"Alarm Ustawiony na godzinę {alarm}.")
            time.sleep(alarm*3641.)
            sound = "alarm_sound.wav"
            repitions = 5

            while True:
                if hour == strTime and minute == strTime:
                    for i in range(repitions):
                        winsound.PlaySound(sound, winsound.SND_ASYNC | winsound.SND_ALIAS)
                        time.sleep(5)
                        winsound.PlaySound(None, winsound.SND_ASYNC)
                    break                                   
        '''
                    







            
       
        
        speak("Coś jeszcze?")
        print("Błędy? Pisz na discordzie: https://discord.gg/EPx9CQBxyF")