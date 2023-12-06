import speech_recognition
import pyautogui
from utils import save, close, program
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


