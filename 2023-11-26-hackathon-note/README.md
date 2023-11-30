# README

- [自力でコード書けない非エンジニアがGPT4新機能ハッカソン24耐で優勝する話](https://note.com/msfmnkns/n/n0ae07a527c2e)
- [OpenAI GPT-4V の API を使って画像を AI に説明させよう！](https://qiita.com/kenji-kondo/items/87e71bf9645338d59ecb)

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