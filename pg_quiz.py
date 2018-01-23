import pyautogui as pg
import time
import webbrowser

pg.prompt (
    """
Which Greys Anatomy character would you rather be?

a) Meredith
b) Izzie
c) Alex

""")

pg.alert ("You chose " + answer)


if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3


pg.prompt (
    """
Which is your favorite couple?

a) Izzie and George
b) Meredith and Derek
c) Cristina and Burke

""")

pg.alert ("You chose " + answer)


if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3

    pg.prompt (
    """
Who is the best attending/resident?

a) Bailey
b) Derek
c) Callie

""")

pg.alert ("You chose " + answer)


if answer == "a":
    points += 1
elif answer == "b":
    points +=2
elif answer == "c":
    points+=3

# END OF SURVEY
pg.alert ("Your character is...")

if points < 5:
    pg.alert("You are Meredith")
             webbrowser.open ("")
elif points >= 5 and points <7:
    pg.alert("You are Izzie")
            webbrowser.open ("")
elif pointa >= 9:
    pg. alert("You are George."
            webbrowser.open ("")


    
