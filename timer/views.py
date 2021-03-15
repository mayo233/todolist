from django.shortcuts import render
import time

def test(request):
    return render(request, 'timer/index.html')
