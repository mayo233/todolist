from django.shortcuts import render
import time

def test(request):
    return render(request, 'timer/index.html')

def add(request):
    todo = Todo(
        start=request.POST['title'],
        stop=request.POST['text'],
        total＿time=datetime.strptime(request.POST['deadline'], '%Y-%m-%dT%H:%M')
    )
    todo.save()
    return HttpResponseRedirect(reverse('todo_index', args=()))

