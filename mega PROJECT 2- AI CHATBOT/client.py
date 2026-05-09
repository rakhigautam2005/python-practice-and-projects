from openai import OpenAI
client = OpenAI(
api_key= "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")
command = '''
Sheet
Kya kiya
Steady state error
Or diagram jo h specification k
Or 2nd order response
L number btao
Lecture
Ki derivation or jo definitions haii wo sabh
Lecture se nhi kiya
3,4,5,6,7
Thenks
Ji
Dcn k kyaaaa
Sheet karo Annaya
Bta rhi thi
Dcn k kyaaaa
11-11:30 m hoo jaigi
Mam bol rhi thi sheet se aayega or hss rhi thi
Sheet karo pehele
Achaaaa
Whi krre bss
Phir  sojaenggg
😭
Yess jldi karlo
Hme to bht time lg jyega
Okayyy 🫩🫩🫩
Karke sona
Bye gn
Okay behn
Bye gn😭
DBMS mai sir ne bataya tha imp??
DBMS mai sir ne bataya tha imp??
nii
Difference between database system and file system 
3 level archecture 
Keys 
Er model 
Relational algebra
Joins 
Integrity constant
Imp
Kiske h Y riya k
Kiske h Y riya k
nahi
Toh
Ananya pr ek do chod ke complete hai
Achaaa
https://chatgpt.com/share/69d53699-b770-8323-846d-9f7b5642fb38
प्रिय छात्र/छात्राओं,
आप सभी को Online Artificial Intelligence (AI) Awareness Program में पंजीकरण करने हेतु प्रोत्साहित किया जाता है।
यह कार्यक्रम आपके AI ज्ञान को बढ़ाने का अवसर प्रदान करता है।
पंजीकरण लिंक: https://www.tcsion.com/courses/ai-awareness-programme
पंजीकरण तिथि 2 अप्रैल 2026 को दोपहर 12:00 बजे
अंतिम तिथि 9 अप्रैल 2026 (12:00 PM)
भागीदारी पूर्णतः निःशुल्क है।
सभी छात्रों से अनुरोध है कि शीघ्र पंजीकरण करें और इस अवसर का लाभ उठाएं।
धन्यवाद।
AKTU

After Registration please fill your registration details via the form below-
https://forms.gle/sbNnS4RikYMXyVx48
Kr diya tha ye toh
Maine bhi
'''

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a developer named rakhi who speaks hindi as well as engish  from India  and is a coder. YOU analyze chat history  and  speaks like rakhi and respond like rakhi."},
        {"role": "user", "content": "command"}
    ]
)

print(completion.choices[0].message)