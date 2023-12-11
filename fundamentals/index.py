from datetime import datetime
from uuid_extensions import uuid7str
import poll
import stt
import tts

uuid = uuid7str()
print(f"ファイル名：output/{uuid}")
tts = tts.TTS(uuid)
stt = stt.STT()
adapter = poll.OpenAIAdapter(uuid)

# 開始時刻を取得
start = datetime.now()
start_str = start.strftime("%H:%M:%S.%f")
print(f"開始時刻: {start_str}", flush=True)

# 読み込んだ文字列から音声ファイルを作る
sample_text_to_audio = datetime.now()
sample_text_to_audio_str = sample_text_to_audio.strftime("%H:%M:%S.%f")
orig_audio_path = tts.create_audio_from_sample_text()
print(f"""
====================
オリジナルの音声ファイル: {orig_audio_path}
時刻：{sample_text_to_audio_str}
前との時間差：{sample_text_to_audio - start}
====================
""")

# 音声ファイルを文字列に戻す
text = stt.create_text(orig_audio_path)
audio_to_text = datetime.now()
audio_to_text_str = audio_to_text.strftime("%H:%M:%S.%f")
print(f"""
====================
音声ファイルから読み取った文字列: {text}
時刻：{audio_to_text_str}
前との時間差：{audio_to_text - sample_text_to_audio}
====================
""")

# 文字列を`OpenAI`に投げて回答を取得する
response_text = adapter.create_chat(text)
openai = datetime.now()
openai_str = openai.strftime("%H:%M:%S.%f")
print(f"""
====================
OpenAIからの回答: {response_text}
時刻：{openai_str}
前との時間差：{openai - audio_to_text}
====================
""")

# 回答を音声に変換する
converted_audio_path = tts.create_audio(response_text)
openai_to_audio = datetime.now()
openai_to_audio_str = openai_to_audio.strftime("%H:%M:%S.%f")
print(f"""
====================
変換された音声ファイル: {converted_audio_path}
時刻：{openai_to_audio_str}
前との時間差：{openai_to_audio - openai}
====================
""")

# 終了時刻を取得
end = datetime.now()
end_str = datetime.now().strftime("%H:%M:%S.%f")
time_req = end - start
# 各種時刻を表示
print(f"終了時刻:   {end_str}", flush=True)
print(f"所要時間: {time_req}", flush=True)
