# README

- GitHub: [aituber_python_programing_example](https://github.com/sr2mg/aituber_python_programing_example/tree/main)
- Book: [AITuberを作ってみたら生成AIプログラミングがよくわかった件](https://bookplus.nikkei.com/atcl/catalog/23/10/31/01079/)
    - [誤植訂正ページ](https://bookplus.nikkei.com/atcl/catalog/update/23/11/24/00173/)
- [VOICEVOX](https://voicevox.hiroshiba.jp/)
    - `VOICEVOX`を立ち上げると起動する`OpenAPI`の画面：<http://127.0.0.1:50021/docs>

```shell
curl -X 'POST' \
  'http://host.docker.internal:50021/audio_query?text=%E3%81%93%E3%82%93%E3%81%AB%E3%81%A1%E3%81%AF&speaker=1' \
  -H 'accept: application/json' \
  -d ''
```    