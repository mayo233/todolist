from django.shortcuts import render
from timer.models import Timer

def index(request):
    # ใในใ็จ
    records = Timer.objects.all()
    return render(request, 'record/index.html', {'records': records})

