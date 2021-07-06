import speech_recognition
import pyaudio
import pyautogui

def openNotepad():
    pyautogui.size()
    icon_location = pyautogui.locateOnScreen(r'screenshots/notepadLogo.png')
    if icon_location is not None:
            if len(icon_location) == 4:
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
    else:
        print("Could not locate Notepad Icon on screen")

def openChrome():
    pyautogui.size()
    icon_location = pyautogui.locateOnScreen(r'screenshots/chromeLogo.png')
    if icon_location is not None:
            if len(icon_location) == 4:
                pyautogui.click(x=icon_location.left, y=icon_location.top, duration=0.25)
    else:
        print("Could not locate Chrome Icon on screen")

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as src:

    audio = recognizer.adjust_for_ambient_noise(src, duration=0.5)
    while True:
        try:
            print("\nPlease speak:")
            audio = recognizer.listen(src)
            speech_to_txt = recognizer.recognize_google(audio).lower()
        except Exception as ex:
            print("Sorry. Could not understand.\n\n")
            continue
           
        print("I heard : " + speech_to_txt)

        if (speech_to_txt == "quit") or (speech_to_txt == "exit"):
            break
        elif speech_to_txt == "scroll up":
            pyautogui.scroll(50)
        elif speech_to_txt == "scroll down":
            pyautogui.scroll(-50)
        elif speech_to_txt == "volume up":
            pyautogui.press('volumeup')
        elif speech_to_txt == "volume down":
            pyautogui.press('volumedown')
        elif speech_to_txt == "mute" or speech_to_txt=="unmute":
            pyautogui.press('volumemute')
        elif speech_to_txt == "open chrome":
            openChrome()
        elif speech_to_txt == "open notepad":
            openNotepad()
        