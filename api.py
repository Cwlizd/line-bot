from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('dh0QOlmcdcUDq8P+UZtBqOiKjReAOtcGIPoO4Gkuij3ERy5sI20bNkMfIuUk3DulLyeqDGwCUCmdWwMb/W+ArZV1cKxdey3Z3k7QYgHWoP/bNq+5O6f1jq7q+nOqlgBJrwc7encv6inYYbmsSvFwJgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('12f9d1d70946ad59278f0e0f478db0b4')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = '所以呢?給魚啊?'

    if msg in ['酷酷呢', '酷酷勒', '酷酷哩', '酷酷在幹嘛']:
        r = '酷酷在睡覺,沒上班'
    elif msg in ['狡猾鵝鵝', '狡猾鵝']:
        r = '你才狡猾,你全家都狡猾'
    elif msg in ['鵝鵝好可愛', '鵝鵝可愛', '鵝鵝你怎麼這麼可愛']:
        r = '那當然'
    elif msg in ['額額抱抱', '鵝鵝親親']:
        r = '抱抱 500, 親親 1000'
    elif msg in ['給你魚']:
        r = '很好,這還差不多,給個五萬條吧'
    elif msg in ['不想上班']:
        r = '你不要讓我生氣,八嘎'
    elif msg in ['傻眼']:
        r = '還好吧,嘿嘿'
    elif msg in ['好啦']:
        r = '要不要給本鵝魚?'
    else:
        r = '所以我說那個魚呢?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()



# heroku git:remote -a cpff-bot(可以開通這條路給HEROKU GIT)