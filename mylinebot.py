import os
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, ImageMessage,TextSendMessage,FollowEvent,ImageSendMessage,
    TemplateSendMessage,ButtonsTemplate,PostbackAction,FlexSendMessage,URIAction,MessageTemplateAction,
    ImagemapSendMessage,BaseSize,URIImagemapAction,ImagemapArea,PostbackEvent,ImageCarouselTemplate,
    ImageCarouselColumn,RichMenu
)

handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET')) #Webhokhandler1調べる
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))


def lambda_handler(event, context):
    print(event)
    headers = event["headers"]
    body = event["body"]

    signature = headers['x-line-signature']

    handler.handle(body, signature)

    return {"statusCode": 200, "body": "OK"}

@handler.add(FollowEvent)
def handle_follow(event):
    with open("test.json", "r") as f:
        flex_message_json = json.load(f)
        flex_message = FlexSendMessage(
            alt_text='This is a Flex Message',
            contents=flex_message_json['contents']
        )
    image_url = "https://drive.usercontent.google.com/download?id=1w_28VSB27jIaV2Uvi-EpENwz6YFmmSKx&export=view&authuser=0"
    line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="友達登録ありがとうございます！株式会社NKです！"),
            ImageSendMessage(original_content_url=image_url, preview_image_url=image_url),
            flex_message
        ]
    )

@handler.add(PostbackEvent)
def handle_postback(event):
    postback_data = event.postback.data
    if postback_data == 'ボタンがタップされました':
        image_url3 = ("https://drive.usercontent.google.com/download?id=1pTa3oKwGbKN5LgRn2pM3PhzuwTylcfDR&export=view&authuser=0")
        line_bot_api.reply_message(
            event.reply_token,
            [
                TextSendMessage(text="早速ですが売却プラン診断をしてみましょう"),
                ImageSendMessage(original_content_url=image_url3, preview_image_url=image_url3),
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
    elif postback_data == '最後のボタンがタップされました':
        with open("carousel.json", "r") as f:
            carousel_json = json.load(f)
            carousel = TemplateSendMessage(
                alt_text=carousel_json['altText'],
                template=ImageCarouselTemplate(
                    columns=carousel_json['template']['columns']
                )
            )
        messages = [
            carousel,
            TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='診断結果をもとに早速売却活動を進めてみませんか？',
                    text='▼ タップして選ぶ ▼',
                    actions=[
                        PostbackAction(label="無料査定・相談をする", data="無料査定・相談をする",
                                       text="無料査定・相談をする"),
                        PostbackAction(label="札幌タワマンくんの強みとは？", data="札幌タワマンくんの強みとは？",
                                       text="札幌タワマンくんの強みとは？")
                    ]
                )
            )
        ]
        line_bot_api.reply_message(event.reply_token, messages)

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    print(event)
    """ TextMessage handler """
    input_text = event.message.text
    messages = list()
    image_url2 = ("https://drive.usercontent.google.com/download?id=1q1ROtx-TrklB_g3YHeAQRwKAbs-tQwVj&export=view&authuser=0")
    if input_text == '買い替え・住み替え':
        messages = [TextSendMessage(text='次の住まいを選んだり引越しの準備を考えたり、とっても大事な時期ですね'),
                    ImageSendMessage(original_content_url=image_url2, preview_image_url=image_url2),
                    TextSendMessage(text="売却を検討している不動産の種別は何ですか？"),
                    TemplateSendMessage(alt_text='ButtonsTemplate',template=ButtonsTemplate(
                        title='【問２】',text='▼ タップして選ぶ ▼',actions=[PostbackAction(label="マンション", data="マンション", text="マンション"),
                                          PostbackAction(label="一戸建て", data="一戸建て", text="一戸建て"),
                                          PostbackAction(label="土地", data="土地", text="土地"),
                                          PostbackAction(label="その他", data="その他", text="その他")])),
                    ]
        line_bot_api.reply_message(event.reply_token, messages)
    elif input_text == '相続予定':
        messages=[TextSendMessage(text='相続は何かと手続きが複雑で悩みも多いもの。希望通りに売却したいですよね'),
        TextSendMessage(text="売却を検討している不動産の種別は何ですか？"),
        TemplateSendMessage(alt_text='ButtonsTemplate',template=ButtonsTemplate(
            title='【問２】',text='▼ タップして選ぶ ▼',actions=[PostbackAction(label="マンション", data="マンション", text="マンション"),
                              PostbackAction(label="一戸建て", data="一戸建て", text="一戸建て"),
                              PostbackAction(label="土地", data="土地", text="土地"),
                              PostbackAction(label="その他", data="その他", text="その他")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '離婚':
        messages=[TextSendMessage(text='トラブルなく売却できるといいですよね'),
        TextSendMessage(text="売却を検討している不動産の種別は何ですか？"),
        TemplateSendMessage(alt_text='ButtonsTemplate',template=ButtonsTemplate(
            title='【問２】',text='▼ タップして選ぶ ▼',actions=[PostbackAction(label="マンション", data="マンション", text="マンション"),
                              PostbackAction(label="一戸建て", data="一戸建て", text="一戸建て"),
                              PostbackAction(label="土地", data="土地", text="土地"),
                              PostbackAction(label="その他", data="その他", text="その他")])),
        ImageSendMessage(original_content_url=image_url2,preview_image_url=image_url2)]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '単純売却':
        messages=[TextSendMessage(text='なるべく負担なく売却できるといいですよね'),
        TemplateSendMessage(alt_text='ButtonsTemplate',template=ButtonsTemplate(
            title='【問２】',text='▼ タップして選ぶ ▼',actions=[PostbackAction(label="マンション", data="マンション", text="マンション"),
                              PostbackAction(label="一戸建て", data="一戸建て", text="一戸建て"),
                              PostbackAction(label="土地", data="土地", text="土地"),
                              PostbackAction(label="その他", data="その他", text="その他")])),
        ImageSendMessage(original_content_url=image_url2,preview_image_url=image_url2)]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == 'マンション':
        image_url4 = ("https://drive.usercontent.google.com/download?id=1IY6VVtu3OWSRI5_Fqd8rWWKwHiSu5HLJ&export=view&authuser=0")
        messages=[TextSendMessage(text='マンション売買のポイントを抑えて、良い条件で売却したいですね'),
                  ImageSendMessage(original_content_url=image_url4, preview_image_url=image_url4),
                  TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                      title='【問3】', text='▼ タップして選ぶ ▼',
                      actions=[PostbackAction(label="まだ検討をはじめたばかり", data="まだ検討をはじめたばかり", text="まだ検討をはじめたばかり"),
                               PostbackAction(label="相場などの情報収集中", data="相場などの情報収集中", text="相場などの情報収集中"),
                               PostbackAction(label="具体的に不動産会社を検討中", data="具体的に不動産会社を検討中", text="具体的に不動産会社を検討中"),
                               PostbackAction(label="売却活動を行っている", data="売却活動を行っている", text="売却活動を行っている")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == 'その他':
        image_url4 = (
            "https://drive.usercontent.google.com/download?id=1IY6VVtu3OWSRI5_Fqd8rWWKwHiSu5HLJ&export=view&authuser=0")
        messages = [TextSendMessage(text='不動産売買のポイントを抑えて、良い条件で売却したいですね'),
                    ImageSendMessage(original_content_url=image_url4, preview_image_url=image_url4),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問3】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="まだ検討をはじめたばかり", data="まだ検討をはじめたばかり",
                                                text="まだ検討をはじめたばかり"),
                                 PostbackAction(label="相場などの情報収集中", data="相場などの情報収集中",
                                                text="相場などの情報収集中"),
                                 PostbackAction(label="具体的に不動産会社を検討中", data="具体的に不動産会社を検討中",
                                                text="具体的に不動産会社を検討中"),
                                 PostbackAction(label="売却活動を行っている", data="売却活動を行っている",
                                                text="売却活動を行っている")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == 'まだ検討をはじめたばかり':
        image_url5 = ("https://drive.usercontent.google.com/download?id=1WQhMoJ6Yxm6qzg2wENJUAaSSyQc348bT")
        messages=[TextSendMessage(text='検討を始めたばかりなんですね！幅広い情報収集をオススメします！'),
                  ImageSendMessage(original_content_url=image_url5, preview_image_url=image_url5),
                  TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                      title='【問4】', text='▼ タップして選ぶ ▼',
                      actions=[PostbackAction(label="2〜3ヶ月以内", data="2〜3ヶ月以内", text="2〜3ヶ月以内"),
                               PostbackAction(label="半年以内", data="半年以内", text="半年以内"),
                               PostbackAction(label="1年以上", data="1年以上", text="1年以上"),
                               PostbackAction(label="じっくり時間をかけたい", data="じっくり時間をかけたい", text="じっくり時間をかけたい")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '相場などの情報収集中':
        image_url5 = ("https://drive.usercontent.google.com/download?id=1WQhMoJ6Yxm6qzg2wENJUAaSSyQc348bT")
        messages = [TextSendMessage(text='今、情報収集をしているんですね！相場などが気になるところですよね'),
                    ImageSendMessage(original_content_url=image_url5, preview_image_url=image_url5),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問4】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="2〜3ヶ月以内", data="2〜3ヶ月以内", text="2〜3ヶ月以内"),
                                 PostbackAction(label="半年以内", data="半年以内", text="半年以内"),
                                 PostbackAction(label="1年以上", data="1年以上", text="1年以上"),
                                 PostbackAction(label="じっくり時間をかけたい", data="じっくり時間をかけたい",
                                                text="じっくり時間をかけたい")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '具体的に不動産会社を検討中':
        image_url5 = ("https://drive.usercontent.google.com/download?id=1WQhMoJ6Yxm6qzg2wENJUAaSSyQc348bT")
        messages = [TextSendMessage(text='不動産会社を検討中なんですね！会社選びは難しいですよね'),
                    ImageSendMessage(original_content_url=image_url5, preview_image_url=image_url5),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問4】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="2〜3ヶ月以内", data="2〜3ヶ月以内", text="2〜3ヶ月以内"),
                                 PostbackAction(label="半年以内", data="半年以内", text="半年以内"),
                                 PostbackAction(label="1年以上", data="1年以上", text="1年以上"),
                                 PostbackAction(label="じっくり時間をかけたい", data="じっくり時間をかけたい",
                                                text="じっくり時間をかけたい")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '売却活動中':
        image_url5 = ("https://drive.usercontent.google.com/download?id=1WQhMoJ6Yxm6qzg2wENJUAaSSyQc348bT")
        messages = [TextSendMessage(text='すでに売却活動中なんですね！進捗が気になるところですよね'),
                    ImageSendMessage(original_content_url=image_url5, preview_image_url=image_url5),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問4】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="2〜3ヶ月以内", data="2〜3ヶ月以内", text="2〜3ヶ月以内"),
                                 PostbackAction(label="半年以内", data="半年以内", text="半年以内"),
                                 PostbackAction(label="1年以上", data="1年以上", text="1年以上"),
                                 PostbackAction(label="じっくり時間をかけたい", data="じっくり時間をかけたい",
                                                text="じっくり時間をかけたい")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '2〜3ヶ月以内':
        image_url6 = ("https://drive.usercontent.google.com/download?id=10vpNJWhxGlbqwdRSnkVeVojHetQF8Y7i")
        messages = [TextSendMessage(text='たしかに、売却期間が長くなると売れ残りのイメージが付きますし、物件はなるべく早めに売りたいですよね！'),
                    ImageSendMessage(original_content_url=image_url6, preview_image_url=image_url6),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問5】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="高く売却できること", data="高く売却できること", text="高く売却できること"),
                                 PostbackAction(label="早く売却できること", data="早く売却できること", text="早く売却できること")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '半年以内':
        image_url6 = ("https://drive.usercontent.google.com/download?id=10vpNJWhxGlbqwdRSnkVeVojHetQF8Y7i")
        messages = [TextSendMessage(
            text='たしかに、売却には意外と時間がかかりますし、良い条件で売れるよう、計画を立てて進めたいですよね'),
                    ImageSendMessage(original_content_url=image_url6, preview_image_url=image_url6),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問5】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="高く売却できること", data="高く売却できること",
                                                text="高く売却できること"),
                                 PostbackAction(label="早く売却できること", data="早く売却できること",
                                                text="早く売却できること")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '1年以上':
        image_url6 = ("https://drive.usercontent.google.com/download?id=10vpNJWhxGlbqwdRSnkVeVojHetQF8Y7i")
        messages = [TextSendMessage(
            text='売却まで時間に余裕を持って進められますね！良い条件での売却チャンスを逃さないようにしたいですね'),
            ImageSendMessage(original_content_url=image_url6, preview_image_url=image_url6),
            TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                title='【問5】', text='▼ タップして選ぶ ▼',
                actions=[PostbackAction(label="高く売却できること", data="高く売却できること",
                                        text="高く売却できること"),
                         PostbackAction(label="早く売却できること", data="早く売却できること",
                                        text="早く売却できること")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == 'じっくり時間をかけたい':
        image_url6 = ("https://drive.usercontent.google.com/download?id=10vpNJWhxGlbqwdRSnkVeVojHetQF8Y7i")
        messages = [TextSendMessage(
            text='良い条件で売れるよう、慎重に行きたいですよね！チャンスに備えて今から準備しておきましょう'),
            ImageSendMessage(original_content_url=image_url6, preview_image_url=image_url6),
            TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                title='【問5】', text='▼ タップして選ぶ ▼',
                actions=[PostbackAction(label="高く売却できること", data="高く売却できること",
                                        text="高く売却できること"),
                         PostbackAction(label="早く売却できること", data="早く売却できること",
                                        text="早く売却できること")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '高く売却できること':
        image_url7 = ("https://drive.usercontent.google.com/download?id=15CYKtc-sIIDhUgGkSyMAov6vij8hsels")
        messages = [TextSendMessage(text='次が最後の質問です!'),
                    ImageSendMessage(original_content_url=image_url7, preview_image_url=image_url7),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問6】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="最初の進め方がわからない", data="最初の進め方がわからない", text="最初の進め方がわからない"),
                                 PostbackAction(label="次に何をすべきかわからない", data="次に何をすべきかわからない", text="次に何をすべきかわからない"),
                                 PostbackAction(label="初めての不動産会社選びが不安", data="初めての不動産会社選びが不安", text="初めての不動産会社選びが不安"),
                                 PostbackAction(label="今の不動産会社で良いのか不安", data="今の不動産会社で良いのか不安",
                                                text="今の不動産会社で良いのか不安")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '早く売却できること':
        image_url7 = ("https://drive.usercontent.google.com/download?id=15CYKtc-sIIDhUgGkSyMAov6vij8hsels")
        messages = [TextSendMessage(text='次が最後の質問です!'),
                    ImageSendMessage(original_content_url=image_url7, preview_image_url=image_url7),
                    TemplateSendMessage(alt_text='ButtonsTemplate', template=ButtonsTemplate(
                        title='【問6】', text='▼ タップして選ぶ ▼',
                        actions=[PostbackAction(label="最初の進め方がわからない", data="最初の進め方がわからない",
                                                text="最初の進め方がわからない"),
                                 PostbackAction(label="次に何をすべきかわからない", data="次に何をすべきかわからない",
                                                text="次に何をすべきかわからない"),
                                 PostbackAction(label="初めての不動産会社選びが不安",
                                                data="初めての不動産会社選びが不安",
                                                text="初めての不動産会社選びが不安"),
                                 PostbackAction(label="今の不動産会社で良いのか不安",
                                                data="今の不動産会社で良いのか不安",
                                                text="今の不動産会社で良いのか不安")]))]
        line_bot_api.reply_message(event.reply_token, messages)

    elif input_text == '最初の進め方がわからない':
        with open("test2.json", "r") as f:
            flex_message_json2 = json.load(f)
            flex_message2 = FlexSendMessage(
                alt_text='This is a Flex Message2',
                contents=flex_message_json2['contents']
            )

        messages = [
            TextSendMessage(text='最後までご回答いただきありがとうございます！'
                                 'あなたにピッタリな売却プランが診断できましたので、結果をご覧ください！'),
            flex_message2
        ]

        line_bot_api.reply_message(event.reply_token, messages)

    else:
         # line_bot_api.reply_message(
         # event.reply_token,
        messages=[TextSendMessage(text=input_text)]
        line_bot_api.reply_message(event.reply_token,messages)

        #image_url8 = ("https://drive.usercontent.google.com/download?id=1bM3yyI3ontgBIyEicG9OtrcTymW32N6I")

