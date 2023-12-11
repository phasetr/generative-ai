import os
import traceback
from uuid_extensions import uuid7str
from openai import OpenAI


class TTS:
    """_summary_
    適当なテキストから音声ファイルを作る。
    """

    def __init__(self) -> None:
        self.audio_directory_name = os.environ.get(
            "AUDIO_DIRECTORY_NAME", "audio")
        # ディレクトリがなければ作る
        if not os.path.exists(self.audio_directory_name):
            os.mkdir(self.audio_directory_name)

        uuid = uuid7str()
        self.orig_audio_path = f"{self.audio_directory_name}/{uuid}-orig.mp3"
        self.converted_audio_path = f"{self.audio_directory_name}/{uuid}-converted.mp3"
        self.sample_text_name = os.environ.get("SAMPLE_TEXT_FILE_NAME")

    def create_audio(self, text):
        """指定されたテキストから音声ファイルを作る"""

        try:
            client = OpenAI()
            response = client.audio.speech.create(
                model=os.environ.get("TTS_MODEL"),
                voice=os.environ.get("TTS_VOICE", "nova"),
                input=text
            )
            response.stream_to_file(self.converted_audio_path)
            return self.converted_audio_path
        except Exception as e:
            print(e)
            traceback.print_exc()
            exit()

    def create_audio_from_sample_text(self):
        """環境変数`SAMPLE_TEXT_NAME`に指定されたテキストファイルを読み込んで音声ファイルを作る"""

        try:
            with open(self.sample_text_name, mode="r", encoding="utf-8") as f:
                text = f.read()

                client = OpenAI()
                response = client.audio.speech.create(
                    model=os.environ.get("TTS_MODEL"),
                    voice=os.environ.get("TTS_VOICE", "nova"),
                    input=text
                )
                response.stream_to_file(self.orig_audio_path)
                return self.orig_audio_path
        except Exception as e:
            print(e)
            traceback.print_exc()
            exit()


if __name__ == "__main__":
    tts = TTS()
    ret_audio_path = tts.create_audio_from_sample_text()
    print(f"音声ファイルを作成しました: {ret_audio_path}")
