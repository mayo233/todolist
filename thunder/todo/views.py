from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {todos: todos})

# def add(request):
#     todo = get_object_or_404(Todo, pk = todo_id)
#     todo.delete()