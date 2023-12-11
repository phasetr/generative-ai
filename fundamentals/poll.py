from openai import OpenAI
import dotenv
import os

# APIキーの設定
dotenv.load_dotenv()
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))


class OpenAIAdapter:
    def __init__(self) -> None:
        # system_promptはsystem_prompt.txtから読み込む
        with open("system_prompt.txt", "r") as f:
            self.system_prompt = f.read()
        pass

    def _create_message(self, role, message):
        return {
            "role": role,
            "content": message
        }

    def create_chat(self, question):
        system_message = self._create_message("system", self.system_prompt)
        user_message = self._create_message("user", question)
        messages = [system_message, user_message]
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages)
        # 返り値のテキストを出力する
        content = res.choices[0].message.content
        return content


if __name__ == "__main__":
    adapter = OpenAIAdapter()
    response_text = adapter.create_chat("こんにちは")
    print(response_text)
