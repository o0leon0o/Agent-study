from email import message
from http import client
import os
from openai import OpenAI

client=OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    basa_url="https://api.deepseek.com/v1"
)

messages = [
    {"role": "system", "content": "你是一个简洁的助手，每次最多回答50个字。"}
]

r=client.chat.completions.create(
    model="deepseek-flash",
    messages=messages
)

print(r.choices[0].message.content)
