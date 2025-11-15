# assistant.py
from core.commands import run_assistant
from core.speech import speak

if __name__ == "__main__":
    print("Starting Personal Voice Assistant...")

    # ✅ Introduction
    speak("Hello! I am your personal voice assistant. I can open apps, search the web, tell the time, "
          "look up Wikipedia, play music, and even give you word meanings. Just say a command and I will do it for you.")

    # ✅ Main loop
    while True:
        run_assistant()
