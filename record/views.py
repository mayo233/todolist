from django.shortcuts import render
from timer.models import Timer

def index(request):
    # テスト用
    records = Timer.objects.all()
    return render(request, 'record/index.html', {'records': records})

