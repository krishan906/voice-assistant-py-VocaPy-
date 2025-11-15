# core/commands.py
import random
import os
import webbrowser
import wikipedia
import pywhatkit as kit
import requests
from datetime import datetime
from core.speech import speak, take_command

# ------------------ Websites ------------------
def open_website(site_name):
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "instagram": "https://www.instagram.com",
        "twitter": "https://www.twitter.com",
        "github": "https://www.github.com",
        "wikipedia": "https://www.wikipedia.org",
        "gmail": "https://mail.google.com"
    }
    if site_name in sites:
        webbrowser.open(sites[site_name])
        speak(f"Opening {site_name}")
    else:
        speak("Sorry, I don't know this website.")

# ------------------ Apps ------------------
def open_app(app_name):
    if app_name == "calculator":
        os.system("calc")
    elif app_name == "notepad":
        os.system("notepad")
    elif app_name == "paint":
        os.system("mspaint")
    else:
        speak("App not configured")

def close_app(app_name):
    processes = {
        "calculator": "Calculator.exe",
        "notepad": "notepad.exe",
        "chrome": "chrome.exe",
        "edge": "msedge.exe",
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "powerpoint": "POWERPNT.EXE",
        "spotify": "Spotify.exe",
        "vlc": "vlc.exe"
    }
    if app_name in processes:
        os.system(f"taskkill /im {processes[app_name]} /f")
        return f"{app_name} closed."
    else:
        return "App not configured."

# ------------------ Time ------------------
def tell_time():
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")

# ------------------ Wikipedia ------------------
def search_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        speak(results)
    except:
        speak("Sorry, I could not find anything on Wikipedia.")

# ------------------ Google Search ------------------
def search_google(query):
    kit.search(query)
    speak(f"Here are Google search results for {query}")

# ------------------ Dictionary ------------------
def meaning(word):
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url).json()
        definition = response[0]['meanings'][0]['definitions'][0]['definition']
        speak(f"The meaning of {word} is {definition}")
    except:
        speak("Sorry, I couldn't find the meaning.")

# ------------------ Greeting ------------------
def respond_to_greeting(query):
    greetings_user = ["hello", "hi", "hey", "hii", "what's up", "how are you"]
    greetings_assistant = [
        "Hello! How are you?",
        "Hi there! I hope you're having a great day.",
        "Hey! How can I help you today?",
        "Hello! Nice to hear from you."
    ]
    for word in greetings_user:
        if word in query:
            speak(random.choice(greetings_assistant))
            return True
    return False

def respond_to_thanks(query):
    thanks_words = ["thank you", "thanks", "thanku", "thx"]
    responses = [
        "You’re welcome!",
        "No problem!",
        "Anytime!",
        "Happy to help!"
    ]
    for word in thanks_words:
        if word in query:
            speak(random.choice(responses))
            return True
    return False

# ------------------ Music ------------------
def play_music():
    speak("Which song should I play?")
    song = take_command()
    if song:
        speak(f"Playing {song} on YouTube")
        kit.playonyt(song)
    else:
        speak("I did not catch the song name.")

# ------------------ Command Handler ------------------
def execute_command(query):
    query = query.lower()

    # Websites
    if "open google" in query:
        open_website("google")
    elif "open youtube" in query:
        open_website("youtube")
    elif "open facebook" in query:
        open_website("facebook")
    elif "open instagram" in query:
        open_website("instagram")
    elif "open twitter" in query:
        open_website("twitter")
    elif "open wikipedia" in query:
        open_website("wikipedia")
    elif "open gmail" in query:
        open_website("gmail")

    # Apps
    elif "open calculator" in query:
        open_app("calculator")
    elif "open notepad" in query:
        open_app("notepad")
    elif "open paint" in query:
        open_app("paint")

    # Close apps / browser
    elif "close calculator" in query:
        speak(close_app("calculator"))
    elif "close notepad" in query:
        speak(close_app("notepad"))
    elif "close chrome" in query or "close browser" in query:
        speak(close_app("chrome"))
    elif "close edge" in query or "close microsoft edge" in query:
        speak(close_app("edge"))
    elif "close word" in query:
        speak(close_app("word"))
    elif "close excel" in query:
        speak(close_app("excel"))
    elif "close powerpoint" in query:
        speak(close_app("powerpoint"))
    elif "close spotify" in query:
        speak(close_app("spotify"))
    elif "close vlc" in query:
        speak(close_app("vlc"))

    # Music
    elif "play music" in query or "play song" in query:
        play_music()

    # Time
    elif "time" in query:
        tell_time()
    
    # Meaning
    elif "meaning of" in query:
        word = query.lower().replace("meaning of", "").strip()
        print("Word to search meaning:", word)  # debug
        meaning(word)

    # Wikipedia
    elif "wikipedia" in query:
        query = query.replace("wikipedia", "")
        search_wikipedia(query)

    # Google Search
    elif "search" in query:
        query = query.replace("search", "")
        search_google(query)

    # Dictionary
    elif "meaning of" in query:
        word = query.replace("meaning of", "").strip()
        meaning(word)

    # Stop assistant
    elif "stop" in query or "exit" in query:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I don't understand that command.")

# ------------------ Main runner ------------------
def run_assistant():
    query = take_command()
    if query:
        query = query.lower()  # normalize

        # 1️⃣ Greeting check
        if respond_to_greeting(query):
            return  # skip other commands if greeting

        # 2️⃣ Thanks check
        if respond_to_thanks(query):
            return  # skip other commands if thanking

        # 3️⃣ Execute other commands
        execute_command(query)