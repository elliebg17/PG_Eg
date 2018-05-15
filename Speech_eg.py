import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's your favorite animal")

answer = pg.prompt("Enter your favorite animal below.")

if answer == "elephant":
    speak.Speak("SAME BUD")

elif answer == "penguins":
    speak.Speak == ("love me some penguins")

else:
    speak.Speak("Thats sick")

speak.Speak("What video do you want to watch?")

website=pg.prompt("Enter video below.")

speak.Speak =
