from django.http.response import HttpResponseBadRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'liff/index.html')
