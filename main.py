import fridayfunctions as FF
import speakandrecognizefunctions as SRF


WAKE_WORD = "friday"
USER = "shikhar"

# GREETINGS ON THE START
SRF.speak("Hello !! I am FRIDAY !!")
FF.wishme()
#speak("if u need me to do anything just ask !")

while True:

    # Constantly hearing in the background
    text = SRF.takecommandbackground()

# Wakes up when it hears the word FRIDAY in the text
    if text.count(WAKE_WORD) > 0:

        SRF.speak("How may i help you ?")
        print("Listening....")

        # takes the command to do stuff
        text = SRF.takecommand()


# This is if u greet friday
        WISH_STR = ["hello", "hey", "hai", "hi", "hola"]
        for phrase in WISH_STR:
            if phrase in text:
                SRF.speak("Hello" + USER)

# This is for taking notes
        NOTE_STRS = ["take note", "take a note", "make a note",
                     "write this down", "remember this"]
        for phrase in NOTE_STRS:
            if phrase in text:
                SRF.speak("what would you like me write down")
                note_text = SRF.takecommand()
                FF.note(note_text)
                SRF.speak("Ok i Have taken the note")

# this is for wikipedia search, command - " search wikipedia for [name] ", "wikipedia search [name]","search on wikipedia for []"
        if 'wikipedia' in text:
            FF.wikipediasearch(text)


# This is if u want to exit the program
        EXIT_STRS = ["exit", "go away", "bye bye"]
        for phrase in EXIT_STRS:
            if phrase in text:
                SRF.speak("Bye Bye " + USER + "see you later")
                exit()
