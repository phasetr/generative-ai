import requests
import json

# url = "http://127.0.0.1:50021/"
# Dockerからアクセスするためにホストを変更している
# 必要に応じて環境変数に指定しよう
url = "http://host.docker.internal:50021/"
text = "こんにちは"
speaker_id = 1
item_data = {
    "text": text,
    "speaker": speaker_id
}
res = requests.post(f"{url}audio_query", params=item_data)
res_json = res.json()

print(res_json)

query_data = res_json
a_params = {
    "speaker": speaker_id
}
res = requests.post(
    f"{url}synthesis",
    params=a_params, 
    data=json.dumps(query_data))
print(res.content)
