from django.conf import settings
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from .models import LinePush

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.
@csrf_exempt
def callback(request):
    # if request.method != 'POST':
    #     return HttpResponse('ん？なんやようか？', status=405)

    HttpResponse('test1')
    signature = request.META['HTTP_X_LINE_SIGNATURE']
    body = request.body.decode('utf-8')
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        return HttpResponseForbidden()
    except LineBotApiError:
        return HttpResponseBadRequest()

    HttpResponse('test2')
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        HttpResponse('test3')
        text_send_message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            text_send_message
        )

    return HttpResponse(status=200)
    # if request.method == 'POST':
    #     signature = request.META['HTTP_X_LINE_SIGNATURE']
    #     body = request.body.decode('utf-8')

    #     try:
    #         events = parser.parse(body, signature)
    #     except InvalidSignatureError:
    #         return HttpResponseForbidden()
    #     except LineBotApiError:
    #         return HttpResponseBadRequest()

    #     for event in events:
    #         if isinstance(event, MessageEvent):
    #             line_bot_api.reply_message(
    #                 event.reply_token,
    #                 TextSendMessage(text=event.message.text)
    #             )
    #     return HttpResponse()
    # else:
    #     return HttpResponseBadRequest()