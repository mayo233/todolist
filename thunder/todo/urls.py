from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.index, name='index'),
    # path('add/', views.add, name='add'),
    # path('<int:todo_id>/remove/', views.remove, name='remove'),
]