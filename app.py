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

line_bot_api = LineBotApi('OXFqUs76Af+1Y8BKdJ4ynY7FTt28ndJBQY+lAkYfGITfisECLxozDn5ua9OxKc7C7Ans464kQKMyp6TsgDRjXtOI8S9pnK1ZYCqnj5kDTGd5NsKVPkv5NUTSe5yGrgRPxequnTwoLwLoKZs5xhSYHwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f46b2d7d625112271e07e27414dfcee8')


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


@app.route("/")
def root():
    return "ok"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="はい　日立です！"))


if __name__ == "__main__":
    app.run()
    
# Set-ExecutionPolicy RemoteSigned -Scope Process
# $env:FLASK_ENV = "development"
# line\Scripts\Activate.ps1
# flask run

# Set-ExecutionPolicy RemoteSigned -Scope Process
# line\Scripts\Activate.ps1
# cd C:\Users\fes77\Downloads\ngrok-stable-windows-amd64
# .\ngrok http 5000