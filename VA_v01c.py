import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

wikipedia.set_lang('pl')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak("Witaj jestm Maja, Twój wirtualny asystent")

def time():
    Time = datetime.datetime.now().strftime("%H:%M")
    speak(Time)
#time()

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
#date()

def wishme():
    speak("Witaj ponownie")
    speak("Teraz jest")
    time()
    speak("Aktualna data to")
    date()
    hour = datetime.datetime.now().hour
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
        speak("Powtórz proszę")
        print("Powtórz proszę")
        return "None"
    return query 
#takeCommand()


if __name__ == "__main__":
    wishme()
    while True:        
        query = takeCommand().lower()


        if 'wikipedia' in query:
            speak("Szukam w wikipedi...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Przechodzę do wikipedii")
            print(results)
            speak(results)
            
        elif 'otwórz youtube' in query:
            webbrowser.open("youtube.com")
            speak("Otwieram Youtube")

        elif 'otwórz google' in query:
            webbrowser.open("google.com")
            speak("Otwieram wyszukiwarkę google")

        elif 'otwórz stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            speak("Otwieram stackoverflow")

        elif 'czas' in query:
            sTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Teraz jest {sTime} sekund")
        
        elif 'otwórz Visual Studio Code' in query:
            codepath = "C:\\Users\\Dawid\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak("Otwieram Visual Studio Code miłego kodowania")






        '''elif 'odtwórz muzukę' in query:
            music_dir = 'tutaj wklej ściężkę do folderu z muzyką'
            songs = os.listdir(music_dir)
            print(songs)
            speak("Odpalam muzyczkę")
            os.startfile(os.path..join(music_dir, songs[0]))
            # FIXME: Opcja do dopasowania indywidalnie w zależności od ścieżki do pliów audio
        '''
