from openai import OpenAI
import os

client = OpenAI()

text_directory_name = os.environ.get("TEXT_DIRECTORY_NAME")
is_exist = os.path.exists(text_directory_name)
if not is_exist:
    print(f"{text_directory_name}を作成してください。")
    exit()

audio_directory_name = os.environ.get("AUDIO_DIRECTORY_NAME")
audio_file_root = "tts-065768f2-f7b9-7939-8000-ab4bb42537fe"
audio_path = f"{audio_directory_name}/{audio_file_root}.mp3"
text_file_path = f"{text_directory_name}/{audio_file_root}.txt"

# 音声ファイルを読み込んでテキストに変換してファイルに書き出す
with open(audio_path, "rb") as f:
    # 音声ファイルを読み込んで変換
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=f,
        response_format="text"
    )
    # 変換結果からテキストを抽出して書き出す
    with open(text_file_path, mode="w", encoding="utf-8") as f0:
        f0.write(transcript)
