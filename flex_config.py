flex_message_json = {
        "type": "flex",
        "altText": "This is a Flex Message",
        "contents": {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://placehold.jp/150x150.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "postback",
                    "data": "ボタンがタップされました"
                }
            }
        }
    }