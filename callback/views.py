import json
from django.http import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LinePush

# line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
# parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

# Create your views here.
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        request_json = json.loads(request.body.decode('utf-8'))
        events = request_json['events']
        line_user_id = events[0]['source']['userId']

        # チャネル設定のWeb hook接続確認時にはここ。このIDで見に来る。
        if line_user_id == 'Udeadbeefdeadbeefdeadbeefdeadbeef':
            pass

        # 友達追加時・ブロック解除時
        elif events[0]['type'] == 'follow':
            LinePush.objects.create(user_id=line_user_id)

        # アカウントがブロックされたとき
        elif events[0]['type'] == 'unfollow':
            LinePush.objects.filter(user_id=line_user_id).delete()

    return HttpResponse()