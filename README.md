# 🏠 mylinebot - 不動産売却プラン診断チャットボット

このプロジェクトは、LINE Messaging API を使用して、不動産売却プラン診断を行うチャットボットです。  
ユーザーがLINEで友だち登録を行うと、質問に回答しながら売却活動をサポートします。

---

## 📌 プロジェクト概要

- LINEチャットボットを通じて、不動産売却に関する質問に回答
- 質問に対して、画像やボタンで選択肢を提示
- ユーザーの選択に応じて、Flexメッセージやテンプレートメッセージを送信

---

##システム構成図

![Image](https://github.com/user-attachments/assets/31d680fe-b298-48ed-9918-a39f243aa3b1)

##使用イメージ

<img src="https://github.com/user-attachments/assets/69703cc5-8301-48f7-bb7e-68a48d4414a4" width="25%">
<img src="https://github.com/user-attachments/assets/fe47c309-8170-497a-a4a4-39a2af24c290" width="25%">
<img src="https://github.com/user-attachments/assets/005f4eca-817e-4cda-8c85-49ac51af5233" width="25%">  
<img src="https://github.com/user-attachments/assets/b5592135-3c93-4e23-9742-c7df98f726da" width="25%">  
<img src="https://github.com/user-attachments/assets/7e079bd3-0878-4adf-8b14-abb390bc25e9" width="25%">



  




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
