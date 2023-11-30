# README

- [自力でコード書けない非エンジニアがGPT4新機能ハッカソン24耐で優勝する話](https://note.com/msfmnkns/n/n0ae07a527c2e)

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