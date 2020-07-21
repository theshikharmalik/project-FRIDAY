import wikipedia
import webbrowser
import random
import os
import datetime
import time
import subprocess
import speakandrecognizefunctions as SRF
USER = "shikhar"


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        SRF.speak("good morning! " + USER)
    elif hour >= 12 and hour < 18:
        SRF.speak("good aftenoon! " + USER)
    else:
        SRF.speak("good evening! " + USER)


def note(text):

    date = datetime.datetime.now()
    filename = str(date).replace(":", "-")+"-note.txt"

    try:
        os.mkdir("notes_folder")
    except FileExistsError:
        pass

    completename = os.path.join("notes_folder", filename)
    with open(completename, "w") as f:
        f.write(text)
        f.close()

    subprocess.Popen(["notepad.exe", completename])


def wikipediasearch(query):
    try:
        #SRF.speak("What do you want to search for ?")
        #wikiquery = SRF.takecommand()
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("on", "")
        wikiquery = query.replace("for", "")
        SRF.speak('searching wikipedia.....')
        print("this is the wikipedia query :" + wikiquery)
        results = wikipedia.summary(wikiquery, sentences=2)
        time.sleep(2)
        SRF.speak("according to wikipedia")
        SRF.speak(results)
    except:
        SRF.speak("i did not get that !!")


'''  
        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser. get(chrome_path). open_new_tab("youtube.com")

        elif "study time" in query:
            speak("starting lofi hiphop")
            webbrowser. get(chrome_path). open_new_tab(
                "https://www.youtube.com/watch?v=hHW1oY26kxQ")

        elif "github" in query:
            speak("opening github")
            webbrowser. get(chrome_path). open_new_tab("https://github.com/")

        elif "play music" in query:
            speak("playing music ")
            music_dir = "C:\\Users\\shikh\\Desktop\\music"
            songs = os.listdir(music_dir)

            num = random.randint(0, len(songs))
            os.startfile(os.path.join(music_dir, songs[num-1]))

        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%I%p")
            speak(f"It's  {strtime} ")

        elif "open code" in query:
            speak("opening visual studio code")
            codepath = "C:\\Users\\shikh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open c plus plus" in query:
            speak("opening codeblocks")
            codepath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codepath)

        elif "open word" in query:
            speak("opening microsoft word")
            codepath = "C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codepath)

        elif "google" in query:
            query = query.replace("google search", "")
            speak('searching on google.....')
            url = "https://www.google.co.in/search?q=" + (str(query)) + "&oq="+(str(
                query))+"&gs_l=serp.12..0i71l8.0.0.0.6391.0.0.0.0.0.0.0.0..0.0....0...1c..64.serp..0.0.0.UiQhpfaBsuU"
            webbrowser.open_new_tab(url)
'''
