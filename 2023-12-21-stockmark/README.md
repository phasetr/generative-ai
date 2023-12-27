# README

- バージョン情報: `pyenv`で`3.11.7`, あとは`venv`
- 参考ページ：[【Stockmark 13B】ChatGPTよりも圧倒的に速い！ビジネス利用特化型日本語LLMを使ってみた](https://weel.co.jp/media/stockmark-13b#index_id2)
- `2023/12/21`時点の`PyTorch`は`3.11`までしか使えない模様
- `Mac`では`stockmark/01.py`が動かないが`GoogleColab`なら動く
  - `GoogleColab`上でライブラリのインストールは次のコマンドで実行

```shell
!pip install transformers accelerate bitsandbytes
```

## 環境構築

### ローカル作業

- 必要に応じて`CDK`と`AWS CLI`をインストールする
- `cdk deploy`する
- 生成した秘密鍵をファイルに出力する

```shell
keyName=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevkeyname`].OutputValue' --output text) \
  && keyPairId=$(aws ec2 describe-key-pairs --key-names ${keyName} --query 'KeyPairs[*].[KeyPairId]' --output text) \
  && aws ssm get-parameter --name /ec2/keypair/${keyPairId} --with-decryption --query Parameter.Value --output text > ${keyName}.pem \
  && chmod 400 ${keyName}.pem
```

- EC2インスタンスにキーペアが関連づけられているか確認する

```shell
id=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevinstanceid`].OutputValue' --output text) \
  && aws ec2 describe-instances --instance-ids ${id} --query 'Reservations[*].Instances[*].KeyName' --output text
```

- `IP`アドレスを取得しつつ生成済みキーを指定して`SSH`ログインできるか確認する

```shell
keyName=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevkeyname`].OutputValue' --output text) \
  && ip=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevipaddress`].OutputValue' --output text) \
  && ssh -i ${keyName}.pem ec2-user@${ip}
```

- 一旦ログアウトする
- ローカルから再帰的にディレクトリをアップロードする

```shell
ip=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevipaddress`].OutputValue' --output text) \
  && scp -r -i stockmark-stack-dev-key.pem FlaskSample ec2-user@${ip}:/home/ec2-user/
```

### `EC2`インスタンスの整備

- `Python`の整備は次のリンク先を参考にすること：必要な内容は下記に転載している
  - [Pythonの様々なバージョンを導入](https://phasetr.com/archive/fc/pg/python/#python_1)
  - [venvを作る](https://phasetr.com/archive/fc/pg/python/#venv)
- `SSH`ログインする

```shell
keyName=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevkeyname`].OutputValue' --output text) \
  && ip=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevipaddress`].OutputValue' --output text) \
  && ssh -i ${keyName}.pem ec2-user@${ip}
```
- `pyenv`を導入する

```shell
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc \
  && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
  && git clone https://github.com/pyenv/pyenv.git ~/.pyenv \
  && source ~/.bashrc \
  && pyenv install 3.11.7 \
  && pyenv global 3.11.7
```

- `FlaskSample`ディレクトリに移動して`venv`を作成する

```shell
cd FlaskSample \
  && python -m venv .venv \
  && source .venv/bin/activate \
  && pip install -r requirements.txt
```

- `Web API`を起動する

```shell
python app.py
```

### `API`実行確認

- ローカルから`API`を実行する

```shell
ip=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevipaddress`].OutputValue' --output text) \
  && curl http://${ip}:8080/
```

## メモ

### `CDK`で設定した`Lambda`の実行

#### コンソールから`Lambda`を実行するときの`JSON`の例

- 開始

```shell
id=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevinstanceid`].OutputValue' --output text) \
  && echo "{\"Action\": \"start\", \"Region\": \"ap-northeast-1\", \"Instances\": [\"${id}\"]}"
```

- 停止

```shell
id=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevinstanceid`].OutputValue' --output text) \
  && echo "{\"Action\": \"stop\", \"Region\": \"ap-northeast-1\", \"Instances\": [\"${id}\"]}"
```

### `AWS CLI`で`EC2`インスタンスを開始・停止する

#### 状態確認

```shell
aws ec2 describe-instances --query 'Reservations[*].Instances[*].{ID:InstanceId,State:State.Name}' --output table
```

#### 開始

```shell
id=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevinstanceid`].OutputValue' --output text) \
  && aws ec2 start-instances --instance-ids ${id}
```

#### 停止

```shell
id=$(aws cloudformation describe-stacks --stack-name stockmark-stack-dev --query 'Stacks[].Outputs[?OutputKey==`stockmarkstackdevinstanceid`].OutputValue' --output text) \
  && aws ec2 stop-instances --instance-ids ${id}
```

### ローカルでのサンプル`Web API`用の環境構築

```shell
cd FlaskSample \
  && python -m venv .venv \
  && source .venv/bin/activate \
  && pip install -r requirements.txt
```
