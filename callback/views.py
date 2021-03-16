from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)
import os

LINE_CHANNEL_ACCESS_TOKEN = "ti9/qdZKQKXbquJHvAYmZ9SQp7AlEi7fqbfMLVJVHjz3eahMPuKwkcGlnctj7eQYq2RuDzVEzHQCU20cRWdwfBcb74Ekb0HsDVRdh+RUxfx9D+1523lDzLzLoeYMvm0vjTCahwgBuvszoDQueDUoEQdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "5fad41bf022893c1e8e5c27cb9dd348a"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        HttpResponseForbidden()
    return HttpResponse('OK', status=200)


# オウム返し
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    line_bot_api.reply_message(event.reply_token,
                               TextSendMessage(text=event.message.text))