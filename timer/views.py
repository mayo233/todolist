from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import time

from .models import Timer

def index(request):
    # テスト用
    records = Timer.objects.all()
    return render(request, 'timer/index.html', {'records': records})


def store(request):
    timer = Timer(
        time = request.POST['time'],
        created_at = request.POST['created_at'],
    )
    timer.save()
    return HttpResponseRedirect(reverse('timer_index', args=()))