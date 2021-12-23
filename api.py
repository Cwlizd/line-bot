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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()