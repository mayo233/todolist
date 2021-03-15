from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('remove/<int:todo_id>/', views.remove, name='remove'),
]