import time
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# SETUP
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

print("Scan QR code in WhatsApp Web...")
time.sleep(15)

# MEMORY SYSTEM

MEMORY_FILE = "memory.json"

if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f)


def load_memory():
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=2)


memory = load_memory

# AI FUNCTION

def ask_ai(chat, user_id):
    system_prompt = """
You are an intelligent WhatsApp assistant.

Rules:
- Decide if you should reply or ignore.
- If message is spam/greeting/no meaning → say IGNORE
- If reply is needed → respond short (1-2 lines)
- Use Hinglish naturally
- Be friendly but not repetitive
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"{system_prompt}\n\nChat:\n{chat}"
    )

    return response.output_text.strip()



# SMART FILTER

def should_reply(reply_text):
    return "IGNORE" not in reply_text.upper()


# GET LAST MESSAGE

def get_last_message():
    messages = driver.find_elements(By.CSS_SELECTOR, "span.selectable-text span")
    if messages:
        return messages[-1].text
    return ""


# SEND MESSAGE

def send_message(text):
    box = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")
    box.send_keys(text)
    box.send_keys(Keys.ENTER)


# MAIN LOOP

last_message = ""

print(" Bot is running...")

while True:
    try:
        time.sleep(3)

        message = get_last_message()

        if not message or message == last_message:
            continue

        last_message = message

        print(" New Message:", message)

        user_id = "default_user"

        # Update memory
        memory.setdefault(user_id, []).append(message)
        save_memory(memory)

        # AI RESPONSE
        reply = ask_ai(message, user_id)

        print(" AI Reply:", reply)

        if should_reply(reply):
            send_message(reply.replace("IGNORE", "").strip())
            print("Sent")
        else:
            print(" Ignored")

        time.sleep(2)  # rate limit

    except Exception as e:
        print(" Error:", e)
        time.sleep(5)