from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import time

from .models import Timer

def index(request):
    message = ''
    return render(request, 'timer/index.html', {'message': message})


def store(request):
    timer = Timer(
        time = request.POST['time'],
        created_at = request.POST['created_at'],
    )
    timer.save()

    message = '保存に成功しました'
    return render(request, 'timer/index.html', {'message': message})
