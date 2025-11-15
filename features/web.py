import webbrowser
from core.speech import speak
import os

def open_google():
    webbrowser.open("https://www.google.com")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_whatsapp():
    webbrowser.open("https://web.whatsapp.com")

def open_facebook():
    webbrowser.open("https://www.facebook.com")

def open_instagram():
    webbrowser.open("https://www.instagram.com")

def open_twitter():
    webbrowser.open("https://twitter.com")

def open_linkedin():
    webbrowser.open("https://www.linkedin.com")

def open_gmail():
    webbrowser.open("https://mail.google.com")

def open_amazon():
    webbrowser.open("https://www.amazon.in")

def open_flipkart():
    webbrowser.open("https://www.flipkart.com")

# ✅ Close browser (all tabs)
def close_browser():
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im msedge.exe /f")
    speak("Browser closed")
