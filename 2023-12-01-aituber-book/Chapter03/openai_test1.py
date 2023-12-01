import openai
import os

key = os.environ.get('OPENAI_API_KEY')
openai.api_key = key

# メッセージを作成
messages = [
    {
        "role": "system",
        "content": "あなたは端的に発言するAIです。"
    },
    {
        "role": "user",
        "content": "こんにちは。"
    }
]

# APIの呼び出し
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

# 結果を出力
# print(res)
print(res["choices"][0]["message"]["content"])
