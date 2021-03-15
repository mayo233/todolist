from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo_index'),
    path('add/', views.add, name='todo_add'),
    path('remove/<int:todo_id>/', views.remove, name='todo_remove'),
]