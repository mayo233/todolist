from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='timer_index'),
    path('add/', views.add, name='timer_add'),
]