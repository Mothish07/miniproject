from openai import OpenAI
import time

client = OpenAI(api_key='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')
messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
    time.sleep(1)