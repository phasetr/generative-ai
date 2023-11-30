# README

- 参考ページ：[つくりながら学ぶ！AIアプリ開発入門 - LangChain & Streamlit による ChatGPT API 徹底活用](https://zenn.dev/ml_bear/books/d1f060a3f166a5)
- 参考ページ：[OpenAI API の API キーの取得](https://book.st-hakky.com/data-science/open-ai-create-api-key/)
- `devcontainer`利用参考：[VSCode+Docker+Dev Containerを使って開発環境をコンテナに作ってみた](https://zenn.dev/harurow/articles/c903de5f479a57)
- `CallCenter`のAPIキーを使っている：`.env`に記録している
- `TODO`s
    - `devcontainer`内から`GitHub`に`push`したい

## 章立て

- Chapter02：環境準備
- Chapter03：最初のAIチャットアプリ
- Chapter04：AIチャットアプリの作り込み
- Chapter05：AIチャットアプリのデプロイ（省略）
- Chapter06：Webサイト要約
- Chapter07：YouTube動画の要約
- Chapter08：長時間YouTube動画の要約
- Chapter09：PDFに質問しよう（前編: PDF Upload & Embedding）
- Chapter10：PDFに質問しよう（後編: RetrievalQA）

## 初期化

- プロジェクト直下の`.env.sample`をコピーして`.env`を作る
- `OpenAI`にアクセスして`API`キーを取得して設定する
- `VSCode`でプロジェクトを開く

## Python

### `Streamlit`

- 簡単なインストール・実行確認

```shell
streamlit hello
```

- 各種ファイル実行の参考用

```shell
streamlit run Chapter2/00_my_first_app.py
```
