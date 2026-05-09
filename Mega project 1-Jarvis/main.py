# imports needed

import speech_recognition as sr      # For converting speech → text
import webbrowser                   # To open websites
import pyttsx3                      # Offline text-to-speech
import requests                     # For API calls (news etc.)
import musiclibrary                 # Your custom music dictionary
from openai import OpenAI           # OpenAI API
from gtts import gTTS               # Google text-to-speech (online)
import pygame                       # To play audio files
import os                           # For system operations
import datetime                     # For time and date

# initialization

print("Jarvis is starting...")
print("Loading modules...")

# Create recognizer object (for listening voice)
recognizer = sr.Recognizer()

# Adjust sensitivity of microphone
recognizer.energy_threshold = 300     # Minimum sound level
recognizer.pause_threshold = 0.8      # Pause before considering sentence complete

# Initialize offline voice engine
engine = pyttsx3.init()

# Initialize pygame mixer (for playing mp3 audio)
pygame.mixer.init()

# api keys

# IMPORTANT: NEVER put real API key directly in code (security risk)
# Instead use environment variables

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# Create OpenAI client
client = OpenAI(api_key="OPENAI_API_KEY")

#memory  and history

memory = {}     # Stores user info (like name)
history = []    # Stores past commands

# Store data in memory
def remember(key, value):
    memory[key] = value

# Retrieve data from memory
def recall(key):
    return memory.get(key, "I don't know yet")

# speak function

# Backup offline voice (if internet fails)
def speak_old(text):
    engine.say(text)
    engine.runAndWait()

# Main speak function using gTTS (better voice)
def speak(text):
    try:
        # Convert text → speech file
        tts = gTTS(text=text, lang='en')
        filename = "temp.mp3"
        tts.save(filename)

        # Load and play audio
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until audio finishes
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Remove file after playing
        pygame.mixer.music.unload()
        os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)
        speak_old(text)   # fallback

# ai function

def aiProcess(command):
    try:
        # Send user command to OpenAI model
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis. Be smart, short, and helpful."},
                {"role": "user", "content": command}
            ]
        )

        # Return AI response
        return completion.choices[0].message.content

    except:
        return "Sorry, I am having trouble connecting to AI."

# news function

def get_news_titles():
    # API URL to fetch Indian news
    url = f"https://newsdata.io/api/1/latest?apikey={NEWS_API_KEY}&country=in&language=en"

    try:
        response = requests.get(url)     # Send request
        data = response.json()           # Convert to JSON

        articles = data.get("results", [])

        # Extract only titles
        return [a["title"] for a in articles if a.get("title")]

    except:
        return []

#command handler

def processCommand(c):
    c = c.lower()       # Convert to lowercase
    history.append(c)   # Save command

    print("Processing command...")

    # Save command with timestamp in file
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} : {c}\n")

    # to exit
    if "exit" in c or "stop" in c:
        speak("Goodbye boss")
        exit()

    # web
    elif "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open instagram" in c:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    # music
    elif c.startswith("play"):
        song = c.replace("play", "").strip()
        link = musiclibrary.music.get(song)

        if link:
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak("Song not found")

    # news
    elif "news" in c:
        speak("Fetching news")
        titles = get_news_titles()

        if not titles:
            speak("Sorry, I couldn't fetch news right now")
        else:
            for title in titles[:5]:
                speak(title)

    # memory
    elif "my name is" in c:
        name = c.replace("my name is", "").strip()
        remember("name", name)
        speak(f"Nice to meet you {name}")

    elif "what is my name" in c:
        speak(recall("name"))

    # time and date
    elif "time" in c:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "date" in c:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today is {date}")

    # system
    elif "open notepad" in c:
        os.system("notepad")

    elif "open calculator" in c:
        os.system("calc")

    elif "shutdown" in c:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    # history
    elif "history" in c:
        speak("Showing last commands")
        for cmd in history[-5:]:
            speak(cmd)

    # personality
    elif "who are you" in c:
        speak("I am Jarvis, your personal AI assistant created by Gautam")

    elif "hello" in c:
        speak("Hello boss, how can I help you today?")

    # ai fallback
    else:
        speak("Let me think")
        output = aiProcess(c)
        speak(output)

# main loop

if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:
        try:
            # Use microphone as input
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)

                # Listen for voice input
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            # Convert speech → text
            word = recognizer.recognize_google(audio)
            print("You said:", word)

            # Process command
            processCommand(word)

        except sr.WaitTimeoutError:
            print("Timeout (no speech detected)")

        except sr.UnknownValueError:
            print("Could not understand")

        except sr.RequestError as e:
            print(f"API error: {e}")