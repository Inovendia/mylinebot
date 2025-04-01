# 🏠 mylinebot - 不動産売却プラン診断チャットボット

このプロジェクトは、LINE Messaging API を使用して、不動産売却プラン診断を行うチャットボットです。  
ユーザーがLINEで友だち登録を行うと、質問に回答しながら売却活動をサポートします。

---

## 📌 プロジェクト概要

- LINEチャットボットを通じて、不動産売却に関する質問に回答
- 質問に対して、画像やボタンで選択肢を提示
- ユーザーの選択に応じて、Flexメッセージやテンプレートメッセージを送信

---

## 💻 インストール

### 必要なライブラリ

- `line-bot-sdk`: LINE Messaging API SDK
- `json`: JSONファイルを扱う標準ライブラリ
- `os`: 環境変数の読み込み

```
pip install line-bot-sdk
```
または以下で一括インストール：

```
pip install -r requirements.txt
```

🔐 環境変数の設定
以下の環境変数を設定してください（.envファイルやAWS Lambdaの環境変数で設定）：

LINE_CHANNEL_SECRET: LINEチャネルのシークレットキー

LINE_CHANNEL_ACCESS_TOKEN: LINEチャネルのアクセストークン

※これらは os.getenv() を用いてプログラム内で読み込まれます。



📁 ファイル構成
```
.
├── README.md
├── carousel.json
├── carousel_flex.json
├── flex_config.py
├── mylinebot.py
├── requirements.txt
├── rich_menu.json
├── template.json
└── test2.json
```
🌐 動作環境
Python 3.x

AWS Lambda

LINE Messaging API

📬 補足情報
Flexメッセージの作成には、LINE Flex Message Simulator を使うと便利です。

✅ 今後の改善案（任意）
UI/UXの精査

ユーザー状態の保存（例：DynamoDB）

より高度な選択肢分岐ロジックの実装
