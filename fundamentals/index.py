import poll
import stt
import tts

tts = tts.TTS()
stt = stt.STT()
adapter = poll.OpenAIAdapter()

# 読み込んだ文字列から音声ファイルを作る
orig_audio_path = tts.create_audio_from_sample_text()
print(f"オリジナルの音声ファイル: {orig_audio_path}")
# 音声ファイルを文字列に戻す
text = stt.create_text(orig_audio_path)
print(f"音声ファイルから読み取った文字列: {text}")
# 文字列を`OpenAI`に投げて回答を取得する
response_text = adapter.create_chat(text, orig_audio_path)
# 回答を音声に変換する
converted_audio_path = tts.create_audio(response_text)
print(f"変換された音声ファイル: {converted_audio_path}")
