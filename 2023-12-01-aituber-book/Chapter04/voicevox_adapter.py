import dotenv
import json
import requests
import io
import os
import soundfile

dotenv.load_dotenv()

class VoicevoxAdapter:
    HOST = os.environ.get("HOST", "host.docker.internal")
    URL = f"http://{HOST}:50021/"

    def __init__(self) -> None:
        """二回POSTする。
        一回目で変換、二回目で音声合成。"""
        pass

    def __create_audio_query(self, text: str, speaker_id: int) -> json:
        """音声合成のためのデータを作成する"""
        item_data = {
            "text": text,
            "speaker": speaker_id
        }
        res = requests.post(f"{self.URL}audio_query", params=item_data)
        return res.json()

    def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
        """音声合成のためのリクエストを作成する"""
        a_params = {
            "speaker": speaker_id
        }
        headers = {"accept": "audio/wav", "Content-Type": "application/json"}
        res = requests.post(
            f"{self.URL}synthesis",
            params=a_params,
            data=json.dumps(query_data),
            headers=headers)
        print(res.status_code)
        return res.content

    def get_voice(self, text: str):
        speaker_id = 3
        query_data: json = self.__create_audio_query(
            text, speaker_id=speaker_id)
        audio_bytes = self.__create_request_audio(
            query_data, speaker_id=speaker_id)
        audio_stream = io.BytesIO(audio_bytes)
        data, sample_rate = soundfile.read(audio_stream)
        return data, sample_rate


if __name__ == "__main__":
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice("こんにちは")
    print(sample_rate)
