# mylinebot
このプロジェクトは、LINE Messaging APIを使用した不動産売却プラン診断のためのチャットボットを実装するものです。ユーザーがLINEで友だち登録を行うと、様々な不動産に関する質問や診断を行い、売却活動をサポートします。

**プロジェクト概要**
ユーザーはLINEチャットボットを通じて、不動産売却に関する質問に回答することができます。
質問に対して、適切な画像やボタンを表示し、ユーザーに次の選択肢を提供します。
ユーザーの選択に応じて、動的に画像やテンプレートメッセージを送信します。

**インストール**
必要なライブラリ
line-bot-sdk : LINE Messaging API用SDK
json : JSONファイルを扱うための標準ライブラリ
os : 環境変数の読み込み

```bash
pip install line-bot-sdk
```

**環境変数の設定**
以下の環境変数を設定してください:

LINE_CHANNEL_SECRET : LINEチャネルのシークレットキー
LINE_CHANNEL_ACCESS_TOKEN : LINEチャネルのアクセストークン
これらの環境変数は、os.getenv()を使って読み込まれます。

**使用方法**
Lambda ハンドラー
本プログラムはAWS Lambdaで動作することを前提にしています。lambda_handler関数がLambdaのエントリポイントです。

```python
def lambda_handler(event, context):
    print(event)
    headers = event["headers"]
    body = event["body"]

    signature = headers['x-line-signature']

    handler.handle(body, signature)

    return {"statusCode": 200, "body": "OK"}
```

**イベントハンドラー**
FollowEvent: ユーザーがLINEで友だち追加したときの処理を定義します。
PostbackEvent: ユーザーがボタンを押したときの処理を定義します。
MessageEvent: ユーザーがメッセージを送信したときの処理を定義します。
これらのイベントに対して、適切な応答を返します。

**フレックスメッセージとボタンテンプレート**
ユーザーの選択肢に応じて、以下のようなメッセージを送信します:

フレックスメッセージ: 複雑なレイアウトを持つメッセージ
ボタンテンプレート: ユーザーにボタンを表示し、選択肢を与えるメッセージ
例: フォロー時の応答
ユーザーが友だち追加をすると、以下のメッセージが送信されます。

友達追加の挨拶
画像
フレックスメッセージ

```python
@handler.add(FollowEvent)
def handle_follow(event):
    with open("test.json", "r") as f:
        flex_message_json = json.load(f)
        flex_message = FlexSendMessage(
            alt_text='This is a Flex Message',
            contents=flex_message_json['contents']
        )
    image_url = "https://example.com/image.png"
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="友達登録ありがとうございます！株式会社NKです！"),
            ImageSendMessage(original_content_url=image_url, preview_image_url=image_url),
            flex_message
        ]
    )
```

例: ボタン選択時の応答
ユーザーがボタンを選択した場合に、次の質問を表示します。

```python
@handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    if postback_data == '買い替え・住み替え':
        # 次の質問を表示
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="次の住まいを選んだり引越しの準備を考えたり、とっても大事な時期ですね"),
                ImageSendMessage(original_content_url="https://example.com/image.png", preview_image_url="https://example.com/image.png"),
                TemplateSendMessage(
                    alt_text='ButtonsTemplate',
                    template=ButtonsTemplate(
                        title='【問1】', text='▼ タップして選ぶ ▼',
                        actions=[
                            PostbackAction(label="買い替え・住み替え", data="買い替え・住み替え", text="買い替え・住み替え"),
                            PostbackAction(label="相続予定", data="相続予定", text="相続予定"),
                            PostbackAction(label="離婚", data="離婚", text="離婚"),
                            PostbackAction(label="単純売却", data="単純売却", text="単純売却")
                        ]
                    )
                )
            ]
        )
```

**ファイル構成**
lambda_handler.py: メインの処理が書かれているファイル
test.json: フレックスメッセージのテンプレート
carousel.json: イメージカルーセルテンプレートの設定
requirements.txt: 必要なライブラリの一覧

**動作環境**
AWS Lambda
Python 3.x
LINE Messaging API
