from typing import Text
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.urls import reverse

from .models import Todo

app_name = 'todo'
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    todo = Todo(
        title=request.POST['title'],
        text=request.POST['text'],
        deadline=datetime.strptime(request.POST['deadline'], '%Y-%m-%dT%H:%M')
    )
    todo.save()
    return HttpResponseRedirect(reverse('index', args=()))

def remove(request, todo_id):
    todo = get_object_or_404(Todo, pk = todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index', args=()))