# Disaster Navigator API

災害情報を提供するFastAPI ベースのWebアプリケーション

## 📋 目次

- [機能](#機能)
- [技術スタック](#技術スタック)
- [セットアップ手順](#セットアップ手順)
- [使い方](#使い方)
- [プロジェクト構成](#プロジェクト構成)
- [API エンドポイント](#api-エンドポイント)

## 🚀 機能

- Hello World API
- RESTful API設計
- Service/Controller レイヤー分離アーキテクチャ
- 自動生成されるAPIドキュメント（Swagger UI）

## 🛠 技術スタック

- **Python 3.12+**
- **FastAPI** - 高速なWebフレームワーク
- **Uvicorn** - ASGIサーバー
- **uv** - 高速なPythonパッケージマネージャー

## 📦 セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/yonaoshi-agents/disaster-navigator-api.git
cd disaster-navigator-api
```

### 2. Python環境のセットアップ

このプロジェクトは `uv` を使用してパッケージを管理しています。

#### uvのインストール（未インストールの場合）

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# またはHomebrewを使用
brew install uv
```

#### 依存パッケージのインストール

```bash
# 依存パッケージを自動インストール
uv sync
```

または、個別にインストール:

```bash
uv add fastapi "uvicorn[standard]"
```

### 3. 仮想環境の有効化

```bash
source .venv/bin/activate
```

## 🎮 使い方

### サーバーの起動

#### 方法1: Pythonスクリプトとして実行

```bash
python main.py
```

#### 方法2: Uvicornコマンドで実行（ホットリロード有効）

```bash
uvicorn main:app --reload
```

サーバーが起動したら、以下のURLにアクセスできます:

- **APIベースURL**: http://localhost:8000
- **Swagger UI（API ドキュメント）**: http://localhost:8000/docs
- **ReDoc（代替ドキュメント）**: http://localhost:8000/redoc

### サーバーの停止

`Ctrl + C` でサーバーを停止できます。

## 📁 プロジェクト構成

```
disaster-navigator-api/
├── main.py                    # アプリケーションエントリーポイント
├── pyproject.toml             # プロジェクト設定とパッケージ依存関係
├── README.md                  # このファイル
├── .venv/                     # 仮想環境（自動生成）
└── app/
    ├── api/
    │   └── v1/
    │       └── endpoints/     # 将来のAPIエンドポイント
    ├── core/                  # コア設定・ユーティリティ
    ├── models/                # データベースモデル
    ├── schemas/               # Pydanticスキーマ
    ├── services/              # ビジネスロジック層
    │   ├── __init__.py
    │   └── hello_service.py   # Hello Worldサービス
    └── controllers/           # ルーティング層
        ├── __init__.py
        └── hello_controller.py # Hello Worldコントローラー
```

### アーキテクチャの特徴

- **Controller層**: APIエンドポイントのルーティングとリクエスト/レスポンス処理
- **Service層**: ビジネスロジックの実装
- **レイヤー分離**: 関心の分離により、保守性とテスト性が向上

## 🌐 API エンドポイント

### ルートエンドポイント

```
GET /
```

API基本情報を取得します。

**レスポンス例:**
```json
{
  "name": "Disaster Navigator API",
  "version": "1.0.0",
  "status": "running"
}
```

### Hello Worldエンドポイント

```
GET /hello/
```

ウェルカムメッセージを取得します。

**レスポンス例:**
```json
{
  "message": "Welcome to Disaster Navigator API",
  "version": "1.0.0",
  "status": "running"
}
```

### カスタム挨拶エンドポイント

```
GET /hello/greet?name={name}
```

パラメータ:
- `name` (optional): 挨拶する対象の名前（デフォルト: "World"）

**リクエスト例:**
```bash
curl "http://localhost:8000/hello/greet?name=太郎"
```

**レスポンス例:**
```json
{
  "message": "Hello, 太郎!",
  "status": "success"
}
```

## 🧪 開発

### 新しいエンドポイントの追加

1. `app/services/` にビジネスロジックを実装
2. `app/controllers/` にコントローラーを作成
3. `main.py` でルーターを登録

```python
# main.py
from app.controllers import your_controller

app.include_router(your_controller.router)
```

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 👥 貢献

プルリクエストを歓迎します。大きな変更の場合は、まずissueを開いて変更内容を議論してください。
