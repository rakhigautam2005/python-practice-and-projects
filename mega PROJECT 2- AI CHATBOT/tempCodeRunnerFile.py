import pyautogui
import time
import pyperclip
from openai import OpenAI
# OPENAI SETUP 
# OPTION 1 (recommended): use environment variable
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OPTION 2 (direct test - replace with your key)
client = OpenAI(api_key="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")

#  MEMORY VARIABLE
last_processed = ""

#  SIMPLE MESSAGE CHECK
def is_new_message(chat_log):
    lines = chat_log.strip().split("\n")
    if not lines:
        return False

    return True  # simple safe logic for now



# START BOT
time.sleep(2)

while True:
    try:
        time.sleep(5)

        #  Click chat area (adjust if needed)
        pyautogui.click(500, 200)
        time.sleep(1)

        #  Select and copy chat
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)

        chat_history = pyperclip.paste()

        if not chat_history:
            print(" Nothing copied")
            continue

        # Avoid duplicate processing
        if chat_history != last_processed:

            print("New message detected")
            last_processed = chat_history

            #  AI RESPONSE
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
You are Rakhi, a friendly Indian coder girl.
Reply in Hinglish (Hindi + English mix).
Keep reply short and natural.

Chat:
{chat_history}
"""
            )

            reply = response.output_text
            print(" Reply:", reply)

            pyperclip.copy(reply)

            # Click input box (YOU MUST adjust coordinates)
            pyautogui.click(800, 700)
            time.sleep(1)

            # Paste & send
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

    except Exception as e:
        print("Error:", e)