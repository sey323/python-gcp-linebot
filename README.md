# python gcp linebot

GCP で FastAPI を利用した LINEBot を構築する際のテンプレートです。

## Quick Start

はじめに仮想環境と必要ライブラリをインストーするする。

```sh:
poetry install
```

環境変数を更新する。

```sh:
source .env
```

下記のコマンドで起動する

```sh:
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## GCP にデプロイ

はじめに gcp の設定を行う

```sh:
cd terraform
bash - ./init.sh
```

その後下記のコマンドでリソースをデプロイする

```sh:
terraform apply
```
