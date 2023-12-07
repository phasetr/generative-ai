import obsws_python as obs
import os
import random
from dotenv import load_dotenv


class OBSAdapter:
    def __init__(self) -> None:
        load_dotenv()
        password = os.environ.get("OBS_PASSWORD")
        host = os.environ.get("OBS_HOST")
        port = os.environ.get("OBS_PORT")

        # 設定されていない場合はエラー
        if password is None or host is None or port is None:
            raise Exception("OBSの設定がされていません")
        self.ws = obs.ReqClient(host, port, password)

    def set_question(self, text: str):
        self.ws.set_input_settings(
            name="Question",
            settings={"text": text},
            overlay=True)

    def set_answer(self, text: str):
        self.ws.set_input_settings(
            name="Answer",
            settings={"text": text},
            overlay=True)


if __name__ == "__main__":
    obsAdapter = OBSAdapter()
    obsAdapter.set_question("こんにちは")
    question_text = f"Questionの番号は{str(random.randint(0, 100))}になりました"
    obsAdapter.set_question(question_text)
    answer_text = f"Answerの番号は{str(random.randint(0, 100))}になりました"
    obsAdapter.set_answer(answer_text)
