#An "AI Autonomous Messaging Assistant" that reads messages and generates intelligent replies using OpenAI API, Selenium, and memory-based conversation handling.

## Features

-  AI-powered smart replies using OpenAI
-  AI Autonomous Messaging  Assistant using Selenium
-  Conversation memory system (JSON-based)
-  Smart reply / ignore decision system
-  Secure API key handling using .env
-  Continuous real-time message monitoring

## Tech Stack

- Python
- Selenium
- OpenAI API
- Python-dotenv
- JSON (for memory)

## How It Works

- Reads messages using Selenium
- Detects new messages in real-time
- Sends message to OpenAI API
- AI decides whether to reply or ignore
- Stores conversation in memory.json
- Sends response back automatically

## System Architecture

User Message → Selenium → AI Processing (OpenAI API) → Decision Engine → Memory (JSON) → Auto Reply

## Installation

- Clone repository:
   git clone https://github.com/rakhigautam2005/ai autonomous messaging assistant

- Install dependencies:
   pip install selenium openai python-dotenv

- Create `.env` file:
   OPENAI_API_KEY=your_api_key_here

- Run the bot:
   python program.py

## What I Learned

- Real-world API integration
- Browser automation using Selenium
- Handling real-time data streams
- Building AI-powered decision systems
- Secure environment variable management

## Project Impact

This project demonstrates how AI can be integrated with real-world communication platforms to automate intelligent responses. It simulates a real-time AI assistant capable of understanding and responding to human messages.

## Future Improvements

- Add voice-based interaction (speech-to-text & text-to-speech)
- Improve memory system using database (SQLite or MongoDB)
- Deploy as a 24/7 cloud-based assistant
- Add sentiment analysis for better response quality
- Support multiple chats simultaneously

## Disclaimer

This AI Automation Assistant is developed strictly for educational purposes.

Users are responsible for ensuring compliance with WhatsApp and OpenAI usage policies.

This project should not be used for spam, bulk messaging, or any harmful activity.

⭐ If you like this project, please give it a star — it motivates me to build more AI systems.


