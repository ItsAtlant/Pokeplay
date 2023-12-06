import os
import sys
import pyautogui
#start program
def program():
    os.startfile(r"game\visualboyadvance-m.exe")
    pyautogui.sleep(2)
    coordinate = pyautogui.locateOnScreen(r"source\argomenti advanced.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)
    coordinate = pyautogui.locateOnScreen(r"source\Open.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)
    try:
        coordinate = pyautogui.locateOnScreen(r"source\gbaLightmode.PNG")
    except pyautogui.ImageNotFoundException:
        coordinate = pyautogui.locateOnScreen(r"source\gbaDarkmod.PNG")

    pyautogui.moveTo(coordinate)
    pyautogui.click(clicks=2, button='left')
    pyautogui.sleep(1)
    pyautogui.keyDown("f1")
    pyautogui.keyUp("f1")

#save
def save():
    pyautogui.leftClick()
    try:
        coordinate = pyautogui.locateOnScreen(r"source\consoleDarkmode.PNG")
    except pyautogui.ImageNotFoundException:
        coordinate = pyautogui.locateOnScreen(r"source\consoleLightmod.PNG")
    pyautogui.moveTo(coordinate)
    coordinate = pyautogui.locateOnScreen(r"source\argomenti advanced.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)

    coordinate = pyautogui.locateOnScreen(r"source\save.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    coordinate = pyautogui.locateOnScreen(r"source\f1slotsave.PNG")
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)

def close():
    pyautogui.leftClick()
    coordinate = pyautogui.locateOnScreen(r"source\close.PNG")
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    sys.exit()