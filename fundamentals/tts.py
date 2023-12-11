import os
from uuid_extensions import uuid7str
from openai import OpenAI

sample_text_name = "sample1.txt"
is_exist = os.path.exists(sample_text_name)
if not is_exist:
    print(f"{sample_text_name}を作成してください。")
    exit()

print("テキストを読み込みます。")
text = ""
with open(sample_text_name, mode="r", encoding="utf-8") as f:
    text = f.read()

print("\n=========")
print(text)
print("=========\n")

audio_directory_name = os.environ.get("AUDIO_DIRECTORY_NAME")
audio_path = f"{audio_directory_name}/tts-{uuid7str()}.mp3"
# ディレクトリがなければ作る
if not os.path.exists(audio_directory_name):
    os.mkdir(audio_directory_name)

print("音声ファイルを作成します。")
client = OpenAI()
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=text
)
response.stream_to_file(audio_path)
print(f"音声ファイルを作成しました: {audio_path}")
