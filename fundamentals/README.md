# README

- `tts.py`：`Text to Speech`、テキストを音声に変換する
- `stt.py`：`Speech to Text`、音声をテキストに変換する

## 初期化

- `.env.sample`をコピーして`.env`を作る
- `OpenAI`から`API`キーを取得して`.env`に設定する

## `uuid7`

- <https://pypi.org/project/uuid7/>

```python
from uuid_extensions import uuid7, uuid7str
print(uuid7())
print(uuid7str())
```
