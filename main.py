import datetime
import time
import sys
import keyboard

def animateText(message, delay = -1):
    for letter in message:
        print(letter, end = "")
        sys.__stdout__.flush()
        time.sleep(
            (0.1 if letter == ","
            else 0.2 if letter == "."
            else 0.3 if letter == "\n"
            else 0.02) if delay == -1 else delay
        )
    print("")

def clear():
    print("\n"*50)

clear()
print("TITLE")
optionStart = ""
try:
    with open('/Users/macbook/Desktop/game/save.txt', 'r') as readSave:
        optionStart = "[CONTINUE]"
except FileNotFoundError:
    optionStart = "[START]"

optionOptions = "[OPTIONS]"
optionCredits = "[CREDITS]"
print(optionStart + "\n" + optionOptions + "\n" + optionCredits)
optionSelect = 0

while True:
    if optionSelect == 3:
        optionSelect = 0
    elif optionSelect == -1:
        optionSelect = 2
    

    if optionSelect == 0:
        try:
            with open('/Users/macbook/Desktop/game/save.txt', 'r') as readSave:
                optionStart = "> [CONTINUE] <"
        except FileNotFoundError:
            optionStart = "> [START] <"
        optionOptions = "[OPTIONS]"
        optionCredits = "[CREDITS]"
    elif optionSelect == 1:
        try:
            with open('/Users/macbook/Desktop/game/save.txt', 'r') as readSave:
                optionStart = "[CONTINUE]"
        except FileNotFoundError:
            optionStart = "[START]"
        optionOptions = "> [OPTIONS] <"
        optionCredits = "[CREDITS]"
    elif optionSelect == 2:
        try:
            with open('/Users/macbook/Desktop/game/save.txt', 'r') as readSave:
                optionStart = "[CONTINUE]"
        except FileNotFoundError:
            optionStart = "[START]"
        optionOptions = "[OPTIONS]"
        optionCredits = "> [CREDITS] <"
        


    if keyboard.is_pressed("down"):
        time.sleep(0.2)
        optionSelect += 1
        clear()
        print("TITLE")
        print(optionStart + "\n" + optionOptions + "\n" + optionCredits)
    elif keyboard.is_pressed("up"):
        time.sleep(0.2)
        optionSelect -= 1
        clear()
        print("TITLE")
        print(optionStart + "\n" + optionOptions + "\n" + optionCredits)
    
    if keyboard.is_pressed("enter"):
        break


if optionSelect == 0:
    try:
        with open('/Users/macbook/Desktop/game/save.txt', 'r') as readSave: 
            pass
    except FileNotFoundError:
        with open('/Users/macbook/Desktop/game/save.txt', 'x') as writeSave:
            writeSave.write('000000:000000:000000:000000')

try:
    with open('/Users/macbook/Desktop/game/save.txt',"r") as readSave: 
        if readSave.readlines()[0] == "000000:000000:000000:000000":
            clear()
        else:
            print(len(readSave.read()[:5]))
            print(len(readSave.read()))
            print(readSave.read())
except FileNotFoundError:
    with open('/Users/macbook/Desktop/game/save.txt', 'x') as writeSave:
            writeSave.write('000000:000000:000000:000000')

animateText("(The following sequence is a description of the cutscene, the actual cutscene is still in development)")
time.sleep(3)
clear()
animateText("'No, no... I don't want this, please just let me escape...")
time.sleep(2)
clear()
animateText("'The door to my room, a safe space...'")
time.sleep(2)
clear()
animateText("They walk in, opening the door, pushing the door back as they enter")
time.sleep(2)
clear()
animateText("Click, 'Safe in my room, from the outside', they locked the door")





locX = 24
locY = 6
bottom = '''▒╬═════════════════════════════════════════════════███
▒▒▒▒▒▒▒▒▒▒▒▒▒▒Press I next to these ⓘ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒██'''

while True:
    print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒Press T for tutorial▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██')
    print('▒╬═════════════════════════════════════════════════███')
    rightSide = ('███', '███', '███', '███', '╬██', 'ⓘ █', 'ⓘ █', '╬██', '███', '███', '███', '███')
    rightSideStep = 0

    for y in range(12):
        print('▒║', end= '')
        for x in range(49):
            if (x == locX and y == locY):
                print('█', end='')
            else:
                print('░', end='')
        if (rightSideStep < len(rightSide)):
            print(rightSide[rightSideStep])
            rightSideStep += 1
        else:
            print('')
    print(bottom)
    movement = print('''\nDEBUG: [  x:  %d  , y:   %d  ] ''' %(locX, locY))

    if keyboard.read_key() == "w" or "a" or "s" or "d":
        if keyboard.is_pressed("w") and locY > 0:
            locY -= 1
        elif keyboard.is_pressed("s") and locY < 11:
            locY += 1
        elif keyboard.is_pressed("a") and locX > 0:
            locX -= 2
        elif keyboard.is_pressed("d") and locX < 48:
            locX += 2
    if locX == 48 and 3 < locY < 8:
        if movement in ('i','I'):
            clear()
            print("cool")

    clear()
     
#update this to support keyboard module