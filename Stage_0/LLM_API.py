
import os
import requests

messages = [
    {"role": "system", "content": "你是一个简洁的助手，每次最多回答50个字。"},
]

def chat(messages):
    r=requests.post(
        "https://api.deepseek.com/chat/completions",
        headers={"Authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}"},
        json={
            "model": "deepseek-flash",
            "messages": messages,
        },
        timeout=60
        )
    if r.status_code != 200:
        print("出错了，状态码:", r.status_code)
        print("服务端原话:", r.text)      # ← 这一行是关键
        return None
    print("   [usage]", r.json()["usage"])
    return r.json()["choices"][0]["message"]["content"]

while True:
    user_input=input("你: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    messages.append({"role": "user", "content": user_input})
    reply=chat(messages)
    if reply is None:
        print("请求失败，请检查网络或API Key。")
        messages.pop()
        continue
    print("助手:", reply)
    messages.append({"role": "assistant", "content": reply})
    print(f"   [历史 {len(messages)} 条]")
