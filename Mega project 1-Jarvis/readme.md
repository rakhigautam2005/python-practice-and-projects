## Jarvis AI Voice Assistant

An AI-powered voice assistant built using Python that can understand voice commands, respond intelligently using OpenAI, and perform automation tasks like opening websites, playing music, fetching news, and controlling system applications.


## Features

-  Voice recognition (Speech-to-Text)
-  Text-to-Speech (gTTS + pyttsx3 fallback)
-  Open websites (Google, YouTube, Instagram)
-  Play songs using custom music library
-  Live news updates via News API
-  AI responses using OpenAI GPT model
-  Memory system (stores user data like name)
-  Time & Date awareness
-  System automation (Notepad, Calculator, Shutdown)
-  Command history tracking
-  Smart fallback for errors & offline mode

## Tech Stack

Python 3.x
speech_recognition
pyttsx3
gTTS
pygame
requests
openai
webbrowser
os
datetime

## How It Works

- Reads messages using Selenium
- Detects new messages in real-time
- Sends message to OpenAI API
- AI decides whether to reply or ignore
- Stores conversation in memory.json
- Sends response back automatically

## Project Architecture

Jarvis-AI-Assistant/
│
├── main.py              # Main logic (voice + AI + commands)
├── musiclibrary.py      # Custom music links dictionary
├── logs.txt             # Stores command history
├── memory.json          # Optional persistent memory storage
└── README.md            # Project documentation



## Installation

# 1. Clone the repository
git clone https://github.com/rakhigautam2005/jarvis-ai-assistant.git

# 2. Navigate to project folder
cd jarvis-ai-assistant

# 3. Create virtual environment (recommended)
python -m venv venv

# 4. Activate virtual environment
venv\Scripts\activate

# 5. Install dependencies
pip install speechrecognition pyttsx3 gtts pygame requests openai

# 6. Set environment variables (IMPORTANT)
.env

# Windows CMD:
setx OPENAI_API_KEY "your_openai_key"
setx NEWS_API_KEY "your_newsapi_key"

# 7. Run the project
python main.py

## what i learned

- How to work with real-world APIs like OpenAI and News API  
- Voice processing using SpeechRecognition (Speech-to-Text systems)  
- Text-to-Speech systems using pyttsx3 and gTTS  
- Handling real-time user input and command-based logic flow  
- Building automation features using Python (web, system, files)  
- Managing project state using memory (dictionaries and files)  
- Error handling and fallback systems for offline/failed API cases  
- Integrating multiple Python libraries into one working system  
- Designing a basic AI assistant architecture  



## Project Impact

- Demonstrates real-world application of AI, voice recognition, and automation in a single system  
- Shows ability to integrate multiple APIs (OpenAI, News API) into one working project  
- Highlights practical use of Python for building intelligent assistants  
- Improves productivity by automating everyday tasks using voice commands  
- Serves as a strong foundation for building advanced AI agent-based systems  
- Can be extended into a real-world personal assistant or smart desktop tool  
- Helps understand how modern AI assistants (like Alexa/Google Assistant) work internally  

## Future Improvements

-  Convert into AI Agent system with tool-calling and smart decision making  
-  Refactor into modular architecture (separate AI, speech, commands, memory)  
-  Add persistent database memory (SQLite or vector database)  
-  Improve wake word system with faster and more accurate detection  
-  Build a GUI dashboard for live commands, logs, and AI responses  
-  Deploy as a cloud-based assistant for remote access  

## Disclaimer

This project is built for educational and learning purposes only.  
It uses third-party APIs (like OpenAI and News API), so functionality depends on internet access and valid API keys.  
The developer is not responsible for any misuse of the system or API usage costs.


##  Support

If this project helped you or inspired you,⭐ Star the repository to show your support  
