import dotenv
import os
import requests
import json
import sounddevice as sd

dotenv.load_dotenv()
host = os.environ.get("HOST", "host.docker.internal")
url = f"http://{host}:50021/"
text = "こんにちは"
speaker_id = 1
item_data = {
    "text": text,
    "speaker": speaker_id
}
res = requests.post(f"{url}audio_query", params=item_data)
res_json = res.json()

# print(res_json)

query_data = res_json
a_params = {
    "speaker": speaker_id
}
res = requests.post(
    f"{url}synthesis",
    params=a_params, 
    data=json.dumps(query_data))
# print(res.content)

with open("sound_device.txt", "w", encoding="utf-8") as f:
    f.write(str(sd.query_devices()))
