import speech_recognition
import pyautogui
import os
from PIL import ImageGrab
import sys
import numpy as np
recogniser = speech_recognition.Recognizer()

times = 1
comandi = {
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "ok": "l",
    "okay": "l",
    "exit": "k",
    "select": "backspace",
    "start": "enter",
    "help": "i"
}
#start program
def program():
    os.startfile(r"C:\Users\david\Desktop\programming\pokemonplay\game\visualboyadvance-m.exe")
    pyautogui.sleep(2)
    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\argomenti advanced.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)
    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\Open.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)
    try:
        coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\gbaLightmode.PNG")
    except pyautogui.ImageNotFoundException:
        coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\gbaDarkmod.PNG")

    pyautogui.moveTo(coordinate)
    pyautogui.click(clicks=2, button='left')
    pyautogui.sleep(1)
    pyautogui.keyDown("f1")
    pyautogui.keyUp("f1")

#save
def save():
    pyautogui.leftClick()
    try:
        coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\consoleDarkmode.PNG")
    except pyautogui.ImageNotFoundException:
        coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\consoleLightmod.PNG")
    pyautogui.moveTo(coordinate)
    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\argomenti advanced.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.sleep(1)
    pyautogui.leftClick(coordinate)

    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\save.PNG")
    pyautogui.sleep(1)
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\f1slotsave.PNG")
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    pyautogui.sleep(1)

def close():
    pyautogui.leftClick()
    coordinate = pyautogui.locateOnScreen(r"C:\Users\david\Desktop\programming\pokemonplay\source\close.PNG")
    pyautogui.moveTo(coordinate)
    pyautogui.leftClick(coordinate)
    sys.exit()

print("Say program to start the emulator")
while True:
    try:
        with speech_recognition.Microphone(1) as mic:
            recogniser.adjust_for_ambient_noise(mic,1)
            print("speak")
            audio = recogniser.listen(mic, phrase_time_limit=5)
            #print(recogniser.energy_threshold)
            if recogniser.energy_threshold > 100:
                text = (recogniser.recognize_google(audio)).lower()
                print(text)
                if "hold" in text:
                    times = 10
                if text in comandi:
                    mapped_key = comandi[text]
                    for x in range(times):
                        pyautogui.keyDown(mapped_key)
                        pyautogui.keyUp(mapped_key)
                if text == "save":
                    save()
                if text == "close":
                    close()
                if "stop" in text:
                    times = 1
                if text == "program":
                    program()

    except speech_recognition.UnknownValueError:
        print("repeat pls")
