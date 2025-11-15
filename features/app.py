import os
from core.speech import speak

def open_notepad():
    os.system("notepad")

def open_calculator():
    os.system("calc")

def open_vscode():
    os.startfile(r"C:\Users\krish\AppData\Local\Programs\Microsoft VS Code\Code.exe")  # apna actual VSCode path daalna

# ✅ Close apps
def close_notepad():
    os.system("taskkill /im notepad.exe /f")
    speak("Notepad closed")

def close_calculator():
    os.system("taskkill /im Calculator.exe /f")
    speak("Calculator closed")

def close_vscode():
    os.system("taskkill /im Code.exe /f")
    speak("VS Code closed")

def close_chrome():
    os.system("taskkill /im chrome.exe /f")
    speak("Chrome browser closed")
