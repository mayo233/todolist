from typing import Text
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Chara

app_name = 'chara'
# Create your views here.
def index(request):
    Charas = Chara.objects.all()
    return render(request, 'chara/index.html', {'Charas': Charas})

