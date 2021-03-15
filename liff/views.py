from django.http.response import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import EmailPush, LinePush

# Create your views here.
def index(request):
    return render(request, 'liff/index.html')

@csrf_exempt
def callback(request):
    """ラインの友達追加時に呼び出され、ラインのIDを登録する。"""
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
