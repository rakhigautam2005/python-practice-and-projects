from openai import OpenAI
client = OpenAI(api_key="OPENAI_API_KEY")
#used an this api key as an example

response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud"}
        {"role": "user", "content": "what is coding" }
        ]
)

print(response.choices[0].message.content)